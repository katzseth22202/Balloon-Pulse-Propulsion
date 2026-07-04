# Electric sail dive-and-boost simulations

Evidence scripts for the paper's "Electric and Solar Sails" subsection.
They size the mission profile: depart Earth's orbit at zero hyperbolic
excess, drop perihelion to 0.5 AU (or 0.35 AU), then thrust back out to
1 AU and cross Earth's orbit at speed.

## Files

- `esail_sim.py` — core 2D heliocentric dynamics and the electric sail
  thrust model (thrust proportional to r^(-7/6), 30 degree steering cone,
  characteristic acceleration `a0` at 1 AU). Running it directly shows the
  naive continuous-thrust dive, which fails instructively: at ~1 mm/s^2
  the thrust is a sixth of solar gravity, so continuous retro-thrust
  spirals the orbit down quasi-circularly and the sail returns with
  almost no Earth-relative speed.
- `esail_dive_boost.py` — the working controller. Brakes only along an
  arc near aphelion (r > 0.85 AU), which pins aphelion at 1 AU while
  perihelion drops, then boosts from perihelion. Produces the table below.
- `solar_sail_sizing.py` — photon-sail comparison: sail area and mass
  needed to push a 25 kg PuffSat at 1 mm/s^2.

## Run

```bash
python3 esail_dive_boost.py    # needs numpy
```

## Results (quoted in the paper)

| a0 (mm/s^2) | dive to | trip | Earth-crossing speed (rel.) |
|---|---|---|---|
| 0.5 | 0.5 AU  | 1.7 yr   | 12.6 km/s |
| 1.0 | 0.5 AU  | 300 d    | 18.8 km/s |
| 2.0 | 0.5 AU  | 264 d    | 26.0 km/s |
| 5.0 | 0.5 AU  | 237 d    | 38.7 km/s |
| 0.5 | 0.35 AU | 2.8 yr   | 15.9 km/s |
| 1.0 | 0.35 AU | 1.4 yr   | 22.9 km/s |
| 2.0 | 0.35 AU | 265 d    | 32.6 km/s |
| 5.0 | 0.35 AU | 240 d    | 48.7 km/s |

Solar sail sizing (25 kg payload, 1 mm/s^2): the sail system must stay
under ~8 g/m^2 areal density even bare; at 3–5 g/m^2 it needs
5,000–8,400 m^2 (a 70–90 m square) massing 15–42 kg.

## Model limits

Planar two-body problem; constant spacecraft mass; no solar wind
variability (real electric sail thrust inherits it); Earth assumed
phased to sit at the crossing point. A planar flip to a retrograde
orbit is impossible for a sail: the path passes through zero angular
momentum, a solar impact trajectory.
