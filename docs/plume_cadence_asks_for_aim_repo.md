# The 1 Hz growth push: asks for `aim_is_all_you_need`

Raised 2026-10-16. **Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`.**
Register items **S33-S35** (`docs/deferred_to_companion_repos.md`). The paper prints ballpark
figures for all of this in `sec:charge_pusher_plume` (commit `f1bb191`), labelled as the paper's own
estimates. These asks are to replace them with your numbers. The gas-side asks (the plume's spread
and the sheet's heating) go to the impact sim as S36-S37, in
`docs/plume_cadence_asks_for_impact_sim.md`.

## Why we are asking

The overtake push at 400 km is priced at the child's schedule, 12 MN s per pulse at 4 Hz, 48 MN,
about 300 s (`PULSE_IMPULSE`; paper `sec:vertical_lob`). Each 100 km/s Kapton sheet flies face-on
through the gas of the pulses before it, which the flat plate throws back up the stream. On the
paper's expanding-cloud model (`sec:jovian_plume_encounter`) at 4 Hz:

- the reference dose is 251 kJ/m^2 (one-axis spread u = 8 km/s; 114-635 kJ/m^2 over u = 12-5);
- a 50-88 g/m^2 sheet would rise 2600-4600 K, passing Kapton's 400 C rating 180-310 ms before impact;
- a 100 um Kevlar strand would rise ~1600 K.

At **1 Hz and 1 g mean** (14.7 MN s per pulse on the 1500 t unit) the reference dose is 19 kJ/m^2,
and the sheet rises 190-340 K. At constant thrust, dose falls in proportion to cadence. Drag is
harmless at either cadence (a ~0.1 ms delay along the approach line).

1 Hz is not free. The paper's estimates of what it costs are below. Each one is a quick scratch
calculation, not a solved figure.

## S33. The 1 g push from a faster lob

The paper's scratch integration was 2D, with no Earth rotation and no drag. Thrust was held in one
inertial direction, along the stream: 1 g on the starting 1500 t, 38.4 km/s of impulse per kg
expelled (`law.push_ve(6.74, 100)`), ending at the 10-day orbit's energy. Rows:

| Climb speed at 400 km | Burn | Lowest altitude | Final periapsis | Mass ratio |
|---|---|---|---|---|
| 0.75 km/s (today) | below 100 km at ~380 s | - | - | - |
| 2.25 km/s | 980 s | 393 km | 268 km | 1.333 |
| 2.5 km/s | 970 s | 400 km | 478 km | 1.330 |
| 3.0 km/s | 954 s | 400 km | 858 km | 1.322 |
| 0.75 km/s at 3.26 g (the 4 Hz push) | 295 s | 400 km | 393 km | 1.325 |

Tilting the thrust upward from horizontal at the start never worked; every tilted case ended with
periapsis below the ground.

Wanted:
1. Rerun this on `lob_rise.push_track` (or the ledger's own push model) with the stream's real
   geometry, Earth rotation and drag. Give the least climb speed at 400 km that keeps the unit on the
   stream at 1 g and 1 Hz, and the push's mass ratio and finite-burn loss.
2. The booster's lofted mass at that climb speed. Unbraked, `lofted_mass` gives 1516 t at 0.75 km/s
   and 1086 t at 2.5 km/s (5000 t booster, Isp 380 s), 28% less.
3. **The booster's return. This is the part that may not close.** At 2.5 km/s the booster separates
   near 191 km at 3.16 km/s (against 133 km at 2.32 km/s today). Falling from rest at 191 km, it
   still crosses 60 km near 1.57 km/s. So `brake_dv` returns NaN (no brake at separation meets
   the 1.5 km/s / ~9 g entry rule), and `braked_lob(2500.0)` does not finish. Unbraked, it crosses at
   3.5 km/s, a peak near 39 g (scaling the paper's 21 g at 2.6 km/s as v^2). Please price a return that
   works. Options we see: a two-burn brake (one at separation, one on the way down), an entry at
   10-12 g, or a lower separation with a longer upper-stage climb. Give the brake reserve and the
   lofted mass for each.
4. Is there a cheaper middle cadence? Give 2 Hz at 2 g in the same terms. The plume dose there
   (14.7 MN s pulses) is ~75 kJ/m^2 at u = 8, which overheats thin Kapton, so 2 Hz needs a thicker sheet (S37).

## S34. The plate and absorber for 14.7 MN s pulses

The paper's scratch figures:
- The survival floor is `_plate_for` scaled to the 1.22x pulse: ~47 t (41 t at 12 MN s).
- On a constant-force absorber, a plate of mass m_p taking impulse I and stopping over stroke s
  pushes the unit with I^2/(2 m_p s). A 16 g peak on the 1500 t unit then needs m_p s ~ 460 t m, about
  a 10 m stroke on the 47 t plate. On `ABSORBER_STROKE` = 2 m it peaks near 78 g.
- A linear spring doubles the peak for the same stroke. The paper notes this, but no row prints it.
- A 16 g peak at a 1 g mean is a pulse ~100 ms long.

Wanted:
1. The least plate-plus-absorber mass for the 1 Hz, 14.7 MN s push at peak caps of 16 g and 100 g
   (the ledger's `G_CAP`), on the paper's gas-spring model (`sec:pusher_plate_mass_stroke`, spring
   tuning theta) rather than the impulsive bound above.
2. What a 10 m stroke costs in gas-spring mass and structure.
3. Whether the same plate still serves the canted departure at its ~3.7 MN s pulse.

## S35. Rerun the ledger on the 1 Hz push

With S33 and S34 in hand: the growth per cycle, the doubling time and the break-even (cheap and dear
seed, 9.86 and 4 R_sun) with the 1 Hz push charged:
- the faster lob and its booster return;
- the longer stroke and the plate;
- the ~970 s burn's fixed-direction loss.

Against the 4 Hz headline (3.60 per cycle, 1.77 yr, $104/kg dear seed at 9.86 R_sun).

Also the **L1 delivery** at 1 Hz, if the delivery adopts it. Data-center hardware rides that push.
Rack servers are rated for short knocks, for example 25 g for 10 ms half-sine operating, mid-rack
(Lenovo ThinkEdge SE455 V3), a speed change of about 1.6 m/s. A 100 ms, 16 g pulse is about 10 m/s,
near 5 Hz, felt as a steady 16 g about a thousand times per push. Please give the delivery's peak g
at 1 Hz on the child's plate, and the plate mass that holds it to 3, 6 and 16 g.

The paper's scratch scripts are available on request (`sheet_plume.py`, `slow_lob.py`,
`cadence_trade.py`).
