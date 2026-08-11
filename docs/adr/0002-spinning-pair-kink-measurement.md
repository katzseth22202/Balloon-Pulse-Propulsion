# The spinning tethered pair measures its center-body kink; it cannot design it away

Status: proposed (five inputs unverified, listed below)

The spinning tethered pair (`sec:spinning_tension_detail`) puts the strobed beacon on a tip
package roughly 12.5 m from the water body the plate is aimed at, so the beacon's bearing is
not the impact point's bearing. Under thrust the 25 m bundle becomes a shallow V with the kink
at the center body, which the two half-tethers have to drag along. Force balance at the center
gives `sin θ = F / 2T`: at F = 400 mN of terminal thrust against T = 0.85 N of tether tension,
**θ = 13.6°, displacing the center body 2.9 m off the tip-to-tip chord**. We decided to
**measure θ** with three co-located MEMS accelerometers on the sensing package and downlink it,
rather than reduce it by design, because the isobaric-charge ceiling caps the spin rate that
sets the tension. This makes an inertial measurement load-bearing for a *disposal* package,
which is why it needs recording: the obvious future "fix" is to spin faster, and that quietly
breaks the explosive charge.

## The constraint chain

Each link is forced by the one above it, and none of it is visible in the paper today.

1. The gassed emulsion is **isobaric** only below ~0.01 g (10% gradient by 0.04 g), which caps
   ω at ~0.74 rad/s for a ~0.18 m charge radius.
2. ω caps tether tension at `T = m ω² r` = 0.85 N for a 125 g tip at 12.5 m.
3. T sets the kink at `sin θ = F / 2T`.

Holding θ ≤ 8 mrad by tension alone needs T ≥ 25 N, hence ω = 4 rad/s, hence 0.29 g at the
charge — 7x past the point where the isobaric argument has already failed. There is no spin
rate that both keeps the charge uniform and keeps the tether straight.

## Scope

θ matters only for the ~10 cm centring refinement, which needs 8 mrad across the 12.5 m arm.
The binding 2 m tolerance would need 9.2° and is not at risk from tether geometry. The 5 m
capture verdict therefore does not depend on any of this.

Applied to **all** variants at one spin rate, not scoped per variant. Non-explosive PuffSats
carry no gassed emulsion and could spin at 4 rad/s, but that means two tether designs, 20 g
tips, a fatter bundle (25 N against a 45 N break is only 1.8x), and it opens cavitation-sphere
stratification on liquid payloads — in bulk water at 10⁻³ Pa·s, Stokes creaming runs ~50,000x
faster than in the 50 Pa·s emulsion the existing buoyancy dismissal is computed for, enough to
strand a 100 µm sphere at the spin axis over a multi-day coast even at 0.01 g. One
configuration everywhere is worth more than the gram the triad costs.

## Considered options

- **Two tip beacons alone — insufficient, but adopted alongside.** Strobing both packages and
  averaging the bearings gives the chord midpoint at σ_θ/√2 (~1.1 µrad) with no range
  knowledge, no package attitude and no tether model. It cancels antisymmetric bend and is
  **blind to the symmetric kink**, which is the term that actually appears. Kept as the
  chord measurement; cannot stand alone.
- **Infer the lever arm from tip accelerometry alone — rejected.** Stacks gyro drift, a
  tip-tangent-vs-chord mode assumption, and a 12.5 m extrapolation, where the beacon pair
  measures the chord directly.
- **Beacon on the center body — rejected.** Removes the lever arm but reintroduces exactly the
  shrapnel-on-the-plate problem the tethered pair exists to solve.
- **Spin faster — rejected**, per the constraint chain above.
- **Throttle down in the terminal window — rejected.** 13.6 mN holds θ under 8 mrad, but that
  surrenders 97% of the aiming authority exactly when aiming matters.
- **Quiet period before impact — unnecessary.** The half-tether's fundamental transverse mode
  is ~11 Hz (`c/2L`, `c = √(T/μ)`, 0.27 g of bundle over 25 m), about 100x the spin rate, so
  the tether tracks throttled thrust quasi-statically with no ring to outlast. **Throttled
  thrust may run continuously to impact.** Solid-charge impulses are the exception (~2x step
  overshoot, ringing at 11 Hz) and stay early in flight.

## Consequences

- The counterweight package gains a beacon, so it is no longer fully passive, and the tracker
  associates 2N beacons instead of N.
- The triad rides the **sensing** package. A 400 mN thruster on a 125 g tip is 3.2 m/s² of
  self-induced specific force against a 0.016 m/s² signal; even 1% thrust-model error is 2x
  the signal. The paper's existing thruster/sensor split already provides this.
- Three units are for 2-of-3 voting against a silent bias (the camera-triad logic of tex:443),
  so they are **co-located, not spread**. Spreading them would buy the centrifugal gradient
  `a₂−a₁ = α×r + ω×(ω×r)`, which the gram-class MEMS gyro already covers better over the
  few-second window at ~0.17 mrad of drift.
- The inflatable bumper / nitrogen tube is **stripped before the drag phase**. At 3 cm over
  25 m it is 0.75 m² broadside and, being light with its own area, is not divided down by
  assembly mass: ~24 mN against 0.85 N of tension is a 28 mrad quasi-static bow, 300x the bare
  bundle. Open cost: the PETN variant loses its grain-strike bumper when the tether is most
  loaded.
- θ downlinks over the low-bandwidth radio (11 bits at ~2 Hz, 22 bps) rather than the beacon
  blink pattern, so the data survives the impact flashes that periodically saturate the
  tracker's rearward view (tex:439). The radio is currently budgeted for housekeeping across a
  multi-day coast, not for a live terminal duty cycle.
- θ is spin-synchronous, full when the tether axis is perpendicular to thrust and zero when
  parallel, so it is a lock-in detection problem rather than a DC-bias one.
- Disposal geometry is unaffected: tips stay 12.15 m off the impact axis against a 5 m plate.

## Open (unverified inputs)

None of these are measured; all five are estimates from the 2026-08-11 grill and belong in
`katzseth22202/aim_is_all_you_need` before any of this reaches the paper.

1. Bundle linear density μ — sets the 11 Hz mode, and with it the "no quiet period" result.
2. Charge radius (assumed 0.18 m from 25 kg at 400 kg/m²) — sets ω through the isobaric ceiling.
3. Tip package mass split (assumed 125 g each) — sets T.
4. Actual terminal thrust profile — sets the 2.9 m. The 400 mN of tex:376 is actuator
   authority, not the drag figure (17 mN), and may not be sustained at the tether-deployed phase.
5. Whether a command uplink already exists. If the PuffSat already receives the tracker's
   bearings, it can do the arithmetic onboard and the downlink is unnecessary.
