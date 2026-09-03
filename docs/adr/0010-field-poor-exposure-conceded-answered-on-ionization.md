# The field-poor exposure is conceded, and answered on ionization rather than on geometry

Status: accepted (2026-09-03, chasing the reference lists of Koba 2025 and Schilling 2024
into the Kyushu magnetic-nozzle programme). Sibling to `0009`, which declines a **rupture**
criterion. This one is about a **performance optimum**, arrives from the opposite direction,
and unlike `0009` it is **conceded rather than declined**.

## The exposure

Five independent sources put the magnetic-nozzle optimum at a field energy several times the
plasma energy. `E_B/E_p` is the inverse of `0009`'s `kappa`.

| source | kind | wants |
|---|---|---|
| Nagamine 1999, adopted by VISTA | simulation | `E_B/E_p = 5` |
| Hyde 1983 flown point design | 2D MHD design | 5 (`kappa` 0.2) |
| Saito 2018 | **measurement** | extraction saturates above **4.3** |
| Inatomi 2023 | simulation | 5, chosen to peak momentum efficiency |
| Itadani 2018 | **measurement** | `beta ~ 10` (pressure, not energy) |

**Our standoff sizing (`B^2/2mu0 = p`) puts `E_B/E_p` near 1**, so the magnet is field-poor by
roughly 4x against where they all point. Worse, Inatomi's momentum efficiency at the optimum is
**0.6–0.7** under a definition matching `eq:eta_jet_def`, and `sec:methalox_rebuttal` requires
**0.775**. We need more than the best case returns, at a quarter of the field it returns it at.

## Why this is not answered the way `0009` is

`0009` declines its criterion on geometry: `kappa`'s denominator presumes a small cloud in a
dipole, we have a bore-diameter plume in a graded solenoid. That argument does **not** transfer
here. Inatomi is a solenoid, scaled with pulse energy as `L ∝ E_p^(1/3)`, which is what we do.
Geometry is not the difference.

**The difference is ionization.** Every number in the table was taken on a thin, fully ionized
plasma. Inatomi's densest case is 3.0e-3 kg/m^3 of gold at 71.8 km/s; the bench experiments
ablate carbon or polystyrene to tens of eV. `tab:bag_sizing`'s coldest pulse is 0.32 kg/m^3
leaving at 10.8 km/s and 1.3 eV, and `sec:jet_efficiency` puts it at **5% ionized**. That is
~100x denser, ~7x slower, an order of magnitude cooler, and 95% neutral.

An `E_B/E_p` optimum measured on a fully ionized plasma says little about a 95%-neutral plume,
because **a neutral does not feel the field at any ratio**. Buying field buys no grip on
uncharged gas. This is the same fact `sec:jet_efficiency` already uses when it notes 94% of the
end-of-growth-push plume is unsteerable.

## What does *not* rescue us, and why the ADR says so

It is tempting to dismiss the whole table because this literature's model-vs-bench comparisons
miss by 3–7x in **both** directions (Inatomi JESA experiment 7x over simulation; Schilling JBIS
simulation 3–7x over experiment; Kawashima's threshold 5x stricter than analytic; Ogawa's
efficiency leaving its own power law; Koba's two pendulum methods disagreeing).

**That argument does not work on this number.** It is a reason to distrust any absolute impulse
the field quotes. A *dimensionless optimum* survives calibration errors that swallow a
magnitude, and two of the four sources for this one are measurements rather than codes. Do not
write that the `E_B/E_p` convergence is speculative. The impulse magnitudes are; the ratio is
the sturdier half of that literature.

## Consequences

- **Conceded in the paper**, in `sec:jet_efficiency`, quantified rather than gestured at.
- **The answer is conditional on ionization fraction**, which is the same
  `sec:solid_PuffSats` radiation-hydrodynamic calculation that `0009`, the radiative-escape
  budget, and `eta_chem` all wait on. If the plume ionizes far above 5%, this answer weakens
  and the field-poor exposure hardens.
- **If the optimum transfers anyway**, the fix is mass, as in `0009`: more field energy, a
  higher virial floor, a heavier magnet, and the amortization floor moves back up.
- **Retired claim**: `sec:jet_efficiency` used to say no published solenoid result states
  `eta_jet` itself. Inatomi 2023 does, under our own definition. That sentence is gone.
