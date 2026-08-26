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
- [ ] **B2** The recombination loan defaults; 19-48% of the budget is stranded
- [ ] **B3** `tab:seed_window`'s `Rm` and `tab:bag_state`'s leak are one quantity
- [ ] **B4** The snowplow front is self-widening, which the paper does not use

## C. Framing written for arguments since retired

- [ ] **C1** The `e1 ~ 0.6` crossover
- [x] **C2** Say plainly that `eta_geom` is unmeasured *(delivered by A1's `sec:jet_efficiency` paragraph)*
- [ ] **C3** The swept grid runs below the forward-thrust floor

## D, E. Citations and reproduction lines

- [ ] **D** Cite the eight existing keys; check the three new ones before adding
- [ ] **E** Reproduction lines on the captions of the six computed tables

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
