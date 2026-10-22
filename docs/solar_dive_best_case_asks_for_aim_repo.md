# The solar dive's best long-term price: ask S53 (for `aim_is_all_you_need`)

Raised 2026-10-22 against aim `80dceb6`. **Written to be copied verbatim into
`katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has. Register
entry: S53 in `docs/deferred_to_companion_repos.md`.

Same ground rules as your own handbacks. Neither document is the source of truth. If a number here
looks wrong, say so rather than working around it.

## The question (Seth, 2026-10-22)

How low can the charge pusher's steady $/kg at Sun--Earth L1 go in the long term? Seth's target is
$3/kg. His levers:

1. **Cheap Sun-wave hardware, about $30/kg blended.** Graphite disks at $10/kg are most of the mass.
   A small Parker-style heat shield over the electronics costs $100/kg, but it covers only a small area.
2. **Reuse the growth-wave push plates and the delivery plates** that move data centers to L1.
3. **No reuse for the Sun plate or the departure-wave bowl.** The Sun plate leaves the solar system.
   The departure wave's cycle is about 3 years, so reuse helps it little and complicates it.
4. In steady state one departure unit seeds several growth units. So the single-use departure
   hardware is spread over many growth units per kg sold, even without reuse.

## What the parent ran (scratch, not a companion change)

We called your `value_design` at each headline closure. Each closure was held at its
`HEADLINE_STARTS` design, so it was **not re-optimized** under the new prices. We read
`steady_lines`. The seed price was passed as 1367 because the steady cost does not depend on it.
Reuse was applied afterwards by dividing the `push_plate` and `delivery_plate` lines by 10 uses.
The `bowl` and `sun_plate` lines were left alone. The paper's book reproduces first ($94.1 and
$73.5 against the printed $94 and $74).

"Cheap Sun hardware" means `disk=10, carrier=30, shield=100, avionics=100`. Lob values are
`SolarDivePrices.lob`, before `lob_climb` and the delivery and growth climb factors.

| Book, cumulative | 9.86 R_sun, X 60 | 4 R_sun, X 90 |
|---|---|---|
| Paper estimate | $94.1 | $73.5 |
| Cheap Sun hardware, push and delivery plates reused 10x | $85.3 | $67.8 |
| + lob $10/kg | $36.8 | $28.9 |
| + lob $5/kg | $20.7 | $15.9 |
| + lob $2/kg | $11.0 | $8.1 |
| + lob $1/kg, polyethylene $1.2/kg | $7.1 | $5.2 |

The last row's lines at 4 R_sun:

| Line | $/kg at L1 |
|---|---|
| `delivery_lob` | 2.13 |
| `bowl` | 0.65 |
| `sun_plate` | 0.48 |
| `lob` | 0.47 |
| `sheets` | 0.39 |
| `delivery_charge` | 0.33 |
| `polyethylene` | 0.21 |
| `delivery_plate` | 0.14 |
| `avionics` | 0.13 |
| `mounts` | 0.09 |
| `shield` | 0.06 |

The parent's reading:

- **Seth's point 4 is already in the ledger.** `push_plate` comes to under $0.05 per kg at L1 on the
  paper's own book.
- **The lob lines are 86-88% of the total on every book above $2.** Each kg at L1 lofts about
  1.35-1.48 kg in its delivery unit, plus the reinvested growth lob. That is about 1.65-2.05 kg
  lofted per kg sold.
- **$3/kg needs a lob near $0.5/kg lofted.** The parent's rough figure for Super Heavy's propellant
  alone is about $0.5/kg lofted: roughly 3,400 t of methalox at the book's $0.2/kg, over a
  1500 t lob. That figure is unsourced, so please check it.

## S53. Wanted

1. **Confirm or correct the table.** In particular, confirm that holding `HEADLINE_STARTS` and
   dividing the lines afterwards is a fair stand-in. If not, say what it misses.
2. **A best-case book.** Make it a named `SolarDivePrices`, for example `MATURE`, with Seth's
   prices above. Put reuse inside the ledger as a use count on the growth push plate and the
   delivery plate (1, 10, 100). Keep the departure bowl and the Sun plate single-use. Then
   re-optimize the five knobs on the **steady** objective at both headline closures and at the two
   `COMPARISONS` closures. The question is whether cheap disks or a cheap lob move the optimum in
   depth, return excess or `k_delivery`.
3. **A lob sweep** from $25 down to $0.5/kg on that book, with the steady $/kg at each step. Also
   give the booster's propellant cost per kg lofted, with its source, on both the 1.1 km/s and the
   2.43 km/s climb. Mark that cost as the floor on the sweep.
4. **What sets lofted kg per kg sold.** Split the delivery unit's 1500 t into polyethylene charge,
   plate and bags, halo methalox and cargo, plus the reinvested growth lob per kg sold. Report this
   at each closure. If a faster return cuts the delivery charge enough to lower the floor once the
   lob is cheap, say so and by how much.
5. **Lines that matter at $5/kg.** Some lines were rounded away below $0.05 or are not charged at
   all. List every one that reaches $0.10/kg on the best-case book. The parent knows of four
   candidates: the apoapsis methalox stage's engine and tanks (S27), the deep-space reserve (S27
   item 3), the steering package's $10 floor, and operations or ground handling per launch unit.
6. **What must fall to reach $3/kg.** Give an ordered list of what has to fall and by how much,
   in the same form as S51's "what must fall to reach it". If $3 is below the floor of any
   chemical-booster lob, say that plainly.

The paper does not wait on this. Nothing goes into `tab:delivery_ledger` until it is answered.
