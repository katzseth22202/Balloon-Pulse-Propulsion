# Solar-dive returns re-intercept Earth by phasing, not by re-aiming

Status: accepted

The "Sorry, I Don't Need ISRU" cycle (`sec:no_isru_rocket`) sends a projectile to a low
solar periapsis, boosts it, and returns it across 1 AU at 150 km/s or more. We had asserted
it "crosses Earth" without addressing how it arrives *where Earth is* rather than merely
crossing 1 AU somewhere else. The boosted orbit is an escaping hyperbola with a single
outbound 1 AU crossing, and that crossing lands about 136 deg of heliocentric longitude
from Earth (the projectile whips ~295 deg around the Sun in ~0.2 yr while Earth advances
only ~71 deg). We decided the miss is fixed by **phasing the return to an Earth resonance**,
which is fundamentally a pay-in-time maneuver, and we revised the growth claim to match:
the re-intercepting cycle floor is ~0.82 yr, so a millionfold scaling takes **~16 years**,
not under a decade. Backed by Appendix `sec:earth_reintercept`.

## Considered options

- **Re-aim at periapsis — rejected.** Turning the velocity vector near the 309 km/s
  periapsis costs ~5.4 km/s per degree, so a tens-of-degrees correction runs to hundreds of
  km/s against a ~24 km/s dive boost. Direction changes want the slowest point on the orbit;
  periapsis is the fastest.
- **Rotate the argument of periapsis for a fast dive — no solution.** Launching from 1 AU
  onto a 4 solar-radii periapsis pins Earth near the orbit's aphelion, which pins the
  crossing ~65 deg behind the launch longitude. The long axis is not a free knob for a deep
  diver launched from 1 AU.
- **Phasing (chosen), realized three ways.** All impulses are PuffSat collisions, not
  carried propellant.
  1. *Two-impulse loop* (periapsis-lowering dip, then deep dive): colinear retrograde
     boosts, free in total impulse (~24 km/s), holds the doubling factor at two. Needs a
     second PuffSat boost node at 1 AU off Earth. First resonance ~0.82 yr. (Apoapsis-raising
     is the wasteful direction: opposing boosts, ~+7.6 km/s, ~1.82 yr.)
  2. *Single-impulse resonant dive* (inject outbound to ~1.9 AU aphelion): only the Earth
     node, but the boost grows 24 to ~37 km/s (the direct dive's ~24 retrograde plus ~28
     outbound radial), dropping the doubling factor below two. ~0.85 yr; the aphelion is
     the knob that closes the geometry.
  3. *Gravity-assist resonant return* (Venus/Earth flyby): impulse-free, ~1-2 yr, constrained
     by flyby timing.

The three trade network complexity against per-cycle doubling factor against schedule, at
cycles of ~0.82 yr, ~0.85 yr, and ~1--2 yr respectively. The paper presents all three rather
than committing to one.

## Consequences

- The paper's central growth timeline moves from "under a decade" to "~16 years" for a
  millionfold, and 16 yr is itself a floor (two-impulse loop, every cycle catching its
  resonance, no Earth turnaround). The single-impulse and gravity-assist routes push past it.
- The companion calculations repo (`katzseth22202/aim_is_all_you_need`) carried the old
  6-month / under-a-decade figure; commit f31bfdc updated it to the derived 0.82 yr floor
  and pinned the appendix numbers with tests. The single-impulse resonant dive (~1.9 AU,
  ~0.85 yr, ~37 km/s) is not yet verified there and should get a closure-solver function.
- The two-impulse loop introduces a new architectural requirement: PuffSat boost nodes at
  heliocentric points off Earth, not just at Earth and at periapsis. This is a mature-network
  capability; early bootstrapping falls back to the single-impulse dive or a gravity assist.
