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
