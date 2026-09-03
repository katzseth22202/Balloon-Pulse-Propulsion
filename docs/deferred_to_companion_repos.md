# Items deferred to the companion repos

Raised 2026-09-01 while applying companion ADR 0023 to `sec:split_dive`. All three are
prices the paper needs before it can state a conclusion the companion ADR already states.
See `docs/adr/0007-the-split-dive-ships-at-held-strength.md` for why each is held.

Target repo for all three: `katzseth22202/aim_is_all_you_need`, module
`src/bielliptic_dive_split.py` unless noted.

**Nozzle items live separately.** Seven asks targeting `katzseth22202/puffsat_impact_simulation`
are in `docs/nozzle_asks_for_impact_sim.md`, numbered N1-N7 so they do not collide with the
S-numbers here. That file is written to be copied verbatim into the companion repo. Two of them
are load-bearing: N1 (the exhaust's second moment, which decides whether `eq:reflection_baseline`
is being applied to an isotropic plume or a pancake) and N3 (whether the plume is a directed
column or a bursting bubble, worth 37-112 t of hot-pulse magnet structure).

---

## S1. Price a dedicated impactor delivery to a 1.96 AU node

**Why.** `split_dive_ledger()` charges the impactors consumed at both nodes and nothing for
getting them to the far one. The **partial split** (`q` = 0.4918 AU) does not satisfy
outer-node co-location, so the returning beam does not reach its far node at 1.9649 AU.
Without this price, "better on both axes the ledger scores" cannot become "dominating."

**What is wanted.** The Earth-departure impulse, and the launched slug per kilogram
delivered, for placing an impactor wave at 1.9649 AU on the partial split's schedule. The
natural comparison is the two-impulse phasing loop's second node at 1 AU, which the paper
already treats as a network-maturity cost rather than an impulse cost.

**What would settle it.** Whether the partial split still beats the single-impulse dive's
2.365 kg/kg once the far node's delivery is added to its 1.536.

**Lifts.** `sec:split_dive_growth`'s held sentence, and `CONTEXT.md`'s **Partial split**
`_Avoid_` line.

---

## S2. Price a larger perihelion burn at the solar node

**Why.** The 19.80 solar-radii conduction crossing moves ~1.9 R☉ per km/s of perihelion
burn (5.58 at 20 km/s, 19.80 at the paper's 35.98 tuning, 35.91 at 45). **38.15 km/s holds
the direct departure conducting out to 23 R☉**, the depth `sec:depth_cost` recommends
starting at, for 6% more burn. So the crossing does not show that the split is *required* to
fly shallow; it shows that the direct route cannot fly shallow *at this burn tuning*.

**What is wanted.** What a perihelion burn of 38.15 km/s rather than 35.98 costs the direct
single-impulse dive at the node, charged the way `jovian_solar_dive_cycle` charges a node, so
the cycle can be scored end to end at both tunings. `paper_resonant_dive_ledger()` is not
sufficient: it takes the stream speed and the Earth burn, charges the node nothing for the
larger boost, and therefore reports the extra burn as a free improvement.

**What would settle it.** Whether there is a depth at which no affordable perihelion burn
keeps the direct departure conducting, and whether the split clears the committed fifteenth
of liftoff at that depth. Related and also unrun: the split dive's own pad-charged launch
ledger across the depth dial, in ADR 0021's `0.25 * chain * survival` form.

**Lifts.** `sec:self_cooling_departure`'s held paragraph, and the depth-window claim that
`sec:split_dive` no longer makes.

---

## S3. Trace whether any ledger already absorbs the opposing stream's placement

**Why.** Placing the opposing stream costs 35.48 km/s of heliocentric impulse at 4 solar
radii and 44.94 at 32, against the payload's own 24.09 falling to 14.62. That is the same
order as the payload's whole injection, and it moves the opposite way under the depth dial,
so it becomes the dominant Earth-side cost past about 8 solar radii. `sec:jovian_dive_open`
sets the opposing side aside twice, once at 1.34--2.15% of the vehicle consumed at the node
and once as "one-way and expendable." Both are about the projectiles once they are in place.
Neither is about the impulse that puts them there, and every impulse in this architecture is
a PuffSat collision charged to a pad.

**What is wanted.** For the direct dive, the Jovian dive cycle and the Jupiter-only chain in
turn: does the growth ledger, the pad ledger, or the impactor bill already carry the cost of
placing the opposing stream, and if not, how much does adding it move the doubling times.

**What would settle it.** One of two sentences. Either the placement is absorbed and the new
subsection says where, or it is not and the paper states the size of the omission.

**Blocks.** The restructure of `sec:split_dive` around the two-arrival asymmetry, agreed in
the 2026-09-01 grill as the subsection's spine. Until S3 lands the subsection keeps its
present order and leads with the Delta-v family.

---

## What landed

All three came back on 2026-09-02 and were applied to `templateArxiv.tex` the same day.
Backing work is companion ADR 0024 (`make opposing-stream`) and ADR 0025 (`make
shallow-dive`), mirrored in companion `docs/paper_changes_owed.md` P1--P6.

| item | verdict | where it landed |
| --- | --- | --- |
| **S1** | **Reverses the claim.** Far-node delivery costs 113.20 km/s of Earth excess and delivers 1.0%; 1.536 kg/kg becomes 3.552 against the dive's 2.365 | `sec:split_dive_growth` strikes the dominance framing; `CONTEXT.md` **Partial split** and **Far-node delivery price** |
| **S2** | **Answered against the split.** 38.10 km/s holds the direct departure conducting to the 22.93 R☉ pad floor, cycle still grows at 0.657 yr | `sec:self_cooling_departure` closing paragraphs; `CONTEXT.md` **Conducting burn** |
| **S2 (extra)** | **Larger than S2 itself.** The stated 0.60 node survival flatters every shallow row; derived, doubling runs 0.3075 / 0.6570 / 0.9484 yr | new `tab:derived_node_survival`; `CONTEXT.md` **Stated versus derived node survival** |
| **S3** | **Omission is real, effect is a rounding error.** Uncharged everywhere, worth under 1.2% of doubling because `k` = 30 makes it a mass question | `sec:opposing_stream_depth`, `sec:jovian_dive_open`; `CONTEXT.md` **Opposing-stream charge** |

Three things landed that were not on this list.

- **P1, node-depth admissibility.** The largest change of the batch and a modelling
  constraint rather than a number. New `sec:node_depth_admissibility`, and `docs/adr/0008`.
- **P5, the pad claim's depth.** "The split buys the pad" holds over (4, 5.58] R☉ only.
  `sec:self_cooling_departure`'s opening.
- **P6** turned out to be a stale note rather than a paper error. `sec:axial_bag` already
  says 1.3 kg, which reproduces from `tab:axial_bag` as 6.2 minus 4.9. Closed in
  `paper_corrections_checklist.md`.

The restructure this document's S3 entry said it was blocking is **retired rather than
executed**; see `docs/adr/0007`'s resolution section for why.

---

## S4. Record the 10-day SEP-versus-methalox run

Raised 2026-09-02 while landing companion ADR 0026 into `sec:split_tail`.

Target repo: `katzseth22202/aim_is_all_you_need`, module `src/sep_split_correction.py`.

**Why.** ADR 0026 is computed at a **20-day** split gap (`PUFFSAT_CYCLE_ORBIT_PERIOD`), but the
paper and `two_wave_growth.DEFAULT_SPLIT_DAYS` both carry **10 days** per ADR 0013. Migrating the
paper to 20 days was attempted and reverted: the gap only reshapes the growth wave, so at 20 days
the coldest growth push moves 45.58 -> 47.49 km/s, and that cold end is the design point for the
entire plume-and-bag thermal chapter in 11 places. A hotter pulse radiates as `T^4`, so the move
reopens thermal margins rather than merely refreshing numbers.

**What was done here.** `analyze_sep_split(split_days=10.0)` was run and `sec:split_tail` is
written from it. It reproduces ADR 0013 exactly (separation burns 398.5 / 556.0 / 1011.3 m/s,
chain mean 0.179 km/s), so the harness is sound at both gaps.

**What is wanted.** A short amendment to ADR 0026, or a new ADR, recording the 10-day column
alongside the 20-day one, and a `make sep-split` invocation the paper's caption can name. The
figures the paper now cites are below.

| quantity | 10 d (paper) | 20 d (ADR 0026) |
| --- | ---: | ---: |
| worst separation burn | 1011.3 m/s | 2089.4 m/s |
| worst total correction | 1029.8 m/s | 2107.9 m/s |
| adaptive doubling, methalox | 1.737 yr | 1.749 yr |
| stricter cadence doubling | 1.863 yr (10 cycles, 4x2S+6x3S) | 1.907 yr (9 cycles, 2x2S+7x3S) |
| cost of dodging the tail | 7.3% of clock | 9.0% |
| never-fall-back, methalox / argon | 2.270 / 1.501 yr | 2.686 / 1.468 yr |
| required specific power | 1.57 kW/t | 3.22 kW/t |
| power at 500 t reference | 0.79 MW | 1.61 MW |
| array fraction at 15 kg/kW | 2.4% | 4.83% |
| argon gain net of its array | 1.1% | 3.7% |

**Also worth recording.** ADR 0026's `STATED_ACCELERATION_1AU = 2.0e-5` is described as the
design's operating point, but nothing in `templateArxiv.tex` states it, and the module's own
comment shows it disagrees both with its Jupiter counterpart and with 100 kW on a 500 t wave. The
paper therefore states the requirement directly and quotes no shortfall ratio against it.
