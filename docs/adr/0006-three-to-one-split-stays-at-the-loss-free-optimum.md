# The 3:1 prograde/retrograde split stays at the loss-free optimum

Status: accepted (2026-08-17 grill). The decision is to publish a number we know is not
the practical optimum, so it needs recording or someone will "fix" it.

`sec:dv_effective` derives a one-quarter retrograde, three-quarters prograde mix as the
split that maximizes momentum per unit of PuffSat mass collided. That derivation assumes
the merged fireball leaves as a single collimated jet, every gram at one speed along one
axis. That is not an approximation that could err either way. It is the momentum-maximizing
bound for a given mass and energy, so every real device lands strictly below it. We decided
to **keep 3:1 as the published result**, name the loss parameter, and state the family the
3:1 belongs to, rather than restate the architecture at the ratio a lossy nozzle actually
prefers.

This is hard to reverse because the split is not a chamber knob. `sec:no_isru_rocket`
commits three quarters of the payload to a prograde Sun-grazing trajectory and one quarter
to the opposing retrograde one, both reached through Jupiter gravity assists. The manifest
is fixed years before the collision happens.

## The reframing

Define the **jet efficiency** `η_jet` as the mass-weighted mean axial exhaust velocity over
the RMS of the full exhaust velocity, both in the rocket frame (`eq:eta_jet_def`). It is
bounded to `(0,1]` by Cauchy-Schwarz. Then

- `v_e = 2 v_p (η_jet √m_rp − m_rp)`
- optimum at `m_rp = η_jet²/4`, i.e. `(4/η_jet²) − 1` parts prograde to one
- `v_e = η_jet² v_p / 2` at that optimum
- thrust **vanishes** at the pass-through floor `η_jet ≤ √m_rp`

So 3:1 is the `η_jet → 1` endpoint of a family. At 0.8 the optimum is ~5:1, at 0.7 ~7:1.

Two things fell out of the reframing that were not obvious beforehand. First, the merged
fireball's centre-of-mass motion does **not** need re-thermalizing, which was the original
worry that opened the grill. It holds a fraction `m_rp` of the energy (25% at 3:1), already
points retrograde, and its momentum exactly equals the incoming projectile's, so on its own
it nets **zero** thrust. All thrust comes from collimating the thermal `1 − m_rp` share, and
roughly half of that heat starts out moving toward the ship and must be mirrored by the
field. Second, the floor at 3:1 is `η_jet = 0.5`, which is uncomfortably close to the values
the paper already assumes.

## Why keep 3:1

- **The peak is flat where it matters.** Holding 3:1 costs about 1% of the thrust achievable
  at `η_jet = 0.9`, 6% at 0.8, and 18% at 0.7.
- **The downstream numbers are already consistent with a lossy nozzle at 3:1.** The lunar
  cycle's assumed `v_e = 3 km/s` against an ideal 5.5 is exactly `η_jet = 0.77` at a 3:1 mix.
  The 1.455 growth factor and the 2.8-year figure need no re-derivation. Restating the split
  would require re-running the companion repo's calculations for a ~9% gain.
- **The derivation answers an idealized question honestly.** Publishing a different single
  number would be equally hostage to an unknown `η_jet`, while publishing the family plus the
  floor is falsifiable.

## Considered options

- **Restate the architecture at ~5:1. Rejected, but it is the better *design*.** A minimax
  over `η_jet ∈ [0.7, 1.0]` puts the robust ratio near 5:1 (retrograde fraction ~0.17), which
  stays within 4% of the achievable optimum across that whole range where 3:1 falls to 82% at
  the low end. It also cuts the average lunar departure ΔV, since retrograde departure costs
  3.7 km/s against 3.0 prograde. Rejected on revision cost, not on merit. The paper now says
  explicitly that a flown architecture should bias prograde.
- **Broaden the existing fudge factor `f` to cover the nozzle. Rejected.** `f` is pusher-plate
  restitution and has no referent where there is no plate. The two also fail differently:
  a plate at any `f` still passes some momentum forward, while a nozzle below its floor passes
  none. `sec:methalox_rebuttal` had asserted the near-Sun mixing-chamber efficiency *was* `f`;
  that was a category error and is corrected.
- **Put the caveat in the appendix only. Rejected.** Two body-text sites contained live
  defects rather than missing caveats, so an appendix-only note would have documented a limit
  the body still violated.

## Consequences

- **A real arithmetic error surfaced and is fixed.** `sec:methalox_rebuttal` conflated `v_g`
  (gas speed, the energy bound) with `v_e` (effective exhaust velocity, after debiting the
  incoming retrograde momentum) at the Earth step, assuming 25 km/s where the head-on ideal
  ceiling is 24. The headline ~$3/kg survives at `η_jet = 1` (now $3.17), but the margin is
  thinner than it read.
- **The methalox rebuttal now carries an explicit requirement.** Break-even against methalox
  sits at `η_jet ≈ 0.9` at the pessimistic $3200 anchor. At 0.8 the doubled bill is ~$17/kg
  and that version of the argument fails. The scale case at $11/kg fleet cost holds to ~0.7.
  Below 0.5 nothing works at any price.
- **`sec:minimum_nozzle` gained a thrust budget** alongside its existing mass and heat budgets.
  It also had a related error: "losing 5% of the pulse costs about 2.5% of exhaust velocity"
  is true of `v_g`, but `v_e` is a difference, so the same loss costs about 5% at 3:1 and far
  more near the floor.
- **`v_g` and `v_e` must stay distinct in all future edits.** Collapsing them is what produced
  the error above.

## Open (unverified inputs)

1. **No nozzle model supplies `η_jet`.** Every value in the paper is a requirement inferred
   from a mission number, not an estimate from physics. This is the single largest unbacked
   input in the direct-launch architecture.
2. **The magnetic pressure needed at the throat** to mirror the ship-facing half of the
   fireball is uncomputed. It belongs with the deferred radiation-hydrodynamic calculation of
   `sec:solid_PuffSats`.
3. ~~Reported laboratory magnetic-nozzle efficiencies have not been checked.~~ **Checked
   2026-08-17, see "Literature check" below.**
4. **`η_jet` is treated as constant across a burn.** It plausibly varies with impactor mass and
   with periapsis depth, in the same way `f` is known to vary with relative velocity.

## Literature check (2026-08-17), and why the decision held

Ahedo and Merino, already cited in the paper as `ahedo2010magnetic`, report a **plume
efficiency** of **0.63 to 0.83** across their sweep of divergence rate and ion magnetization
(Table II: 0.83, 0.81, 0.78, 0.72, 0.69, 0.63, 0.63). They define it as the axial share of the
downstream jet's energy, so it is power-like and maps to `η_jet²`. That caps **`η_jet` at
roughly 0.79 to 0.91**, and only because it charges for radial spreading and not for spread in
axial speed. Real `η_jet` sits below that ceiling. Their model assumes a collisionless,
electron-magnetized, current-free, low-β plasma, none of which describes a dense fireball whose
own pressure exceeds the field, so it anchors the question rather than settling it. A lower and
less transferable anchor: a REGULUS-150-Xe simulation study (arXiv:2411.11977) finds magnetic
nozzle energy conversion falling from ~0.5 to ~0.2 as anomalous cross-field transport rises to
Bohm scaling, i.e. `η_jet ≈ 0.71` down to 0.45. That is a 30-150 W RF thruster and is not cited
in the paper.

This reopened the 5:1 option, because the effect that matters in the cost cascade is not
exhaust velocity but **dilution of the expensive retrograde mass, six-fold at 5:1 against
four-fold at 3:1**. That moves the methalox break-even from `η_jet ≈ 0.90` to `≈ 0.80`, from the
top of the Ahedo band to its middle. The original ADR had rejected 5:1 on revision cost "not on
merit", and the merit side had just improved.

**Decision reaffirmed: keep 3:1.** The 0.9 figure is not a physics requirement and not an
architecture requirement. It is the break-even of one rhetorical argument against methalox at
its own deliberately worst-case $3200/kg early-generation projectile price, which is 290 times
the $11/kg the same paper projects at scale. Nothing about the propulsion fails at 0.85. Only
three thresholds are real, and they differ in kind:

- **`η_jet` < 0.5** — no thrust at all at 3:1, the fireball passes through. The only hard
  physical limit, and the Ahedo band clears it.
- **`η_jet` < 0.7** — the scale energy case stops delivering under $1/MWh.
- **`η_jet` < 0.9** — the $3200 early-generation anchor stops undercutting methalox.

The paper now states the band and the three thresholds outright rather than restating the
architecture, which is an honest result rather than a failure and costs no revision pass. Should
the projectile-cost anchor ever become load-bearing rather than rhetorical, revisit 5:1 first.

## Editing constraint

Applied additively at the author's instruction. Every original sentence survives except four
corrections where keeping the text would mean keeping an error: the 25 km/s assumption at
`sec:methalox_rebuttal` (above its own 24 km/s ideal ceiling) and its downstream arithmetic,
the labelling of `v_g` as an "energy ceiling" on exhaust velocity, the pricing of a 5% radiation
loss at 2.5% of `v_e` rather than of `v_g`, and the attribution of the near-Sun nozzle efficiency
to the pusher-plate restitution factor `f`. The appendix section title keeps its original
wording with the new subsection appended.
