# Does a penetrating Sun disk couple better? Answers to S65 (for the parent and aim)

Answered 2026-11-17, settled 2026-11-18, in `puffsat_impact_simulation`. **Written to be copied
out.** It answers [`penetrating_sun_disk_asks_for_impact_sim.md`](penetrating_sun_disk_asks_for_impact_sim.md)
(a copy of the parent's S65). It is Result 26 of [`xray_collision_study.md`](xray_collision_study.md)
and [ADR-0077](adr/0077-penetrating-sun-disk-heat-through-the-depth.md). Every number below comes
from `python/puffsat/xray_collision/penetrating_disk.py` (`make xray-collision-penetrating-disk`),
whose tables are `data/results/xray_collision/penetrating_disk_*.csv`. The 2-D runs are
`sweep --penetrating-disk`, `--spear-channels` and `--spear-disk`, each on 0.05 / 0.025 / 0.0125 m
bowl cells where noted.

## The short answer

**No. A spear disk couples no better than the flat disk. Keep the flat disk.**

- **Your spears tie the flat disk.** A central rod and rings at your 4.5 cm pitch, each 5.1 cm of
  graphite reaching two-thirds into the x1.2 charge, give **0.999x** the flat disk on our finest
  grid. Spears twice as far apart lose 6% (0.940x).
- **Radiation does not decide it.** Every loss that moves with depth is under 0.1% of the pulse,
  at 392 and at 616.6 km/s.
- **The pod does nothing** (0-2.2%), which closes the paper's open item.
- **Nothing goes to aim.** There is no gain to set against the rod's side kick and the bore's
  clearance.

We reported two different answers on the way here: a 12% gain on 2026-11-17, then a 6-10% loss
the same day. Both are withdrawn; "How we got here" explains why. If either reached the paper,
replace it with this one.

## Premises to correct first

- **Our spear length is 5.1 cm, not 5.6 cm.** Birkhoff's `sqrt(2200 / 950)` is 1.52, so a spear
  reaching two-thirds of the 11.7 cm column (7.8 cm) is 5.1 cm of graphite. One reaching the far
  face, the failure you named, is **7.7 cm**.
- **Our 2-D code has no solids.** Graphite and polyethylene are both run as gamma-law gas at
  their real densities. At 392 km/s strength is negligible, so what decides the result is mass,
  density and speed, which the gas carries.

## Item 1: the loss budget

At 392 km/s, as a share of the pulse:

| loss | share | moves with depth? |
|---|---|---|
| radiation as the disk sweeps the charge, one-zone (40 eV, tau 1e5) | 4.3e-5 | yes |
| the same, if the struck 0.25 kg radiated alone (104 eV) | 1.3e-4 | yes |
| the same, if the struck 1 kg radiated alone (145 eV) | 4.3e-4 | yes |
| radiation as the gas stagnates on the bowl (Result 9: e = 0.53 at 83 km/s) | 0.126 | no |
| polyethylene's frozen ions and carbon bonds (Result 11) | 0.0075 | no |

The bowl's 12.6% is real, but it is set where the gas meets the bowl, whatever the disk's shape.
What spreading the heat could win back is under 0.05%.

**The specific energy against depth**, just after the flat disk's snowplow passes
(`penetrating_disk_depth.csv`):

| depth | heat per kg | over the mean | kT | heat so far |
|---|---|---|---|---|
| struck face | 76.8 GJ/kg | 21x | 258 eV | 0 |
| 0.58 cm (5%) | 19.2 | 5.3x | 145 eV | 52.5% |
| 1.17 cm (10%) | 8.5 | 2.3x | 80 eV | 70% |
| 3.9 cm (1/3) | 1.3 | 0.36x | 20 eV | 91.3% |
| 11.7 cm (floor) | 0.17 | 0.05x | 4.4 eV | 100% |

kT is read on the CH2 table at its 1284 kg/m^3 ceiling. Shocked solid is about 4x denser.

## Item 2: thick against thin, per kilogram

Each disk on its best charge, as J/(m v) over the thin disk's matched charge, on three grids:

| grid | thin 1 kg (best width) | thick 2.5 kg (best width) | thick over thin |
|---|---|---|---|
| 0.05 m | 1.082 (x1.25) | 1.152 (x1.5) | 1.065 |
| 0.025 m | 1.078 (x1.25) | 1.141 (x1.375) | 1.059 |
| 0.0125 m | 1.074 (x1.19) | 1.108 (x1.33) | **1.032** |

The 1.177x you cite is against the thick plate's own matched charge. Per kilogram against the thin
disk, the thick plate is 3% ahead, and that falls on refinement. The 2-D disk is a gas slab and
does not penetrate, so **none of it is a depth effect**. What is left is the shape of the charge
column (length over radius 1.11 against 0.49).

## Item 3: the spear disk, struck on the bowl

`sweep --spear-disk` (`penetrating_disk_spear_disk.csv`). The rings are millimetres wide, far
below the bowl's 1.25-5 cm cells, so each collision runs in two stages:

1. **The strike, on a fine box.** A 0.78 mm grid around the disk and charge, with no plate, runs
   the rod and rings into the charge.
2. **The bowl.** Three column crossings after the strike, each bowl cell takes the volume mean of
   its fine cells' mass, momentum and energy, so all three carry over exactly. The run then
   finishes on the plate.

Under 7e-4 of the energy leaves the fine box before the handover. **The flat disk goes through
the same two stages, and it is the reference.** A central rod and rings at 9 or 4.5 cm pitch carry
the disk's 1 kg. Each is 5.1 cm long, so the fill is 0.071 (rings 3.2 mm wide at 4.5 cm).

Plate impulse net of the 0.25 m bore, over the flat disk's:

| bowl cells | rings, 9 cm | rings, 4.5 cm (yours) |
|---|---|---|
| 0.05 m | 1.066 | 1.047 |
| 0.05 m, handed over at 6 crossings | 1.027 | 0.996 |
| 0.025 m | 0.993 | 1.037 |
| **0.0125 m** | **0.940** | **0.999** |

- **On the finest grid no spear disk beats the flat disk.** Yours ties it, and wider spacing loses.
- **The coarse grid's gains do not survive.** They shrink on refinement and when the handover
  comes later. The spread between grids and handovers (about 5%) is larger than any gain left.
- **The bowl's peak load is not resolved.** It swings 0.3-1.8x the flat disk's between grids, so
  we cannot say whether spears ease the bowl.

## How we got here: two answers withdrawn

**The shortcut's 12% (2026-11-17).** Our first runs skipped the strike. They started the column
already merged at the common speed, with the collision's heat laid along it by hand: at the face
as the flat disk's snowplow leaves it, or evenly to two-thirds of the depth for spears. Net of the
bore, over the flat disk run straight on the bowl:

| start | 0.05 m | 0.025 m | 0.0125 m |
|---|---|---|---|
| the flat disk, run straight on the bowl (J/mv) | 2.108 | 2.192 | 2.296 |
| shortcut, heat at the face | 1.095 | 0.982 | 0.887 |
| shortcut, heat even to two-thirds | 1.161 | 1.152 | 1.123 |

That 1.12x compared two things made differently, and both are biased:

- **The flat disk run straight on the bowl comes out low.** The bowl's cells resolve its hot struck
  layer only in whole cells. The same disk through the fine box couples 1.07-1.10x more
  (`penetrating_disk_spear_disk.csv`).
- **The shortcut undersells face heat** by a similar amount, about 11% in the planar cell below.

**The planar cell's 6-10% loss (2026-11-17).** One periodic slice of graphite slats struck the
column the disk meets, beside the flat disk (`penetrating_disk_channels.csv`). It measured the
momentum crossing planes *beyond* the charge, where the plate sits in S64's growth sheet. Your
Sun bowl's plate sits *behind* the struck face, so that tally is not the bowl's impulse. The slats
gave 0.90-0.94x the flat disk at pitches from 9 to 1.1 cm, but that does not carry over to the
bowl.

Item 3's run removes both biases: spears and flat disk go through the same stages on the same
grid, and the impulse is the bowl's own.

## Item 4: the pod

A tenth of the heat in a central 4 cm pod gives the shortcut face start's J/mv to within 0.0-2.2%
on every grid. It moves a tenth of the heat, and it does not move the result. **Close the open
item: the pod does not change coupling.**

## Item 5: 4 R_sun

The closing speed there is 616.6 km/s. The 2-D gas has no speed scale, so item 3's ratios carry
over unchanged: **the spears tie the flat disk at 4 R_sun too.** The one loss that moves with
depth grows but stays under 0.1%: 4.6e-4 of the pulse one-zone, and 2.0e-4 / 9.5e-4 if the struck
0.25 / 1 kg radiated alone. The frozen toll falls to 0.31%.

## Suggested changes (for the parent to make)

- `sec:sun_wave_ranging`, the disk: "A disk of graphite spears reaching two-thirds into its charge
  couples no better than the flat disk: a rod and rings at 4.5 cm pitch tie it in the 2-D gas, and
  wider spacing loses about 6% \cite{Katz_penetrating_disk_2026}. Radiation, under 0.1% of the
  pulse, does not decide it either. The flat disk is kept."
- The pod's open item: "A central pod holding a tenth of the disk changes coupling by under 2%."
- aim: nothing to price. The spear disk is not carried forward.
- If the paper took up the 12% gain from our first answer, remove it.

## Still open

None of these would revive spears unless the tie broke by more than the ~5% spread between grids.

- **The fine box's own resolution.** Only 0.78 mm was run. Halving it costs about 8x, and the
  1-2 cm pitches need it.
- **Rods, not rings.** The 2-D runs are axisymmetric, so spears off the axis are rings.
- **What a spear does on the way in.** It may tunnel or break up rather than erode evenly.
- **The bowl's peak load** with spears.
