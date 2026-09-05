# Water-injected pusher plate for the overtake leg

Proposed 2026-09-05 by Seth Katz. Handoff to `katzseth22202/puffsat_impact_simulation`,
written to be copied into that repository's `docs/` directory. This is a proposed
comparison, not a simulation result or a decision to replace the magnetic nozzle.

## Scenario and question

On the growth push, a PuffSat overtakes the vehicle from behind. Spray water through
distributed holes in the rear-facing pusher plate just before and during the pulse.
The water mixes with the incoming gas near the plate, absorbs collision energy, and
joins the exhaust that expands back out behind the vehicle. Include bowl-shaped
plates, with shallow bowls in the initial comparison rather than treating them as
a later refinement.

The question is whether this arrangement delivers more useful impulse per kilogram
of carried consumables than the magnetic nozzle under the same overtake conditions.
Two mechanisms could help. Cold water may prevent some dissociation or allow broken
molecules to re-form while the mixture still pushes the plate. The added water also
provides exhaust mass that collision heat can accelerate. A material plate accepts
pressure from neutral gas without a conductivity requirement.

The reference encounter is a 25 kg water/ice PuffSat, represented at impact by an
explicit gas or droplet state. Use the growth-push closing-speed anchors of
45.58 and 56.53 km/s for the 3-synodic case, and 61.83 and 65.13 km/s for the
2-synodic case. These are overtake cases. The approximately 75 km/s head-on
departure is a different impulse ledger and is outside this proposal.

Let `k = m_water / m_projectile`. Include `k = 0` as the unsprayed control and
`k = 8.5` as a matched-water-mass comparison with the existing nozzle. At 25 kg,
the latter injects 212.5 kg per pulse. This is bulk reaction mass, not a thin
protective coating. Sweep intermediate water loads; 8.5 is a comparison point,
not an assumed optimum.

## Requested order: ideal mixing first, atomization requirements second

Seth's instruction is to assume successful gasification and mixing for the first
performance calculation. Do not make droplet breakup, evaporation, or injector
engineering prerequisites for that calculation.

**Stage 1: assume the delivery works.** Treat the added reaction mass as fully
gasified and locally mixed with the incoming material wherever their flows meet,
with immediate thermal equilibration there. Specify the injected gas's spatial
density, temperature, velocity, and time profile. This assumption removes a local
mixing delay; it does not redistribute mass across the entire bowl instantaneously.
Run the flat and shallow-bowl comparisons and compute the resulting impulse,
chemistry, and wall loading. Successful gasification does not prescribe full
recombination recovery; that remains an output of the cooling history.

Keep the energy accounting consistent with the stored material. If the pulse
supplies vaporization energy, subtract it from the pulse budget. If a separate
system supplies that energy, record it as an input. Water is the reference, but
the concept permits another substance that becomes gas just before mixing.
Name its gas products and phase-change or chemical energy rather than assuming
water's properties for it.

**Stage 2: work backward to the required water atomization.** For the useful Stage 1
cases, replace the ideal gas delivery with liquid-water droplets and determine how
fine the spray must be to retain the benefit. Atomization means breakup into small
droplets; gasification means their conversion to vapor. Report both processes.

Start with a broad logarithmic sweep of initial droplet diameter and refine near
the performance transition. Include aerodynamic breakup, droplet acceleration,
heating and vaporization, and heat and mass transfer into the surrounding gas.
Use the local shocked flow and its changing relative velocity, not the projectile's
closing speed throughout. Compare pre-injection lead time with injection during
the pulse at fixed total water mass. Track expansion or freezing before arrival
when it changes the available water distribution.

Report the following requirements for each selected speed, water load, and bowl:

- Largest initial droplet diameter retaining 90%, 95%, and 99% of the ideal
  collision-induced impulse gain. Define that gain consistently as
  `G = J_with_pulse_and_injection - J_injection_only - J_unsprayed_with_pulse`.
  Compare `G_droplets / G_ideal` only where `G_ideal > 0`; otherwise report
  absolute impulse differences. These are reporting contours, not requirements
  that have already been chosen for the vehicle.
- The acceptable size distribution, including a mass-weighted upper-tail diameter
  and the allowed mass fraction in larger drops. A small number-average diameter
  can conceal most of the water mass in a few ineffective large drops.
- Breakup, vaporization, and thermal-equilibration times alongside the interval
  over which the ideal case delivers its impulse. Report vaporized and mixed mass
  fractions during that interval, rather than only after the exhaust has departed.
- Injection timing and gas-density ranges that retain the gain, with surviving
  liquid or ice, missed water, and residual chemical energy included in the ledger.

The Stage 2 deliverable is a usable spray specification in micrometers and timing
units, with its dependence on the encounter conditions. If a single size threshold
does not describe the result, provide the diameter-versus-timing contour instead.
If water cannot meet it, identify whether pre-gasification or a different
gas-generating material removes the limiting process. Report Stage 1's result
before undertaking that design work.

## What the chemistry argument does and does not establish

The paper's water-nozzle reference calculation finds chemical freeze-out with
90–100% of the dissociation store still held, stranding about 19–47% of the
dissipated collision energy across its reference cases. These percentages belong
to that nozzle trajectory, not to every water impact or to the proposed spray.
See the companion repository's `python/puffsat/fireball.py` and
`python/puffsat/toll.py`.

The plate study's ADR-0026 retains equilibrium chemistry as its central estimate.
At the ordinary-impact performance dip, its compressed gas reaches roughly
2–8 kg/m³ and 7,000 K, and its estimated recombination time is shorter than the
rebound. That is evidence for dense-phase recovery, not a resolved cooling history
for this faster, water-injected encounter. The same ADR retains a pessimistic
freeze bracket and gives the hotter, dilute 69 km/s case a weaker kinetics defence.

Test the proposed mechanism where molecular formation becomes favorable, not only
at peak compression. Follow temperature, gas density, species, chemical energy,
and expansion time through the part of the pulse that produces wall impulse.
For `H + OH + M -> H2O + M`, the reaction time scales as
`1 / (K(T) n_OH n_M)`. Density helps strongly, but the partner abundance and
temperature must come from the evolving mixture. Liquid droplet density is not
the gas density to insert into this rate.

Distinguish energy never spent on dissociation from energy returned by
recombination. Also distinguish returned energy that becomes useful pressure work
from energy leaving as radiation, warm droplets, or internal energy in the exhaust.
Recombination after the gas ceases to push the plate does not recover vehicle impulse.
Track ionization and molecular bond energy separately, with a consistent energy zero
for liquid, vapor, and dissociated species. Vaporizing the injected water costs energy.

Equilibrium and sudden-freeze runs can bracket an initial screen. A favorable
equilibrium run alone cannot establish the claimed chemistry advantage. The useful
follow-up is a trajectory-based freeze check or finite-rate species evolution that
resolves how much chemical energy returns before pressure coupling ends.

## Momentum accounting and the paper claim this tests

The current paper, `sec:two_leg_nozzle`, argues that mixing one projectile kilogram
with `k` stationary kilograms gives `(1+k)` kilograms drifting at `w/(1+k)`.
Those factors cancel when computing the incoming bulk momentum. It then concludes
that a slugged plate gives only `2 f m_projectile w`, and says a plate cannot use
the collision's thermal energy.

The bulk-momentum cancellation is correct. Extending it to all of the impulse is
not justified for a hot mixture expanding against a plate. The cancellation omits
pressure driven by the dissipated collision energy and the acceleration of injected
water into exhaust. This proposal asks the simulation to measure that contribution;
it does not assume that all thermal energy is captured.

Use the initial vehicle frame with `+z` prograde. The incoming projectile has
momentum `+m_projectile w`, and useful exhaust leaves in `-z`. For a control volume
covering the vehicle and its initially carried water, the complete pulse ledger is

`J_vehicle = m_projectile w - P_out,z`,

with all escaping material and radiative momentum included in `P_out,z`. Account
for residual stored momentum if the integration stops before the pulse settles.
Include injection recoil and feed-system forces when reconciling this ledger with
the integrated force on the plate. Spraying water already transfers momentum;
do not count it again when that water is struck or redirected. Run a spray-only
control to separate injection thrust from the collision-induced increment.

For negligible vehicle recoil, initially stationary cold water, negligible added
injection energy, complete ejection, and loss-free axial exhaust, the ceiling is

`J_max = m_projectile w [1 + sqrt(1+k)]`.

It follows from `E_in = m_projectile w²/2` and exhaust mass
`M_ej = (1+k) m_projectile`, giving maximum backward momentum
`sqrt(2 M_ej E_in)`. This is an energy-and-momentum ceiling, not a plate prediction.
It is available to either material or magnetic redirection under those assumptions.
At `k = 8.5` it gives `J_max / (m_projectile w) = 4.082`, compared with 2 at `k = 0`.
Count pump energy or additional ablated mass explicitly if either changes the budget.
Do not add the incoming momentum a second time to a wall impulse that already includes it.

Report `beta = J_vehicle / (m_projectile w)` for this study. Retain the existing
`f` convention for the unsprayed plate control, where `beta = 2f`. Injected mass
changes the available exhaust momentum, so the old bare-plate normalization is
not a universal efficiency ceiling for the new device.

## Plate geometry and water delivery

Start with a flat control and shallow bowls at depth-to-diameter ratios
`delta/D = 0.10` and `0.15`, matching the existing plate geometry anchors.
Here `D = 2R` is the projected plate diameter and `delta` is rim height above the
vertex. Hold projected diameter and incoming footprint fixed in the first comparison.
Report actual surface area and structural mass as curvature changes.

The bowl may redirect radial flow backward and retain pressure near the plate
longer. Measure those effects rather than prescribing a collimation gain. Record
local peak pressure and heat flux, especially where opposing flows converge.
ADR-0021 already finds a pressure-concentration cost for shallow concavity.
Greater total impulse does not by itself make the curved plate survivable.

Deeper bowls can be a second-stage comparison if the shallow cases justify them.
The existing deep-bowl objection concerns focusing a nearly parallel incoming pulse;
its scope amendment and ADR-0032 distinguish that from expansion out of a compact
source. A distributed spray struck by an incoming pulse is neither automatically
a point source nor the old plane-wave problem. Determine where energy is deposited
before selecting a focal geometry or transferring either study's curvature result.

Compare water placed just before impact with the same total water split between
pre-injection and injection during the pulse. Specify the time profile, velocity,
temperature, injection angle, and radial distribution. In Stage 1, prescribe these
as gas-source conditions. Begin with axisymmetric injection bands if needed,
documenting how they represent discrete holes. Include a uniform distribution and
a distribution chosen to intercept outward flow across the bowl. Stage 2 adds the
droplet-size distribution and resolves the actual delivery.

The Stage 2 delivery model must establish the gas density after breakup and
vaporization, the intercepted water column mass, and the mixing time relative to
the pulse. Its purpose is to determine how closely a spray can approach the
assumed Stage 1 performance. Feed-system implementation follows the ideal screen:
water injected during the pressure peak must overcome local pressure or use a feed
arrangement that prevents backflow. Then include gas leakage through holes, loading
of the perforated face, and the consumed water and pumping energy in the comparison.
ADR-0024's thin-cushion result does not settle this bulk-water design, but its
requirement to account for the full pressure history still applies.

## Comparisons and requested outputs

Run the following controls at matched arrival speed, projectile mass, footprint,
and pulse duration:

| Configuration | What it separates |
| --- | --- |
| Unsprayed flat and shallow-bowl plates | Existing rebound and curvature performance |
| Spray-only plates | Injection recoil and water lost before interception |
| Water-injected flat and shallow-bowl plates | Added-mass benefit, chemistry, and curvature together |
| Water magnetic nozzle at the same `k` | Whether changing the cooling and redirection path recovers the water penalty |
| Current argon-nozzle alternative, with all composition changes named | Whether a water-plate advantage survives comparison with avoiding molecular dissociation in the nozzle |

Use the nozzle's demonstrated result or stated performance range. Its geometric
efficiency remains an input unless computed. Likewise, do not import a plate's
equilibrium `f` as a measured result for the new spray. The ordinary plate study's
separation of thermophysics from geometry needs checking here because injection,
curvature, and mixing can change the cooling history together.

For each candidate report:

- Net vehicle impulse, `beta`, and `J_vehicle / m_projectile`.
- Impulse per kilogram of carried consumables, including all injected water,
  ablator, and other expendables. Report `Isp_eff = J_vehicle / (g0 m_charged)`
  only when that denominator is nonzero. Charge water that misses the pulse too.
- Exhaust axial momentum and kinetic energy, with sideways escape, remaining
  thermal and chemical energy, radiation, and wall heating reconciled to the input.
- Cumulative wall impulse alongside chemical-energy release and gas density through
  cooling. This is the evidence that any recombination recovery occurs soon enough.
- Peak local pressure, heat flux, integrated wall heat, ablation, and the plate and
  injection-system mass needed to support the selected geometry and cadence.

First establish whether injecting water increases collision-induced impulse, then
whether the gain pays for the consumed water, and finally whether a survivable bowl
outperforms the nozzle at matched carried mass. The companion mission calculation
can price permanent hardware and repeated consumption after those per-pulse outputs
exist. A chemistry advantage by itself does not establish the preferred architecture.

## Source trail for the receiving repository

Reviewed against `puffsat_impact_simulation` at `6fe8cf3`:

- `CONCLUSION.md` and `docs/adr/0026-frozen-recombination-bracket.md` for the plate
  chemistry bracket and its limits.
- `python/puffsat/fireball.py` and `python/puffsat/toll.py` for water-nozzle freeze-out
  and the distinction between the chemical penalty and incoming bulk momentum.
- `docs/adr/0021-plate-shape-deep-dish-foreclosed.md`, including its scope amendment,
  for shallow bowls and pressure concentration.
- `docs/adr/0024-wall-side-cushion-cannot-relieve-peak.md` for the thin-buffer argument.
- `puffsat_tamper_isp_prd.md` for carried-mass accounting and the related head-on
  study. This proposal has an incoming momentum credit (`+1`), whereas that study
  has a debit (`-1`). Its numerical optima and source geometry do not transfer.

In the paper repository, the relevant passages are `sec:two_leg_nozzle` and
`sec:watering_it_down` in `templateArxiv.tex`. This handoff requests the comparison;
it leaves their replacement prose for a separate paper edit.
