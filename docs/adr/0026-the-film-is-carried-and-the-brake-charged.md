# The spray cup's film is carried as launched mass; the booster's larger brake is charged

Status: accepted (2026-10-06). Amends ADR 0025 §4 and its unpriced items. Paper:
`sec:vertical_lob`, `sec:spray_cup_film`, `sec:growth_ledger`, `sec:mass_interest`,
`sec:heat_shield_bill`, `tab:delivery_ledger`, `tab:l1_comparison`, `tab:growth_prices`,
`tab:seed_return`, `tab:seed_amortization`, `tab:plate_designs_cost`,
`tab:growth_ledger_doubling`, `tab:growth_ledger_ten_year`, `tab:growth_ledger_slug`,
`tab:doubling_ladder`.

## Context

`aim_is_all_you_need` @ `46ea0db` (its ADR 0043) answered S12 and the brake ADR 0025 left
unrecomputed. The film burns pulse by pulse out of the 1500 t unit at 4-6 kg per 12 MN s pulse
vapor-shielded, 28-33 kg unshielded; a push is ~1060 pulses, not 1200-1500. A 1.1 km/s climb
separates the booster near 140 km at 2.43 km/s, so holding the same 1.5 km/s (~9 g) crossing
takes a 1.58 km/s brake (was 1.39) and a 164 t reserve (was 144).

## Decision

1. **The lob charge is the braked one: x1.065 at 1.1 km/s and 380 s** (4-10% over 1.0-1.2 km/s
   and 350-380 s). Lob $26.6/kg lofted, $53.2 pessimistic; booster 1.15-1.32x Super Heavy.
   Reproduced with `make lob-brake`. Committed first as paper `c82070c`.
2. **The headline carries the film, shielded, at the heavy end: 6 kg per pulse**
   (`SPRAY_CUP_SHIELDED`). The film-in-the-book run (0.1% of PuffSat mass) undercounts it and is
   not printed. The author: "we should be honest/conservative with the numbers."
3. **Unshielded, 33 kg per pulse, is a labeled worst-case row** in `tab:plate_designs_cost`
   and a sentence in the text, not compounded into the pessimistic column.
4. **Solved methane's cheap-seed break-even is printed as $205, just over Suncatcher's $200.**
   No correlated-demand upside (a cheap seed implying faster learning on our plates) is
   priced or named; the author called it wishcasting.
5. **The plug keeps the book's film line** (no sim figure, S15), and the unmixed 0.57 downside is
   quoted before its film is charged (S14). Both are said in the text.

## Consequences

- Solved H2 doubles in 2.03 yr (was 2.02) and grows 28x in ten years (was 29); methalox 7.92 yr.
  Unshielded: 2.06 / 8.41 yr.
- Estimate steady cost $122 / $124 / $294 (H2 / CH4 / methalox), was $119 / $122 / $285.
  Break-even cheap / dear seed: H2 $192 / $377, CH4 $205 / $473, methalox $776 / >3000.
  Pessimistic $508 / $563 / $885. The dear-seed undercut of Starship to L1 is 2.6x or more.
- The seed is unchanged at 102-112 t; seed per fleet kg behind solved H2 is $12-329.
- Asks S14-S16 go back to the companions.
