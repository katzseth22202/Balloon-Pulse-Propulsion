# The nozzle winding flares to follow the plume, and `eq:bore_from_length` sizes the bag rather than the magnet

Status: accepted (2026-09-04 grill on `puffsat_impact_simulation`'s answers to the nozzle asks
N1--N7, `docs/nozzle_asks_answered.md` @ `49a5e49`). Supersedes nothing, but it settles item P7
of that document, which was handed back to this repository as a decision rather than a
calculation.

**Current field amendment:** accepted ADR-0013 adopts an 11 T peak following
P18/P19. The 12 T flare dimensions and conductor prices below remain the reference
hardware envelope and budget; no 11 T winding or expansion rerun is claimed.

## Companion field-line check, P16 accepted

The companion calculation at `6fe8cf3` traces paths through a 48-coil reference
winding. Starting points sample a uniform-density column, with equal-volume
radial bins and uniformly spaced axial stations. This differs from placing every
starting point at a single chamber inlet.

| Winding | Reference field | Sampled paths crossing winding boundary |
| --- | --- | ---: |
| Straight, 3.50 m radius | Original 20 T profile | 17% |
| Straight, 3.50 m radius | 12 T cap | 14% |
| Flared | 12 T cap | 0% |

This supports retaining the flare. The calculation uses the prescribed vacuum
field and original 3.0 m bag radius / 23.8 m column. It is not an 11 T rerun and
does not include plasma feedback on the field. No sampled paths crossing the
boundary is not a measured zero liner-impact fraction. The actual mass profile
left by the snowplow and the wall interaction remain unresolved.

These figures supersede the paraxial path-clearance estimates below for the tested
reference configurations. The old conversions from geometric fractions to
kilograms striking the liner are not a wall-loading result and do not replace
the ablation budget. Likewise, the uniform-column starting distribution is an
assumption, not a reconstructed post-snowplow state.

Source: `puffsat_impact_simulation`, `docs/nozzle_replies_answered.md`, P16,
`python/puffsat/fluxtube.py`. Reproduce with `make analysis-nozzle-fluxtube`.
The decision history below retains the earlier paper-side reasoning; its
single-particle conversion mechanism was retired under P11/P12.

## What forced the question

P1 of the answer document found the merged fireball is a pancake. The axial share
`alpha = <v_z^2>/<v^2>` comes out at 0.088 against the 1/3 `eq:reflection_baseline` assumes,
and a spherical control run isolates the cause as the bag's shape. A 23 m column is nearly an
infinite cylinder, so free expansion follows the radial pressure gradient.

P2 answered it: a diverging field converts the pancake back, because `mu = v_perp^2/2B` is an
adiabatic invariant and the flare drops `B` by the area ratio. That argument is sound, and it is
the reason the design survives P1.

P7 then observed that the paper has no flare to run the argument on. `eq:bore_from_length`
(`r = sqrt(V/(pi l))`) gives a constant 3.02 m, and a flux tube that expands fourfold has twice
the radius. A cylinder has no room for it.

## The finding that decides it

`A/A*` is one ratio read two ways, and the answer document's P2 reads only the first:

| | |
|---|---|
| conversion | `alpha_exit = 1 - (1 - alpha_0) B_exit/B_start` |
| expansion | `r_exit/r_start = sqrt(B_start/B_exit)` |

**Conversion cannot be bought without radial spread, because they are the same number.** A
nozzle that converts harder is a nozzle that spreads wider, and spreading wider is what puts
plasma on hardware. This is why regrading the field to buy back `eta_geom` fails. Holding the
exit at 5 T (P9 forbids lowering it) and raising the column field instead:

| profile | field energy | virial structure | plume missing a 3.5 m winding | `eta_geom` |
|---|---:|---:|---:|---:|
| flown, 20/12/9/5 T | 1.00x | 10--30 t | **12.9%** | 0.48--0.64 |
| flat 9 T | 1.34x | 13--40 t | 25.3% | 0.55--0.69 |
| flat 12 T | 1.99x | 20--60 t | 38.9% | 0.60--0.75 |
| flat 16 T | 3.28x | 33--98 t | 50.8% | 0.64--0.80 |
| flat 20 T | 4.92x | 49--148 t | **58.2%** | 0.67--0.83 |

The third row already reaches the 37--112 t of structure that `0009` refused, and the last row
buys a 26% better nozzle by throwing 58% of the propellant at the coils. The lever is
self-defeating and no retuning escapes it.

## The decision

**The winding follows the plume's bounding flux tube**, the one born at the bore edge in the
chamber, `r(z) = 3.02 sqrt(19.80/B(z))` with clearance:

- **3.50 m at the chamber to 6.50 m at the throat**, a half-angle of 7.8 degrees
- **1.50x conductor.** The 500 A figures move from 4.4 t (cold) and 7.2 t (hot) to 6.6 t and
  10.8 t, and `sec:minimum_nozzle`'s "no amount of clever winding gets the magnet under about
  8 t" becomes about 12 t
- every flux tube is accommodated, so the geometric load on the liner is zero

## Amended 2026-09-04, same session: ADR-0012's cap makes the flare cheaper

`0012` caps the chamber field at 12 T. The flare is sized by the bounding flux tube, `r ~ B^-1/2`,
so a lower chamber field means the tubes expand less and the flare is gentler:

| profile | chamber `B` | tube grows | winding at the throat | conductor |
| --- | ---: | ---: | ---: | ---: |
| flown, as decided above | 19.8 T | 1.99x | 6.50 m | 1.00x |
| **12 T cap (reference)** | **12.0 T** | **1.55x** | **5.17 m** | **0.79x** |
| 9 T cap, if R9 allows | 9.0 T | 1.34x | 4.54 m | 0.67x |

**Against the original straight 3.5 m winding at the flown field, the capped flare costs 1.18x,
not the 1.50x priced above.** The 500 A figures become about 5.2 t (cold) and 8.5 t (hot), and
`sec:minimum_nozzle`'s "under about 8 t" floor becomes about 9.4 t rather than 12 t. **The
fairing consequence also softens**: the flare exit is 10.3 m across, not 13 m.

## What this does to `eq:bore_from_length`

Nothing, and that is the point. The equation was introduced to size **the bag**, by pouring
660 m³ of standoff volume into a column instead of a ball. The paper then reused the same `r` as
the solenoid radius in the conductor cost two sentences later, and as "the wall of a 3 m bore" in
the needle-through-fog arithmetic. That silent identification is what created P7's contradiction.

**The bag stays a cylinder that sits inside the flare rather than filling it.** Its current geometry is **660 m³, 23.78 m long, with a 2.972 m radius**
([ADR-0014](0014-bag-volume-fixes-the-column-geometry.md), P20 accepted 2026-09-05).
This supersedes R14's 672.9 m³ adoption, which combined separately rounded simulation inputs.
The winding results quoted in this ADR retain their original input geometry.

## Considered and rejected

| option | cost | why not |
|---|---|---|
| **keep the cylinder** | free in conductor | delivers 12.9% of the plume, about 27 kg/pulse, to the liner against the 4.9 kg/pulse the ablation budget books. A 6x rebooking, and the 585 MW sublimation channel was sized for the smaller number. |
| **regrade the field** | 1.3--4.9x field energy | self-defeating, per the table above. Also reaches `0009`'s refused structure band by the third row. |
| **narrow bag, longer column** | 2x conductor | `eq:bore_from_length` turns a 1.51 m bag radius into a 92 m column for the same 660 m³. Strictly worse than the flare, and a 92 m vehicle. |

## Consequences

- `eta_geom` lands at **0.48--0.64** with the flown grading and the flare, evaluated across
  P3's 1.44--2.00 exit-radii detachment window. (It peaks at 0.53--0.66 at 0.95 radii, but
  detachment is physics rather than a design choice, so the window is what we get.) This is below P2's 0.70--0.88 and above
  `sec:mass_interest`'s forward-thrust floor of `1/sqrt(1+k)` = 0.324. It does not reach the
  0.775 the growth tables sweep to.
- P2's headline therefore needs qualifying rather than adopting. The nozzle is bounded, which is
  the advance, but it is not yet clear of the target, so "where the chain misses it is
  `eta_chem` doing it" does not hold.
- The 7 m coils `sec:mass_interest` already claims clear a Starship fairing assembled. **A
  10.3 m flare exit does not** (13 m before the amendment above). **Resolved 2026-09-04**: the
  paper concedes it where the bag row is chosen. The chamber end fits an 8 m fairing, the throat
  end does not, and the magnet ships in sections and is joined once.
- `eta_geom` above is superseded. `mu` conservation is the wrong framework for a plume at
  `Kn` ~ 1e-6; see the amendment box on R1 in `docs/nozzle_replies_to_impact_sim.md`. **The
  flare decision does not rest on it**, since the flare is what accommodates the flux tubes
  whatever converts them.

## Provenance of the original paper-side numbers

The flux-tube accounting, the divergence term and the flare pricing are **paper-side probes**,
written this session and living in `todos/`: `station_weighted_alpha.py`, `regrade.py`,
`fluxtube.py`, `flare_price.py`. They use a paraxial field (`B_r = -(r/2) dB_z/dz`, first order
in `r`, evaluated out to 6 m against a 3.5 m coil), uniform mass in the bore, and one detachment
surface for all streamlines.

**The decision is firm; the figures are first-order and owed back to
`puffsat_impact_simulation` for confirmation.** They are the substance of the reply to that
repository's P2 and P7.
