# Jupiter-return pushes fly high: the growth wave at 400 km, the departure at 600 km

Status: accepted (2026-09-16 grill). Recorded because a later reader will ask why the paper's
200 km interception altitude does not apply to the Jupiter chain, and why the departure burn
gives up Oberth gain it could have had.

Interception altitude is set per arriving stream, not per customer. The 11 km/s LEO and 200 Mile
High Club streams stay at 200 km. Every Jupiter-return Earth encounter flies higher, and
data-center deliveries inherit the chain's altitudes because their cargo rides the same push.
The **growth wave** (overtake, plate) meets the craft at 400 km. The **departure wave** (head-on,
nozzle) meets it at 600 km, reached by a 1.7 m/s periapsis raise at the 20-day orbit's apoapsis.
Both are fixed. Neither moves on storm days.

Aim is not the reason for either. Air-drag lag lies along the approach line, as the plume's does.
The reasons are what a 57 km/s stream does to thin hardware. Drag heating goes as speed cubed.
At 200 km an inbound half-pass delivers 290 kJ/m^2 to a growth-wave bumper, the same as the 4 Hz
plume dose, and takes the ring's bare Kevlar spokes to 644-651 K, past aramid's ~523 K strength
limit. On the departure rod, drag on each 83 g guidance package acts as an axial push, which the
bridle caps at tension/15 = 7.3 mN; at 200 km a 0.01-0.04 m^2 package takes 9-36 mN and a line
goes slack.

## Considered options

- **Growth wave at 300 km, raised toward 350 km on forecast storms.** Heat and spokes pass on
  normal days, but a storm-day raise is a late retarget of 19-58 cm/s per 50 km. At 400 km the
  spokes stay at or under 464 K even at 10x density, so no raise is needed. The push is also
  165 m/s cheaper than at 200 km (10.785 km/s against 10.950); the lifting stage pays for the
  height.
- **Departure at 300-350 km.** Both fail the 10x density case on line heat or slack.
- **Departure at 400 km.** Holds at 10x with packages up to ~0.04 m^2 and saves 51-52 m/s in a
  finite-burn integration with ship drag, about 1.2% of departure PuffSats. Declined because the
  departure is the precision leg: uncorrected cross-line drift over the last 9 s is 4.7 mm there
  in a storm against under 0.2 mm at 600 km, and 600 km leaves package area free up to 1.5 m^2.
- **Departure at 450 km.** Saves ~0.9%; caps package area at 0.14 m^2 in a storm.
- **A storm-day switch for the departure.** Declined: it retargets the tight-aim leg 1-3 days out.

## Consequences

- The departure burn at 600 km needs 107-110 m/s more than at 200 km, about 2.5% more
  departure-wave PuffSats. The companion owes the compounded net as **S9**.
- The paper's other Jupiter-return speeds stay quoted at the 200 km reference altitude, with the
  offsets stated once.
- The lifting stage reaches the growth push by a booster-only **vertical lob** (430 km apex), which
  needs no boostback but must brake 1.33-1.38 km/s after separation to avoid a ~21 g vertical entry.
- Density multiples (3x, 10x) are sensitivity cases, not a forecast. Figures come from the gitignored
  probes `todos/data_center_interception_altitude.py` and `todos/vertical_lob_lift.py` on Vallado's
  exponential atmosphere.
