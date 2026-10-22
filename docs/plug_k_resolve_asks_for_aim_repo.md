# Re-solve k on the shaped plug's catch and backup: ask S55 (for `aim_is_all_you_need`)

Raised 2026-10-22 against aim `80dceb6`. **Written to be copied verbatim into
`katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has. Register
entry: S55 in `docs/deferred_to_companion_repos.md`. It follows your S51 answer (carried here as
`docs/iapetus_cycle_answers_from_aim_repo.md`) and the impact sim's Result 21 (S52, carried as
`docs/shaped_plug_answers_from_impact_sim.md`, sim `2992448`, ADR-0072).

Same ground rules as your own handbacks. Neither document is the source of truth. If a number here
looks wrong, say so rather than working around it.

## Why this ask

Your S51 answer chose **k = 4 on the compact plug**, its lowest run, because "low wins". k is the
plug's mass as a multiple of the bag's 25 kg. That choice priced the plug only as mass, with the
backup at a placeholder miss rate p = 5% and a backup failure q = 1e-3. Result 21 replaces both
placeholders, and k = 4 fails on both.

- **The catch is small at low k.** The catch radius, the largest lateral miss that still lands
  the whole bag on the plug, is the plug's radius less the bag's 0.18 m. It is 0.04 m at k = 4
  and 0.14 m at k = 8.5. The gun fires whenever the predicted miss exceeds it.
- **The backup fails at low k.** At k = 8.5 a bullet meeting the bag 46 m out spreads it enough
  that the plate holds (1.80 GPa against maraging's 2.3). At k = 4 no tested meeting holds
  (2.41 GPa at 31 m, 3.04 GPa at 46 m). There a backup costs the plate.

The paper prints your S51 result as `tab:saturn_cycle`. The solar dive won every cell by a wide
margin, so the paper expects the headline to survive. The Saturn numbers will move, and they
get reprinted from this answer.

The companion ask S54 to the impact sim sweeps meeting distances out to 120 m at k = 4-6. It may
lower the floor on k. Until it lands, price both policies (below).

## Result 21's numbers to carry

The plug is ice (917 kg/m^3), a cylinder twice the bag's depth (0.726 m) at 2 F on the delta/D
0.5 paraboloid. Its radius is `r = sqrt(25 k / (917 pi 0.726))` m: 0.22 m at k = 4, 0.32 m at
k = 8.5, 0.42 m at k = 15.

| k | leverage (frozen edge) | graphite charged | catch c | plate | graphite a push |
|---|---|---|---|---|---|
| 4 | 8.18x (7.32) | 7.88x | 0.04 m | 26.6 t | 12-35 t |
| 8.5 | 8.81x (7.65) | 8.74x | 0.14 m | 33.3 t | 2.9-8.4 t |
| 15 | 8.39x (7.37) | 8.37x | 0.24 m | 38.7 t | 0.8-2.3 t |

The compact column (your S51 base) stays as the fallback row: 8.12x at k = 4, 7.20x at 8.5.

- **Backup rate:** `p = exp(-c^2 / 2 sigma^2)`, with sigma the track error per axis at the plug
  after its last ~100 ms of steering. Nobody has sized sigma. Carry 3, 5 and 10 cm as labelled
  rows. At k = 8.5, 5% needs 5.6 cm.
- **A backup that holds** (k >= 8.5): the plug is spent, the pulse gives 4.16x (2.50 MN s), the
  liner takes up to 28-84 kg of graphite. The gun is ~1 km/s and fires 2.2 km out.
- **A backup that fails** (k < 8.5 until S54): the plate and its ship are lost, as in your
  residual plate-loss row.

## S55. Wanted

1. **Swap in Result 21.** Replace the push band with the lens curve above, interpolated over
   k = 4-15, with the graphite-charged leverage as the base and the frozen edge as a row. Use the
   27-39 t plate on the spring law and the liner per push. Keep the compact column as a fallback
   row.
2. **The backup from the catch.** Replace p = 5% with `p(k, sigma)` above, at sigma = 3, 5 and
   10 cm. On a backup that holds, charge a spent plug and the 4.16x pulse. Keep q = 1e-3 as the
   chance the gun also fails.
3. **Two policies across the unrun band.** Policy A: the backup fails below k = 8.5, so every
   backup there costs the plate (q = 1). Policy B: the backup holds down to k = 4 at Result 21's
   k = 8.5 cost (the outcome S54 is testing). Print both.
4. **Re-solve k** on the gated break-even (10%), the 4% loan and steady cost, for each policy and
   sigma. Report the chosen k and the plug line in $/kg at it.
5. **Reprint the S51 headline cells** at the new k: the water NTR (Ledger A and B), the kept
   reactor plus methalox at Phoebe, and the no-nuclear-near-Earth row, each against the solar
   dive's $143 / $86 at the eccentric orbit. Say plainly if any Saturn cell now beats the dive.
6. **What sigma has to be.** The largest sigma at which the chosen k's backup adds under $1/kg,
   and under 1% to the best Saturn cell.

Items 1, 4 and 5 first. They set what `tab:saturn_cycle` reprints.
