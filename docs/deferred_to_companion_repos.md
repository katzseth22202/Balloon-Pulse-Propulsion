# Items deferred to the companion repos

Raised 2026-09-01 while applying companion ADR 0023 to `sec:split_dive`. All three are
prices the paper needs before it can state a conclusion the companion ADR already states.
See `docs/adr/0007-the-split-dive-ships-at-held-strength.md` for why each is held.

Target repo for all three: `katzseth22202/aim_is_all_you_need`, module
`src/bielliptic_dive_split.py` unless noted.

**Guidance items live separately.** Four asks targeting `katzseth22202/puffsat_control_simulation`
are in `docs/asks_for_control_sim.md`, numbered G1-G4 (raised 2026-09-16: the departure rod's GNSS
grade, its terminal loop, the moving door's handover, and plate capture at 57 km/s).

**Nozzle items live separately.** Sixteen asks targeting `katzseth22202/puffsat_impact_simulation`
are in `docs/nozzle_asks_for_impact_sim.md`, numbered N1-N16 so they do not collide with the
S-numbers here. N9-N16 cover the walled thermal nozzle of ADR-0016 and carry
their own geometry, which is not the magnetic one N1-N8 assume. That file is written to be copied verbatim into the companion repo. Two of them
are load-bearing: N1 (the exhaust's second moment, which decides whether `eq:reflection_baseline`
is being applied to an isotropic plume or a pancake) and N3 (whether the plume is a directed
column or a bursting bubble, worth 37-112 t of hot-pulse magnet structure).

**The walled-nozzle asks are closed except N11 and N13.** Two returns landed, both carried
here and applied in ADR-0016 and `CONTEXT.md`.

**First return, 2026-09-09**, companion `6d74d3f`, document
`docs/walled_nozzle_answers_from_impact_sim.md` (W1-W9). It answers N9 item 0 and all of N10.
The headline is that the paper-side dissociation correction of the same day is withdrawn: the
chamber is 93-98% dissociated, not 49-76%.

**Second return, 2026-09-10**, companion `1ffd367`, document
`docs/walled_nozzle_grid_answers_from_impact_sim.md` (W10-W24). It answers N9 items 1-7 and the
whole of N16, which had absorbed N14 and N15. **N9 items 1-7 no longer gate the section.**
Four paper-side positions reversed: the temperature dial runs the other way (so N14's premise
was backwards), water loses in all 128 grid cells rather than tying at the cold end, the named
water-plus-hydrogen configuration loses to plain methane, and the deep throat N15 wanted is past
a chemical wall at `A/A*` ~ 140. The throat is also a consumable rather than self-healing, which
is N9 item 5 reversing.

**What is still owed on this track.** **N11** is the only wholly untouched item. **N13**, the
walled nozzle's exit-plane velocity distribution, is confirmed unreachable from the companion's
quasi-1-D machinery and needs its 2-D axisymmetric Euler kernel, which is days rather than
hours; it is worth about 30 s out of 1,500, so it gates nothing. **The one number that binds is
a Stanton number**, bracketed over a factor of ten on the convective channel, and it decides a
100 m³ against a 150 m³ chamber and nothing else.

**The convention question is settled from both sides.** The walled ladder had been scored on a
different convention from the magnetic nozzle it is compared against, and the companion adopted
the paper's own `w(eta*sqrt(1+k) - 1)/(k*g0)` on 2026-09-10. Methane is 738 s at the ask's own
7 m² throat and 976 s at the configuration ADR-0016 now proposes, against the magnet's 1,249.
That 1,249 is a performance target rather than a solve, which is the balancing point the section
has to carry.

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

---

# Interception-altitude batch, raised 2026-09-16

Target repo: `katzseth22202/aim_is_all_you_need`. Raised while grilling the data-center
delivery legs. Backing entry: **Interception altitude (by stream)** in `CONTEXT.md`; paper-side
probe `todos/data_center_interception_altitude.py`.

## S9. Re-run the flown chain at the new Jupiter-return altitudes

**Decision the paper has taken.** Every Jupiter-return Earth encounter now flies above the
200 km the chain was computed at. The **growth wave** pushes at **400 km**, every time. The
**departure wave** meets the craft at a **600 km** periapsis, every time, reached by a raise at
the 20-day parking orbit's apoapsis. (Earlier the same day: growth 300 km with a storm raise,
and a departure briefly at 400 km.) The 11 km/s LEO and
200 Mile High Club streams stay at 200 km. The reasons are physical and are not up for re-scoring
here: at 57 km/s and 200 km, air heating matches the 4 Hz plume dose and takes bare Kevlar past
its strength limit, and drag on the tethered rod-guidance packages exceeds the tension/15 slack
limit of `sec:tethered_rod_packages`.

**Paper-side two-body numbers, for checking, not for quoting.**
- Growth-push target at 400 km, same 20-day period: **10.785 km/s** against 10.950 (-165 m/s).
- Periapsis raise 400 -> 600 km at apoapsis (v_apo ~118 m/s): **1.73 m/s**, carried.
- Departure burn at 600 km against 200 km, 3S range: **+107 to +110 m/s** instant-burn. A 400 km
  departure would save 53 m/s instant, **51-52 m/s** finite (240-320 s, thrust fixed along the
  stream, ship drag included); the paper declined it to minimize drift on the precision leg.
- **Finite-burn loss, new.** The head-on nozzle's thrust is locked to the stream direction, so
  the burn cannot follow the turning velocity. From 600 km at v_inf 12.13 km/s: +7 / +16 / +27 /
  +59 / +101 m/s over 160 / 240 / 320 / 480 / 640 s; about +16 to +29 m/s at 400 km for 240-320 s.
  The flown cadence is 2 Hz; the paper bounds a 100 t craft at ~640 pulses (320 s).

**What is wanted.**
1. The eleven flown cycles re-run with the growth push at 400 km and the departure burn at
   600 km, with the finite-burn loss charged at 2 Hz, all else held (split days, recovery values, `PUFFSAT_CYCLE_ORBIT_PERIOD`).
2. The **compounded multiple** over the flown span against the 200 km baseline. The paper-side
   departure penalty (+107-110 m/s against 200 km, plus the finite-burn loss) has not been
   compounded, and the 165 m/s growth-push saving partly offsets it. The net is the number the paper needs.
3. The same with the departure at **400 km**, the declined alternative, so the size of the 600 km
   premium is on record.
4. Whether any constant hard-codes 200 km (escape speed 11.01 km/s, the 10.95 km/s periapsis)
   outside the orbit-geometry module.

**Hazards.** Periapsis at 400 km with the period held moves apoapsis by 200 km, which is
negligible but should not be absorbed by silently changing the period. The lifting stage that
lofts the craft to 400 km is outside the chain calculation and stays outside; do not add it.

| ask | what is wanted | status |
| --- | --- | --- |
| **S9** | Re-run the flown chain with the growth push at **400 km** and the departure at **600 km**, finite-burn loss charged at 2 Hz; report the compounded multiple against 200 km and against a 400 km departure | **open** |

# Spray-plate batch, raised 2026-10-06

From applying `aim_is_all_you_need` @ `a440fba` (ADR 0041) and the impact sim's Draft 2 @
`7e1d8f7`. Paper-side record: `docs/adr/0025-the-growth-push-flies-the-spray-cup.md`.

## S10. The climbing lob is charged from the wrong baseline (aim_is_all_you_need)

`src/lob_rise.booster_growth` returns `lofted_mass(0) / lofted_mass(v)`, an apex at 400 km. The
parent's `sec:vertical_lob` lofts its 1250-1430 t to a ~430 km top, so it already passes 400 km
at ~0.75 km/s, and ADR 0037's 1.1-1.2x booster was sized from those figures. The charge should
be `lofted_mass(750) / lofted_mass(v)`. Same integrator, 380 s: **1.029 / 1.044 / 1.059** at
1.0 / 1.1 / 1.2 km/s (350 s: 1.032 / 1.048 / 1.065), against ADR 0041's 1.070-1.101. The paper
charges **1.044** (1.1 km/s, the operating point that holds ±65 km). Wanted: confirm, and make
`plate-designs-cost` take the baseline as a parameter.

## S11. Commit targets for the cells the paper now prints (aim_is_all_you_need)

The paper prints these behind the spray cup (and the grid behind the plug), run paper-side
from a scratch driver over the companion's own functions, no code changes:
- `tab:growth_ledger_doubling` / `_ten_year`: every chamber share (50/70/90/100%) plus solved,
  and methalox, at k <= 8.52 with k <= 10 in parentheses, `PlateDesign` SPRAY_CUP and PLUG.
- The ledger sensitivities: hold sweep, methane pitch 1.4/5.6 kg, the 10-day orbit, and water
  at all-in η_jet 0.50/0.53/0.56 (`WATER_SLUG`, `NO_BONDS`).
- The full `growth_cost_report` sections 2-9 behind SPRAY_CUP, and the headline and odds
  behind PLUG and ADR_0033_PLATE, with the S10 lob.
- `seed_cost` amortization and the `harvest` delivery and grow-or-harvest tables behind
  SPRAY_CUP.
**Hazard found while doing it:** `two_wave_growth.DEFAULT_SPLIT_DAYS` is **10** and
`growth_ledger.DEFAULT_PARKING_DAYS` is **20**. Calling `adaptive_two_wave_cycles()` bare
silently flies the 10-day orbit; only the ledger's `main` and `seed_cost.chains` pass 20.
Consider one default.

## S12. Carry the plate film's mass (aim_is_all_you_need)

The spray cup burns 4-6 kg of pitch per 12 MN·s pulse vapor-shielded, 28-33 kg unshielded
(impact sim P5): 5-9 t or 34-50 t per 1200-1500-pulse push. The ledger does not carry it, and
the cost book's film line is 0.1% / 4% of PuffSat mass against 4-8% / 30-45%. Wanted: the
doubling with the film charged as launched mass at both ends.

## S13. The plug in the deep bowl, and the push as a finite burn (puffsat_impact_simulation)

- The plug's best cases were on a shallow dish with an 8 m skirt; run it in the d/D 0.30 bowl
  with the 2 m skirt, so the paper's two designs share a plate.
- The handoff's ~250 s push and ~70 km stream climb disagree with the companion's in-plane
  integration (~300 s, ~185 km). The paper prints the latter.

| ask | what is wanted | status |
| --- | --- | --- |
| **S10** | lob climb charged from 0.75 km/s, not an apex | answered by companion ADR 0042 (`67d0a36`); charge superseded by ADR 0043's braked lob, x1.065 |
| **S11** | make targets for the spray-cup and plug grids and cost cells | answered: `make plate-grid`, `plate-cost`, `plate-seed` (`67d0a36`) |
| **S12** | film mass in the ledger | answered by companion ADR 0043 (`46ea0db`); paper carries 6 kg/pulse, ADR 0026 |
| **S13** | plug in the deep bowl; push duration reconciled | open |

# Film and brake batch, raised 2026-10-06

From applying `aim_is_all_you_need` @ `46ea0db` (ADR 0043). Paper-side record:
`docs/adr/0026-the-film-is-carried-and-the-brake-charged.md`.

## S14. Make targets for the film-carried cells the paper now prints (aim_is_all_you_need)

The paper headlines the spray cup with its film carried at 6 kg/pulse (`SPRAY_CUP_SHIELDED`),
not the film-in-the-book `SPRAY_CUP` that `make plate-grid`, `plate-cost` and `plate-seed` run.
Reproduced paper-side with the companion's own CLIs, no code changes:
`growth_ledger --designs-grid spray-cup-shielded`, `growth_cost_report --plate
spray-cup-shielded`, `seed_cost --plate spray-cup-shielded`, `harvest --plate
spray-cup-shielded`, and `seed_cost --plate spray-cup-unshielded` for the worst-case row of
`tab:plate_designs_cost`. Wanted: point the three plate targets at the shielded design (or add
`-film` twins), so `make` reproduces the printed cells.

Also: the unmixed downside (`spray-cup-unmixed`, 2.10 / 2.38 yr) still flies with no film. The
paper says so. Wanted: an unmixed design carrying 6 kg.

## S15. The plug's film (puffsat_impact_simulation)

The plug carries no film figure, so its cost rows price film from the book (0.1%). Wanted: film
burned per 12 MN s pulse on the plug, shielded and unshielded, as P5 gave for the spray cup.

## S16. Unit mass through the push, and the brake as a finite burn (aim_is_all_you_need)

- `sec:vertical_lob` says the unit's mass falls to about 0.8 of its start; ADR 0043 says ~0.65
  and integrates ~1060 pulses (the paper now prints 1060). Reconcile the end fraction, and the
  push duration with S13 (1060 pulses at 4 Hz is ~265 s against the printed ~300 s).
- The brake is impulsive at separation. Integrate it as a finite burn under 4 g with drag.

| ask | what is wanted | status |
| --- | --- | --- |
| **S14** | make targets for the film-carried grid, cost and seed cells; unmixed with film | open |
| **S15** | the plug's film per pulse | open |
| **S16** | end mass fraction and duration of the push; finite brake | open |

# Survivable chamber batch, raised 2026-10-08

From applying `puffsat_impact_simulation` @ `69d1f40` (chamber note §1/§3e-§5; plate P10/P12).
Paper-side record: `docs/adr/0027-the-departure-chamber-bulges-and-wraps-dry.md`. Full text of
S17 for the aim repo: `docs/survivable_chamber_asks_for_aim_repo.md`.

## S17. Recompute the ledger, cost book and seed with the survivable chamber (aim_is_all_you_need)

One 5 kg methane chamber at 2 Hz, 212 m^3, 48.2 t dry-wrap wall, 4.9 / 14.7 t extension, 117 kg
charge+plug and 3.5-24 kg pitch per pulse, 906 / 971 kN s net, on 500-600 t stacks with the
finite-burn loss (+3.1-4.8%) charged. Lead with methane; hydrogen rows labeled wall-unverified.
The paper flags its ledger tables as pricing the old 19 t chamber until this lands.

## S18. The hydrogen chamber with the rod and plug as material, the bulge and the dry wrap (puffsat_impact_simulation)

Centred spike ~2.95 GPa at 20 m^3, at steel's spall strength. Not run with the solved rod and
plug, the bulge, or the dry wrap; and its copper liner is bonded, the arrangement that peels
for carbon. Wanted: the same zone-by-zone wall study as the methane chamber, and whether a
bonded or unbonded copper liner survives. The paper proposes methane until then.

## S19. Loose ends the paper now prints as open (puffsat_impact_simulation)

- The port gate in the bulged chamber: at ~94 bar and a 1.33 m^2 throat the open port is under
  1% of the throat (leak cost ~2% against 10.5%), and the gate's pistons push about a fifth as
  hard. The paper says whether the gate still earns its place is open (`sec:port_gate`). Wanted:
  the leak with and without the gate in the 212 m^3 chamber, and the gate's close time at 94 bar.
- Peaks are not converged (+15-25% per halving at 0.25 cm); a real-EOS run is owed.
- Wall heat at the bulged chamber's own state; the high pitch edge (24 kg/pulse) comes from
  unresolved radiation.

## S20. The charge per pulse in the bulged chamber (puffsat_impact_simulation)

Raised by the S17 answer (aim `a45604d`, `docs/survivable_chamber_for_parent.md` item 3). The
117 kg of charge and plug per 5 kg rod is `k + P` = 23.4, against the sphere's 29.3 at 7000 K.
That is 120 MJ/kg against 96 MJ/kg, and the ~94 bar the note reports is 26% above the 75 bar a
7000 K charge would give by `p ~ m/V`. Both say the charge runs about 25% hotter. Holding 7000 K
would take ~146 kg. Wanted: which is meant, the impulse or the pitch at that state, and the
plug's share of the energy. Full text: `docs/survivable_chamber_asks_for_impact_sim.md`. The
paper prints the 117 kg rows with the source stated and this ask cited.

## S21. Fly the survivable chamber behind the film-carrying spray cup (aim_is_all_you_need)

`src/survivable_chamber.py` (aim `a45604d`) flies `SPRAY_CUP`, which carries no film, while every
other row the paper prints flies `SPRAY_CUP_SHIELDED` (6 kg of film a pulse as launched mass,
paper `353e1a1`). The handback's hydrogen check ("$120, matching the previous published figure")
compares against the companion's own earlier figure; the paper prints $122 and $192 / $377, which
`growth_cost_report --plate spray-cup-shielded` at `a45604d` still reproduces. Carried, the
headline methane row goes from 2.76 to 2.78 yr; every other ledger row moves 0.01-0.03 yr.
The fix swaps the plate in four places. The parent applied it in a scratch clone and prints the
rerun; the patch is in `todos/` for the aim repo to take.

Also correct in the handback: **`tab:delivery_ledger` does change.** Its rows are the steady-state
$/kg columns of the cost book, and "Departure hardware" is the chamber each reinvested growth unit
expends. The chamber never flies a delivery, but it is charged to every kilogram sold.
`tab:l1_comparison` changes with it.

## S22. Make targets for the survivable cells the paper now prints (aim_is_all_you_need)

ADR 0028 prints cells for the survivable methane chamber (A/A* 300, 24 kg pitch, priced by mass)
that no target produces. The parent ran them on the companion's own functions; the drivers and
their output are in `todos/survivable_parent_drivers/` for reference. Wanted, as S11/S14 did:
- `tab:growth_ledger_doubling` / `_ten_year`: methane at 50/70/solved/90/100% of the 0.669
  ceiling behind the plug and the 0.84 plate, and k <= 10 behind the spray cup and plug.
- `tab:plate_designs_cost`: methane behind the unshielded cup, the plug and the 0.84 plate, by mass.
- `tab:seed_return` / prose: odds 25/100%, liquidation, Earth loop, stepped and flat rates,
  growth uncharged, lob $10/$50, the flat chamber and package prices that match methalox, plates
  built, pass rates and steady/liquidation at 7.6% and 30%, all by mass.
- `tab:growth_ledger_slug` and the smaller settings: water at 0.50/0.53/0.56, the 10-day orbit,
  the unmixed 0.57 cup, all for the survivable chamber.
- Methane at half its ceiling: its cost rows (no growth; liquidation $1750 / >$3000).

## S23. The methane wall at the ledger's longest burns (puffsat_impact_simulation)

Behind the spray cup the ledger's two-synodic departures fire up to 4470 five-kilogram pulses
(A/A* 300, 24 kg pitch; 5167 at the 3.5 kg edge, where the stack burns more gas). The dry-wrap
wall was checked for 4200. Wanted: the fatigue and crack margin at ~4500-5200 pulses, or the cap
the chain must respect. The paper prints the 6% overrun as open (`sec:one_chamber`).

## S24. A wider throat for the survivable methane chamber (aim_is_all_you_need)

ADR 0044's AR 100 and AR 300 nozzles share the 1.33 m^2 throat, so the throat that sets the
pulse rate has never been varied. Doubling it halves blowdown to fill pressure (278-336 ms to
139-168 ms) and could open 4 Hz. Wanted: the cycle, the impulse and the ledger for a 2.66 m^2
throat at the same 22.5 m exit (A/A* 150) and at the same A/A* 300 (31.9 m exit, ~29.5 t
extension), with the recombination question S20 raised. Full text:
`docs/throat_and_turn_asks_for_aim_repo.md`. The paper prints no wider throat until it lands.

## S25. The Earth turn on the flown chain (aim_is_all_you_need)

The paper now prints 164.5 deg (circular 3S, visible mirror) in place of the chain's 150.4, and
the turn through head-on during the burn at the reference loading `k` = 3. Wanted: visibility on
each flown cycle (is the 2S 160.6 occulted?), the turn at the methane chamber's 24-37 minute
burns and its own `k + P` of ~23, and the loading behind the retired 0.9% / 0.5%. Full text:
`docs/throat_and_turn_asks_for_aim_repo.md`.

## S26. Recombination rates in the bulged chamber's nozzle (puffsat_impact_simulation)

Every methane eta the paper prints is a limit, carbon frozen or in equilibrium
(`tab:nozzle_area_ratio`). The bulged chamber's charge is about 6.3 times thinner than the
sphere's, so three-body recombination runs about 40 times slower, and a doubled throat at a fixed
area ratio buys only `sqrt(2)` more time. Wanted: which limit the 971 kN s takes, and a
finite-rate quasi-1D solve for today's nozzle and S24's options (a) and (b), with the sphere for
calibration. Full text: `docs/throat_kinetics_asks_for_impact_sim.md`. S24's impulse waits on it.

## S27. Charge the solar dive's apoapsis methalox stage (aim_is_all_you_need)

ADR 0072's departure-wave unit burns 0.237 km/s of methalox at apoapsis (0.211 at 4 R_sun), about
68 t per unit. Nearly all of it turns the orbit from the push axis to the thrust axis. The
propellant is charged; the engine and tanks are not. The paper's "no new kind of nozzle" wording
rests on this stage being priced. Full text: `docs/solar_dive_asks_for_aim_repo.md`.

## S28. Does the push wave's aim shrink the apoapsis turn? (aim_is_all_you_need)

Whether the turn angle was in the objective of ADR 0072's push-wave route solve. A curiosity;
nothing waits on it. Full text: `docs/solar_dive_asks_for_aim_repo.md`.

## S29. A smaller solar-dive seed (aim_is_all_you_need)

The seed is hard-coded at one launch unit of ships (676 t, $0.88-3.37B at 9.86 R_sun). Wanted:
whether anything is indivisible below that, and the headline on a 1- and 2-ship seed. The paper
prints the one-unit seed now and says plainly it is dearer up front; nothing waits on S29. Full
text: `docs/solar_dive_asks_for_aim_repo.md`.

## S30. Bare-sheet hits on the flat plate (puffsat_impact_simulation)

A charge that fails to deploy lets a Kapton sheet hit the flat plate bare. Wanted: peak pressure,
spall fragments (the debris risk), how many hits at 2 Hz the plate takes, whether a canted
departure sheet with no charge even strikes the plate, and a furled sheet's hit. Full text:
`docs/departure_abort_asks_for_impact_sim.md`.

## S31. The abort buffer spray (puffsat_impact_simulation)

The lowest k of methane sprayed on the face, spray-cup style, that makes a bare hit survivable,
and its lead time and spread. Full text: `docs/departure_abort_asks_for_impact_sim.md`.

## S32. A pessimistic price book for the solar dive (aim_is_all_you_need)

Only an Estimate book exists. The paper prints the two worst single levers (lob at $50/kg; 20 g
cap) in place of a pessimistic column until one lands. Full text:
`docs/solar_dive_asks_for_aim_repo.md`.

## S33. The 1 g push from a faster lob (aim_is_all_you_need)

At the priced 4 Hz, thin sheets overheat in the earlier pulses' gas. 1 Hz at 1 g fixes the sheets
but needs the unit climbing ~2.5 km/s at 400 km (paper's 2D scratch integration). The booster then
lofts ~28% less, and its braked return does not close (`brake_dv` NaN at 191 km / 3.16 km/s).
Wanted: the solved climb speed, the lofted mass, and a booster return that works. Full text:
`docs/plume_cadence_asks_for_aim_repo.md`.

## S34. The plate and absorber for 14.7 MN s pulses (aim_is_all_you_need)

The paper's impulsive bound: a 16 g peak needs ~10 m of stroke on a ~47 t plate (~78 g on the 2 m
stroke). Wanted: the least plate-plus-absorber mass on the gas-spring model at 16 g and 100 g caps.
Full text: `docs/plume_cadence_asks_for_aim_repo.md`.

## S35. Rerun the ledger on the 1 Hz push (aim_is_all_you_need)

Growth, doubling and break-even with S33-S34 charged, against the 4 Hz headline. Also the L1
delivery's peak g at 1 Hz, since the data-center hardware rides it. Full text:
`docs/plume_cadence_asks_for_aim_repo.md`.

## S36. The flat plate's backward plume (puffsat_impact_simulation)

The exhaust's speed and angle distribution up the stream axis, the best-fit receding-cloud U and u,
the species, and whether a canted plate clears the axis cheaply. The paper's dose depends mostly on u,
which is a free input today. Full text: `docs/plume_cadence_asks_for_impact_sim.md`.

## S37. The sheet's response, and the 1 mm option (puffsat_impact_simulation)

The heat a 100 km/s Kapton face really keeps, whether a sheet that gasifies 0.1-0.3 s out still
works as the impactor, a 1 mm sheet on a 1 cm charge, and where Kevlar strands fail. Full text:
`docs/plume_cadence_asks_for_impact_sim.md`.

## S38. Is the canted departure behind Earth? (aim_is_all_you_need)

`departure_nozzle_ledger` picks the departure's mirror sign on delivery alone and never places the
ship. The paper's planar scratch check finds the flown sign puts periapsis on the night side, 11-21
degrees from the sheets' direction of travel, so they would pass through Earth. The other sign is
visible and no worse on `earth_ve` (extrapolated, impact 117-130 deg). Wanted: confirm with
`departure_visibility`, constrain the sign, check the apoapsis turn, and rerun the headline. Full
text: `docs/departure_occultation_ask_for_aim_repo.md`.

**S33-S35, S37 (part) and S38 answered** 2026-10-19: aim `a27448e` (ADR 0073,
`docs/two_plates_and_1g_push_for_parent.md`) and sim `bfea495` / `a8924b3` (Results 13-14,
ADR-0064 amendment, ADR-0065). Taken into the paper the same day.
- **S33:** the 1 g push needs a 2.43 km/s climb. The booster brakes on the way down (entry burn),
  and every lob costs x1.48 ($39.4/kg lofted).
- **S34:** the push flies 2 Hz, 1 g, 7.35 MN s. Its plate is absorber-set at 12.2 t; the 41-47 t
  point-blast floor does not apply to a planar sheet.
- **S35:** rerun. The paper flies deliveries at 2 Hz too (S39 item 1).
- **S37:** 1 mm sheets rejected (5-9 GPa), ~100 um sheets hold at u >= 8 km/s, coatings do not
  help. Still open: 37.1 accommodation and sputtering, 37.2 a sheet with a decomposed face, 37.4
  strands.
- **S38:** the flown sign was occulted. The ship departs on the visible sign (130 deg at 9.86 R_sun,
  117 deg at 4 R_sun) on a second plate, a bowl with a 1 m hole. The bowl is x1.6-1.9 the flat
  plate's Isp. Apoapsis turn 0.33 km/s.

The paper's headline moved to the cheapest closure per depth, on one cadence: 3.81x, 1.70 yr,
$134 dear at 9.86 R_sun (60 km/s return), and 5.72x, 1.30 yr, $89 at 4 R_sun (90 km/s). These
come from a paper-side rerun, `todos/two_plates_figures_2026-10-19.md`.

## S39. The two-plate cycle on one cadence (aim_is_all_you_need)

Make the 2 Hz delivery the default and confirm the paper's rerun. Resize the 156 t delivery plate
for the 7.35 MN s pulse at a data-center g cap. Print the growth stream's speed beside the
departure stream's. Price graphite growth sheets. Dispose of the push plate (~4 m/s at apoapsis).
Fix two sensitivity rows that change the delivery's footing. Print `corrections_report` for the
flown headline. The paper prints the rerun now and says the companion has been asked. Item 8 (added the same day): make the growth-to-departure gap (`PARKING_DAYS`) a real parameter, which is frozen in defaults and an `lru_cache` today, and sweep 3 / 5 / 10 days. A 5-day gap at 4 R_sun brings the growth stream to 119 km/s and may keep Kapton viable there. Full text:
`docs/two_plates_followup_asks_for_aim_repo.md`.

## S40. The growth wave above 100 km/s (puffsat_impact_simulation)

Result 13 ran at 100 km/s. The 4 R_sun headline's growth wave arrives at 137 km/s, and the faster
returns at 132-208 km/s. Wanted:
- the sheet heating at those speeds;
- whether any Kapton thickness survives both heat and plate pressure;
- graphite impactors' geometry, their overtake law and the compact point-blast plate floor;
- a bare compact impactor on the bowl.

The paper prints its own ballpark (Kapton fails above ~130 km/s, graphite holds thermally) and
says "probably needs graphite". Full text: `docs/fast_growth_wave_asks_for_impact_sim.md`.

## S41. The Jupiter-only chain on plates, no Sun dive (aim_is_all_you_need)

Seth's question (2026-10-19): fly the Jupiter-only loop on ADR 0073's plates, with no nozzle and
no Sun dive. The paper's ballpark (`todos/no_sun_plate_loop_2026-10-19.md`) gives 2.49x, 2.48 yr
and $292 dear at the best exact-3S phase, against the Sun dive's 3.81x, 1.70 yr and $134. The 2S
lock does not grow. Wanted:
- the full chain on plates, with real ephemerides and a dollar-optimal k;
- the departure-rate trade;
- the seed route at 12-14 km/s;
- whether a faster unpowered return exists.
The paper prints the ballpark as `tab:no_sun_loop` (`sec:why_sun_dive`), flagged as our rerun. Full text: `docs/plate_jupiter_loop_asks.md`.

## S42. The bowl nearly head-on, the push at 57-69 km/s (puffsat_impact_simulation)

Confirm `hole_ve` at 160-168 deg and 70-85 km/s, and `push_ve` plus the sheets' heating at
57-69 km/s, for S41. Full text: `docs/plate_jupiter_loop_asks.md`.

**S39, S40 and S41 answered** 2026-10-19: aim `db158ed` (ADR 0074,
`docs/two_plates_followup_answers_for_parent.md`) and `e18dc45` (ADR 0075,
`docs/plate_jupiter_loop_answers_for_parent.md`), sim `f7cce80` (Result 15, ADR-0066 proposed,
`docs/fast_growth_wave_answers_for_parent.md`). Reproduced here with `make solar-dive ARGS="--gaps"`,
`ARGS="--sweep"` and `make plate-jupiter-loop`, then taken into the paper the same day.
- **S39:** the paper's rerun is confirmed. The delivery plate is the 25 g absorber bound (51 / 46 t,
  not 156 t), so the dear break-even falls to $118 at 9.86 R_sun and $79 at 4 R_sun on Kapton. The
  push plate's disposal is charged (4.2 m/s, two-body). The gap is a parameter, and 5 days is ~$2
  cheaper; the paper keeps 10 (Seth).
- **S40:** Kapton has no window at 137 km/s on the flown 2 m standoff, and none at u = 5 at any
  speed. Above ~130 km/s the sheets are dry woven carbon fabric. The paper charges it $100/kg
  (Seth), so the 4 R_sun headline is $88 dear. A bare compact impactor leaves the 130 deg bowl
  through its mouth; at 117 deg the charge moves to 2.5 F. The re-derived overtake law runs 1-9%
  below the ledger's (S43 item 1).
- **S41:** the flown Jupiter-only chain on plates is 2.01x / $573 dear at 0.25 g and 2.59x / $238
  at 1 g, against the dive's 3.80x / $118. The ballpark was too kind. The 2S windows do grow.
- **S42** is still open.

## S43. Follow-up to ADR 0074 (aim_is_all_you_need)

Adopt the sim's re-derived `push_ve`. Make the sheet material a function of the growth stream,
with carbon fabric at $100/kg above 130 km/s and a switch for the 100-130 km/s band. Settle the
8 R_sun optimum (X 60 $107 in the answer, X 75 $102 in its own sweep). Start the sweep's headline
points from `HEADLINE_STARTS`. Propagate the push plate's disposal with the Moon. Full text:
`docs/two_plates_followup_asks_for_aim_repo.md`.

## S44. Follow-up to Result 15 (puffsat_impact_simulation)

Kapton at 115-122 km/s, where three printed closures sit (4 R_sun X 75 on Kapton would be $83 and
would move the headline). The bowl's capture with the charge at 2.5 F, at 117 deg. S36, the push
plate's S30 / S31, and S42 stay open. Full text: `docs/fast_growth_wave_asks_for_impact_sim.md`.

## S45. Size the Earth plates on a lossless spring (aim_is_all_you_need)

`_inertia_plate` brings each plate to rest within every pulse, which would dissipate 4.4 TJ a push in
the 12.2 t push plate (363 MJ/kg). Replace it with the paper's lossless-spring law
(`sec:pusher_plate_damping`; mass x stroke = 507 t m at 2 Hz / 1 g), at Seth's 8 m stroke: 63 t
push and delivery plates, a 34 t bowl. Price one shared spring and assembly for push and bowl (Seth),
charge the bags, and drop the delivery g-cap rows. Full text:
`docs/two_plates_followup_asks_for_aim_repo.md`. The paper flags the plates as too light and keeps
its figures until this lands.

## S46. The gas spring's loss (puffsat_impact_simulation)

The bag spring's hysteresis and heating over 2000 cycles at 2 Hz, and whether ADR-0064's face results
carry to a 63 t plate. Full text: `docs/fast_growth_wave_asks_for_impact_sim.md`.

**S36, S42, S43, S44, S45 and S46 answered** 2026-10-19: aim `fd33d3a` / `efe6121` (ADR 0076,
`docs/spring_plates_and_fast_law_for_parent.md`) and sim `1bed1c6` (Results 16-17) and `9bcc8be`
(Result 18). Each reproduced here (ADR 0076 headlines exact; plate loop exact) before editing.

- **S45:** every plate on the spring, 63.4 t on 8 m; one shared push-and-bowl assembly (two springs
  within $1); g-cap rows dropped. **S43:** the sim's law vendored as a grid ($10 / $1 dear);
  carbon fabric by stream; the Moon-flown disposal nudge is 0-15 m/s, and ~1/9 of lunar phases
  put the Moon near the push's path (new constraint, unsolved).
- **S44 / S42 (sim Result 16):** Kapton holds at 115-122 km/s on maraging; 2.5 F costs 8-10% of
  `hole_ve`; the head-on bowl interpolation is 0-3% optimistic; the push at 54-69 km/s is 9-17%
  below the linear law.
- **S46 (sim Result 17):** the spring law holds nonlinearly (1.22x, stroke within 1%); loss
  0.14-0.37% a cycle; **nitrogen** bags (+65-74 K); the **gas column is 18.6 m**; a sheet narrower
  than the plate rings ~38% of each kick in bending, so the sheet flies **as wide as the plate**.
- **S36 (sim Result 18):** the computed plume gives u = 8.0 at 99 km/s on the floor-wide sheet;
  Kapton holds through 137 km/s; a spaced carbon veil is the light fallback; cones rejected.

The paper prints a rerun of ADR 0076 with Results 16-18 applied (3.36x / $146 at 9.86 R_sun;
4.99x / $87 at 4 R_sun on Kapton) and asks aim to adopt them (S47). Seth (2026-10-19): keep
theta = 2 pi/3 and name theta = pi as the column fix; burst and coast is not for the plate.
Still open on the sim side (its own lists): the plume's axis density within 1 deg, aim scatter,
face erosion, Kapton decomposition kinetics (not yet in a module), S30 / S31.

## S47. Consolidate sim Results 16-18 into the ledger (aim_is_all_you_need)

Kapton to 140 km/s on the floor-wide sheet, nitrogen bags with bladder, the 2.5 F bowl below
122 deg, theta = pi with nitrogen, the 9.86 R_sun 60 / 75 tie, the Jupiter loop's steady column,
and a launch-window rule for the Moon. Full text and the paper's override script:
`docs/consolidation_asks_for_aim_repo.md`.
The doc is written to be copied into aim and is self-contained: it explains each run-time
override and how to run it (verified 2026-10-20: the script as published reproduces $146 / $87).

## S48. Keeping the lossless spring on its cycle (puffsat_impact_simulation)

A lossless spring never forgets an impulse error. At 2-10% pulse scatter the 63 t plate's swing
walks off the 8 m stroke within ~25-625 pulses, and the bags' 0.14-0.37% loss holds it only at
0.7-5x the swing (paper estimate). Burst and coast is ruled out for the plate. Wanted: the scatter's
sources, the drift flown on the nonlinear spring, and the trim that holds it (next charge's mass,
standoff, arrival time, a switched orifice), also at theta = pi. Also the plate's rocking mode, which is as
lossless as the swing and must be held by the same cell-to-cell gas trim that aims the bowl. The paper holds its text until this
lands (Seth, 2026-10-20). Full text: `docs/spring_trim_asks_for_impact_sim.md`.

## E1-E6, G5-G9 answered for puffsat_impact_simulation (2026-10-16)

The sim's near-Sun environment ask (`docs/solar_environment_ask_from_impact_sim.md`) is answered in
`docs/solar_environment_answers_for_impact_sim.md`. It returns three new items to the sim: the CME
push on the disks as a guidance budget, ~1% SEP attrition with >= 100 krad electronics, and fluence
(not peak-flux) scaling for dose. Owed by whoever has the tools: a CREME96/SPENVIS shielded-dose run,
and Parker's measured dust and CME-density data at 9.86 R_sun.
Added 2026-10-16 (item 4 of that doc): the edge-on disk rule assumes purely radial CME flow. A
20% out-of-plane flow tilts it 11 degrees and returns ~15 m/s and ~27 km for an extreme CME at
4 R_sun (est.). Owed: CME density at 4-10 R_sun with its peak-to-mean ratio, and a bound on
non-radial CME flow near the Sun. Item 5 corrects the edge-on sunlight error from ~5 m to ~80 m.
Item 6 adds four Sun-wave co-flyers at the corners, ~500,000 km off the disk train, ranging the
network's shape to centimetres. Owed: (c) aim repo, whether a Jupiter flyby supplies the ~1.3 km/s
out-of-plane offset; (d) control sim, the Sun-wave landing tolerance and the network error budget.
**Item 4 answered** 2026-10-16, sim `ec90d3f` (`docs/cme_drift_answers_from_impact_sim.md`). Densities
at 4 R_sun ~1e5-6e5 cm^-3 typical; tilt ~1 deg in ejecta, 23 deg in Parker's sheath. Edge-on holds;
worst stacked sheath 14 m/s, 25 km, 23 g of gas. Item 5 confirmed (0.108 / 0.048). Still owed: the
out-of-plane flow inside near-Sun ejecta and the sheath thickness at 4 R_sun (an MHD CME run), plus (c), (d).

**S26 answered** 2026-10-13, sim `2addc17` (`docs/throat_kinetics_answers_from_impact_sim.md`). The
971 kN s is full equilibrium in carbon and hydrogen, without the 1% gate (958 with it). Over the
whole blowdown, hydrogen at its measured rate costs 1.3-1.5% of thrust at A/A* 300. Net impulse
is 938 kN s (gated) on the 1.33 m^2 throat and 941 on option (b), if carbon trades atoms freely. If
carbon is frozen at the chamber state the floor is 845 / 849. These replace the sim's 861 / 892
of 2026-10-12, whose sudden freeze tripled the hydrogen loss. Option (a) gives 908, losing to the
shorter expansion rather than to chemistry. The sphere loses 0.6% against 1.5%, so density is
the cause, at about 1/25 of the size feared. A 10 degree cone is not worth a row. Carbon has no
measured rate, so it stays bracketed, but keeping up needs a coefficient about 100x below the
one carbon measurement. S24's impulse can now proceed on these figures.

**S26 second issue** 2026-10-13, sim `df4bc6e`, replacing the first in the same file. It adds the
row the calcs ledger actually flies since aim ADR 0055: the doubled 2.66 m^2 throat at A/A* 100
on an 18.4 m exit, **885 kN s** with free carbon exchange (floor 810), against 883 / 808 on the
1.33 m^2 throat. The printable pair is now **885 / 941 kN s** on 2.66 m^2 (floor 810 / 849).
Checked against the sim's `finite_rate/pulses.csv`: the 2.66 m^2 AR 100 thrust ratio is 0.9936
against 0.9925 on 1.33 m^2, which is the +0.2%. The sim also flew the calcs ledger on {885, 941}
at 24 kg pitch: doubling 3.36 / 3.33 yr against ADR 0055's 3.57 / 3.86, so **A/A* 100 loses its
lead and the two ratios are level**; the carbon-frozen floor gives 4.66 / 4.94 yr. The handoff
cites the calcs repo's `docs/companion_replies_2026-10-13.md` for these, but that file on GitHub
(aim `37cc336`) is still the first issue's ~78%-share note with no 3.36 / 3.33. Unverified on
the calcs side, so nothing paper-side moves on them until S24 lands.

**S18 answered** 2026-10-12, sim `7afdba3` (B5 of the calcs repo's hydrocode asks, carried as
`docs/hydrocode_answers_from_impact_sim.md`). The r 3.0 m bulge with the dry wrap holds hydrogen:
2.5 kg rod with rod and plug as material, 106 m^3, 142 bar, 0.84 m^2 throat, **37.0 t wrap,
passes** at 2.20% fling in the taper against Kevlar's 2.4% (1.09x, against methane's 1.43x).
Hydrogen adds a 1.19 GPa hit on the cone, where solid steel would crack in 80 pulses. Checked
against `zone_loads.csv` (zones sum to 36.96 t). The costs: 6-8% impulse per rod against the
sphere (624 / 658 kN s against 666 / 697 at A/A* 100 / 300), and **~2-3 Hz, not 4**; the
ledger's 4 Hz belongs to the sphere, whose wall is still unresolved at ~2.95 GPa. A doubled
hydrogen throat fails the wrap (2.69%). Still owed: the 0.25 cm grid check of the 1.09x margin.
Not addressed: the bonded-versus-unbonded copper liner, which the bulged design does not use (it
carries a 10 mm liner under the wrap). **One caution before printing the 6-8%.** B5's impulse
uses the same sudden (Bray) freeze that S26 found tripled methane's hydrogen loss, and the sim
says the bulge's cost is "mostly in the nozzle freeze." The finite-rate figure is likely
smaller; no one has run it.

**S19 partly answered**, same commit. Wall heat at the bulged chamber's own state: 3-14% of the
pulse energy (B1), or 2-12% of the impulse at 212 m^3 (B6, 1.33 m^2 throat), less on the doubled
throat because it empties sooner. That bracket applies on top of every S26 figure. Convergence is
still owed: the B-series wall loads are gamma-law 2-D at 0.5 cm, scaled to real-gas pressure, and
peaks still rise 15-25% per halving. The port gate's leak and close time at 94 bar were not run.

**S24 landed** 2026-10-13 as aim `dbeec7e` (ADR 0056), carried verbatim in
`docs/throat_answers_from_aim_repo.md`. The 1.33 m^2 throat does not close even 2 Hz with a
polymer throat film sealed at 0.3 bar (548 ms cycle), so the doubled 2.66 m^2 throat is required,
not optional. The paper flies option (b), A/A* 300 on a 31.9 m exit (Seth, 2026-10-13), at 2 Hz,
on the finite-rate 941 kN s. Headline moves 2.78 -> 3.33 yr and $162 -> $197/kg. Option (a) is
printed as one sentence (3.26 yr, $10/kg cheaper); 3 Hz is not printed. Verified by re-running
`--paper-grid`, `--paper-cost`, `--ledger` and `--cost`; three corrections and the cells the
note skipped are listed in the carried file's header. Item 5 (a hydrogen-sphere row) is open.

**S23 is not answered, and its count moved.** The calcs repo's ADR 0055 ledger
(`hydrocode_answers_for_parent.md` item 5) has the longest cycles firing 4,630 (A/A* 100) to 4,880
(A/A* 300) pulses on one wall, 10-16% past the 4,200-pulse check, on 790-860 t stacks. It suggests
the paper say the chamber must be rated for ~5,000 pulses. The 4,470 / 5,167 in S23 are the ADR
0044 counts.

**S20 answered** 2026-10-08, sim `79e40d9`: the 117 kg is 7000 K. At the bulged chamber's lower
density more of the methane is dissociated and ionized, so each kilogram holds 115-120 MJ at
7000 K against 93 MJ in the 20 m^3 sphere. The paper-side `p ~ m/V` check assumed a fixed
composition and was wrong. Verified against the sim's `near_term/volume_trade.csv`: 7000 K charge
per 2.5 kg rod is 55.7 kg at 80 m^3 and 53.7 kg at 120 m^3, so ~54.4 + 4.4 plug at 106 m^3, x2 =
~117 kg. With the frozen-methane plug it is 115 kg; the ledger's 117 kg is kept (2%). The sim's
first fix printed "0.28 kg/m^3, ~46 bar"; sim `2491d15` corrected it to ~0.55 kg/m^3 and ~95 bar,
matching the ~94 bar the paper prints.

**S17 landed** 2026-10-08 as aim `a45604d` (ADR 0044, `make survivable-chamber`). It corrected
the ask on three points: the ledger has charged a fixed-direction finite-burn loss since ADR
0032 (7-12% of the burn, not 3-5%); the departing stack is ~800 t, not 500-600 t; and the
117 kg above. The paper prices the chamber by mass against the sphere's 21.2 t (Seth,
2026-10-08), not per unit.

| ask | what is wanted | status |
| --- | --- | --- |
| **S17** | ledger, cost and seed with the one 5 kg chamber; methane headline | landed (aim `a45604d`) |
| **S18** | hydrogen chamber wall study at this pulse size | answered (sim `7afdba3`, B5): bulge + 37.0 t dry wrap passes at 1.09x; 2-3 Hz; 0.25 cm check owed |
| **S19** | gate in the bulged chamber; convergence; wall heat at 94 bar | partly (sim `7afdba3`): wall heat 2-12% of impulse; gate and convergence open |
| **S20** | is 117 kg charge+plug per 5 kg pulse intended, and at what temperature | answered (sim `79e40d9`): 7000 K |
| **S21** | survivable rows behind the film-carrying spray cup; `tab:delivery_ledger` does change | landed (aim `502a64f`) |
| **S22** | make targets for the survivable cells the paper runs on companion functions | partly: `--paper-grid` / `--paper-cost` cover the methane tables; water-slug row, 10-day orbit, unmixed cup, parity and pass rates still run on functions |
| **S23** | the methane wall at 4470 pulses, 6% past its 4200-pulse check | open; doubled-throat ledger fires up to 4,708 (12% past), as the paper now prints |
| **S24** | a wider throat for the survivable chamber: cycle, impulse, ledger | landed (aim `dbeec7e`): 2.66 m^2 at A/A* 300, 3.33 yr, $197; item 5 (hydrogen row) open |
| **S25** | the Earth turn and mirror visibility on the flown chain, at the chamber's burns | open |
| **S26** | finite-rate recombination in the bulged chamber's nozzle, both throat options | answered (sim `2addc17`, second issue `df4bc6e`): 885 / 941 kN s on 2.66 m^2, floor 810 / 849 |


## S49. An errant departure impactor on the bowl (puffsat_impact_simulation)

Goal (Seth, 2026-10-20): a missed aim aborts the departure but must not turn the ship into solid
debris. The bags sit behind the bowl, off the approach line, so a miss hits the bowl's back face.
Wanted: the wall thickness below which the disk punches cleanly through (cloud out the mouth)
rather than craters back toward the ship; the rim's solid fragments and their speed distribution;
damage elsewhere in the 63 t assembly; and whether the next bare impactors still clear. The
fragment speeds also price Seth's methalox pre-burn (200-300 m/s before the PuffSat burn, so most
fragments escape). Full text: `docs/errant_departure_impactor_asks_for_impact_sim.md`.
Items 5-6 added the same day (Seth): the departure charge stacked outboard as a thick sacrificial
shield over the bags and frame, and dark water snow in sealed polyethylene balloons as that charge.
The paper names both, and the methalox pre-burn (unpriced), in `sec:charge_pusher_abort`.

## S50. A water bag on the overtake plate, with carried charge (puffsat_impact_simulation)

For the Iapetus water cycle (not in the paper; Seth, 2026-10-20). Returning water bags overtake the
Earth ship at 51.1 km/s (60 and 68-70 km/s as sensitivities). Unlike the floor-wide Kapton sheet, a bag
bursts from near a point, so the face load peaks on axis; Seth expects a heavier plate, possibly a
paraboloid with the burst near its focus. Wanted: the arrival state (intact, released ahead, partly
frozen), a `k` sweep from 0 to about 30 with `eta_jet`, flat against paraboloid plates, the plate mass
on the spring law, aim tolerance and rocking, and face erosion. Parent placeholder: 10.3x push per kg at
`k = 8.5`, `eta_jet = 0.775`, against 6.7x bare. Full text: `docs/iapetus_bag_plate_asks_for_impact_sim.md`.

**Answered 2026-10-21** (sim `1d7cedf`, Result 20, ADR-0071;
`docs/iapetus_bag_plate_answers_from_impact_sim.md`). About 8x, not 10.3x: compact ice plug on a
delta/D 0.5 paraboloid at 2 F gives 8.12x at k = 4 and 7.20x at k = 8.5; point-fireball ceiling
8.42x / 8.83x. Plate 25-32 t, graded, graphite liner. An unspread bag holes the plate (29-40 GPa);
a gun's bullet-spread bag peaks at 1.03 GPa. Follow-up is S52.

## S52. A shaped plug spreads the bag, the bullet is the backup (puffsat_impact_simulation)

Seth (2026-10-21): a squat-lens ice plug about the bag's depth spreads the bag into a near-point
burst; the gun fires only on a predicted miss; the bags get their own Earth bag plate. Wanted: the
lens sweep (depth 1-2x the bag's at k = 2-15), punch-through, the safe overlap that sets the
trigger, the backup pulse, the trigger window, the plate regraded for the lens, and k = 1-4. Items
1-3 first. Full text: `docs/shaped_plug_asks_for_impact_sim.md`.

## S51. The Iapetus water cycle: ledger and true cost (aim_is_all_you_need)

A 9.5-year round with Saturn dog-legs, a single-use water nuclear thermal stage (UO2-tungsten cermet,
SiC barrier eroding to SiO2 in steam, Seth 2026-10-20) disposed into Saturn behind redundant
reactors, and two rounds in 19 years. Base exhaust 1300 K at about 1 MPa (200 s, 1.85x NERVA's thrust per
reactor): NASA's SiC recession law puts 1800 K at centimeters of coat, 1300 K at 0.3-0.6 mm for the run.
Burn policy: 12-hour periapsis burn, 32.5 h of engine run, about 826 t of PuffSat per 560 MW engine;
3-hour growth policy as a second row. Wanted: the mass ledger; a cost ledger with the engines priced per
kg of U-235 ($40M / $60M / $100M per 560 MW engine, fixed plus per-MW); and $/kg to the eccentric orbit against the paper's current route there, printed as two ledgers: A, reuse at scale ($200K
Earth plate per flight, $1/kg electronics, 12 h burn) and B, no reuse ($5M plate, 6 h burn, 554 t).
Parent estimates: reactor about $5/kg of the ~8,000 t pushed, ship-carried plug mass about $25/kg. Valued on gated
rNPV (10%) and a 4% government loan, both gated (odds 95/90/85/90%, about 65%, Seth confirmed). A tankage row with
walls made at Saturn from local carbon by a 40 kWe surface fission unit. The core comparison (Seth, 2026-10-21): the nuclear rocket (one single-use reactor per stage) vs a nuclear reactor plus chemical rockets (one reactor launch fuels many stages). A reusable heat-only reactor drives a ceria cycle that makes methalox from ice and CO2, and only the chemical stage is thrown away; about 1,600-2,200 t of methalox per 826 t of PuffSat, priced at Iapetus and Phoebe, at a 5-10 MWt target with an electric plant (Brayton plus solid-oxide electrolysis) as a second row, a carbon processing kit priced by regolith handled, and bulk carbon as the open gate (0.1/1/10% rows). No hydrolox. The water cycle stays the paper's base (simplicity, certain water); methalox is the later upgrade, with about 12x the thrust per engine. Target: about $1-2/kg for data-center launch on reusable plates; report what must fall to reach it, starting with the ship-carried plug mass, priced on reusable plates along an optimised trajectory (the target's assumption). Score the sites on growth rate `ln(G)/T`, not growth per round (Seth, 2026-10-21): the Iapetus dog-leg costs 2.34 yr of the 9.5-yr round, and Phoebe has none (about 7.7-yr round, outbound Saturn side about 4.1 km/s against 4.76 in parent scratch); dropping the dog-leg at Iapetus costs 2.5x the methalox, so it stays. Report both pipelined and whole-round counts, since two rounds fit 20 years either way. Parent ballpark from the earlier 3-4 h life sizing: about 23x over
19 years base, 120x
optimistic (all on the stale 10.3x). **Updated 2026-10-21 for S50:** the Earth push is a band
(compact 8.12x at k = 4 base, shaped-plug ceiling labelled unrun), k solved on the whole ledger's
$/kg, backup pulses at a 5% placeholder miss rate, a residual plate-loss row, the Earth bag plate,
graphite liner and gun as lines, and no survivable bare-plate row. Ready to send. Full text:
`docs/iapetus_cycle_ledger_asks_for_aim_repo.md`.
**Answered 2026-10-21** (aim `80dceb6`, ADRs 0078-0081; carried verbatim as `docs/iapetus_cycle_answers_from_aim_repo.md`). The solar dive wins the gated break-even in every Saturn scenario (best Saturn cell $172, aerocapture with the water NTR at Iapetus, against $143 / $86). Printed in `sec:saturn_cycle_priced` (`tab:saturn_cycle`). Not run: the head-on-impactor Saturn cycle; if it is, re-check the headline.

## S53. The solar dive's best long-term price (aim_is_all_you_need)

Seth (2026-10-22): how low can the charge pusher's steady $/kg at L1 go, against a $3 target?
His levers are Sun hardware at about $30/kg blended (disks $10, shade and avionics $100), growth
push plates and delivery plates reused, and the departure bowl and Sun plate single-use. Parent
scratch over aim `80dceb6`'s `value_design` holds the headline designs. Cheap hardware plus 10x
reuse gives only $85 / $68. The lob lines are 86-88% of the total. With the lob at $1/kg lofted
(about 2x booster propellant) and polyethylene at $1.2, the total is $7.1 / $5.2 at 9.86 / 4 R_sun.
$3 needs a lob near $0.5/kg, about the propellant alone. Wanted: confirm the method, add a
best-case `SolarDivePrices` with in-ledger reuse counts, re-optimize on the steady objective, run a
lob sweep with a sourced propellant floor, break down lofted kg per kg sold, list lines that reach
$0.10/kg at $5, and say what must fall to reach $3. Ready to send. Full text:
`docs/solar_dive_best_case_asks_for_aim_repo.md`.
