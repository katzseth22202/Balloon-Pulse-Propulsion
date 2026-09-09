# Items deferred to the companion repos

Raised 2026-09-01 while applying companion ADR 0023 to `sec:split_dive`. All three are
prices the paper needs before it can state a conclusion the companion ADR already states.
See `docs/adr/0007-the-split-dive-ships-at-held-strength.md` for why each is held.

Target repo for all three: `katzseth22202/aim_is_all_you_need`, module
`src/bielliptic_dive_split.py` unless noted.

**Nozzle items live separately.** Thirteen asks targeting `katzseth22202/puffsat_impact_simulation`
are in `docs/nozzle_asks_for_impact_sim.md`, numbered N1-N13 so they do not collide with the
S-numbers here. N9-N13 cover the walled thermal nozzle of ADR-0016 and carry
their own geometry, which is not the magnetic one N1-N8 assume. That file is written to be copied verbatim into the companion repo. Two of them
are load-bearing: N1 (the exhaust's second moment, which decides whether `eq:reflection_baseline`
is being applied to an isotropic plume or a pancake) and N3 (whether the plume is a directed
column or a bursting bubble, worth 37-112 t of hot-pulse magnet structure).

**N9 item 0 and all of N10 came back on 2026-09-09**, companion `6d74d3f`. The answer document
is carried here at `docs/walled_nozzle_answers_from_impact_sim.md` and applied in ADR-0016 and
`CONTEXT.md`. The headline is that the paper-side dissociation correction of the same day is
withdrawn: the chamber is 93-98% dissociated, not 49-76%, so methane returns to 1,120-1,133 s.
**N9 items 1-7 gate the walled-nozzle section**, and N12 and N13 were raised on the way in. N12
is already answered on the paper side. **N13 is the one that matters**: applying the return
showed the walled ladder had been scored with `eta_chem = 1` where the magnetic nozzle it is
compared against carries `eq:eta_chem`'s 0.910, so on a matched convention methane is 571-716 s
against the magnet's 1,249 rather than 1,129 against it. N13 asks for the walled nozzle's own
`eta_geom`, which decides where in that range it lands.

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

---

# Fly-and-park batch, raised 2026-09-08

**These four live separately.** Asks **S5-S8**, targeting `katzseth22202/aim_is_all_you_need`,
are in `docs/fly_and_park_asks_for_aim_repo.md`. That file is written to be copied verbatim
into the companion repo, the same way `docs/nozzle_asks_for_impact_sim.md` is, so the full
text is kept there rather than duplicated here.

Raised while grilling the companion's `docs/paper_corrections_fly_and_park_2026-09-07.md`
(ADR 0030, `src/fly_and_park.py`). Backing decision:
`docs/adr/0015-2s-and-3s-are-operating-points-not-a-succession.md`.

**All four are answered and written into the paper.** Companion commit `e384232`, backed by
its ADR 0031 and handed back in `docs/paper_corrections_synodic_lock_2026-09-08.md`. The paper
carries them in `sec:synodic_lock` and `tab:doubling_ladder`.

| ask | what is wanted | status |
| --- | --- | --- |
| **S5** | Implement, test and **chain-check the 2.00 S synodic lock**, constructed here at phase 0.781 but not run through the chain search | **answered, and the construction was wrong.** The 9-day park is inadmissible; the admissible lock is the resonance the paper already flies. **0.873 yr**, not 0.84 |
| **S6** | One **doubling ladder** with the scorer named on every rung, because 1.19 yr and 1.45 yr are different quantities at the same `f` = 0.8 | **answered: a different measurement of a different thing.** Not at matched efficiency and not at matched scope. Ladder is `tab:doubling_ladder` |
| **S7** | Absorb the **launch-window layout**, one contiguous arc widening 71 to 241 to 399 days, which the companion publishes fractions for but not shape | **absorbed and pinned.** One arc at every exhaust speed; the Isp 1200 width is **240** days, not 241 |
| **S8** | Say whether the 2S lock is a **padded member of the 2S vs 3S cadence family** already flown (`dv` 7.25 against 6.84-7.17, `v_b` 63.2 against 61.83-65.13) | **yes, and more strongly than asked.** The flown cycles are already exact locks, drift under 1e-4 S, so nothing needs padding |

**S5's hazard was the right one, and it fired.** The ask flagged that the 2.00 S lock needed a
**9-day** park against a 20-day `PUFFSAT_CYCLE_ORBIT_PERIOD`, and asked whether that was
admissible. It is not, and the question found a wrong constant in the companion:
`MINIMUM_PARK` was 0.02 S, about eight days, standing in for a coast it is 2.5x under. The
park is the bound near-escape orbit's period **lengthened**, since the push lands at one
periapsis and the departure burn lights at the next, so it can never be shorter than one lap.
Charging the coast moves the lock from phase 0.781 to **0.8082**, where it coincides to every
digit with `fixed_points()`' own two-synodic resonance. Fly-and-park does not produce the 2S
operating point. There is no remainder left to pad.

**What moved on the way in.** Two published companion figures shifted (padding beats plain 3S
at **16** of 30 phases at Isp 1200, not 17; the perfect-retrograde premium's median is 1.037
over 29 phases). Neither is quoted in the paper. One paper figure was corrected: `sec:mass_interest`
called the 1.74 yr rung's knob a *"nozzle geometric efficiency"*, and it is the **nozzle impulse
recovery**. Both are 0.6 here and they are different parameters.

**Re-derived rather than transcribed**, because the handback and ADR 0015 counted two different
things. Phases offering a lock, coast charged, from `synodic_lock()`: 2S is **none** at Isp 380,
**11 of 73** at 1200 and **26 of 73** at 2214; 3S is **12**, **44** and **73 of 73**. ADR 0015's
73-of-73 came off the *usable-phase* fraction, which is a looser test. Its conclusion survives.

**Vocabulary settled in the same grill** and recorded in `CONTEXT.md`: **fly-and-park**,
**synodic lock** (with **2S lock** / **3S lock**), **departure phase**, **sweet phase**,
**usable phase**. The lock term exists because "2S" already meant two incompatible things in
this paper, and fly-and-park makes a third.

**C1 turned out not to be owed.** The paper never quotes x74.8, x90.2 or a ninth cycle. One
hazard if anyone sweeps for it: the paper does contain the phrase *"a second steering knob"*,
about **real ephemerides** rather than the perijove burn, and that sentence is correct.
