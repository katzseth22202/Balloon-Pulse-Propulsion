# A water bag on the overtake plate, with carried charge: ask S50 (for puffsat_impact_simulation)

Raised 2026-10-20 in `Balloon-Pulse-Propulsion` (after `5d63e81`). **Written to be copied into
`puffsat_impact_simulation`.** Nothing here is in the paper yet. Seth (2026-10-20) wants real
sizes for the slug ratio `k` and the plate before the companion `aim_is_all_you_need` builds a
ledger for the cycle (S51, `docs/iapetus_cycle_ledger_asks_for_aim_repo.md`).

**Answered 2026-10-21** (sim `1d7cedf`, Result 20, ADR-0071), carried as
`docs/iapetus_bag_plate_answers_from_impact_sim.md`. Seth's follow-up is S52
(`docs/shaped_plug_asks_for_impact_sim.md`): a shaped plug spreads the bag, the gun's bullet is
the backup.

## The cycle this serves

A new source of returning PuffSats: water mined on Saturn's moon Iapetus, shipped to Earth by a
single-use water-propellant nuclear thermal stage that burns at a low Saturn periapsis
(150,000 km, outside the main rings) and is then braked back and dropped into Saturn. The
PuffSats coast for about 3.7 years and overtake an Earth-launched ship at the 200 km interception
altitude. They push it to the paper's eccentric orbit (10.916 km/s at 200 km, the
`tab:mass_scenarios` row "PuffSats approach Earth from Jupiter and push a rocket into an elliptical
orbit"). Seed hardware for the next round rides that push.

Closing speeds (parent scratch model, circular coplanar planets, about 10% uncertainty):

| Arrival | Closing speed at 200 km | Why it matters |
|---|---|---|
| Reference | **51.1 km/s** | The cheap inward-plunge transfer the growth optimum picks |
| Sensitivity | 60 km/s | Intermediate |
| Sensitivity | 68-70 km/s | Head-on retrograde Hohmann arrival, the costlier transfer |

All three are **overtakes**: the PuffSat catches the ship from behind and its momentum already
points where the ship is going. The head-on departure chamber is not part of this ask.

## What is different from the current growth push

The paper's current Earth push flies a **floor-wide Kapton sheet** onto a polyethylene charge
(your Results 16-18; the plate is 63.4 t on an 8 m nitrogen spring at 2 Hz). A sheet the width of
the plate loads the plate nearly uniformly.

These PuffSats are **bags of water**, compact and mostly mass at the center. On rupture the pulse
spreads from roughly a point, so the face load is peaked on the axis and falls off with radius.
Seth's expectation: this needs a heavier plate, and possibly a **parabolic** one with the burst
near its focus, so the reflected flow leaves axially. The parent has not computed either.

Parent ballpark, to check rather than adopt. For a 25 kg bag at 51.1 km/s with `k = 8.5` and
`eta_jet = 0.775` on the paper's overtake law `I/(m w) = eta_jet sqrt(1+k) + 1`, the pulse is about
4.3 MN s against the sheet's 7.35 MN s. Its kinetic energy is about 33 GJ.

## The leverage the parent is carrying (to be replaced by your numbers)

Integrating the overtake law over the push gives, per kilogram of returned PuffSat,
`M_f/m = k / ((w/(w - v_f))^(k/B) - 1)` with `B = 1 + eta_jet sqrt(1+k)`, `w` the closing speed and
`v_f = 10.916 km/s`.

| Arrival | Bare plate (`eq:PuffSat_ratio`, f = 0.8) | k = 8.5, eta_jet = 0.775 | Best k (about 20) |
|---|---|---|---|
| 51.1 km/s | 6.7x | **10.3x** | 10.7x |
| 68 km/s | 9.4x | 16.0x | n/a |

The 10.3x moves the cycle's growth over 19 years from about 10x to about 23x (base case), so it
is load-bearing. The cost is that the lob carries `k` kilograms of charge per kilogram of
returned PuffSat.

## S50. Wanted

1. **Arrival state.** What a 25 kg water bag (about 0.36 m across as liquid) looks like when it
   reaches the plate at 51.1 km/s, for three cases. (a) Intact until contact. (b) Ruptured a
   set distance ahead by the paper's explosive or ice-wire release
   (`sec:explosive_puffsat`; the grid that caps fragments near 2.5 mm radius on the Jupiter
   push). (c) Partly frozen, since the bag spends about 3.7 years in deep space and the paper's
   sunlight melt (`sec:icy_puffsat`) may not finish. Give the cloud's radius and density profile at contact for each, or say which case
   cannot couple.
2. **The k sweep.** For the best arrival state from item 1, sweep the slug ratio from `k = 0`
   (the bare-plate control) through 8.5 to about 30. Report delivered impulse per kilogram of
   PuffSat, and `eta_jet` as your model defines it, at 51.1 km/s, with 60 and 68 km/s at a few
   `k`. Say what the charge should be (the polyethylene charge of the current push, sprayed water,
   or another) and where it should sit relative to the burst. The parent's optimum near
   `k = 20` assumes `eta_jet` does not fall with `k`. Does it?
3. **Plate shape.** Compare a flat plate with paraboloids of a few depths, the burst point at or
   near the focus. For each: impulse per kilogram (item 2's best `k`), the face's peak pressure
   and heat flux on and off axis, and how much of the plume leaves past the rim. Include the
   current 2.5 F bowl geometry (`sec:charge_pusher_plume`) as one case if that is cheap.
4. **Plate mass.** The areal density each shape needs where the load peaks, and the total plate
   mass on the paper's lossless-spring law (mass x stroke = 507 t m at 2 Hz / 1 g, 8 m stroke)
   or on whatever law the peaked load forces instead. Is the 63.4 t plate enough, and if not,
   what is?
5. **Aim tolerance.** A point burst off the axis tilts a paraboloid's exhaust and rocks the
   plate. Report the impulse direction error, and the rocking kick per metre of lateral miss.
   Use the same quantities as S48 item 5 so the two can be read together.
6. **Face survival.** Erosion per pulse at the peak, for the face materials already in your
   Results (maraging steel with the sprayed thermal layer), over a push of about 2000 pulses.

The parent needs items 2 and 4 first. They set the leverage and the plate mass that S51 prices.

Paper edits that wait on this: none yet. The Iapetus cycle is not in the paper; it waits on S50 and
S51.
