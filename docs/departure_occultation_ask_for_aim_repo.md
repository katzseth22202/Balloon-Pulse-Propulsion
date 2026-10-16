# Is the canted departure behind Earth? An ask for `aim_is_all_you_need`

Raised 2026-10-16. **Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`.**
Register item **S38** (`docs/deferred_to_companion_repos.md`). Nothing in the paper has changed
yet. The paper still prints the flown geometry (`sec:charge_pusher_cycle`, step 3: the stream
meets the ship "at about 101 degrees to its thrust axis").

## The concern

On the solar-dive charge pusher (ADR 0072), the departure wave's sheets come out from the Sun, so
near Earth they travel roughly away from it. They can reach the departing ship only if its
periapsis is on the side of Earth they arrive from, roughly the day side. If periapsis is downstream
of Earth, the sheets would have to pass through Earth to reach the ship.

`departure_nozzle_ledger` (`src/jovian_solar_dive_cycle.py:1399`) tries both mirror signs of the
departure hyperbola (`axis = aim +/- half_turn`). It keeps the one with the larger delivered
fraction. It uses velocities only, so it never places the ship relative to Earth.
`src/departure_visibility.py` (ADRs 0045, 0066) has exactly this check, but only the chamber chain
uses it. `solar_dive_growth._route` takes the sign from the ledger unchecked.

## What the paper's scratch check found

The check is planar and two-body, in your angle convention: from Earth's prograde, toward
`atan2(v_radial, v_t - v_earth)`, so +90 deg points away from the Sun. The thrust axis is the
periapsis velocity, so periapsis lies 90 deg from it, on the side the orbit's sense sets:
- sign +1 is the clockwise orbit, with periapsis at axis + 90;
- sign -1 is the counter-clockwise orbit, with periapsis at axis - 90.

A ship at 600 km is called blocked if it sits downstream of Earth's center and within
R_E + 100 km of the stream axis through Earth. That means within 68 deg of the stream's direction of
travel. The check sampled +-30 deg of arc about periapsis, about what the 8-10 minute burn sweeps.
Routes are `departure_route(9.86, 60)` and `departure_route(4.0, 90)`.

| Route | Sign | Thrust axis | Periapsis | From sunward | To stream travel | Blocked |
|---|---|---|---|---|---|---|
| 9.86 R_sun (stream toward 105.6 deg, 75.5 km/s) | +1 (flown) | 26.2 | 116.2 | 154 deg | 11 deg | **yes** |
| | -1 | -16.7 | -106.7 | 17 deg | 148 deg | no |
| 4 R_sun (stream toward 103.5 deg, 102.0 km/s) | +1 (flown) | 34.2 | 124.2 | 146 deg | 21 deg | **yes** |
| | -1 | -7.0 | -97.0 | 7 deg | 160 deg | no |

On the canted plate's own law (`StageLaws.earth_ve` at the headline `k_earth`), the visible sign is
no worse:

| Route, sign | Mean impact angle | Mean closing | v_e | Mass ratio |
|---|---|---|---|---|
| 9.86, +1 (flown) | 89.2 deg | 75.0 km/s | 11.24 km/s | 1.454 (4.21 km/s, k 5.21) |
| 9.86, -1 | 129.9 deg | 84.0 km/s | 11.87 km/s | 1.425 |
| 4, +1 (flown) | 76.5 deg | 98.8 km/s | 15.09 km/s | 1.342 (4.44 km/s, k 5.0) |
| 4, -1 | 117.0 deg | 107.9 km/s | 15.56 km/s | 1.331 |

That comparison is weak in one way. `earth_ve` holds `v_e / w` flat outside the two simulated
angles, so the -1 rows are extrapolated. Their gain is the higher closing speed, not a solved law.

## S38. Wanted

1. **Confirm or refute the occultation.** Run the flown solar-dive departures (both headline
   closures and the depth sweep) through `departure_visibility.visible_burn`, or an equivalent
   check. Use the push wave's own departure too, if it uses the same geometry. The paper's check could
   simply have the orbit sense backwards. Please state which side periapsis is on, relative to the Sun
   and to the incoming stream.
2. **If it is blocked:** make visibility a constraint in the solar-dive mirror-sign choice (and in
   `departure_nozzle_ledger` wherever else it feeds a flown route). Choose the sign on the canted
   plate's law rather than the magnetic-nozzle impulse law it was picked on.
3. **Check the turn.** The apoapsis methalox turn (`apoapsis_methalox`, about 0.24 km/s) rotates the
   orbit from the push axis onto the departure axis. Does the visible sense change the rotation it
   needs, or force the orbit's sense to flip? A flip from the push's own sense might not be cheap.
4. **The canted law at the new angle.** If the visible sign meets the stream at about 117-130 deg
   rather than 77-89 deg, say whether that needs a new canted-plate run from the impact sim. Pass the
   ask on if so. Until then, give the ledger on both the held-flat extrapolation and a pessimistic
   case: the 89 deg ratio at the old closing speed.
5. **Rerun the headline** on the visible sign: growth per cycle, doubling and dear-seed break-even at
   9.86 and 4 R_sun, against today's 3.60 / 1.77 yr / $104 and 4.92 / 1.43 yr / $67.

The paper's scratch scripts (`departure_shadow.py`, `departure_sign_cost.py`) are available on request.
