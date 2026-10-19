# The growth wave above 100 km/s: asks for `puffsat_impact_simulation`

Raised 2026-10-19. **Written to be copied verbatim into `katzseth22202/puffsat_impact_simulation`.**
Register item **S40** (`docs/deferred_to_companion_repos.md`). Responds to Result 13 / ADR-0064
(`docs/plume_cadence_answers_for_parent.md`) and Result 14 / ADR-0065
(`docs/departure_hole_answers_for_parent.md`), which the paper has taken.

## What changed

The paper flies every Earth push at 2 Hz and 1 g with ~100 um Kapton on the 12.2 t plate, and
the departure on the hole bowl at 1 Hz, 0.25 g. Result 13 ran the sheets at `V_CLOSE` = 100 km/s.
That matches the 9.86 R_sun headline, whose growth stream crosses 400 km at 99.2 km/s. It does not
match the rest:

| closure (return excess) | growth stream at 400 km | k_push | push v_e (calcs law) |
|---|---|---|---|
| 9.86 R_sun, 60 (headline) | 99.2 km/s | 7.07 | 36.7 km/s |
| 4 R_sun, 90 (headline) | 137.1 km/s | 6.67 | 53.0 km/s |
| 9.86 R_sun, 90 | 132.1 km/s | 7.93 | 44.7 km/s |
| 4 R_sun, 150 | 207.8 km/s | 8.21 | 68.4 km/s |

## The paper's ballpark (printed as its estimate)

Your `coated_sheet.py` with only `V_CLOSE`, `K_PUSH` and `VE_PUSH` changed. It reproduces your
96 / 38 / 17 kJ/m^2 and 572 K exactly at 100 km/s.

| closing | dose, u = 5 / 8 / 12 | bare 100 um face, u = 8 | 250 um, u = 8 | 100 um, u = 5 |
|---|---|---|---|---|
| 99.2 | 97 / 38 / 17 | 573 K | 528 K | decomposes through |
| 132.1 | 134 / 53 / 24 | 708 K | 648 K | through |
| 137.1 | 131 / 52 / 23 | 708 K | 648 K | through |
| 207.8 | 212 / 83 / 37 | 1045 K, 52 um lost | 950 K, 25 um lost | through |

The plate side, scaled from your `c(h) sigma v^2` with c = 0.65 at 2 m: a 100 um sheet puts
0.91 / 1.6 / 1.7 / 4.0 GPa on the face at 99 / 132 / 137 / 208 km/s, against ~1.5 GPa for HY-100
and ~2.5 GPa for maraging 300. So above ~130 km/s a thicker Kapton sheet runs cooler but hits
harder, and the paper sees no window.

Graphite, lumped (c_p held at 710 J/kg/K, front emissivity 0.85, same flux history): at 208 km/s
and u = 5, a 100 um film peaks at 1591 K and a 1 mm plate at 435 K. At 132 km/s, 1123 K and 385 K.
Gas met is ~0.01 g/m^2, so sputtering removes nanometres. The paper says the 4 R_sun loop and the
faster returns "probably need graphite sheets".

## S40. Wanted

1. **Result 13 at the real closing speeds.** Rerun the 2 Hz, 1 g sheet heating at 132, 137 and
   208 km/s with each row's k and v_e above. Confirm or correct the paper's ballpark.
2. **Is there a Kapton window at 137 km/s?** That is the thickness range that stays under the
   rating at u = 8 and under the face's allowable, on HY-100 / 4340 and on maraging 300. If there
   is none, say what face (thicker, layered, sprayed) would open one.
3. **Graphite growth impactors.**
   - What geometry works: a film, a thick plate, or compact disks like the Sun wave's?
   - The overtake law (`push_ve`) for graphite onto the polyethylene charge at 100-210 km/s. The
     bond toll differs from Kapton's.
   - If it is compact, the push plate's survival floor as a point blast at 7.35 MN s. ADR-0064's
     absorber-set 12.2 t assumed the planar sheet's even load.
4. **A bare compact impactor on the bowl.** The departure's impactors are compact, so a failed
   charge puts a compact body on the bowl, not a film. Extend S30/S31 to it: the peak, the spall
   and the abort spray.
5. **S36 stays open.** The plume's spread `u` still sets most of the dose at every speed.

---

# S44. Follow-up to Result 15 (raised 2026-10-19)

**Written to be copied verbatim into `katzseth22202/puffsat_impact_simulation`.** Responds to
`docs/fast_growth_wave_answers_for_parent.md` @ `f7cce80`, which the paper has taken: Kapton to
~100 km/s, dry carbon fabric above ~130 km/s at $100/kg, the bowl's bare hits settled by
geometry at 130 deg. S42 (`docs/plate_jupiter_loop_asks.md`) is still open.

## S44. Wanted

1. **Kapton in the 100-130 km/s band.** Nothing between 99 and 132 km/s has been run, and three
   closures the paper prints sit there. Each is the ledger's own k and `push_ve` on Kapton:

   | closure | growth stream | k_push | push v_e (calcs) |
   |---|---|---|---|
   | 9.86 R_sun, X 75 | 114.8 km/s | 7.45 | 40.9 km/s |
   | 4 R_sun, X 90, 5-day gap | 119.0 | 6.20 | 48.4 |
   | 4 R_sun, X 75 | 121.8 | 6.53 | 47.8 |

   For each, give the Kapton window at u = 5 / 8 / 12 on HY-100 and maraging 300 at the flown
   2 m standoff. If 4 R_sun X 75 holds on Kapton, it breaks even at $83 dear, against $88 for the
   carbon X 90 headline, and the paper would move.
2. **The bowl's capture with the charge at 2.5 F, at 117 deg.** Result 15 moves the charge out
   so a bare impactor clears the rim at 4 R_sun. `hole_ve` has only been run at 1.5 F. Please give
   the law at 2.5 F, and say whether the hole's share or the rim spray changes.
3. **Still open:** S36 (the plume's spread `u`), the push plate's S30 / S31 (a bare film on the
   flat plate, and its abort spray), and S42.
