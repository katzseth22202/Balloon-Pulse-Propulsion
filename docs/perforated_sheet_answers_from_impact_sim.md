# A perforated Kapton sheet on the fast growth wave: answers to S64 (for the parent and aim)

Answered 2026-11-16 in `puffsat_impact_simulation`. **Written to be copied out.** It answers
[`perforated_sheet_asks_for_impact_sim.md`](perforated_sheet_asks_for_impact_sim.md) (a copy of the
parent's S64). It is Result 25 of [`xray_collision_study.md`](xray_collision_study.md) and
[ADR-0076](adr/0076-perforated-sheet-half-fill.md). Every number below comes from
`python/puffsat/xray_collision/perforated_sheet.py` (`make xray-collision-perforated-sheet`). Its tables
are `data/results/xray_collision/perforated_sheet_{heat,print,radiation}.csv`. The new 2-D runs are
`sweep --perforated-sheet [coarse]`: one periodic cell of a slat web on the headline push charge.

## The short answer

**Your 2x is right, but fly a fill of 0.5, not 0.2-0.3.**

- **Heat.** A strand of fill `f` is `t / f` thick under the same flux. Kapton's diffusion length
  is 88 / 125 um over 0.1 / 0.2 s, so the face's rise over 300 K falls to 0.54-0.61x at fill 0.5,
  0.40-0.52x at 0.3 and 0.35-0.49x at 0.2. That is the near-2x you expected. Little is gained
  below 0.3.
- **Coupling is not the film's at low fill.** Your premise was that coupling cannot move. In
  the 2-D gas, a web's thick strands punch their own columns through the charge and do not fully
  merge with it. Less of the sheet's energy becomes heat, and heat is what pushes. The downward
  momentum is **0.994x** the film's at fill 0.5, but **0.943x at 0.28, 0.873x at 0.20 and 0.838x
  at 0.16**.
- **Fill 0.5 holds at 208 km/s with margin.** On Result 18's design 3 deg cone it peaks at 480 K
  (193 K under 400 C), against the film's 632 K. On the unconverged 1 deg axis, where the film
  fails at 874 K, it peaks at 645 K and holds.

## A premise to correct first: the film already holds at 208 km/s

Result 18 (`plume_sheet.csv`) has the floor-wide 9.5 m Kapton film holding at 208 km/s on
maraging. It is 33 um against a 28 um heat floor and a 54 um load ceiling. On HY-100 it fails:
its ceiling is 33 um. Your ask cites the same three numbers, but the carbon-fabric step above
140 km/s was the ledger's choice, not a failure we found. What perforation buys at k = 8.21 is
**margin**: 41 K becomes 193 K on the 3 deg cone. It also buys a pass on the 1 deg axis, where the
film fails.

**Your table's 208 km/s row now flies near k = 26**, and every run here is at k = 7.07. A k = 26
push makes a sheet of ~25 um carrying a cloud 2.2x heavier. We give that row on the k = 7.07
exhaust's shape, and it is far outside it:

| 208 km/s at k = 26 (indicative) | 3 deg cone | 1 deg axis |
|---|---|---|
| film, 25 um | 1093 K, fails | 1363 K, fails |
| fill 0.5 | 815 K, fails | 1149 K, fails |
| fill 0.3 | 652 K, holds by 21 K | 930 K, fails |
| fill 0.2 | 594 K, holds by 79 K | 792 K, fails |

Pricing that row needs the plume run at k = 26 (`sweep --plume-2d` at the new k), which we have
not done.

## Item 1: face temperature

The floor-wide 9.5 m sheet, the pulse's mass spread as Kapton, on Result 18's computed plume.
Peak face temperature, and whether Result 13's rule holds (under 400 C until the last 10 ms).
The 3 deg cone is the design value. The 1 deg axis is the worst the runs give, and is not
converged; we read it as your "slowest spread run".

| closure | film | fill 0.5 | 0.3 | 0.2 |
|---|---|---|---|---|
| 137 km/s (k 6.67), 3 deg | 52 um: 597 K | 103 um: 483 K | 172 um: 455 K | 258 um: 446 K |
| 137 km/s, 1 deg | **838 K, fails** | 624 K | 555 K | 533 K |
| 158 km/s (k 7.13), 3 deg | 44 um: 607 K | 88 um: 476 K | 147 um: 445 K | 220 um: 433 K |
| 158 km/s, 1 deg | **848 K, fails** | 628 K | 543 K | 516 K |
| 208 km/s (k 8.21), 3 deg | 33 um: 632 K | 65 um: 480 K | 108 um: 433 K | 163 um: 417 K |
| 208 km/s, 1 deg | **874 K, fails** | 645 K | 536 K | 495 K |

Every perforated entry holds. At 208 km/s the margins under 400 C are 193 / 240 / 256 K on the
3 deg cone and 28 / 138 / 178 K on the 1 deg axis.

The 158 km/s closure is not one of ours. Its k is interpolated between the 137 and 208 km/s rows,
and its `v_e` (58.2 km/s) is the calcs law, which reproduces every printed row to 0.1%. The
strands' side walls take no gas, since the flow is along the axis to ~0.02 deg. Their radiation
is left out, which errs hot.

## Item 2: does the web print on the plate?

One periodic cell of a planar web of square slats, with the slat as wide as it is thick. Your
fills are exactly slat width over pitch. It strikes the headline push charge face-on: k = 7.07,
the 70 um film's mean areal density and real densities. Below the charge we tally the downward
momentum crossing, `int (p + rho u_z^2) dt`, and its spread across the pitch. A gamma gas has no
speed scale, so this serves 99 and 137 km/s alike. Spread across the pitch, (max - min) / mean,
production grid (32 cells across the half pitch):

| web | 1 pitch | 5 | 10 | 20 pitches | peak load, 20 pitches |
|---|---|---|---|---|---|
| fill 0.5 (0.14 mm, 0.28 mm pitch) | 9% | 7% | 5% | **5%** | 24% |
| 0.28 (0.25 mm, 0.9 mm) | 56% | 18% | 26% | 23% | 43% |
| 0.20 (0.35 mm, 1.75 mm) | 77% | 49% | 26% | 28% | 101% |
| 0.16 (0.45 mm, 2.9 mm) | 70% | 66% | 36% | 44% | 65% |

**At fill 0.5 the strands do not print.** The impulse is even to 5% at 20 pitches (6 mm), against
2 m to the plate. The low fills keep columns of 23-44% to 20 pitches. In an inviscid gas those
columns move at different speeds and share momentum only through pressure. The finer grid keeps
them sharper (fill 0.20 at 20 pitches: 10% coarse, 28% production), so they are not converged.
What mixes them in reality, shear across the columns, is not in the model. Read the low-fill
prints as an upper bound. A load ceiling set by mean areal density holds at fill 0.5. Below about
0.3, we cannot say it holds.

## Item 3: coupling against the film

The downward momentum crossing 5 pitches below the charge, per `sigma w`, against the flat film's
(the film's is 1.71; the gas thrown back up the stream carries the rest). The other stations agree
to under 1%:

| web | coarse (16 cells) | production (32) |
|---|---|---|
| fill 0.5 | 0.998 | **0.994** |
| 0.28 | 0.945 | 0.943 |
| 0.20 | 0.891 | 0.873 |
| 0.16 | 0.863 | 0.838 |

The plate's impulse follows this momentum (Result 11: `(1 + e)` of what arrives). **Fill 0.5 is
within 1% of the film. Below 0.3 the web loses 5-16% in the model.** That loss grows on
refinement, for the same reason as the print: an inviscid gas does not mix the columns. So it is
the pessimistic end, and full mixing would recover the film. Either way, "within 1%" is not
something we can confirm below fill 0.5.

The reason is the local mass ratio. Under a strand the charge is `k f` times the strand: 3.5 at
fill 0.5, but 1.4 at 0.2. A strand with that little charge in front of it is not stopped. It
carries its column on as a fast jet, and the charge between strands is struck only from the side.

## Item 4: radiation from the hot channels

The one-zone fireball on the CH2 table (Result 10's model) at the strand's local ratio `k f`
gives the most a channel could radiate before it shares its heat sideways:

| | film | fill 0.5 | 0.3 | 0.2 |
|---|---|---|---|---|
| 137 km/s: start kT / radiated share | 19 eV / 1.5e-6 | 28 eV / 1.3e-5 | 36 eV / 5.7e-5 | 43 eV / 1.4e-4 |
| 208 km/s | 30 eV / 1.6e-5 | 45 eV / 1.6e-4 | 62 eV / 4.6e-4 | 77 eV / 7.6e-4 |

The channels run 1.5-2.6x hotter, but the dense charge is 10^4-10^5 optical depths thick. Even
fill 0.2 at 208 km/s radiates under 0.1%. Radiation does not bear on the choice.

## Item 5: the thickest web that holds at 208 km/s

**Fill 0.5: a 65 um web from the 33 um film.** It is the thickest whose print (5%) and coupling
(0.994x) stay with the film's. Thicker webs run cooler but lose coupling and print, at least in
the inviscid model. Its face holds by 193 K on the design cone and 28 K on the 1 deg axis, on
maraging or HY-100 alike, since the load ceiling stays the film's. On HY-100 that ceiling is
33 um against a 33 um sheet: marginal before perforation and unchanged by it.

## Suggested changes (for the parent to make)

- `sec:charge_pusher_plume`, after the sheet: "Above 140 km/s the sheet can stay Kapton if it is
  perforated to half its area at the same mass. Each strand is then twice as thick and its face
  heats about half as much. At 208 km/s it peaks near 480 K against the film's 630 K, and it
  couples as the film does to within 1% \cite{Katz_perforated_sheet_2026}. Finer fills run
  cooler still but leave fast jets through the charge that cost up to 16% of the push."
- `tab:charge_pusher_fast` and its text: Kapton at fill 0.5 replaces carbon fabric at 158-208
  km/s at k near 7-8. Whether it survives the 208 km/s row at k = 26 waits on a plume run at that k.
  aim prices the swap.

## Still open

- The plume's shape at k = 26, which the 208 km/s row now flies.
- Mixing between strand columns below fill 0.3: what turns the inviscid bound into a number.
- The 1 deg axis is unconverged (Result 18), and erosion of the strand faces by the plume's atoms
  is unmodelled.
- Planar slats stand in for a 2-D web of holes. The holes' crossings, which you rejected as knots,
  are not modelled.
