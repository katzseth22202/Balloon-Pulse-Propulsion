# Release the growth wave warm from its carrier at 1.3 AU

Status: accepted (2026-09-13 grill). Recorded because a later reader will ask three things. Why
does hardware that flew in from Jupiter carry heat and stowed bumpers all the way to 1.3 AU? Why
is the fill plain water when an antifreeze was proposed and priced? Why does this ring fly without
the hub bag that `sec:tethered_ring` argues for?

On the three-synodic returns the growth wave falls in almost radially: 36 km/s sunward and
12.6 km/s against Earth's motion at 1 AU, on orbits with perihelion 0.07-0.10 AU. The carrying
craft keeps the bags liquid and their bumpers stowed until **Release** at 1.3 AU, 15.6-16.5 d
before Earth. It then pays the burn that spreads the salvo over the push, 4.3-4.4 m/s for the
outermost units to cover +/-108.5 s of stream time, by paired ejection or by burning between
releases. Afterwards it diverts about 7 m/s to miss Earth by 10,000 km. Carrier delta-v under
about 20 m/s is treated as negligible. The fill is plain water under a bumper pattern near 302 K
at 1 AU, which holds a 9 kg bag released at 295 K between 278 and 292 K for the whole coast. The ring
has no hub bag and flies the impact attitude from release, so nothing re-points.

## Considered options

- **Frozen fill thawing on the way in.** A bag cannot pass its local radiative equilibrium. On a
  280 K pattern even 50 wt% glycol melts fully only at 1.04-1.10 AU, days before Earth. Heating on
  the carrier is what makes a liquid release possible.
- **50 wt% ethylene glycol fill.** Freezes near 238 K and holds 0.76 kPa at 280 K, and on a 280 K
  pattern it keeps a +22 K freeze margin. Set aside while the charge holds the 273-300 K
  **Sensitizer-set thermal band**. Once the coast stays above 276 K, water never freezes, and
  glycol would add only about 19% of fill mass as carbon in the plume, a fuel beside an
  oxidizer-rich charge, and 5-33x water's viscosity. It returns if the charge proves cold-tolerant.
- **Release farther out.** The burn halves at 1.5 AU (2.5 m/s), but the longer coast runs colder
  and from 1.7 AU a bag slushes. With the burn free, the temperature floor decides.
- **Bumpers exposed through cruise.** The pattern window allows alpha/eps drift of only
  -10%/+11% for a 9 kg bag. No darkening figure exists for aluminized PET or PEN after years of
  cruise and a 1.056 R_J Jupiter pass, so stowing removes the unknown instead of measuring it.
- **Thermal attitude with a late ~40 deg re-point, or keeping the hub bag.** Only the centered hub
  bag needs the thermal attitude, since off-axis ring bags stay side-heated at every Sun angle.
  In the impact attitude the Sun sits 44-50 deg off the axis and would hold 64-72% of normal
  sunlight on the hub bag's sunward pole, exactly where centrifugal stirring vanishes.

## Consequences

- The ring arrives as a donut. The gas cloud is shaped to fill the center as well as it can, but
  that shaping couples with the water the plate injects and is left for expert modeling. Restitution
  and capture fraction remain single-cloud values.
- The carrying craft keeps the stream's heliocentric orbit after its divert (perihelion
  0.06-0.11 AU, aphelion 4.2-7.6 AU), far from Earth.
- The figures come from `todos/jupiter_3s_release_geometry.py` and `todos/glycol_fill_thermal.py`,
  gitignored probes. Arrival states are the companion's Lambert return arcs for the adaptive 2S/3S
  chain at a 10-day split, back-propagated Sun-only; bag temperatures use a lumped radiative model
  with effective emittance 0.090 taken from the paper's 38 W anchor. The companion has not yet
  reproduced them.
