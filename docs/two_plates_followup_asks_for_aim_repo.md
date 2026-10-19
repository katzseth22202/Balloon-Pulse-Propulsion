# The two-plate cycle on one cadence: follow-up asks for `aim_is_all_you_need`

Raised 2026-10-19. **Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`.**
Register item **S39** (`docs/deferred_to_companion_repos.md`). Responds to ADR 0073 and
`docs/two_plates_and_1g_push_for_parent.md` @ `a27448e`, which the paper has taken.

## What the paper did

`make solar-dive ARGS="--sweep --child"` reproduces ADR 0073 exactly here. The paper then made
three choices (Seth, 2026-10-19):

1. **One cadence for every push.** The growth push (inbound) and the L1 delivery both fly 2 Hz at
   1 g from the 2.43 km/s lob. The departure (outbound) stays 1 Hz at 0.25 g on the bowl. The
   delivery's sheets fly through the same plume as the growth push's, so the 4 Hz delivery the
   ledger still flies would cook them (S37).
2. **The headline is the cheapest closure at each depth:** 9.86 R_sun at a 60 km/s return and
   4 R_sun at 90 km/s. ADR 0073's `HEADLINES` (90 and 150 km/s) are printed as the
   "faster returns" rows of a new table (`tab:charge_pusher_fast`).
3. **The faster growth waves probably need graphite sheets.** See S40 to the impact sim.

The paper prints figures from a paper-side rerun of your code, starting the optimizer from
`replace(HEADLINE_STARTS[key], slow_delivery=True)`, plus the sweep with `Design` defaulting to
`slow_delivery=True`. Nothing else was changed. Those figures are the reproduction target:

| closure | k push / dep / Sun / delivery, arc | growth | doubling | steady | break-even cheap / dear |
|---|---|---|---|---|---|
| 9.86 R_sun, 60 | 7.07 / 12.67 / 20.0 / 5.33, 4.92 h | 3.81 | 1.70 yr | $98.6 | $122 / $134 |
| 4 R_sun, 90 | 6.67 / 12.07 / 20.2 / 5.00, 2.17 h | 5.72 | 1.30 yr | $78.2 | $88 / $89 |
| 9.86 R_sun, 90 | 7.93 / 13.89 / 20.0 / 6.67, 5.11 h | 3.27 | 1.92 yr | $102 | $139 / $171 |
| 4 R_sun, 150 | 8.21 / 13.74 / 20.0 / 7.18, 2.31 h | 3.85 | 1.68 yr | $88 | $110 / $124 |

Depth sweep, dear optimum per depth: 4 -> 90 km/s (5.72, $89); 6 -> 90 (4.78, $102); 8 -> 75
(4.22, $117); 9.86 -> 60 (3.81, $134); 12 -> 60 (3.43, $158); 15 -> 75 (2.49, $380).

## S39. Wanted

1. **Make the 2 Hz delivery the default** (`slow_delivery=True`), re-optimize the headline
   closures and the sweep on it, and confirm or correct the table above. Please make the
   headline closures the paper's (60 and 90 km/s) and keep 90 / 150 as the comparison.
2. **Resize the delivery plate for the 2 Hz pulse.** `DELIVERY_PLATE` is still the child's 156 t
   plate and absorber, sized for the 4 Hz, 12 MN s pulse. At 7.35 MN s the absorber bound
   `I^2 / (2 s M a)` falls as `I^2`, about 0.38 of the 4 Hz value at the same peak. The paper's
   estimate is that the 156 t plate on a 2 m stroke peaks at 6-8 g over ~85 ms per pulse. Please
   set the delivery's g cap from the data-center cargo (the paper cites a 25 g, 10 ms rating for a
   rack server), size the plate to it, and report its mass, peak g and pulse length.
3. **Print both stream speeds.** "Earth wave ~100 km/s" in ADR 0073 is the departure stream at
   600 km. The growth stream at 400 km is faster, because those ships come home ten days early:
   99 / 132 km/s at 9.86 R_sun (60 / 90 km/s returns) and 137 / 208 km/s at 4 R_sun (90 / 150).
   The sheet physics depends on the growth stream, so please print it in `headline_report` and
   the sweep.
4. **Price graphite growth sheets.** At 137 km/s and above, 100 um Kapton passes its rating and
   overloads the plate (S40). A graphite sheet body is a commodity film, not a $1000/kg Sun disk.
   Its steering packages are already priced. Please add `sheet_body` as a graphite price with a
   source if you have one, and a sensitivity. The paper-side bound: every sheet body at $100/kg
   moves the dear break-even from $171 to $184 at 9.86 R_sun, 90, and from $124 to $132 at 4 R_sun,
   150. Once S40 returns the point-blast plate floor for compact graphite impactors, carry the
   heavier push plate too.
5. **Dispose of the push plate.** It is left in the 10-day orbit with its perigee near 400-460 km,
   which crosses low orbit every ten days. The paper says a ~4 m/s nudge at apoapsis (385,000 km)
   drops its perigee to 100 km (our two-body estimate). Please confirm and charge it, even if it
   rounds to zero.
6. **Two sensitivity rows change the footing.** On a `slow_delivery=True` design, "lob climb not
   charged" and "push at 3.26 g" print a steady cost of $71-76 against the headline's $99, because
   they also drop the delivery's climb. Please make each row change only what it names.
7. **`corrections_report` is fixed to 90 / 150 km/s.** The paper had been quoting those inputs
   (4.34 km/s burn, 15.07 km/s mirror, 6.72 R_J) against its 60 km/s headline. It now says so.
   Please print the report for the flown headline as well (4.21 km/s, 15.05 km/s, 6.79 R_J at
   9.86 R_sun, 60).

8. **Make the growth-to-departure gap a parameter** (added 2026-10-19, Seth). `PARKING_DAYS` is
   frozen into the defaults of `departure_burn`, `apoapsis_methalox` and `push_route` when
   they are defined. `push_route` also sits behind `lru_cache`, so overriding its default does
   nothing: a first paper-side run at 3 days silently kept the 10-day growth wave. Please thread
   the gap through `Design` (or the closure key) to every use, add `--parking-days` to
   `make solar-dive`, and sweep 3 / 5 / 10 days at both headline depths. The paper-side run,
   with `push_route` called explicitly:

   | gap | turn | growth stream | growth | doubling | steady | BE cheap / dear |
   |---|---|---|---|---|---|---|
   | 9.86 R_sun, 10 d | 0.33 km/s | 99.2 | 3.81 | 1.70 | $98.6 | $122 / $134 |
   | 9.86 R_sun, 5 d | 0.54 | 87.1 | 3.71 | 1.73 | $96.2 | $118 / $131 |
   | 9.86 R_sun, 3 d | 0.76 | 82.6 | 3.52 | 1.81 | $97.1 | $121 / $136 |
   | 4 R_sun, 10 d | 0.31 | 137.1 | 5.72 | 1.30 | $78.2 | $88 / $89 |
   | 4 R_sun, 5 d | 0.50 | 119.0 | 5.60 | 1.32 | $76.4 | $85 / $87 |
   | 4 R_sun, 3 d | 0.71 | 112.3 | 5.36 | 1.35 | $76.3 | $85 / $87 |

   The gap acts through geometry. Arriving `d` days early means crossing 1 AU about `d` degrees
   earlier in Earth's orbit, which a near-Sun hyperbola does only by straightening: X 60 -> 87.4
   swings 139.3 -> 129.7 deg past perihelion. At 4 R_sun a 5-day gap brings the growth stream to
   119 km/s, where the sim's model keeps 100 um Kapton under its rating (640 K at u = 8) and the
   plate under HY-100's allowable (1.31 GPa), so the graphite swap (item 4, S40) may not be needed
   there.

The paper's figure sheet is `todos/two_plates_figures_2026-10-19.md` on request.
