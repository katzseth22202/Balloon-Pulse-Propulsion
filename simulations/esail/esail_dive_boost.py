"""Electric sail dive-and-boost with an aphelion-arc braking controller.

This is the run that produces the numbers quoted in the paper's
"Electric and Solar Sails" subsection.

Strategy. Because continuous retro-thrust at ~1 mm/s^2 just spirals the
orbit down quasi-circularly (see esail_sim.py), the sail brakes only
while r > 0.85 AU, near aphelion. That pins the aphelion at 1 AU while
the perihelion drops to the target. It then coasts to perihelion and
thrusts flat out along the velocity vector (cone-limited) back to 1 AU.

Assumptions: planar two-body problem, departure from Earth's orbit at
zero hyperbolic excess, thrust proportional to r**(-7/6), 30 degree
steering cone with cos-loss, constant spacecraft mass, no solar wind
variability, Earth phased to sit at the crossing point. Earth-relative
speed is the coplanar vector difference with Earth's circular velocity.
"""
import numpy as np

import esail_sim as es


def run_dive_boost(a0_mm, peri_target_au, aph_arc=0.85, dt=500.0, years=8.0):
    a0 = a0_mm * 1e-3
    peri = peri_target_au * es.AU
    state = np.array([es.AU, 0.0, 0.0, es.VE])    # depart Earth, C3 = 0
    t = 0.0
    reached = passed = False
    while t < years * 365.25 * 86400:
        _, _, _, e, rp = es.orbit_elements(state)
        r = np.hypot(state[0], state[1])
        vr = (state[0] * state[2] + state[1] * state[3]) / r
        if not reached:
            mode = "retro" if r > aph_arc * es.AU else "coast"
            if rp <= peri:
                reached = True
                mode = "coast"
        elif not passed:
            mode = "coast"
            if vr > 0 and r < 0.75 * es.AU:
                passed = True
                mode = "pro"
        else:
            mode = "pro"
            if r >= es.AU:
                vrel, vr_, vt_ = es.rel_speed(state)
                return (t / 86400, np.hypot(state[2], state[3]) / 1e3,
                        vrel / 1e3, vr_ / 1e3, vt_ / 1e3)
        state = es.rk4(state, dt, a0, mode)
        t += dt
    return None


if __name__ == "__main__":
    for peri in (0.5, 0.35):
        for a0 in (0.5, 1.0, 2.0, 5.0):
            out = run_dive_boost(a0, peri)
            if out:
                t, vh, vrel, vr, vt = out
                print(f"dive {peri} AU  a0={a0} mm/s^2: trip {t:6.0f} d "
                      f"({t / 365.25:4.2f} yr)  helio {vh:5.1f} km/s "
                      f"(vr {vr:+5.1f}, vt {vt:+5.1f})  Earth-rel {vrel:5.1f} km/s")
            else:
                print(f"dive {peri} AU  a0={a0} mm/s^2: no crossing in 8 yr")
        print()
