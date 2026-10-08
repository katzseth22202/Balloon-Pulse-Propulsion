# The ledger and cost book fly the survivable methane chamber, priced by its mass

Status: accepted (2026-10-08). Completes ADR 0027 §5 (tables flagged until S17). Paper:
`sec:heat_shield_bill`, `sec:mass_interest`, `sec:one_chamber`, `sec:growth_ledger`,
`sec:spray_cup_film`, `tab:delivery_ledger`, `tab:l1_comparison`, `tab:doubling_ladder`,
`tab:seed_amortization`, `tab:growth_prices`, `tab:seed_return`, `tab:plate_designs_cost`,
`tab:one_chamber`, `tab:growth_ledger_doubling`, `tab:growth_ledger_ten_year`,
`tab:growth_ledger_slug`; superseded labels on `tab:wall_pairing_doubling` and
`tab:rod_2p5kg_doubling`.

## Context

`aim_is_all_you_need` @ `a45604d` (its ADR 0044) answered S17, and @ `502a64f` took the parent's
S21 patch so its rows carry the spray cup's film like every other table. The impact sim @
`79e40d9` / `2491d15` answered S20: the 117 kg per pulse is a 7000 K charge, lighter per rod
kilogram than the sphere's because the thinner gas dissociates more.

## Decision

1. **Headline:** methane, A/A* = 300, 24 kg pitch (the high wall-heat edge): 2.78 yr doubling,
   10.5x in ten years, $162/kg steady, $340 / $810 break-even (cheap / dear seed). Methane rows
   lead every table; hydrogen keeps its rows, marked wall unverified (S18).
2. **The chamber is priced by its mass** (author's choice). The book's $40M first / $3M floor /
   $200M pessimistic were set for the 21.2 t sphere; the 62.9 t chamber is 2.97x, so $119M /
   $8.9M / $594M. Per unit it would be $138 and $251 / $723.
3. **Corrections the S17 answer made, adopted:** the departing stack is 780-820 t, not 500-600 t;
   2900-4500 pulses over 24-37 min; the fixed-direction finite-burn loss (charged since aim ADR
   0032) is 7-12% of the burn, not the sim's steered 3-5%.
4. **`tab:delivery_ledger` changes** although the handback first said it would not: its
   departure-hardware line is the chamber each reinvested growth unit expends.
5. **Claims that flipped, reworded rather than defended:** at 30% cost of capital methane would
   now rather liquidate (steady/liquidation 0.97); methane at half its ceiling does not grow; at
   pessimistic prices methane ($1073) is dearer than methalox ($885); methane misses Suncatcher's
   $200 on either seed and Starcloud's $500 on the dear seed; hydrogen leads methane at every
   ceiling share (the rows no longer compare like with like).
6. **Sphere tables kept as a record**, labelled superseded.

## Consequences

- Cells the companion has no target for were run in a scratch driver on its own functions
  (`todos/survivable_parent_drivers/`): methane behind the plug, the 0.84 plate and the
  unshielded cup; the k <= 10 and ceiling-share grid; odds, rate, lob, package and Earth-loop
  sensitivities priced by mass; water slugs; the 10-day orbit; grow-or-harvest. The paper says
  "run on its functions without a target yet" at each. Ask S22.
- The longest two-synodic departures fire up to 4470 pulses, 6% past the 4200 the wall was
  checked for. Printed in `sec:one_chamber`; ask S23 to the impact sim.
- Not changed: `tab:ntr_departure` and its prose (the synodic-lock model of the 200 m^3
  chambers, a different calculation), and the push-ratio sentence in `sec:growth_ledger`'s
  unpriced list (8.3-8.8 t per t, measured on the old chambers).
