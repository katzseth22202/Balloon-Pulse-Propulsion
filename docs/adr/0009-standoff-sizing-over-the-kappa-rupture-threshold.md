# Standoff sizing stands, and the `kappa` rupture threshold does not bind us

Status: accepted (2026-09-03 grill on Schilling 2022, UAH PhD, "Modeling a power-generating
pulsed nuclear magnetic nozzle"). Recording this because a future reader who meets the
`kappa` literature will run the arithmetic on our own numbers, find us short of a published
threshold, and reasonably conclude the magnet is undersized. The paper now states that
exposure openly, so the reasoning behind refusing it has to be written down too.

**Amended 2026-09-03**, after reading the primary sources rather than Schilling's summary of
them. The decision is unchanged. Three supporting facts were wrong and are corrected below:
the parameter's **name**, its **attribution**, and what its denominator **counts**. The
correction is not cosmetic. The third item is now the strongest argument in this ADR.

We keep the **standoff sizing** of `sec:minimum_nozzle` (field energy density `B^2/2mu0`
set equal to plume pressure `p`) and decline to resize the magnet to the **`kappa` rupture
threshold**, on the grounds that the threshold was built for a plume geometry we do not have.

## Naming, corrected

The paper and this ADR previously called the parameter `eps_b` and credited it to Zakharov's
group. Both were wrong, and the error came from reading Schilling sec 2.2.2.1 rather than the
papers it summarises.

- The energy ratio is **`kappa`**, from Nikitin & Ponomarenko 1993 (*J. Appl. Mech. Tech.
  Phys.* 34(6) 745, `10.1007/BF00852074`).
- **`eps_b` is a different parameter**, from Zakharov's 1999 Toki overview: the ratio of the
  **ion Larmor radius to the initial plasma radius**. Schilling's own nomenclature list defines
  the two separately. For our plume that ratio is ~1e-4, four orders under any threshold, so a
  reader applying the old label literally would find the passage self-refuting.
- The value **0.4 traces to Vchivkov et al. 2003** (*JJAP* 42 6590), not to Nikitin &
  Ponomarenko, and it is for a plasma born **on the axis of the field**, not "inside a
  solenoid".

## The criterion, and where we sit against it

Nikitin & Ponomarenko define

    kappa = 12 pi E_p R0^3 / (mu0 |mu_d|^2) = E_p / E_M

where `E_p` is the plasma cloud's **kinetic** energy, `E_M` is the **dipole** field energy
integrated **beyond** the sphere of radius `R0`, and `R0` is the coil-to-target distance. The
threshold separates *quasi-capture* (field decelerates the cloud in every direction) from
*rupture* (cloud tears through and leaks). Published and measured values:

| | `kappa` |
|---|---|
| Rupture threshold, cloud born **on the field axis** (Vchivkov 2003) | 0.4 |
| Rupture threshold **measured** on a bench (Kawashima 2016) | 0.077 |
| Hyde's 1983 flown point design | 0.2 |
| **Ours, charging bore field only** | **1.50** |
| **Ours, counting bore-downstream plus exterior field** | **0.99 – 1.22** |
| **Ours, counting only field outside the plume's own volume** | **2.9 – 6.5** |

**The 1.50 is a tautology, not a measurement.** Standoff sets the bore field energy to `pV`,
and a monatomic plume holds `pV/(gamma-1) = 1.5 pV`, so the bore-only ratio is `1/(gamma-1)`
for every pulse the paper flies, whatever the geometry, whatever the propellant. No retuning
reaches 0.4. Only field energy stored *outside* the bore can lower it, and
`todos/field_energy_integral.py` computes that: modelling the graded 23 m column as a
current sheet at the 3.0 m bore and integrating `B^2/2mu0` to 400 bore radii puts 23–52%
more energy outside than a bore-only count credits. Total is a stable 19–20 GJ.

**Kawashima 2016 is the only experiment that checked the threshold** (*Plasma Fusion Res.* 11
3406012). 6.0 J into a 500 um polystyrene sphere 13 mm from a 96-turn coil; deceleration
appears only above 0.67 T, where `kappa = 0.077`. The authors call 0.4 an overestimate **for
their apparatus** and name their own geometry as the reason, since their plume left the target
on the laser side alone. Note this is one shot on one bench with an author-flagged caveat, and
that Schilling's summary of it ("`kappa_c` = 0.1 for all cases") overstates it in both the
number and the scope.

## Why we decline it anyway

**The denominator does not survive the trip.** `kappa` divides by the field energy in the
region **beyond where the plasma is born**. For a cloud born at a point that region is
unambiguous, because the cloud's own volume is negligible against it. Our plume arrives at
bore diameter, so it is not. Counting the whole bore downstream of the collision plus the
exterior gives 0.99–1.22. Counting only the field outside the plume's own volume gives 2.9–6.5.
The criterion does not say which reading is meant, because in the dipole geometry it was built
for the two coincide, and here they differ by 3–5x. **What the paper computes is a bore-based
analogue of `kappa`, not `kappa`**, and it is the flattering end of that range. The paper now
says so.

**Rupture is a bubble bursting.** The threshold was set on a compact plasma ball, born
at a point, expanding isotropically until its pressure tears open a field that was set once
and left. Three features of our pulse each break that picture, and the first is the one that
also explains Schilling's own 0.34:

1. **Our plume is not isotropic.** The collision leaves a drift along the thrust axis, so
   there is no spherically growing bubble. Weight this least of the three: `f_d = 1/(1+k)`,
   which is only 0.105 at the flown k = 8.5, worth ~3% on `eq:reflection_baseline`.
2. **It is not born at a point.** The bag (`sec:watering_it_down`) delivers the plume already
   at bore diameter, so nothing has to punch its way out to nozzle scale.
3. **The field is not set once.** Line ~1129's graded profile (20 T at 1 m falling to 5 T at
   the exit) tracks the falling snowplow pressure station by station, so there is no fixed
   field to overrun.

A criterion for whether a growing sphere escapes a fixed field is not a criterion for
whether a directed column follows a shaped one.

## Consequences

- **The exposure is quoted, not hidden.** If the criterion does transfer, the hottest pulse's
  magnet goes from 10–30 t to **37–112 t** of structure against the analytic 0.4, and further
  still against Kawashima's measured 0.077. `sec:mass_interest`'s claim that a single Starship
  can loft the seed vehicle fails. The paper states this.
- **It is conditional on a calculation we have not run.** The impact simulation of
  `sec:solid_PuffSats` decides whether the plume is a directed expansion or behaves like a
  bomb. That is the same deliverable the radiative-escape budget already waits on, so this
  adds a consumer rather than a new task.
- **If we are wrong, the fix is mass and not architecture.** Nothing about the cycle changes;
  the nozzle gets heavier and the amortization floor moves back up toward a larger ship.
