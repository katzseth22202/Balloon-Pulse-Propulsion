# The staged path's co-flyer is a permanent tracker platform, not a reused rocket

Status: proposed (2026-08-12 grill; the delta-v budget is a hand calculation, and the
platform's optical sizing is inherited unchanged from ADR-0003)

`CONTEXT.md` has said that the co-flying tracker is the reused launch rocket, with the explicit
warning *"Avoid: treating it as a dedicated new satellite (it is the launch rocket, reused)."*
That holds for `sec:starship_safelaunch`, where Starship lifts the PuffSats and then flies along
with them. It does not hold for the staged crewed launch of `sec:periapsis_challenges`, because
there **is no launch rocket to reuse**: the PuffSats come out of a staging carrier already in
orbit, and the crew vehicle's reusable ground launcher (line 752) gives only a low-speed initial
nudge and never approaches the 10.9 km/s needed to fly alongside. We decided the role is filled
by a **permanent, refuelable tracker platform** parked in the staging ellipse, distinct from the
mass carriers.

This needs recording for two reasons. It contradicts a standing instruction in the glossary, so
a future reader will think it is a mistake. And it looks like it reopens a decision that was
already made and should not be reopened.

## Why this does not reopen the coordinator-node rejection

The 2026-06-30 resolution rejected a dedicated **per-mission** co-flying coordinator satellite
and redistributed its work into the off-board nav assets. It did not reject shared
infrastructure. The apogee nav constellation, accepted in the same breath, is permanent shared
infrastructure that no single mission owns. A tracker platform serving many carriers across many
waves lands on the accepted side of that line, not the rejected one. The distinction that
matters is per-mission-expendable against permanently-shared, not dedicated against reused.

## Why the platform is separate from the carrier

The tempting simplification is to let the staging carrier be its own co-flyer, since it deployed
the PuffSats and is therefore already in the right neighbourhood. We rejected it on lifecycle
mismatch. Waves double every re-intercept cycle, so carriers proliferate, and a carrier is a
cheap tank that empties. A half-metre-class telescope on every emptied tank is the wrong place
to spend. A carrier's mass and centre of gravity also shift by most of their value as it
dispenses, which is an unhelpful property in a metrology platform.

The null option, dropping the co-flyer from staged flights and leaning on the target-side array
alone, was considered and rejected because ADR-0003 gives the co-flyer the entire mid-course
from deployment down to the 2 to 3 second handover.

## Budget

The platform never leaves the staging ellipse.

- Parks at a drag-free perigee (~1000 km, pending the lunisolar drift number owed by ADR-0004),
  drops to a ~200 km operating perigee for the push, and returns. About 26 m/s each way.
- Call it 50 to 150 m/s per flight all in. Under 3% of vehicle mass per flight at methalox
  exhaust velocity, so roughly 30 flights on a propellant load equal to dry mass.
- The 200 km operating perigee against the PuffSats' 50 km disposal perigee is a 150 km
  **radial** offset bought for about 5 m/s at apogee. ADR-0003's geometry rule requires it be
  paired with a comparable along-track offset, since a purely radial vantage is blind in the
  radial miss axis.
- Refuelling rides up as a dedicated propellant consignment in each wave's payload, swapped as a
  tank rather than transferred as a fluid. Scavenging the carriers' water and running on-demand
  electrolysis was considered and set aside: it works, but buys a water plant and a several-kW
  array to avoid carrying a tank that costs a rounding error against an 850 t wave.

## Amendment to ADR-0003

ADR-0003 describes the co-flyer as "the spent carrier that deployed the PuffSats near apoapsis."
For the staged path that identification is superseded here. **None of ADR-0003's conclusions
change**: the phase split, the 2 to 3 second handover, the fusion rather than switching, the
plate-beacon differencing, the decoupled star channel, and the 25 to 35 mas sizing all carry
over unchanged, because every one of them turns on the vantage geometry and on the platform
being quiet, not on which vehicle provides it. A permanent platform is quieter than a spent
carrier, so if anything the case strengthens.
