# The Jupiter-only loop on plates, with no Sun dive: asks for both companions

Raised 2026-10-19. **Written to be copied verbatim** into `katzseth22202/aim_is_all_you_need`
(S41) and `katzseth22202/puffsat_impact_simulation` (S42). Register items **S41-S42**
(`docs/deferred_to_companion_repos.md`). The paper prints the ballpark below as `tab:no_sun_loop` in `sec:why_sun_dive`, flagged as its own rerun.

## The question (Seth, 2026-10-19)

Fly the Jupiter-only chain (`sec:jupiter_only_growth`, `growth_ledger`) with no Sun dive and no
nozzle, on the charge-pusher plates of ADR 0073:
- the growth push on the flat push plate at 2 Hz, 1 g;
- the departure on the holed bowl at 1 Hz, 0.25 g, with the stream nearly head-on.

Plates are light and are not temperature-limited, and no $1000/kg disks are needed. Does that
give an attractive growth cycle and seed cost without the Sun dive?

## The paper's ballpark

Method: `solar_dive_growth.fly_unit` steps 1-3 are copied unchanged, and the Sun stage is
removed. The departing stack, less 1% avionics, returns as the next wave. The role split, the
lob, the 2 Hz delivery, the seed and the gated rNPV are all yours.
- Gates: 95 / 85 / 90, with no Sun gate.
- Growth-wave ships pay the chain's mean 0.179 km/s split burn.
- Apoapsis: a 180 deg reversal (`apoapsis_methalox(180)`, 0.386 km/s).
- Stream: 164.5 deg to the thrust at 200 km, which is ~167 deg and 74-83 km/s at mid-burn.
  `hole_ve` has 180 deg runs, so this is interpolated.

Operating points are from CONTEXT (fly-and-park, the 2S lock).

| operating point | dep. excess | return v_b | growth | doubling | steady | break-even cheap / dear |
|---|---|---|---|---|---|---|
| exact 3S, best phase | 12.30 | 61.3 | 2.49 | 2.48 yr | $114 | $179 / $292 |
| 3S fly-and-park | 13.85 | 68.7 | 2.46 | 2.52 yr | $114 | $201 / $462 |
| 2S lock | 16.17 | 63.35 | 0.85 | none | | |
| exact 3S, departure at 0.5 g | 12.30 | 61.3 | 2.68 | 2.30 yr | $110 | $160 / $240 |
| Sun dive, 9.86 R_sun (paper headline) | 10.24 | 76 / 99 | 3.81 | 1.70 yr | $99 | $122 / $134 |

The Sun dive wins for four reasons:
- It departs slower (10.24 against 12.3 km/s).
- Its departure stream is at 130 deg rather than head-on.
- Its faster returns raise both Earth plates' v_e.
- Its seed is half as dear per kg and is divided over a 138x fleet rather than 23x.

## S41. Wanted (aim_is_all_you_need)

1. **The plate chain, properly.** Fly `growth_ledger`'s Jupiter-only chain on ADR 0073's plates:
   - the push on `push_ve` at 2 Hz / 1 g from the 2.43 km/s lob;
   - the departure on `hole_ve` at the visible sign's real angle and closing speed, at 1 Hz /
     0.25 g, with its finite-burn loss;
   - the apoapsis reversal, and each cycle's own split burn;
   - real ephemerides and the 2S / 3S cadence;
   - the 2 Hz delivery, and the gated rNPV with no Sun gate.
   Report growth, doubling, steady cost and both break-evens against the solar-dive headline.
2. **Pick the slug ratios for dollars**, as ADR 0073 does. The ballpark's optimum is k ~ 6.6 push
   and ~7.7-13 departure, not "relatively high". At ~60 km/s a higher k lowers v_e faster than it
   saves impactor. Say if the full chain disagrees.
3. **The departure rate.** At 0.25 g a 5.7-6.9 km/s burn lasts 45-56 minutes and loses
   0.9-1.3 km/s. The 2S lock's 8.8 km/s burn runs off `departure_loss`'s table. Give the trade
   against 0.5 and 1 g, which the plate allows.
4. **The seed at 12-14 km/s.** `seed_price_range` is $2400 / $10580 per kg at 12.3 km/s and
   $4274 / $25002 at 13.85. Is a stripped Starship the right seed there, or a gravity-assist route
   (`seed_route`)?
5. **Is there a faster unpowered return?** At a fixed 12.1 km/s departure, a 69 km/s return
   would give 3.21x and $151 dear (ballpark). Is any Jupiter-only closure faster-returning without
   a dearer departure, for example by choosing the phase on the plate ledger rather than the
   nozzle ledger?

## S42. Wanted (puffsat_impact_simulation)

1. **The bowl nearly head-on.** Confirm `hole_ve` at 160-168 deg and 70-85 km/s closing, between
   the 129.9 and 180 deg runs, at k = 7-14. Report the hole's share of the impulse when the
   impactor arrives through the bowl's back almost on axis.
2. **The push at 57-69 km/s.** `push_ve` at those closing speeds and k = 6-8 underpins a growth
   push that takes 36-40% of the unit. Confirm it is inside the runs, and check the sheet's
   heating at 2 Hz / 1 g (it should be milder than at 100 km/s).
