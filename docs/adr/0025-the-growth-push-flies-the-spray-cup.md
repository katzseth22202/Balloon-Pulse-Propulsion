# The growth push flies the spray cup; the plug follows; the lob climbs at 1.1 km/s

Status: accepted (2026-10-06). Paper: `sec:spray_cup` through `sec:spray_cup_tamper`,
`sec:growth_ledger`, `sec:vertical_lob`, `sec:mass_interest`, `fig:plate_stack`,
`fig:plate_shapes`, `tab:plate_designs_cost`.

## Context

`puffsat_impact_simulation` sized a real overtake plate (its ADR-0055; handoff Draft 2 @
`7e1d8f7`, filed here as `docs/spray_plate_answers_from_impact_sim.md`). Its spray cup reaches
η_jet 0.60 (0.57 unmixed); its plug ~0.70. `aim_is_all_you_need` @ `a440fba` (ADR 0041) ran
both through the ledger and cost model and added a climbing-lob charge.

## Decision

1. **The spray cup is the flown plate, η_jet = 0.60, and every headline figure moves to it.**
   The plug is printed beside it; 0.57 is quoted as the downside. The comparison row is the plate
   the ledger flew before, η = 0.7 (η_jet 0.84). 0.775 is not a plate number in this paper.
2. **The Jupiter plate lives in `sec:water_injected_overtake`.** The low-orbit plate sections
   (`sec:lightweight_pusher_plates`, `sec:pusher_plate_mass_stroke`, `sec:segmented_steel_plate`)
   keep their 11 km/s design; the new text points back to them where the two differ.
3. **Skirt fixed to the vehicle, floor sliding inside, carbon hoop wrap.** Aramid was offered by
   the author and declined on mass after the sim's own aramid rows were shown (43 t vs 32 t).
4. **The lob is charged only for the climb above 0.75 km/s.** The paper's lob was already sized to
   pass 400 km at ~0.75 km/s (apex ~430 km). The companion's `lob_rise.booster_growth` divides by
   an apex-at-400 km lob and so charges 7-10%. From 0.75 to the 1.1 km/s operating point the same
   integrator gives 4.4% (3-6% over 1.0-1.2 km/s): booster ~1.13-1.28x Super Heavy, lob
   $25 -> $26.1/kg lofted. Asked back as S10; answered by the companion's ADR 0042.
5. **The full grids are reproduced by the companion's `make plate-grid`, `plate-cost` and
   `plate-seed`** (its ADR 0042), written from this pass because ADR 0041 ran only the solved
   chambers and methalox (S11). Delivered to the author as a patch,
   `todos/aim_is_all_you_need_adr0042.patch`, to apply on the companion's `main`. The
   50%-of-ceiling rows stay as the floor sweep.
6. **No numbers massaged.** The weaker Starship comparison is printed as it comes out (author,
   2026-10-06).

## Consequences

- Solved hydrogen doubles in 2.02 yr (was 1.59), breaks even at $189 / $370 (was $134 / $194).
  Methalox doubles in 7.8 yr and repays no dear seed. Pessimistic solved chambers miss $500.
- The seed is 102-112 t, more than one stripped ship (was 0.79-0.94).
- Unpriced and named in the text: the film's mass (5-9 t per push shielded, 34-50 t
  unshielded), the booster's brake at the faster climb, the plug in the deep bowl.
