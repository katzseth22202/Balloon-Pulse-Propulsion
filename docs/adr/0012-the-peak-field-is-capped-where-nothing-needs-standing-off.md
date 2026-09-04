# The peak field is capped at 12 T, because the profile demanded its strongest field where nothing needs standing off

Status: accepted (2026-09-04 grill on `puffsat_impact_simulation`'s nozzle answers). Settles item
P6 of `docs/nozzle_asks_answered.md`, which was blocked on P7 and is unblocked by `0011`.
The cap sits at 12 T rather than the 9 T the argument allows, pending R9.

## What P6 found

A solenoid smooths field structure over about its own radius. The graded profile demands a 40%
drop between 1 m and 3 m, a 2 m gradient, from coils about 3.5 m in radius. An all-positive
winding delivers 15.42 T where 19.80 T is asked, a 22.1% shortfall, and because magnetic pressure
goes as `B^2` **undershooting the field by 22% overshoots `beta` to 1.65** at the highest-pressure
station in the column. Matching the profile exactly wants counter-wound coils, which nobody
builds.

P6 offered "a converging bore lets the coils be small exactly where the gradient is steep" as the
cheap fix, blocked on P7. **That fix is dead.** `0011`'s flare keeps 3.50 m coils at the chamber,
because the bag is 3.02 m there, and nothing about the flare makes the chamber coils smaller.

## What the field at the chamber is for

Decided this session: **wall standoff.** The field is there to keep plasma off the liner.

Under that reading the requirement is over-specified, and the paper's own front geometry says so.
The shocked layer leaves a 0.15 m rod at a half-angle set by its own sound speed
(21.1 km/s against a 45.58 km/s advance, so 24.9 degrees):

| station | front radius | wall at | field demanded |
| --- | ---: | ---: | ---: |
| z = 1 m | **0.61 m** | 3.02 m | **19.8 T** |
| z = 3 m | 1.54 m | 3.02 m | 12.2 T |
| z = 6 m | 2.94 m | 3.02 m | 9.0 T |
| z = 23 m | full bore | 3.02 m | 5.0 T |

**The profile asks for its strongest field exactly where the front is smallest and the wall is
furthest.** The grading was derived by setting the snowplow's pressure against
`eq:bore_from_length`'s bore area at every station, and for the first six metres the front does
not fill the bore.

Note also that the 6 m figure owes nothing to the field. It comes from a gas-dynamic spreading
angle with no field in it, and field only slows spreading, so the field cannot be what sets it.
`sec:needle_through_fog` already accepts wall contact at 6 m and prices the coupling on it.

## The decision

**Hold the flown profile from the wall-contact station to the exit, and flatten everything
upstream of it into a shelf.** Monotonicity (P8's no-local-minimum requirement) floors the shelf
at the field where the shelf meets the profile.

**The cap is 12 T**, meeting the flown profile at z = 3.12 m.

| shelf | peak `B` | field energy | virial structure | tape | `eta_geom` |
| --- | ---: | ---: | ---: | ---: | ---: |
| none, as flown | 19.8 T | 1.00x | 10--30 t | 1.00x | 0.527--0.660 |
| **12 T (adopted)** | **12.0 T** | **0.88x** | **9--27 t** | **0.96x** | **0.528--0.662** |
| 9 T, if the sound-speed spread holds | 9.0 T | 0.75x | 7--22 t | 0.90x | 0.530--0.664 |

## Why `eta_geom` does not pay for this

It is the coupling of `0011` running backwards. Dropping the chamber field costs `mu` conversion
for the mass born in the first few metres, **and in the same stroke reduces the divergence those
flux tubes suffer**, because they no longer fan by `sqrt(19.8/5)`. Conversion and radial spread
are one ratio, so the trade is nearly free in both directions. `eta_geom` moves by less than
0.005 across the whole table, in the favourable direction.

## Why 12 T and not 9 T

The wall-contact station rests on the spreading rate, and the paper brackets it:

> Venting the shocked layer sideways until its pressure balances the cold cloud's ram pressure
> gives a spreading speed 1.6 to 1.9 times the sound speed, so taking the sound speed is the
> conservative choice.

**Conservative for the coupling argument and anti-conservative here.** A faster front reaches the
wall sooner, so the shelf must start earlier and sit higher. At 1.9x the half-angle is 41.3
degrees, contact comes at 3.26 m, and the flown profile asks 11.8 T there. **12 T is immune to
the whole bracket.** The extra saving is recoverable if the sound-speed figure holds, which is
asked as R9 in `docs/nozzle_replies_to_impact_sim.md`.

## Consequences

- **The 20 T SPARC-class anchor is no longer load-bearing.** `sec:needle_through_fog` cites
  `creely2020sparc` to show 20 T at 20 K is a working point industry already builds to. At a 12 T
  peak the citation becomes a comfort rather than a requirement, and the argument gets easier.
- **P6's realizability finding stops binding.** A flat shelf demands no gradient, and 12 T to 5 T
  over 20 m is well inside what a 3.5 m coil delivers. No counter-wound coils.
- Field energy, virial structure and tape all fall, and `sec:minimum_nozzle`'s magnet numbers
  move with them.
- **The `beta` = 1.65 exposure is retired** rather than answered. There is no longer a station
  that asks for more field than a winding can make.

## Provenance

Paper-side probes, first order, in `todos/`: `chamber_tradeoff.py`, `chamber_relax.py`. Same
caveats as `0011` (paraxial field, uniform mass, one detachment surface). Owed back to
`puffsat_impact_simulation` with R1 and R9.
