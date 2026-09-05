# Nozzle deliverables owed by `puffsat_impact_simulation`

Raised 2026-09-03, grilling Schilling 2022 (UAH PhD, *Modeling a power-generating pulsed
nuclear magnetic nozzle*) against `sec:jet_efficiency` and `sec:minimum_nozzle`. Written to be
copied verbatim into `katzseth22202/puffsat_impact_simulation`, so it repeats context the
paper repo already has.

Companion register for the other repo is `docs/deferred_to_companion_repos.md` (items S1–S4,
targeting `aim_is_all_you_need`). These are N1–N8 to avoid collision.

**One sentence of context.** The paper's growth chain multiplies an uncertain projectile cost
against a nozzle efficiency nothing computes. `sec:jet_efficiency` says so outright: nothing in
the paper or either companion repo bounds `eta_geom`, and it is the largest remaining
uncertainty in the chain. Everything below is an attempt to make that sentence obsolete, plus
one item (N3) that could move a headline mass number in either direction.

**Geometry to run against, unless an item says otherwise.** The Jupiter-cycle departure burn:
a 25 kg ice projectile closing head-on with a 213 kg water slug at slug ratio `k = 8.5`, over
the burn's speed range of 45.58 km/s (coldest, last pulse) to 75 km/s (hottest). Standoff
volume 672.9 m³ poured into a 23.8 m column of 3.0 m bore (`eq:bore_from_length`) at a bag
density of 0.3165 kg/m³, with the field
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
