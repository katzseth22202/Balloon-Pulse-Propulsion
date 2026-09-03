# Standoff sizing stands, and Zakharov's rupture threshold does not bind us

Status: accepted (2026-09-03 grill on Schilling 2022, UAH PhD, "Modeling a power-generating
pulsed nuclear magnetic nozzle"). Recording this because a future reader who meets the
`eps_b` literature will run the arithmetic on our own numbers, find us three times short of
a published threshold, and reasonably conclude the magnet is undersized. The paper now
states that exposure openly, so the reasoning behind refusing it has to be written down too.

We keep the **standoff sizing** of `sec:minimum_nozzle` (field energy density `B^2/2mu0`
set equal to plume pressure `p`) and decline to resize the magnet to Zakharov's
**`eps_b` rupture threshold**, on the grounds that the threshold was measured on a plume
geometry we do not have.

## The criterion, and where we sit against it

Zakharov's group (via Schilling sec 2.2.2.1) defines

    eps_b = (plasma energy) / (integrated magnetic field energy)

with a threshold separating *quasi-capture* (field turns the plasma cleanly) from *rupture*
(expanding plasma bursts the field and leaks). Published values:

| | `eps_b` |
|---|---|
| Rupture threshold, plasma expanding **inside a solenoid** | 0.4 |
| Rupture threshold, plasma expanding **outside** the nozzle | 0.1 |
| Hyde's 1983 flown point design | 0.2 |
| **Ours, charging bore field only** | **1.50** |
| **Ours, integrating field energy over all space** | **0.99 – 1.22** |

**The 1.50 is a tautology, not a measurement.** Standoff sets the bore field energy to `pV`,
and a monatomic plume holds `pV/(gamma-1) = 1.5 pV`, so `eps_b = 1/(gamma-1) = 1.5` for
every pulse the paper flies, whatever the geometry, whatever the propellant. No retuning
reaches 0.4. Only field energy stored *outside* the bore can lower it, and
`todos/field_energy_integral.py` computes that: modelling the graded 23 m column as a
current sheet at the 3.0 m bore and integrating `B^2/2mu0` to 400 bore radii puts 23–52%
more energy outside than a bore-only count credits. Total is a stable 19–20 GJ. That closes
about a quarter of the gap and leaves us short by 2.5–3x.

## Why we decline it anyway

**Rupture is a bubble bursting.** The threshold was measured on a compact plasma ball, born
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
  magnet goes from 10–30 t to **37–112 t** of structure, and `sec:mass_interest`'s claim that
  a single Starship can loft the seed vehicle fails. The paper states this.
- **It is conditional on a calculation we have not run.** The impact simulation of
  `sec:solid_PuffSats` decides whether the plume is a directed expansion or behaves like a
  bomb. That is the same deliverable the radiative-escape budget already waits on, so this
  adds a consumer rather than a new task.
- **If we are wrong, the fix is mass and not architecture.** Nothing about the cycle changes;
  the nozzle gets heavier and the amortization floor moves back up toward a larger ship.
