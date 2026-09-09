# Nozzle deliverables owed by `puffsat_impact_simulation`

Raised 2026-09-03, grilling Schilling 2022 (UAH PhD, *Modeling a power-generating pulsed
nuclear magnetic nozzle*) against `sec:jet_efficiency` and `sec:minimum_nozzle`. Written to be
copied verbatim into `katzseth22202/puffsat_impact_simulation`, so it repeats context the
paper repo already has.

Companion register for the other repo is `docs/deferred_to_companion_repos.md` (items S1–S4,
targeting `aim_is_all_you_need`). These are N1–N12 to avoid collision. **N1–N8 are the magnetic
nozzle and use the geometry below. N9–N12 were added for the walled thermal nozzle of
ADR-0016 and carry their own geometry, which is not this one.**

## Status, 2026-09-09

**N9 item 0 and all of N10 came back** at `puffsat_impact_simulation` `6d74d3f`, computed at
`4a448c0`. The answer document is carried in this repo at
`docs/walled_nozzle_answers_from_impact_sim.md` and applied in ADR-0016 and `CONTEXT.md`.

| item | status |
| --- | --- |
| N1–N8 | open, magnetic nozzle |
| **N9 item 0** | **answered.** The question dissolves: column length cancels, it is a throat question, and it fails at 7 m² |
| **N9 items 1–7** | **open, and now the only thing gating the paper section.** W4 confirms the sealed vessel does not soften the arrival transient |
| **N10 items 1–5, 4b** | **all answered.** See "What landed" below |
| N11 | open, not started |
| **N12** | **new**, raised 2026-09-09 by the answer to N10.3 |

**What changed in the asks themselves.** Two inputs written into N9 and N10 below are wrong and
are left in place with corrections marked, so the record shows what was asked. The
11 km/s sound speed in N9 item 0 is atomic hydrogen's and the right figure is 6.0–6.3 km/s. N10
item 4b's premise, that the chamber is 49–76% dissociated, is the thing that did not survive:
it is 93–98%.

**One sentence of context.** The paper's growth chain multiplies an uncertain projectile cost
against a nozzle efficiency nothing computes. `sec:jet_efficiency` says so outright: nothing in
the paper or either companion repo bounds `eta_geom`, and it is the largest remaining
uncertainty in the chain. Everything below is an attempt to make that sentence obsolete, plus
one item (N3) that could move a headline mass number in either direction.

**Geometry to run against, unless an item says otherwise.** The Jupiter cycle uses
a 25 kg ice projectile and a 213 kg water slug at ratio `k = 8.52`. Closing speed reaches
45.58 km/s at the slow end of the overtake burn and about 75 km/s on the head-on departure. Following P20, the adopted standoff volume is 660 m³ in a
23.7789 m column of 2.97236 m radius at 0.322727 kg/m³ (ADR-0014). The historical field is
graded per `sec:watering_it_down`: 20 T at 1 m from the chamber, 12 T at 3 m, 9 T at 6 m, 5 T
at the exit. Liner is pyrolytic graphite on an aluminium shell.

---

## N1. Report the exhaust's second moment about the thrust axis

**Priority: highest.** Cheapest item here per unit of argument it settles.

**Why.** `eq:reflection_baseline` asks what `eta_jet` would be if the nozzle only *reflected*,
reversing every particle whose lab-frame axial velocity points at the ship and losing every
transverse component. It comes out at 0.500 for a drift-free plume and 0.529 at the `k = 8.5`
we fly. **That derivation assumes the thermal remainder is isotropic, and `sec:minimum_nozzle`
says in the same breath that the head-on stagnation region "squirts radially into the field."**
Those two statements are in tension and nobody has checked which wins.

The sensitivity is steep. Write `alpha = <v_z^2>/<v^2>` over the thermal part, so isotropic is
`alpha = 1/3`. For a Gaussian family the drift-free baseline is `sqrt(2*alpha/pi)`:

| `alpha` | 0.333 | 0.300 | 0.250 | 0.200 | 0.100 |
| --- | ---: | ---: | ---: | ---: | ---: |
| baseline | 0.461 | 0.437 | 0.399 | 0.357 | 0.252 |
| shape | isotropic | mildly oblate | oblate | pancake | strong pancake |

A 40% shortfall in `alpha` costs 23% of the baseline. If the plume really is a pancake, the
paper's whole comparison against the pulsed-nuclear literature moves, and it moves the wrong
way.

**What is wanted.** The mass-weighted `<v_z^2>/<v^2>` of the expelled mass at the exit plane,
in the ship frame, with `z` along the thrust axis. A single number per pulse condition, plus
its variation across the 45.58–75 km/s range. If the distribution is far from a spheroid,
a histogram of `v_z/|v|` is more useful than the moment.

**What would settle it.** Whether plume divergence is a trim on `eta_geom` or the dominant
term in it.

**Lifts.** The unqualified use of `eq:reflection_baseline` in `sec:jet_efficiency`, and the
first of the three remaining `eta_geom` contributions.

---

## N2. Report `eta_jet` itself

**Why.** The sim already solves the expansion, so it can compute the parameter directly rather
than leave the paper quoting requirements. `eta_jet = <v_x>/v_g`, mass-weighted over the whole
expelled mass in the rocket frame, with `v_g = sqrt(2E/m)` the loss-free one-axis speed. This
is the same quantity Schilling reports as `eta_th = m*v_z/sqrt(2*m*E0)`, so the result is
directly comparable to his 0.34 and to Hyde's solenoid work.

**What is wanted.** `eta_jet` at both ends of the burn, and if the run permits, split into
`eta_chem` (already computed at 0.731 cold and 0.910 hot from the solved expansion) times
`eta_geom`. Report `eta_geom` separately even if only as a range.

**Calibration targets.** The paper's swept value is `eta_jet = 0.775`, i.e. 147% of the 0.529
reflection baseline at `k = 8.5`. Published solenoids deliver 130–170% of their own baseline;
Schilling's strut cage delivers 68% of his. **Anything at or above 130% of the baseline
supports the paper as written. Anything below 100% is a serious problem**, since it would mean
the field is doing worse than a plain mirror.

**Lifts.** `sec:jet_efficiency`'s admission that nothing bounds `eta_geom`, and the caveat in
`sec:methalox_rebuttal` that its cost chain rests on an unconfirmed efficiency.

---

## N3. Directed column or bursting bubble? The `kappa` question

**Priority: highest. This is the one that can move a mass number.**

**Why.** Nikitin & Ponomarenko report a threshold `kappa = E_p/E_M` separating clean deflection
from **rupture**, where the expanding plasma bursts through the field and leaks. `E_p` is the
cloud's kinetic energy and `E_M` the dipole field energy integrated **beyond the radius the
cloud is born at**. For a cloud on the field axis the threshold is 0.4 (Vchivkov 2003); Hyde's
flown design ran at 0.2; the one bench measurement is 0.077 (Kawashima 2016). Our standoff
sizing (`B^2/2mu0 = p`) pins the bore-only ratio at `1/(gamma-1) = 1.5` identically, because the
bore field energy is `pV` and a monatomic plume holds `1.5 pV`. That is a tautology of the
sizing rule, not a property of the magnet, and no retuning escapes it. Counting bore-downstream
plus exterior field brings it to 0.99–1.22, and counting only field outside the plume's own
volume gives 2.9–6.5.

Do not call this parameter `eps_b`. That is Zakharov's separate ion-Larmor-radius ratio, and the
paper carried the mix-up until 2026-09-03.

The paper declines the criterion on two grounds (`docs/adr/0009`). The denominator presumes a
cloud small against the field structure, which our bore-diameter plume is not, so the reading is
ambiguous by 3–5x. And rupture was measured on a compact ball born at a point and swelling until
it tears a fixed field, while ours arrives at bore diameter and meets a field graded to the
falling pressure. Both arguments are prose. This item replaces them with a run.

**What is wanted.** Expand the fireball inside the graded field above and report:
1. **Maximum `beta = p/(B^2/2mu0)` reached anywhere along the trajectory**, and where.
2. **The mass fraction that reaches the liner**, against the 4.9 kg/pulse (2.3% of slug) the
   ablation budget already books.
3. Whether the plume ever detaches from the bore and re-expands outside the winding.

**What would settle it.** Whether the magnet is sized right at 8–15 t (cold) and 17–38 t (hot),
or whether the field energy has to rise ~3× against the analytic 0.4, and over 10× against
Kawashima's measured 0.077, taking the virial floor with it. **The exposure
is 37–112 t of hot-pulse structure**, which is the difference between a seed vehicle a single
Starship can loft and one it cannot.

**Lifts.** The conditional in `sec:minimum_nozzle` ("our sizing is defensible if the plume is a
directed expansion; if it behaves like a bomb the magnet is three times too light against the
analytic threshold, and over ten times against the measured one"), ADR `0009`'s status, and
`sec:mass_interest`'s single-Starship claim.

---

## N4. Radiative escape fraction

**Why.** Standing ask, predating this session, and the binding one. `sec:minimum_nozzle` needs
the product of (radiated share of pulse energy) × (share of sky filled by hardware) near 1e-4.
With coils filling of order a tenth of the sky, **radiative escape must stay below about a tenth
of a percent for the nozzle to remain a passive structure**. The propulsive budget is far
looser: losing 5% of the pulse costs about 2.5% of `v_g` and about 5% of `v_e` at the
three-to-one mix. The thermal limit binds roughly two orders of magnitude earlier.

**What is wanted.** The radiated share of pulse energy over the full expansion, at both ends of
the burn. `tab:bag_sizing` currently estimates 1.0% to 3.6% at the flown 5.4 m bag by holding
the plume at a fixed temperature, which is acknowledged to understate the hot end threefold.

**Also wanted, separately.** The same fraction for a **100 g near-Sun projectile**. The opacity
estimate behind the current assumption was sized for the denser, slower low-orbit collision, and
`sec:minimum_nozzle` flags applying it to a gram-scale near-Sun pulse as an extrapolation. This
sets the lower edge of the 0.1–2.5 kg impactor band.

**Lifts.** `sec:solid_PuffSats`'s radiation-hydrodynamic target, the passive-structure claim,
and the lower edge of the impactor mass band.

---

## N5. Residence: confirm the plume actually leaves

**Why.** New from this session, and it is the argument that distinguishes us from Schilling.
His plume died not because his coupling was lossy (his magnetic Reynolds number runs 300 to
3e4 against our 39–650, so his field grips *more* cleanly than ours) but because his geometry
would not let plasma leave: a fenced field with 32 strut gaps and no liner, and a magnetic
bottle with its strongest field at the closed apex. The paper claims our monotonic 20 T → 5 T
profile has no local minimum, so every gram has a downhill path out. That claim is currently
geometric intuition about an on-axis profile.

**What is wanted.**
1. Time for 95% and 99% of the expelled mass to cross the exit plane, against the ~1 ms bore
   transit a 20 km/s plume implies.
2. Any mass still inside the bore when the run ends, and where it sits.
3. Confirmation that `|B|` has no local minimum along the field lines the plume actually
   samples, not just along the axis. The radial direction is the one not yet checked.

**What would settle it.** Whether "residence, not resistivity" survives contact with the real
field topology, or whether the graded solenoid has a trap nobody has looked for.

**Lifts.** The residence paragraph in `sec:jet_efficiency`.

---

## N6. Alfvén margin through the whole expansion

**Why.** Detachment needs the flow to cross from sub-Alfvénic to super-Alfvénic. The paper
computes this at one station and gets `M_A` = 1.63 (coldest pulse) and 2.06 (hottest), from
`v_A = sqrt(2*R_g*T/Mbar)` after the density cancels out of the standoff condition. Two routes
agree to 3%. But 1.63 is thin, and it is a single-point check on a quantity that varies along
the bore.

**What is wanted.** `M_A(z)` along the column, confirming the crossing happens near the throat
(`v_A/c_s = sqrt(2/gamma) = 1.095` predicts it lands about 10% past the sonic point) and stays
above 1 thereafter. Flag any station where it dips back below.

**What would settle it.** Whether the retirement of magnetic drag from `eta_geom` holds across
the whole expansion or only at the exit.

**Lifts.** The detachment paragraph's single-station check in `sec:jet_efficiency`.

---

## N7. Confirm the drift fraction the merge actually produces

**Why.** `eq:reflection_baseline` takes `f_d = 1/(1+k)` from a clean inelastic merge: the
projectile brings all the kinetic energy, the slug brings mass alone, so the centre of mass
moves at `w/(1+k)`. But `sec:needle_through_fog` establishes that the merge is *not* clean. A
compact rod punches a column through a 0.32 kg/m³ bag and sweeps 27 g of 213 kg before exiting
the far side, which is why the design moved to a plug and a snowplow. A snowplow deposits
momentum differently from a uniform merge.

**What is wanted.** The realised `f_d`, meaning the bulk kinetic energy of the merged fireball's
centre of mass as a fraction of pulse energy, against the 0.105 the clean-merge formula predicts
at `k = 8.5`.

**What would settle it.** Whether the reflection baseline is being evaluated at the right `f_d`.
Low stakes on its own, since the drift is worth only about 3% at flown `k`, but it feeds N1 and
it is nearly free once N1's diagnostics exist.

**Lifts.** The `f_d = 1/(1+k)` substitution in `sec:jet_efficiency`.

---

## N8. Re-solve the plume state at the adopted bag density

> **Density request withdrawn, 2026-09-05.** P20 restores 660 m³, giving
> 0.322727 kg/m³, which rounds to the simulation's 0.323 kg/m³. Do not rerun at
> 0.3165 kg/m³ on this request. A geometry rerun remains owed for the corrected
> 2.97236 m radius and 23.7789 m length. Existing artifacts retain their original
> inputs. See [ADR-0014](adr/0014-bag-volume-fixes-the-column-geometry.md).
> The text below records the superseded request.

**Why.** R14 adopted your 23.8 m column and the 672.9 m³ it encloses, and `aim_is_all_you_need`
has now rebuilt its own geometry on it (its ADR 0029). The bag density that falls out is
213/672.9 = **0.3165 kg/m³**. Your plume state (`data/plume_state.csv`), the conductivity fits
behind `tab:seed_window`, the conductivity cliff and the shocked sound speeds behind the
snowplow were all solved at **0.323 kg/m³**, which is 213 kg in the old 659.6 m³. The two
repositories are now 2% apart on an input every one of those solves takes.

**Nothing suggests it matters, and this is filed anyway.** The sound-speed table moves 9% across
an eightfold span in shock compression, so 2% in density is a fortieth of a known-small
sensitivity. It is raised because a vendored input should not quietly disagree with the geometry
it is used with, not because anything is expected to move.

**What is wanted.** Either the same solves rerun at 0.3165 kg/m³, or a statement that the
sensitivity is below the precision the paper prints. Either one closes it.

**What would settle it.** Whether any cell the paper quotes from those runs moves at printed
precision.

**Lifts.** Nothing. No paper edit is blocked on it. `aim_is_all_you_need` evaluates its
cross-repo pins at `nozzle_geometry.SIM_SOLVE_DENSITY` = 0.323 meanwhile, so they stay exact and
stay honest about which bag they are.

---

## N9. Does the shocked front reach the wall, and at what temperature?

**Priority: highest of the three thermal-nozzle items.** It is the load case the walled
nozzle stands or falls on, and nothing else here substitutes for it.

**Different geometry from N1–N8.** ADR-0016 admits a walled de Laval chamber as a
non-magnetic option on the head-on departure burn. Same 660 m³ column, 3 m bore, 23.8 m
length. No field. 25 kg impactor at 75 km/s into methane vapour, equilibrated chamber 10,000 K.
**Slug ratios updated 2026-09-09 from the companion's own solve** (W1, W8): methane
`k = 19.56` at 200 m³, 19.11 at 400 and 18.92 at 673, so **489 kg of methane at 200 m³** and 478
at 400, against the 474 kg and `k = 18.96` this ask first carried. Pre-charge is 1.4 bar at
111 K **in the 200 m³ chamber**, 0.70 bar in 400 and 0.41 in 673. Ammonia at `k = 28.54`
(estimated, no EOS) is the storable alternative and is worth running alongside. The flown fluid
changed from ammonia to methane on 2026-09-09 (ADR-0016), so earlier drafts of this ask carry
ammonia numbers.

**Run items 1-7 at 2, 4 and 7 m² throats, not at 7 alone.** W6 recommends narrowing the throat
and every other result agrees with it, but that stretches the pulse from 8 ms to 28 ms and
passes the same power through a third of the throat area. Pricing that is this item's job.

**Why.** The section clears the wall against the *equilibrated* 10,000 K state, where the
gas is optically thick (`tau` about 12.5 across the bore) and the wall sees 54.8 MW/m²,
1.6 MJ/m² per 30 ms pulse. That is not what arrives first. `sec:needle_through_fog` puts the
freshly shocked layer at the nose of a 45.58 km/s arrival near 94,600 K and has the 24.9°
cone reaching a 3 m wall after 6 m of the column. At that station the front has swept only
about 14 m³ of the column, roughly 14 kg against a 25 kg impactor, so its local slug ratio is
near 0.56 and a first estimate puts it near 200,000 K.

**What we need.**

0. ~~**First, and it changes the geometry:**~~ **ANSWERED 2026-09-09, and it is not a geometry
   question.** The item asked whether a *sealed* vessel escapes the coupling problem
   `sec:needle_through_fog` is about, on the grounds that at an 11 km/s sound speed a 7 m column
   equilibrates about fifty times during the blowdown, and asked for 200 m³ over 7.1 m, 400 m³
   over 14 m and 673 m³ over 23.8 m so the three would separate. **They cannot separate**: the
   turnover count is `A_bore / (f A*)` and the length divides out analytically. The 11 km/s is
   atomic hydrogen's; dissociated methane averages 3.33 amu per particle, so it is 6.0–6.3 km/s.
   The count is 23.8 turnovers at a 2 m² throat, 11.9 at 4 and **6.8 at 7, which fails the
   tenfold criterion.** The sealed vessel sets `k` only for throats of about 4 m² or narrower.
   The geometry choice returns to the thermal and Isp arguments, and the Isp argument is worth
   1.2% across the range, so it is thermal and structural.
1. Contact station and arrival time of the front against the wall at 75 km/s into methane at
   `k = 18.96`, with the spreading model already used for `sec:needle_through_fog`.
2. Local temperature, density and swept mass at contact.
3. Fluence delivered to the wall over the contact transient, in MJ/m², separated into
   radiative and convective parts.
4. Whether a continuously injected cold film at 0.02 to 0.2 kg/m² measurably reduces (3),
   given that at those areal densities it is optically thin to the equilibrium field.

5. **Throat carbon deposition.** The methane exhaust carries 376 kg of carbon per pulse through
   a 2 to 7 m^2 throat. A drifting throat area is the one dimension a nozzle cannot tolerate.
   The throat is the hottest and fastest station so it should self-clean, but nothing shows it.
   Report net deposition or removal per pulse at the throat and along the liner, since the same
   number decides whether the liner is self-healing (0.34 to 3.7% redeposition suffices).
6. Whether a sprayed carbon film laid between pulses survives the front. `sec:watering_it_down`
   rules a sprayed film out for the magnetic nozzle liner ("no film thin enough to spray lasts
   through it") because that liner faces a plume at 45.58 km/s. The walled case stagnates the
   gas and the load is radiative, so the rejection may not carry over. Paper-side numbers are
   2.2 microns per pulse at 200 m³ and 12.5 at 673 m³, against GA-5009's ~150 microns of
   antiablation oil on a 0.8 to 1.5 s recycle.

7. **Convective wall flux, which is the crudest number carrying the most weight.** The paper-side
   estimate is a Bartz-like scaling off a single anchor, giving 123 to 281 MW/m^2 between 10,000
   and 18,000 K against a radiative 16 to 75. It is therefore 80-90% of the wall load, and it is
   what sets the chamber temperature ceiling rather than radiation. Report it properly at
   200/400/673 m^3 and at 10,000, 12,000 and 15,000 K. **The flown point is 10,000 K**, chosen
   because the gain from going hotter is 2.5% per 2,000 K and smaller than this very estimate's
   own uncertainty. What the run would decide is whether that choice is forced or merely
   prudent: 15,000 K is worth 1.192 GN.s per launch load against the magnetic nozzle's 1.225, so
   if the wall turns out to be comfortable the near-tie is reachable after all.

**What it decides.** Whether the section states a survivable wall or carries the front as an
open condition, and it picks the chamber geometry and temperature. It also decides whether the wall is a thin
sprayed steel skin or a thick refractory liner, currently booked at 2.2 to 12.5 microns of
graphite per pulse from the equilibrium load alone.

## N10. Recombination along a walled expansion, `N+N+M` and `H+H+M`

**Priority: high. ANSWERED 2026-09-09, in favour of equilibrium.** The Damköhler number never
enters the freezing band anywhere in the bore, with 2.16 decades of margin at the flown point
against a 0.5-decade rate uncertainty, so the frozen 793 s branch does not apply.

**Why.** The whole case for a walled nozzle over a magnetic one is that a physical throat
holds density up where a field lets the plume thin, and three-body recombination goes as
`n²`. `sec:watering_it_down` finds the water plume freezing at 0.02 kg/m³ with 90 to 100% of
the bond energy still held, because a magnetic nozzle free-expands it. Bray's sudden-freezing
criterion is the mechanism (`bray1959recombination`). Hand-estimated margins against a 1 ms
transit at chamber density are ×3400 for `H+H+M` and ×403 for `N+N+M`. Nitrogen is about eight
times slower, which is why it freezes in arcjets at 0.1 to 1 bar. Nobody has solved it here.

**There is a published anchor, and it should be reproduced first.** Project 242
(`augelli2013project242`, read in full 2026-09-08) writes that molecular recombination is *not*
fast, but its carried baseline of 2700 s needs 351 MJ/kg of stagnation enthalpy where
sensible-only hydrogen at 10,000 K gives 206. That implies about 67% of the dissociation energy
returning at a few bar, where paper-side arithmetic puts the `H+H+M` margin near 0.014.
**Those two statements are in tension and the solver should say which is right**, because our
own claim rests on the same reaction at 139 times the number density. Run their case at a few
bar and 10,000 K alongside ours at 206 and 694 bar. Reproducing a published Isp at the thin end
while predicting recombination at the dense end exercises the mechanism across four orders of
magnitude in three-body rate with a real answer at one end, which is the strongest single
validation available here.

**What we need.** Along the de Laval expansion from 206 bar and 10,000 K through a 7 m² throat:
1. The freezing station and the frozen fraction for `N+N+M` and for `H+H+M` separately.
2. ~~Fraction of the atomisation energy returned as directed kinetic energy: 103.7 MJ/kg for
   methane, 68.9 for ammonia.~~ **ANSWERED.** Atomisation is 102.35 MJ/kg on a 0 K reference
   state, not 103.7 on a 298 K one. Through the flown 7 m² throat the nozzle converts **39.3 to
   40.6% of the wall-cap energy into directed kinetic energy**, which is the convention-free
   statement and carries nobody's normalisation. Ammonia is not run: there is no `eos_ammonia`.
3. The same for a water slug at `k = 37.70` and for pure hydrogen at `k = 7.99`, so the ladder
   in ADR-0016 rests on solved chemistry rather than on the equilibrium assumption.
4. Sensitivity to throat area, since that is the knob that sets how long the gas stays dense.
4b. **Chamber dissociation equilibrium. ANSWERED 2026-09-09, and the premise did not survive.**
   The item was written as "report the composition, we already know it is 49 to 76%". It is
   **93 to 98%**, the store is 95 to 99% charged, and the paper-side correction that moved
   methane from 1,132 s to 1,059-1,095 s is withdrawn. The paper-side two-parameter fit missed
   because `H2 <-> 2H` at 10,000 K has `D0/kT = 5.2`: half dissociation would need 81.5 kg/m³
   and ~14,000 bar, thirty times the densest chamber here. **N9 and N10 are no longer one
   question.** Volume is worth 1.2% on Isp across 200 to 673 m³, not 3.4%, so it no longer
   fights the thermal case and the geometry can be chosen on thermal and structural grounds
   alone.
5. **Carbon condensation. REFRAMED 2026-09-09 and much smaller than booked.** The item treated
   the whole 43% as hostage to nucleation. `2 CH4 -> C2H2 + 3 H2` returns 89.0% of full
   atomisation with no particle formed, so 84% of the carbon store comes back in the gas phase
   and only **7 points of atomisation, 5.2% of the energy budget**, needs actual condensation.
   The 52%/43% split itself is confirmed exactly (52.6 and 43.3). **What is now the top priority
   on this rung is the acetylene kinetics, not the nucleation**: the Damköhler work prices
   `H + H + M` only, so nothing shows the `C -> C3 -> C2H2` path keeps up during the expansion,
   and it is worth 59 points of atomisation against soot's 7. That is ordinary combustion
   kinetics (`C2H + H2`, `C2H2 + H`). The remaining 7 points still need classical nucleation
   theory and cannot be substituted by a rate coefficient: the evaluated literature holds one
   measurement of `C + C + M` and nothing at all for `C + H + M`.

## N11. Radiative escape and wall fluence for a carbon-bearing plume

**Priority: medium.** It moves a number the section prints rather than a conclusion.

**Why.** The paper-side estimate anchors opacity on an A0 photosphere and scales it as
`sqrt(rho)`, which is a hydrogen argument applied to a nitrogen-bearing gas. Nitrogen's first
ionisation is 14.53 eV, above hydrogen's 13.60, so its free-electron continuum should be lower,
but its bound-bound line forest is not something the scaling covers.

**What we need.** Planck and Rosseland means for the methane plume between 3,000 and 15,000 K
at 0.5 to 4 kg/m³, then the escaping flux and the per-pulse wall fluence through
`eq:cooling_race`. Report the radiated share of the 70.3 GJ pulse. The paper-side figure is
1.2%, and it is the least defended number in the section.

## Where N9-N11 land in the code that already exists

Read against `puffsat_impact_simulation` at `c11424c` (2026-09-06). **None of these three is a new
simulation.** Each is a species set and a geometry on machinery that is already written.

| ask | already there | missing |
| --- | --- | --- |
| N9 | `python/puffsat/front.py`: `integrate`, `shock_state`, `spread_speed_table`, `FrontRun`, `FrontStation`. It already returns contact stations (ADR-0013 quotes them). | Run at 200/400/673 m³ on the 3 m bore with a methane EOS, reporting **contact temperature and swept mass** rather than `field_demanded_at`. Sealed-vessel equilibration (item 0) needs no EOS at all. Add throat carbon deposition. |
| N10 | `python/puffsat/recombination.py` is already exactly Bray's criterion as a Damköhler ratio, with `atom_three_body_coefficient` (`K_ATOM_THREE_BODY = 6.1e-38`, exponent `-2.0`) for `H + OH + M -> H2O + M`, the ionisation and dissociation stores carried separately, and a field reporting how many decades the coefficient could be wrong before the verdict flips. `expansion.nozzle_history` already walks a throat. `eos_water.INTERMEDIATES` **already contains H2**. | `H + H + M` and `N + N + M` coefficients beside the existing one, plus **carbon nucleation, which is not a three-body reaction and needs different machinery**; an `eos_methane.py` (and `eos_ammonia.py` for the alternative); a no-field variant of `nozzle_history`; the Rubbia validation case. |
| N11 | `opacity_bracket.py`, `continuum.py`, `radiance.py`, `lte.py`, the TOPS grid. | These are water-shaped. Nitrogen opacity is the genuinely hard extension here and the reason N11 is ranked below the other two. |

`eos_water.py` is 783 lines of from-scratch partition functions and a Saha ladder, and it is the
single largest piece of work. It is built around a reusable `Diatomic` dataclass, so N2 and H2 drop
into the same frame rather than needing a new one.

**Do N10 first.** ~~It decides an effective specific impulse of 1,080 s against 793 s~~ **Done,
2026-09-09, and it came back on the equilibrium side with 2.16 decades of margin.** The Rubbia
validation worked: 2,700 s is 24–29% above the frozen ceiling, so their own number requires the
recombination their prose denies.

**Do N9 items 1–7 next, and they are now the only gate on the paper section.** Everything else
that could move a number has moved. Two of N10's answers make them harder rather than easier:
W6 recommends narrowing the throat from 7 m² to 4 or 2, which stretches the pulse from 8 ms to
28 and passes the same power through a third of the throat area; and W4 shows the impactor
crosses the column in 0.08 of an acoustic transit, so the sealed vessel does nothing for the
arrival transient. **Run items 1–7 at 2, 4 and 7 m² rather than at 7 alone.**

## What landed, N9 item 0 and N10

Nine findings, W1–W9 in the answer document. The four that moved a number the paper prints:

| finding | verdict | where it landed |
| --- | --- | --- |
| **W1** (N10.4b) | **Reverses the ask's premise.** 93–98% dissociated, store 95–99% charged. The 2026-09-09 paper-side correction is withdrawn | ADR-0016's ladder; `CONTEXT.md` **The store is charged**. Methane 1,120–1,133 s |
| **W2** (Project 242) | **Settled.** 2,700 s is 24–29% above the frozen ceiling of 2,085–2,229 s and needs 52–63% of the store back | ADR-0016's Project 242 section; `CONTEXT.md` **Project 242 read in full** |
| **W5/W6** (N10.1–4) | **Fork closes on equilibrium**, and the binding constraint turns out to be expansion ratio rather than chemistry | ADR-0016 **The throat is the largest lever**; `CONTEXT.md` **The throat is the lever** |
| **W9** (N10.5) | **Carbon exposure is six times smaller.** 84% returns as gas-phase acetylene; 5.2% of the budget is hostage to soot | ADR-0016 **What stays open**; `CONTEXT.md` **Acetylene is where the carbon store actually goes** |

**One correction went back the other way.** W1 scaled specific impulse by `sqrt(1+k)/k` and got
two answers 3% apart depending on which paper row it anchored on, and flagged that something
else was in the paper's column. It is the drift term: the paper's form is
`w(eta*sqrt(1+k) - 1)/k` and the `-1` subtracts a velocity rather than scaling one. Applying the
paper's own formula to the solved `k` gives 1,120 / 1,129 / 1,133 s at 200 / 400 / 673 m³,
between W1's two rows. `todos/ladder_companion_k.py` reproduces all three sets.

## N12. Carry per-fluid conversion into the launch ledger

**Priority: highest of the walled-nozzle items after N9.** It is the number ADR-0016's central
fluid choice rests on, and nothing in the paper owns it.

**Why.** The ladder charges every fluid the same conversion fraction, meaning it assumes each
one hands back the same share of its store through the nozzle. W8 solved three of them through
identical geometry and they do not agree: hydrogen 0.532, water 0.415, methane 0.406. Hydrogen's
store banks straight into `H2`; methane's parks in `C3` at the exit plane (W9). Exhaust speed
goes as `sqrt(conversion)`, so carrying the difference raises hydrogen 14.5% against methane and
moves the launch ledger to 1.032 against methane's 1.098. **Methane's lead closes from 32% to
6%, which is inside the uncertainty on `eta_geom` that the paper already sweeps.**

**What is wanted.** Conversion fraction for each fluid on the ladder through the same throat,
solved rather than borrowed, and specifically an `eos_ammonia` so the one assembled rung becomes
a solved one. Ammonia draws level with methane at a conversion of 0.601 against methane's 0.406,
which is a large ask but not an absurd one, since hydrogen reaches 0.532 in the same geometry.

**What would settle it.** Whether ADR-0016 still names methane, and whether the ladder's
ordering below its top rung survives.

**Lifts.** ADR-0016's "Why methane rather than the hydrogen the precedent points at", and the
`_Avoid_` line on `CONTEXT.md`'s **Conversion is a chemistry result, not a nozzle constant**.

## Suggested order

N1 and N3 first. N1 is a diagnostic on runs that probably already exist and it decides whether
the paper's central efficiency comparison stands. N3 needs a field to be added to the model but
is the only item that can move a quoted mass. N2 falls out of N1's diagnostics. N4 is the
standing ask and binds two orders of magnitude before the propulsive budget does, so it should
not wait behind the new items. N5, N6 and N7 confirm arguments the paper already makes and are
cheap once the machinery for N1–N3 exists. N8 is bookkeeping and is on nobody's critical path.

## Reproducing the paper-side numbers

Probes live in the paper repo under `todos/` (gitignored, so copy rather than expect them):

| probe | what it computes |
| --- | --- |
| `reflection_baseline.py` | `eq:reflection_baseline`, `f_d(k)`, the anisotropy table of N1 |
| `alfven_detachment_probe.py` | `v_A` two ways, `M_A`, downstream scaling |
| `epsilon_b_probe.py` | `kappa` against the rupture threshold, mass exposure (filename predates the rename) |
| `field_energy_integral.py` | field energy over all space for the graded column |
| `temperature_floor_probe.py` | what the 3800 K and 2450 K floors cap in `k` |
| `ladder_dissociation.py` | the **withdrawn** 2026-09-09 dissociation correction; kept so the mistake reproduces |
| `ladder_companion_k.py` | the ladder, the throat table and the N12 sensitivity on the companion's solved `k` |
