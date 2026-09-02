# Checklist for `paper_corrections.md`

Tick an item only when the edit is in `templateArxiv.tex` and `./build.sh` is
clean. Each line carries the one-phrase version of the change so this file can
be read without opening the corrections document beside it.

Worked in numeric order rather than the corrections document's priority order,
because the dependencies run that way: A3 supersedes A5 and regenerates the
column A8 asks about, so doing A3 first makes both cheaper.

## A. Numbers that are wrong or that move

- [x] **A1** Growth-table axes are `eta_geom`, not `e`; `eta_jet = eta_chem * eta_geom`
      *(`tab:space_mortgage_growth` only; `tab:two_leg_growth` deferred, see D1)*
- [x] **A2** The gas expands at 14.1 km/s, not 17
- [x] **A3** Field leak is 0.11-2.54%, not 4.4%, and the bag film goes to 0 kg
      *(bag requoted at Earth storage; handling-sized membrane owed, see D4)*
- [x] **A4** Nozzle mass floor is ~8 t, not 3.7 t, and the tape current needs naming
      *(baselined at 500 A, band 300-1000 A given)*
- [x] **A5** `tab:bag_state`'s leak row contradicts its own arithmetic *(lapsed: A3 replaced the row)*
- [x] **A6** The mirror passage needs `gamma` = 1.2 and its 56 km/s closing speed stated
- [x] **A7** Ice rod is 41 kg/m^2, not 55, and lasts five days, not a week
      *(also corrects the evaporation rate, see D5)*
- [x] **A8** `tab:bag_sizing`'s mist column has no stated model
      *(model stated and column regenerated at A3's vapour fraction)*
- [x] **A9** `tab:seed_window`'s `Rm` column is not one expansion
      *(regenerated at vL = 7.4e4; sigma column added; floor moves 3300 -> 3800 K)*
- [x] **A10** The radiated-loss column is a cold-pulse figure, not a burn-wide one
- [x] **A11** State the optical-thickness convention (diameter, not radius)

## B. Arguments that reach the right answer by the wrong route

- [x] **B1** The aperture argument is about neutrals, not open area
      *(growth figures quoted at eta_geom = 1 in the source, see D6)*
- [x] **B2** The recombination loan defaults; 19-48% of the budget is stranded
      *(also unified E_a at 50.9 MJ/kg, see D7; divergence bracket, see D8)*
- [x] **B3** `tab:seed_window`'s `Rm` and `tab:bag_state`'s leak are one quantity
      *(cliff restated at the vL A9 prints, see D9)*
- [x] **B4** The snowplow front is self-widening, which the paper does not use

## C. Framing written for arguments since retired

- [x] **C1** The `e1 ~ 0.6` crossover *(objection retracted; D3 resolved)*
- [x] **C2** Say plainly that `eta_geom` is unmeasured *(delivered by A1's `sec:jet_efficiency` paragraph)*
- [x] **C3** The swept grid runs below the forward-thrust floor
      *(space_mortgage handled by A1; two_leg annotated, cannot be re-tabulated, see D1)*

## D, E. Citations and reproduction lines

- [x] **D** Cite the eight existing keys; check the three new ones before adding
      *(all three verified against the primary literature before adding, not pasted)*
- [x] **E** Reproduction lines on the captions of the six computed tables

## Citation audit

Ran 2026-08-26 over A1-A11. Section D of the corrections document assigns a key
to each item; four commits had landed new numbers with no companion cite (A6,
A8, A10, A11) and A9 carried the impact-sim cite but not the conductivity
measurements its new `sigma` column rests on. All closed. Every number added by
A1-A11 now names the repository or the measurement it came from.

## Deferred

Items raised here and owed back to a companion repo are recorded in
`deferred_to_companion_repos.md`. D1 and D2 came out of A1.

## Reproduction log

Every companion target below was run locally on 2026-08-26 rather than taken on
trust, against a shallow clone of `katzseth22202/aim_is_all_you_need` with its
dependencies installed by `uv`. All reproduce the corrections document.

| target | covers | status |
| --- | --- | --- |
| `make cruise-thermal` | A7 | reproduces |
| `make bag-state` | A3, A5, A8, A10 | reproduces |
| `make plume-state` | A9 | reproduces |
| `make nozzle-geom` | A4, A6, B4 | reproduces |
| `make two-wave` | A1, C3, `tab:space_mortgage_growth` | reproduces |
| `make two-leg` | C1, `tab:two_leg_growth` | reproduces |

## D. Items deferred to the companion repos

Raised in `docs/deferred_to_companion_repos.md` while applying A--E, worked in
the companions on 2026-08-26, and applied back here the same day. Five paper
edits fell out (P0--P4); that document's "What landed" table is the record.

- [x] **P0** Strike the two stale rows in `paper_corrections.md`
      *(B2's cold-leg row regenerated with both sweep axes labelled; A1's `eta_chem` 0.754 -> 0.731)*
- [x] **P1** The conductivity cliff is 2450 K, not 2570, and the gap is ~1350 K
      *(2570 came from interpolating the table; the paper now says so and gives the band)*
- [x] **P2** Name the elasticity the plate column is priced at
      *(clause already landed under C1; the same sentence had the two chains swapped, now corrected)*
- [x] **P3** Requote the bag film on the handling floor, not the pressure vessel
      *(printed as the 6-25 um gauge band; no Echo 1 citation could be verified)*
- [x] **P4** `tab:seed_window`'s `Rm` column moves with the stated `vL`
      *(no-op: A9 had already regenerated the table at vL = 7.4e4)*

One item outside D1--D9 was found and left alone at the time. `sec:axial_bag` was
said to quote "0.8 kg more film", which reproduced from no row of `tab:axial_bag`.
**Closed 2026-09-02, no edit needed.** The section now reads "1.3 kg more film",
which is the 23 m row minus the sphere (6.2 - 4.9) from that table. The note also
pointed at a "One thing left alone" section of `deferred_to_companion_repos.md`
that no longer exists, since that file was deleted and recreated with only S1--S3.
Both halves of the reference are retired here rather than repaired.

## S. Items deferred to the companion repos, second round

Raised in `deferred_to_companion_repos.md` on 2026-09-01 while applying companion
ADR 0023, answered in the companions on 2026-09-02, applied back here the same day.
That document's "What landed" table is the record; `docs/adr/0007` carries the
reasoning. Six paper edits fell out (P1--P6), and two of the three answers went
against the conclusion the hold was waiting for.

- [x] **P1** Node-depth admissibility, and the plunger placement is barred
      *(new `sec:node_depth_admissibility`; four paragraphs of plunge trade in
      `sec:opposing_stream_depth` compress to one and the arithmetic moves to
      `sec:arrival_angle`; `docs/adr/0008`)*
- [x] **P2** S3 answered: the second arrival is uncharged everywhere and worth
      under 1.2% of doubling; name the architecture the 35.48-44.94 km/s belongs to
      *(the planned restructure is retired, not executed)*
- [x] **P3** S2 answered: 38.10 km/s flies the direct route shallow, so the
      crossing is about the tuning and not the architecture
- [x] **P4** The stated 0.60 node survival flatters every shallow row
      *(new `tab:derived_node_survival`; the 0.305-0.358 yr degradation was an
      artefact of the held constant)*
- [x] **P5** Bound "the split buys the pad" by its depth, (4, 5.58] R☉
      *(and at the recommended shallow end neither architecture earns its launch)*
- [x] **P5b** S1 answered the other way: the partial split's dominance is retired
      *(1.536 kg/kg becomes 3.552 once the far-node delivery is charged)*
- [x] **P6** The dangling cross-reference and the item it pointed at
      *(no-op on the paper; see the paragraph above)*
