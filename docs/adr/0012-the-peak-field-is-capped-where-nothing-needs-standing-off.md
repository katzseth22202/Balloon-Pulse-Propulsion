# The peak field is capped at 12 T, because the profile demanded its strongest field where nothing needs standing off

Status: accepted (2026-09-04 grill on `puffsat_impact_simulation`'s nozzle answers). Settles item
P6 of `docs/nozzle_asks_answered.md`, which was blocked on P7 and is unblocked by `0011`.
The cap sits at 12 T rather than the 9 T the argument allows, pending R9.

**Amended in proposal by `0013`** (2026-09-05). The cap table below measures wall contact to the
bag bore at every station, and `0011` puts the liner at 3.50 m flaring to 5.17 m. Reading the
same flown profile at the contact station against the liner gives 10.59 T rather than 11.75 T at
the binding bracket, so `0013` proposes **11 T**. That amendment is conditional on R15, which
asks the impact simulation which surface the standoff requirement is written against. **Until
R15 lands, 12 T is the flown number.**

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

The field-energy, structure, and tape figures below retain the original first-order
paper-side estimates. They have not been recomputed with the companion expansion model.

| shelf | peak `B` | field energy | virial structure | tape |
| --- | ---: | ---: | ---: | ---: |
| none, as flown | 19.8 T | 1.00x | 10--30 t | 1.00x |
| **12 T (adopted)** | **12.0 T** | **0.88x** | **9--27 t** | **0.96x** |
| 9 T, if the sound-speed spread holds | 9.0 T | 0.75x | 7--22 t | 0.90x |

## Why the cap improves the modeled expansion efficiency

**Amended following P13, accepted in the paper review.** The former `eta_geom`
column and its claim of a change below 0.005 used single-particle `mu` conservation.
That model does not apply to the collisional plume. The continuum comparison below
supersedes those efficiency figures.

Reducing the chamber field from 20 T to 12 T, with the exit held at 5 T, reduces
the expansion area ratio from 4.0 to 2.4. More thermal motion remains at the exit,
but the denser plume has a lower Alfvén speed. It reaches the model's release
condition sooner and suffers less downstream divergence. The net effect improves
`eta_exp`, the mean axial speed divided by the root-mean-square speed in the
plume's initial rest frame.

| Closing speed | Branch | `eta_exp`, 20 T | `eta_exp`, 12 T | Change |
| --- | --- | ---: | ---: | ---: |
| 45.58 km/s | Equilibrium | 0.520 | 0.582 | +0.062 |
| 45.58 km/s | Frozen | 0.554 | 0.599 | +0.045 |
| 75 km/s | Equilibrium | 0.656 | 0.795 | +0.139 |
| 75 km/s | Frozen | 0.704 | 0.859 | +0.155 |

These cases have no downstream extension. The gain is 0.045--0.155 across the
four rows; P13's summary range of 0.06--0.15 omits the smaller cold frozen gain.
The companion source calls this factor `eta_geom`; the paper uses `eta_exp` to
separate it from the full ship-frame impulse factor. No replacement expansion
result is supplied for the 9 T case.

The values are from `puffsat_impact_simulation` at `6fe8cf3`,
`docs/nozzle_replies_answered.md`, P12--P13. They retain that model's 3.0 m chamber
radius and 23.8 m field length; ADR-0014's corrected bag geometry has not been
rerun through it. Reproduce with `make analysis-nozzle-extension` in that checkout.

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

The original field-sizing estimates use paper-side probes, first order, in `todos/`: `chamber_tradeoff.py`, `chamber_relax.py`. Same
caveats as `0011` (paraxial field, uniform mass, one detachment surface). Owed back to
`puffsat_impact_simulation` with R1 and R9.
