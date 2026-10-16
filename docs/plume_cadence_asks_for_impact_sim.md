# The sheets in the old plume: asks for `puffsat_impact_simulation`

Raised 2026-10-16. **Written to be copied verbatim into `katzseth22202/puffsat_impact_simulation`.**
Register items **S36-S37** (`docs/deferred_to_companion_repos.md`). The paper prints ballpark
figures in `sec:charge_pusher_plume` (commit `f1bb191`). The trajectory and plate asks for the
1 Hz push went to the aim repo as S33-S35 (`docs/plume_cadence_asks_for_aim_repo.md`).

## Context

On the 400 km overtake push, each ~100 km/s Kapton sheet (50-88 g/m^2, 35-62 um) flies face-on
through the gas of the pulses before it. That gas is the sheet plus its polyethylene charge at
k = 6.74, ~359 kg per pulse. The flat skirted plate throws it back up the stream, toward the sheets
still arriving. The paper models each earlier pulse as a Gaussian cloud whose center recedes at U
and spreads at u along any one axis (`sec:jovian_plume_encounter`). U = 20.5 km/s is just what the
12 MN s pulse's momentum requires. **u is a free input, and it sets most of the answer.**

| Cadence, pulse | Dose at u = 5 / 8 / 12 km/s (kJ/m^2) | 50 g/m^2 sheet rise at u = 8 |
|---|---|---|
| 4 Hz, 12 MN s (priced) | 635 / 251 / 114 | 4570 K |
| 2 Hz, 24 MN s | - / 125 / - | ~2300 K |
| 1 Hz, 14.7 MN s | 47 / 19 / 8 | 340 K |

The doses assume full absorption of incident momentum and kinetic energy, no radiation, no
recombination and no sputtering. 90% of the dose arrives in the last ~0.25 s at 4 Hz and in the last
~0.5 s at 2 Hz.

## S36. The flat plate's backward plume

From your overtake runs at k ~ 6.7 and ~100 km/s (`overtake_sheet.csv`'s flat skirted plate), give:
1. The mass-weighted distribution of the exhaust's velocity, both speed and angle from the stream
   axis, in the plate frame. In particular, the mass fraction moving up the stream within ~5 degrees
   of the axis, since that is the gas the next sheet meets. A table in bins of speed and angle is
   enough.
2. Equivalently, the best-fit U and u for the Gaussian cloud above, or a reason that shape is wrong,
   for example a hollow cone that leaves the axis nearly clear.
3. The species and their internal energy at ~1-10 km from the plate: how much is still dissociated or
   ionized, and the recombination energy a Kapton face would collect.
4. The same for a plate canted or curved to throw the exhaust off the stream axis, and what that
   costs in momentum efficiency. If ~10-20 degrees of tilt clears the axis cheaply, the 4 Hz push may
   keep thin sheets.

## S37. The sheet's response, and the 1 mm option

1. The heat a 100 km/s Kapton face actually keeps from that gas: the accommodation, sputtering and
   implantation of ~50 eV/amu particles, against the paper's full-absorption bound.
2. When a 35-62 um sheet starts to decompose, at 1, 2 and 4 Hz. If it gasifies in the last ~0.1-0.3 s,
   does it still work as the impactor? The paper's guess is that the film vaporizes evenly across its
   face, so the vapor leaves mostly fore and aft, along the flight line. It would then arrive as a
   slab ~100-300 m thick, a ~1-3 ms arrival instead of an instant hit. Does the charge-pusher law
   (0.61 of ideal momentum on the flat plate) survive that?
3. The **1 mm sheet** (1.42 kg/m^2; 46 kg is a 3.2 m radius) on a ~1 cm, ~9.6 kg/m^2 charge, to hold
   k = 6.74. The paper's 1D conduction gives a 535 K front face at 2 Hz and a ~0.1 mm charred skin at
   4 Hz. Wanted: the momentum efficiency and the plate's peak pressure at two standoffs, against the
   thin sheet on its thin charge.
4. 100 um Kevlar strands broadside: where they pass ~520 K, on your gas rather than the paper's
   Gaussian. The paper's rule (nothing the strands carry may be needed in the last ~0.2 s) stays
   either way. The number decides how thick the rigging must be.
