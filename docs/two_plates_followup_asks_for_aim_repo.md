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

---

# S43. Follow-up to ADR 0074 (raised 2026-10-19)

**Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`.** Responds to
`docs/two_plates_followup_answers_for_parent.md` @ `db158ed`, which the paper has taken.
`make solar-dive ARGS="--gaps"` and `ARGS="--sweep"` reproduce every printed figure here, except
item 3. The impact sim's Result 15 (`docs/fast_growth_wave_answers_for_parent.md` @ `f7cce80`)
also feeds items 1-2.

## What the paper did (Seth, 2026-10-19)

- The delivery plate's headline cap is 25 g, with 10 g ($130) and 50 g ($115) printed.
- The gap stays 10 days; 5 days is one sentence.
- Above ~130 km/s the growth sheets are **dry woven carbon fabric** (the sim's call, not a
  graphite film), charged at **$100/kg of body**. Your `graphite sheets $100/kg` row is the 4 R_sun
  headline: 5.71x, 1.30 yr, $75 steady, $87 / $88.
- Kapton is shown to hold at 99 km/s and to fail at 132 km/s, and 100-130 km/s is unrun. So
  `tab:charge_pusher_depth` prints both policies. The paper's rerun, each point re-optimized
  from `_SWEEP_START` with `sheet_body = 100`, at every point whose growth stream passes 100 km/s:

| r_p, X | stream | growth | doubling | steady | BE cheap / dear |
|---|---|---|---|---|---|
| 4, 60 | 107.5 | 4.81 | 1.45 | $86 | $102 / $107 |
| 4, 75 | 121.8 | 5.46 | 1.34 | $79 | $92 / $94 |
| 4, 90 | 137.1 | 5.76 | 1.30 | $76 | $87 / $88 |
| 4, 110 | 159.1 | 5.61 | 1.32 | $74 | $85 / $86 |
| 4, 150 | 207.8 | 3.85 | 1.68 | $82 | $104 / $117 |
| 6, 75 | 117.9 | 4.83 | 1.44 | $83 | $99 / $102 |
| 6, 90 | 133.9 | 4.79 | 1.45 | $81 | $96 / $100 |
| 8, 75 | 115.9 | 4.23 | 1.57 | $88 | $108 / $115 |
| 8, 90 | 132.6 | 3.94 | 1.66 | $88 | $111 / $121 |
| 9.86, 75 | 114.8 | 3.72 | 1.73 | $94 | $121 / $134 |
| 9.86, 90 | 132.1 | 3.27 | 1.92 | $97 | $134 / $163 |
| 9.86, 110 | 157.8 | 2.33 | 2.69 | $121 | $261 / $494 |
| 15, 75 | 113.8 | 2.49 | 2.49 | $123 | $223 / $356 |

## S43. Wanted

1. **Adopt the sim's re-derived overtake law.** `fast_wave_law.csv` gives `push_ve` 1-4% below
   yours at 99-137 km/s (35.5 against 36.7 km/s at 99.2, k 7.07) and 9% below at 208 km/s. Most
   of the low-speed gap is your linear-in-log-k interpolation between the k = 5 and 10 rows. Rerun
   both headlines and the sweep on it, and say how far growth and the dear break-even move.
2. **Make the sheet material a function of the growth stream.** Charge carbon fabric at
   $100/kg by default above 130 km/s. Carry the 100-130 km/s band as a switch (Kapton / carbon),
   so the sweep prints both, as the paper does. Confirm or correct the table above. If you have a
   citable bulk price for dry spread-tow or triaxial carbon fabric, use it. The paper calls $100/kg
   its own hypothesis, between bulk tow (~$34/kg) and retail fabric (~$165/kg).
3. **The 8 R_sun optimum.** Your answer's sweep summary says 8 -> X 60 (4.13, $107), but your
   own sweep table, rerun here, has X 75 at $80 / $102. The paper prints X 75 at $102. Which is
   right?
4. **One number at 9.86 R_sun, X 60.** The headline prints 3.80x and the sweep 3.81x, from
   different optimizer starts (`HEADLINE_STARTS` against `_SWEEP_START`). Please start the
   sweep's headline points from `HEADLINE_STARTS` so the two agree.
5. **Propagate the push plate's disposal with the Moon.** The 4.2 m/s nudge at a 385,000 km
   apoapsis is two-body. The paper says the 100 km perigee is unpropagated.

---

# S45. Size the Earth plates on a lossless spring (raised 2026-10-19)

**Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`.**

## The problem

`_inertia_plate` (and ADR-0064's absorber-set plate) sizes each Earth plate by
`m_p = I^2 / (2 s M a)`. That is a plate brought to rest within each pulse by a constant-force
absorber, which must dissipate the plate's kinetic energy `I^2 / (2 m_p)` every pulse:

| plate | per pulse | power | per push / burn | per kg of plate |
|---|---|---|---|---|
| growth push, 12.2 t, 7.35 MN s at 2 Hz | 2.2 GJ | 4.4 GW | 4.4 TJ (2000 pulses) | 363 MJ/kg |
| departure bowl, 13.2 t, 1.97 MN s at 1 Hz | 0.15 GJ | 0.15 GW | 0.28 TJ | 21 MJ/kg |
| delivery, 51 t, 7.35 MN s at 2 Hz | 0.53 GJ | 1.1 GW | 1.1 TJ | 21 MJ/kg |

Steel vaporizes at ~7 MJ/kg, so no dissipative absorber of that mass survives. The paper's own
`sec:pusher_plate_damping` already requires a nearly lossless gas spring tuned across pulses: the
plate never stops, and each pulse reverses its swing. Its law, checked here by direct integration
(stroke to under 1% at theta = 2 pi / 3; exact for a heavy craft; theta must use the reduced mass,
so theta = pi is the edge of contact), is

    peak / mean = (theta/2) / sin(theta/2)
    stroke      = (M a / (m nu^2)) tan(theta/4) / (2 theta)

At theta = 2 pi / 3 that fixes `m x stroke = 0.138 F / nu^2`, with F the mean thrust, whatever g cap
is chosen. Cargo then sees ~1.2x the mean (under 2 g at the delivery's end), so the delivery's g
cap (ADR 0074 item 2) stops mattering.

## The paper's ballpark (Seth chose an 8 m stroke, 2026-10-19)

| plate | m x stroke | at 8 m | ledger now |
|---|---|---|---|
| growth push (2 Hz, 14.7 MN) | 507 t m | 63 t | 12.2 t |
| departure bowl (1 Hz, 1.97 MN) | 272 t m | 34 t | 13.2 t |
| delivery (2 Hz, 14.7 MN) | 507 t m | 63 t | 51 t |

Seth's suggestion: one spring and one moving assembly for both growth-unit legs. The push plate and
the bowl fly up together; as one 63 t assembly the departure needs only 4.3 m of the same stroke.

## S45. Wanted

1. **Replace `_inertia_plate` with the spring law** above, the stroke a parameter (default 8 m,
   theta = 2 pi / 3), for the push plate, the bowl and the delivery plate. Keep the bowl's blast
   floor as a minimum. Rerun both headlines, the sweep and the sensitivities.
2. **The shared assembly.** Fly the push plate and the bowl on one spring as one moving mass, with
   whatever stays attached for the departure charged to it. Compare it against two separate springs
   (the push plate left in the parking orbit as now). Report which grows faster and is cheaper.
3. **The bags' mass.** Charge the gas spring itself. Peak gas `PV` is fixed at `gamma F^2 / k` (the
   paper's form). A fiber bag needs at least ~3 PV rho / sigma; the paper used 2.5 GPa at
   1600 kg/m^3 with a safety factor of 2.
4. **Drop the delivery g-cap rows** (10 / 25 / 50 g) once the spring law is in, or say what they
   mean on it.
