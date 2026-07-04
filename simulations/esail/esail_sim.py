"""Electric sail heliocentric trajectory model.

2D heliocentric dynamics with the standard electric sail thrust model:

    a = a0 * (1 AU / r)**(7/6) * cos(TILT)

where a0 is the characteristic acceleration (thrust per unit spacecraft
mass at 1 AU). The r**(-7/6) thrust law comes from Janhunen & Sandroos
2007 (Ann. Geophys. 25:755-767, doi:10.5194/angeo-25-755-2007) and is
the model used in Mengali, Quarta & Janhunen 2008 (J. Spacecraft
Rockets 45(1):122-129, doi:10.2514/1.31769), whose reference designs
target a0 near 1 mm/s^2. The thrust vector is steerable within a cone
of TILT about the anti-Sun line, with a cos(TILT) magnitude penalty;
the solar wind cannot push a sail sunward.

Running this module directly demonstrates the NAIVE dive strategy:
thrust continuously against the direction of motion to dive, then
continuously along it to boost. At a0 near 1 mm/s^2 the thrust is
about a sixth of solar gravity at 1 AU, so continuous retro-thrust
spirals the orbit down while keeping it nearly circular. The sail
comes home nearly circular and gains almost no Earth-relative speed.
esail_dive_boost.py holds the aphelion-arc strategy that fixes this
and produces the numbers quoted in the paper.

A planar flip to a retrograde orbit is not attempted: the path from
prograde to retrograde passes through zero angular momentum, which is
a solar impact trajectory.
"""
import numpy as np

GM = 1.32712440018e20          # solar gravitational parameter, m^3/s^2
AU = 1.495978707e11            # astronomical unit, m
VE = np.sqrt(GM / AU)          # Earth circular speed, ~29.78 km/s
TILT = np.radians(30.0)        # max thrust-cone half angle from anti-Sun line
CT = np.cos(TILT)              # thrust magnitude penalty at full tilt


def accel(state, a0, mode):
    """State derivative. mode: 'coast', 'retro' (max braking within cone),
    or 'pro' (cone-limited projection of the velocity direction)."""
    x, y, vx, vy = state
    r = np.hypot(x, y)
    rhat = np.array([x, y]) / r
    grav = -GM / r**2 * rhat
    if a0 == 0.0 or mode == "coast":
        return np.array([vx, vy, grav[0], grav[1]])
    mag = a0 * (AU / r)**(7.0 / 6.0) * CT
    that = np.array([-rhat[1], rhat[0]])          # tangential unit vector
    if (x * vy - y * vx) < 0:                     # match direction of motion
        that = -that
    if mode == "retro":
        c, s = np.cos(TILT), np.sin(TILT)
        tdir = c * rhat - s * that                # cone edge opposing motion
    elif mode == "pro":
        v = np.array([vx, vy])
        vhat = v / np.linalg.norm(v)
        ang = np.arccos(np.clip(np.dot(vhat, rhat), -1, 1))
        if ang <= TILT:
            tdir = vhat
        else:                                     # rotate rhat toward vhat by TILT
            sign = np.sign(rhat[0] * vhat[1] - rhat[1] * vhat[0])
            c, s = np.cos(TILT), sign * np.sin(TILT)
            tdir = np.array([c * rhat[0] - s * rhat[1],
                             s * rhat[0] + c * rhat[1]])
    else:
        raise ValueError(mode)
    th = mag * tdir
    return np.array([vx, vy, grav[0] + th[0], grav[1] + th[1]])


def rk4(state, dt, a0, mode):
    k1 = accel(state, a0, mode)
    k2 = accel(state + 0.5 * dt * k1, a0, mode)
    k3 = accel(state + 0.5 * dt * k2, a0, mode)
    k4 = accel(state + dt * k3, a0, mode)
    return state + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)


def orbit_elements(state):
    """Return specific energy, angular momentum, semi-major axis,
    eccentricity, perihelion radius."""
    x, y, vx, vy = state
    r = np.hypot(x, y)
    v2 = vx * vx + vy * vy
    E = v2 / 2 - GM / r
    h = x * vy - y * vx
    a = -GM / (2 * E) if E < 0 else np.inf
    e = np.sqrt(max(0.0, 1 + 2 * E * h * h / GM**2))
    rp = h * h / GM / (1 + e)
    return E, h, a, e, rp


def rel_speed(state):
    """Earth-relative speed at a 1 AU crossing: coplanar, Earth prograde
    and phased to be at the crossing point."""
    x, y, vx, vy = state
    r = np.hypot(x, y)
    rhat = np.array([x, y]) / r
    that = np.array([-rhat[1], rhat[0]])
    vr = vx * rhat[0] + vy * rhat[1]
    vt = vx * that[0] + vy * that[1]
    return np.hypot(vr, vt - VE), vr, vt


def run_continuous(a0_mm, peri_target_au, dt=1000.0, years=8.0):
    """Naive controller: continuous retro-thrust until perihelion reaches
    the target, coast to perihelion, continuous pro-thrust out to 1 AU."""
    a0 = a0_mm * 1e-3
    peri = peri_target_au * AU
    state = np.array([AU, 0.0, 0.0, VE])          # depart Earth, C3 = 0
    t = 0.0
    reached = passed = False
    mode = "retro"
    while t < years * 365.25 * 86400:
        _, _, _, e, rp = orbit_elements(state)
        r = np.hypot(state[0], state[1])
        vr = (state[0] * state[2] + state[1] * state[3]) / r
        if not reached and rp <= peri:
            reached = True
            mode = "coast"
        if reached and not passed and vr > 0 and r < 0.75 * AU:
            passed = True
            mode = "pro"
        if passed and r >= AU:
            vrel, vr_, vt_ = rel_speed(state)
            return t / 86400, np.hypot(state[2], state[3]) / 1e3, vrel / 1e3, e
        state = rk4(state, dt, a0, mode)
        t += dt
    return None


if __name__ == "__main__":
    print("Naive continuous-thrust dive (demonstrates quasi-circular spiral):")
    for a0 in (0.5, 1.0, 2.0):
        out = run_continuous(a0, 0.5)
        if out:
            t, vh, vrel, e = out
            print(f"  a0={a0} mm/s^2: trip {t:6.0f} d, helio {vh:5.1f} km/s, "
                  f"Earth-rel {vrel:5.1f} km/s, arrival e={e:.2f}")
