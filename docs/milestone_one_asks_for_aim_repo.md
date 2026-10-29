# Milestone 1: methalox departure behind the Kapton push: ask S63 (for `aim_is_all_you_need`)

Raised 2026-10-29 against aim `c559cc7`. **Written to be copied verbatim into
`katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has.
Register entry: S63 in `docs/deferred_to_companion_repos.md`.

Same ground rules as your own handbacks. Neither document is the source of truth. If a premise
here is wrong, say so rather than working around it.

## Why this is asked

The child (`puffsats_for_datacenters`, `480194d`) now prints the cycle as three milestones, each
adding one burn:

1. The Jupiter-only loop with Kapton sheets overtaking the push plate, leaving Earth on
   **methalox** in place of the departure bowl.
2. The same loop with the bowl: your ADR 0075 chain, `make plate-jupiter-loop`, 1.65x per
   3.276 yr at 0.5 g, $761 / $1881.
3. The Sun dive: `make solar-dive`, the paper's headline.

Milestone 1 has no ledger behind today's plates. The nearest one is `growth_ledger`'s methalox
incumbent (`best_methalox_cycle`, `_methalox_row`). It flies three-synodic only, behind the
**spray cup** (jet efficiency 0.60, 150 t plate, sprayed argon on ice PuffSats). It doubles in
7.92 yr on the 20-day orbit and 9.66 yr on the 10-day orbit, about 1.33x and 1.27x per 3.276 yr.
`survivable_chamber.cost_designs()[0]` prices it at $353 steady and $2323 / >$5000 (your
`make solar-dive ARGS="--child"`). The child's own rough estimate said the loop would shrink. The
parent answered that it grows, on the spray cup, and that the size on today's plates is unknown.

## S63. Wanted

1. **Milestone 1's ledger.** In `plate_jupiter_loop`, replace the bowl departure with
   `growth_ledger.methalox_departure` (Raptor 3, 380 s, 0.018 tank fraction, engines optimized,
   engines and tanks expended). Keep everything else as ADR 0075 flies it: the flat push plate on
   the gas spring at 2 Hz and 1 g, Kapton at the simulation's re-derived law, the 10-day parking
   orbit, the apoapsis raise and turn, the real-ephemeris chain. The whole batch pushes, so there
   is no role split. Report:
   - growth per 3.276 yr, doubling, steady $/kg at L1 and break-even cheap / dear, on the gated
     valuation with the Sun gate dropped (as `tab:no_sun_loop`);
   - the push stream's speed band at 400 km on the windows methalox can fly;
   - engines, methalox mass and payload sent on per unit;
   - the seed in tonnes and stripped Starships at its excess.

   If the methalox stage cannot fly a window at all, say which, as `growth_ledger` found for the
   two-synodic burn.
2. **Its best departure.** With methalox paying, sweep the departure excess downward from the
   chain's 11.9-13.2 km/s. Say whether any slower departure still closes on the 3S clock, and what
   it does to the next push's stream speed and the loop's growth. The parent's unrun reasoning: a
   Hohmann-like 8.8 km/s needs about five synodic periods and returns a ~14 km/s stream at 400 km,
   so it cannot pay. Confirm or correct.
3. **S29, re-raised.** The child asks the same question. Is anything indivisible below one 1500 t
   launch unit? What are both headlines on a 1-ship and a 2-ship seed (break-even both ends, up-front
   bill, years until the fleet matches the one-unit seed's harvest)? Full text in
   `docs/solar_dive_asks_for_aim_repo.md`, S29.
4. **The headline seed's tonnage.** The paper prints 622 t at 9.86 R_sun (4.0 / 4.6 ships,
   $0.81 / 3.10 B) and 725 t at 4 R_sun (`tab:seed_amortization`, since parent `1adf379`). A
   parent scratch on a fresh clone of `c559cc7` takes `headline_report()`'s optima and forms
   `value_design`'s `seed_mass`. It gets **567 t** (push share 0.743, 3.68 / 4.23 ships) and
   **674 t** (0.693, 4.79 / 5.59 ships). Which is the seed at the paper's adopted headline (x1.2
   charge, 1.36 cm, track hold; `make disk-train-aim`)? If the track hold's 6.1 t and 11.7 t of ship
   mass, or anything else in ADR 0086/0087, changes the departing ships, give the figure with it.

## What the parent will do with the answers

Item 1 goes to the child as milestone 1's growth and price, and into the parent as a row in
`tab:no_sun_loop` if Seth wants it there. Item 2 decides one clause in the child's milestone
paragraph. Items 3 and 4 settle the seed sentence in both papers and, for item 4, the
`tab:seed_amortization` row. Nothing in the parent's headline waits on S63.
