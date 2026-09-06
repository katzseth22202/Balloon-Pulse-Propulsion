# The liner sets wall standoff, with an adopted 11 T peak

Status: **accepted** in the P18/P19 paper review. Amends ADR-0012's peak field
and standoff surface. R15's surface question is answered by
`puffsat_impact_simulation` at `6fe8cf3`, P19 and ADR-0042.

## Decision

Evaluate wall contact against the graphite liner. Adopt an **11 T peak** while
retaining the 5 T exit and the existing flared hardware envelope. Existing 12 T
expansion and winding results remain reference calculations; their mass estimates
remain the paper's budget. No 11 T performance or mass rerun is claimed.

The bag is a consumable membrane. The field protects the liner, whose radius
starts at 3.50 m and widens downstream. Beyond the bag boundary the clearance
gap is empty, so the swept area cannot grow beyond the bag's cross-section.

## What the companion model actually computes

`front.integrate` uses a constant scalar wall radius, not the full flared contour.
It integrates the front with a spreading speed derived from the current shock
speed. The reported binding cases across the tested closing speeds are:

| Spreading speed | Constant wall radius | Contact station | Original profile demand |
| --- | ---: | ---: | ---: |
| Sound speed | 3.50 m | 7.29 m | 8.25 T |
| 1.9 times sound speed | 3.50 m | 3.83 m | 10.95 T |

The liner stays at or outside 3.50 m. Within this prescribed front model, contact
with the actual flare can only occur later, where the original field demand is
lower. Rounding the binding 10.95 T upward gives the adopted 11 T cap. The 8.25 T
sound-speed case does not cover the faster spreading bracket.

The model reproduces the paper's shocked-layer estimates with 94,632 K and
21.12 km/s at 45.58 km/s and fourfold compression. As the front slows, its sound
speed also falls. Holding that sound speed fixed while reducing the axial speed
would spuriously accelerate lateral spreading. Taking the sound speed as the
spreading rate understates swept mass for coupling, but also delays wall contact
and understates the field cap.

Swept mass is unchanged when the reporting wall radius changes because the
integrator caps swept area at the bag boundary. The wall radius only selects
when contact is recorded. This is not a coupled calculation of feedback from
lateral expansion into the gap onto the front or magnetic field.

## Relation to the original proposal

The original paper-side probe used a flared contour and gave 4.14 m / 10.59 T
at the faster bracket, and 8.50 m / 7.71 T at the sound speed. Those were different
geometry calculations, not the companion results above. Both faster-bracket
estimates round up to 11 T. The old sound-speed-only 8 T proposal is not adopted.

The original proposal's shelf-energy ratios are not a recomputation of the whole
magnet. They are not applied to the mass budget. ADR-0012's 12 T energy and tape
figures retain their original first-order provenance; ADR-0011's 3.50--5.17 m
winding and conductor pricing remain the reference envelope and budget.

## Deferred: grade the whole profile against the liner

P19 confirms that the original 20/12/9/5 T profile was derived against the bag
bore at every station. The 5 T exit is therefore a bag-referenced standoff number,
not an independent collision requirement. It remains the chosen exit field while
a new grading is evaluated.

The paper-side `B ~ 1/r` option suggests about 8.44 T peak and 2.87 T exit. That
radial scaling and the resulting expansion have not been solved together. The
corresponding argument that conductor cost becomes bore-independent uses the
same scaling and does not justify a revised tape budget here.

A downstream bell or magnetic extension addresses expansion and release after
the bag. It does not change the wall-contact station that sets the upstream cap
in this prescribed model.

## Provenance

- `puffsat_impact_simulation` at `6fe8cf3`, `docs/nozzle_replies_answered.md`,
  P18--P19, `python/puffsat/front.py`, and ADR-0042.
- Reproduce the companion contact calculations with `make analysis-nozzle-front`.
- These results retain the companion's original geometry inputs. ADR-0014's
  corrected bag dimensions have not been rerun through the impact model.
- Historical paper-side comparison: `todos/peak_field_vs_flare.py`.
