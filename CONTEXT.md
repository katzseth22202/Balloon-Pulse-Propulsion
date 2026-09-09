# PuffSat Pulsed Propulsion

Canonical language for the *Aim Is All You Need* white paper and its companion
control simulation. These are the project-specific terms that recur across the paper,
the edit backlog (`updates_back_to_paper.md`), and the design discussions. Definitions
are tight and opinionated: where several words exist for one idea, one is canonical and
the rest are listed as aliases to avoid.

## Language

### Core propulsion

**PuffSat**:
A small expendable projectile (gas-generating or solid) sent to collide with a moving
rocket and transfer momentum for pulsed propulsion.
_Avoid_: pellet, slug (those evoke the pellet-beam prior art the paper distinguishes
itself from).

**Pusher plate**:
The momentum-buffer surface on the main craft that the PuffSat gas or solids strike,
mounted on a shock absorber. About 5 m wide in the near-term design, where it doubles as
a debris shield.
_Avoid_: target plate, impact plate.

**Medusa-style sail**:
A flexible pusher mounted *behind* the rocket on shock-absorbing struts. Because it sits
behind, its struts carry **compression** (and can buckle), unlike real Project Medusa's
front-mounted **tension** sail.
_Avoid_: calling ours simply "Medusa" without the behind/compression qualifier.

**Buffer invariant**:
The relation `m·s ≈ M a T²/4` tying buffer mass `m` and absorber stroke `s` for craft
mass `M`, acceleration `a`, and pulse period `T = 1/f`. The shared law behind both the
rigid plate (short stroke, heavy or high-frequency) and the Medusa sail (long stroke,
light).

**Fudge factor (`f`)**:
The energy-loss factor in the PuffSat-to-rocket mass-ratio law (`eq:PuffSat_ratio`): the
axial momentum a gas pulse delivers to the pusher plate as a fraction of the
full-capture, perfect-bounce ideal. Ranges `0.5` (perfectly inelastic, gas sticks) to `1`
(perfectly elastic, gas rebounds and pushes about twice as hard), and below `0.5` if some
gas misses the plate. The paper selects `f = 0.8`. A preliminary single-code hydrodynamic
simulation (companion repo `puffsat_impact_simulation`) finds `f ≈ 0.8` reasonable across
the 3.2–16 km/s gas-collision envelope; the same analysis finds **sideways spill** (gas escaping past the
plate edge, a.k.a. sideways escape; the geometric loss channel that pushes `f` toward and
below 0.5) subdominant in the LEO insertion band; the result is *not yet independently validated*, so
the paper cites it as plausible, not confirmed (see Flagged ambiguities).
_Avoid_: presenting `f = 0.8` as validated/confirmed; the symbol `f` also denotes pulse
frequency in the buffer invariant (`T = 1/f`), a distinct quantity; using `f` for the
prograde/retrograde collision-plus-nozzle case (that is **jet efficiency (`η_jet`)**, a
different quantity with a different failure mode); using `f` for the slug-augmented
head-on departure nozzle (that is **recovery (`e`)**, a collimation claim, not an elasticity one).

**Jet efficiency (`η_jet`)**:
The nozzle-side loss factor in the prograde/retrograde collision law (`eq:ve_general` in
`sec:jet_efficiency`): the mass-weighted mean *axial* exhaust velocity divided by the
loss-free gas speed `v_g`, both measured in the rocket frame over the whole expelled mass.
Cauchy-Schwarz and energy conservation bound it to `(0,1]`. It reaches 1 only if every gram
leaves at the loss-free speed in one direction. Its square is the fraction of available
collision energy represented by coherent axial momentum. This definition absorbs plume
divergence, exhaust-speed spread, radiation escaping before it can be turned, frozen-flow
(ionization/dissociation) losses, and mass the field fails to grip. Consequences: the optimal
mix is `m_rp = η_jet²/4`, i.e.
`(4/η_jet²) − 1` parts prograde to one retrograde, so **3:1 is the `η_jet → 1` endpoint of a
family, not a fixed number**; `v_e = η_jet² v_p / 2` at that optimum. Forward thrust vanishes
at the pass-through floor `η_jet = √m_rp` and reverses below it (0.5 at 3:1, 0.2 at 24:1).
Because a plate at any `f` still passes some momentum forward while a nozzle below its floor
produces net backward impulse, heavy dilution is the cheap insurance wherever the added
propellant is cheap. Values the paper pins implicitly: 0.77 (lunar cycle,
`sec:no_isru_rocket`), ~0.89 required (methalox rebuttal at its
$3200 pessimistic anchor), ~0.7 required (scale energy case). None is computed from a nozzle
model; all are requirements, in the same sense as the radiative-escape budget of
`sec:minimum_nozzle`. Published anchors (2026-09-03): Ahedo & Merino's plume efficiency
of 0.63-0.83 (power-like, so its square root bounds `η_jet`) gives a divergence-only ceiling
near **0.79-0.91**; their model is collisionless, electron-magnetized, current-free and
low-β, so it anchors rather than settles. Hyde's 2D MHD **solenoid returns 0.65**, the
geometry-matched **upper bound** -- Table 2.1's column is Nakashima's *plume efficiency*
(Eq 2.8, `sum m*v_z / sum m*|v0|`), a collimation ratio, **not** the `η_th` that equals our
`η_jet`. Only Schilling's **0.34** is `η_th` (Eq 2.10, `m*v_z/sqrt(2mE0)`, which *is*
`<v_x>/v_g`), and it sits below our 3:1 floor. But his plume is a drift-free exploding target,
so his **reflection baseline** is 0.50 and he reached 68% of it, against our 0.775 at 83% of
0.93. **No published solenoid result states `η_jet` itself for a pulse like ours.** One named
component of `η_geom` is now retired: see **detachment**.
_Avoid_: conflating with the **fudge factor (`f`)**; calling `η_jet` an efficiency in the power
sense; treating 3:1 as a validated optimum rather than the loss-free endpoint; conflating with
**recovery (`e`)**, which scales the impulse *after* the momentum debit and so has no floor.

**Recovery (`e`)**:
The third efficiency, and the steep axis of the Jupiter-only 30-year growth table
(`sec:jupiter_only_growth`, companion ADR `0013`). The fraction of the *ideal collimated
impulse* a real magnetic nozzle delivers on the slug-augmented head-on departure burn:
collimation, geometric capture and plasma coupling lumped into one number.
`v_e = e · w · (√(1+k) − 1) / k`, where `w` is closing speed and `k` the slug ratio.
Distinguished from the other two on purpose:
- vs **jet efficiency (`η_jet`)**: `η_jet` scales the jet *before* the incoming-momentum debit
  is subtracted (`v_e = η_jet v_g − 2 v_p m_rp`), which is why it has a pass-through floor at
  `√m_rp`. `e` scales the whole net impulse, debit already inside the bracket, so **`e` has no
  thrust-reversal floor**: any `e > 0` still pushes forward. The `e = 0.25` row of the growth
  table fails on *transport accounting* (the loop cannot pay its own costs), not on thrust
  reversal, and must not be described as a physics wall.
- vs **fudge factor (`f`)**: `f` is an elasticity claim about gas bouncing off a plate; `e` is a
  collimation claim about a plume. They coincide numerically only in the `k → 0` limit, which is
  why `astro_constants.STD_FUDGE_FACTOR = 0.8` is reused as the ideal-ceiling `e`. Different
  hardware claims; no source calibrates either. That same `k -> 0` limit is what makes a pusher
  plate the *no-slug nozzle*, and so decides the leg-1 device choice: see **Overtake leg vs
  head-on leg**.
ADR `0013` makes `e ≈ 0.3` the architecture's survival threshold and finds `f` worth about as
much as `e` (a 0.3 drop in `f` costs what a 0.2 swing in `e` does).
_Avoid_: quoting an `e` without the `f` it assumed, or vice versa; calling the `e = 0.25` row a
thrust floor; using `η_jet`'s 0.5 three-to-one floor as if it bounded `e`.

**Gas speed (`v_g`) vs effective exhaust velocity (`v_e`)**:
Two distinct quantities in `sec:dv_effective`. `v_g = 2 v_p √m_rp` is what the collision energy
alone allows, the speed the merged mass would carry if every gram left at one speed along one
axis. `v_e = η_jet · v_g − 2 v_p m_rp` is what the rocket actually gains per unit PuffSat mass
spent, after debiting the momentum the retrograde PuffSat brought in head-on. At the 3:1
optimum they differ by 2× (`v_g = v_p`, `v_e =
v_p/2`). Because `v_e` is a *difference* rather than a fraction, a fractional loss in `v_g`
appears roughly doubled in `v_e` at 3:1, and far more as `η_jet` nears the pass-through floor.
The retrograde share arrives externally, so total collision mass per final vehicle mass is
`[exp((1-m_rp) Δv/v_e) - 1]/(1-m_rp)`, not the conventional `exp(Δv/v_e) - 1`.
_Avoid_: calling `v_g` an "energy ceiling" on exhaust velocity; it ceilings `v_g`, not `v_e`.
That conflation produced a real error in `sec:methalox_rebuttal` (an assumed 25 km/s that
exceeded the 24 km/s ideal ceiling), corrected 2026-08-17.

**Impulse trim (mass-mismatch trim)**:
How a pre-placed transport formation absorbs the rocket plane's flight-day mass differing
from the mass the orbits were planned around (decided 2026-07-17 grill; lives at the end of
`sec:200_mile_high`). The formation is sized for the plane's **maximum takeoff mass**; every
lighter flight trims the delivered impulse *down*, since nothing already in orbit can add
impulse for a heavier plane. Three knobs in authority order: (1) **unit count** — withhold
surplus PuffSats (~1/N granularity; withheld units deorbit on their microthrusters or hold
for a later window); (2) **timing detune** — atomize early/late so the cloud arrives at the
plate off-shape, lowering the delivered momentum via the **fudge factor (`f`)**; fine vernier
only, because the impact sim's shape study (ADR-0028) finds `f` gently sloped and cliff-free
(max normalized sensitivity S ≈ 0.26 inside an *assumed* ±20% shape box) and the
timing-to-arriving-shape mapping (the deferred cloud-schedule study) is not yet simulated;
(3) **onboard ballast/fuel trim** — top off fuel or ballast toward the design mass and pump
fuel between tanks so the center of mass sits where the down-kick plate geometry
(`sec:pusher_plate_down_kick`) assumes it (Concorde trim-tank precedent, Rech & Leyman).
The retrograde deceleration formation inherits the same knobs with better information
(reentry mass is fixed at takeoff).
_Avoid_: presenting timing detune as a large-authority knob or quoting its S value without
the assumed-shape-box caveat; "axially symmetric mass distribution" (the requirement is the
center of mass on the impulse line through the impact point, not full symmetry).

**Magnetic nozzle**:
A magnetic field that redirects the conductive collision plasma with no material contact,
so there is no ablation and no thermal-fluence size floor. The plasma cooperates only when
it is hot enough to be a near-perfect conductor (high magnetic Reynolds number `Rm`), so a
magnetic nozzle is a *high-energy-regime* tool: favored near the Sun (fully ionized,
`Rm ~ 10⁷`), not at LEO insertion (weakly ionized gas, where a material plate wins). Used
two ways with opposite energy goals. In **propulsion** (near-Sun chamber,
`sec:periapsis_challenges`) it *reflects* the plasma near-elastically to redirect momentum
for thrust; the field is a conservative spring, and the momentum floor still reacts as J×B
on the coil. In the **Straw Way power plant** it *guides* the plasma (a ~90° turn from the
vertical tube into a horizontal, km-long MHD channel) so its kinetic energy can be
*extracted* as electricity; here braking the plasma is the point, not conserving its
momentum.
Coupling has **two** sides and the paper long argued only one. `Rm` measures **grip**;
**detachment** measures **release** (see its own entry). Pushing `Rm` up is what the design
does on purpose, and that is exactly the knob Hoyt says causes the dominant steady-state loss.
_Avoid_: implying it removes the momentum/mass floor (it removes ablation only); conflating
the propulsion "reflect for thrust" role with the power-plant "guide-then-extract" role;
arguing `Rm` upward without saying how the plume gets loose again.

**Wall-cap energy density (the argument that picks the working fluid)**:
How much energy a kilogram of slug can hold at the temperature a wall survives. A walled
nozzle's exhaust speed is `w/sqrt(1+k)`, and `k` is set by this number, so it decides
everything. At 10,000 K, solved by the companion: **hydrogen 320.8 MJ/kg**, methane 136.8,
ammonia 95.2, water 69.4. Helium is 31 and unsolved. The paper-side estimates were 338 /
143 / 98 / 72, high by 3 to 5%. Hydrogen holds five times water because it has 992 mol of particles per kilogram
after dissociation and parks 214 MJ/kg in H-H bonds, which is storage that costs no
temperature and comes back on expansion.
Corollary that explains why the magnet is not simply beaten: a magnetic nozzle has **no**
temperature cap, so it runs water at `k = 8.52` and 15,000 K holding 295 MJ/kg of mixture,
and wins even while freezing 19-47% of its chemistry. A walled *water* nozzle gives 872 s
effective against the magnet's 1,249 s and is strictly dominated. The wall's cap costs more
than the magnet's frozen chemistry unless the fluid is hydrogen.
_Avoid_: arguing fluid choice from temperature at fixed `k` (any gas reaches 10,000 K if you
carry enough of it); arguing it from launch cost (methane wins that, see below).

**Why methane, and the two objections against it that failed (2026-09-09)**:
Methane was rejected on 2026-09-08 and reinstated as the flown pick on 2026-09-09. Both
objections were mine and both were wrong.
**The soot-lag objection was calibrated on the wrong particle.** Solid rockets pay 5-8% because
alumina is ~5 um of dense liquid. Soot primaries are 30 nm. Velocity relaxation times against a
1 ms residence: 30 nm gives 1e-9 s (x1e6 margin), a 1 um agglomerate 1.1e-6 s (x900), 5 um
alumina 2.8e-5 s (x36). Even micron agglomerates follow the flow with three orders to spare.
**The Z>1 glow objection reverses in an optically thick chamber.** Carbon does give 1.84x the
free electrons and 3.4x the volumetric emission at 10,000 K. But escape is
`sigma T^4 (1-e^-tau)/(1+0.75 tau)` and the same electrons raise `tau`. At `tau >> 1` more
absorbers means **less** escapes. Rubbia's chamber is `tau ~ 0.003`; ours is 7 to 42. His
transparency argument is a low-density argument, exactly like his recombination finding, and
neither transfers. Same mistake as the recombination one, made twice.
**The endothermic cost is a tie.** What never returns is the formation enthalpy, not the
atomisation energy: NH3 -> 1/2 N2 + 3/2 H2 costs 2.70 MJ/kg, CH4 -> C(s) + 2 H2 costs 4.15
(the paper carried 4.66; the gap is a 298 K against a 0 K reference state, and ammonia's has not
been rechecked at 0 K). Both a few percent.
**And the carbon is the sacrificial layer the design already wants.** The liner loses 1.26 to
13.9 kg per pulse against **376 kg of carbon in the exhaust**, so 0.34% to 3.7% has to
redeposit for it to be self-healing. A water or ammonia exhaust carries nothing that could
rebuild it and has to be sprayed. Methane's exhaust is the spray.
_Avoid_: the "75% condensed is unprecedented" framing; it compares soot to alumina droplets.

**The slug ladder (thermal nozzle, solved by the companion 2026-09-09)**:
Every `k` below is the companion's, solved on a nine-species equilibrium EOS with NIST-JANAF
thermochemistry (`puffsat_impact_simulation@4a448c0`, W1 and W8). They are **outputs**, and
where the paper had already stated one they come back inside 5%: hydrogen 7.77 against a
stated 7.99, water 39.55 against 37.70. Effective Isp and the ledger are the paper's own,
from `todos/ladder_companion_k.py`.
The section presents a family ordered by **Wall-cap energy density**, not a single fluid.
At 75 km/s head-on, 10,000 K chamber, 400 m^3, `eta_geom = 0.852`, 25 kg impactor,
7 m^2 throat:

| slug | k | slug/pulse | holds | eta_chem | eff Isp | GN.s/load | vessel | storage |
|---|---|---|---|---|---|---|---|---|
| **methane (flown pick)** | 19.56 | **489 kg** | **136.8** | 0.637 | **571-716 s** | **0.560-0.702** | **8.7 t** | 422 kg/m^3 @ 111 K |
| ammonia* | 28.54 | 714 kg | 95.2 | *0.640* | *523-642 s* | *0.513-0.630* | 9.5 t | 682 kg/m^3 @ 240 K |
| liquid hydrogen | 7.77 | 194 kg | 320.8 | 0.729 | 828-1,100 s | 0.460-0.611 | 11.6 t | 71 kg/m^3 @ 20 K |
| water alone | 39.55 | 989 kg | 69.4 | 0.644 | 483-584 s | 0.473-0.573 | 9.2 t | ambient |
| (water on the magnetic nozzle) | 8.52 | 213 kg | -- | 0.910 | 1,249 s | 1.225 | 17.3-37.6 t | ambient |

**The ranges are the two ends of `eta_geom`, 0.852 and 0.98, and that is ask N13.** The
`eta_chem` column is what changed on 2026-09-09: every walled row used to carry an implicit
1.000 and the magnetic row has always carried 0.910. See **The two nozzles were never on the
same convention**.

\* **Ammonia is assembled, not solved.** There is no `eos_ammonia`, so its `k` comes from the
paper's own 68.9 MJ/kg atomisation plus an exact translational term, and its conversion
fraction is borrowed from methane. It is the one row that could still move by more than a few
percent.
**Methane is the flown pick.** It leads on launch ledger (+11% over ammonia), vessel mass
(-8%), slug mass per pulse (-33%) and toxicity, and Starship already flies it so the tankage and
boil-off management are flown hardware. Hydrogen keeps the best Isp, by 45-54%, and loses the
ledger to volume by 15-22%. **Ammonia is second on Isp, not fourth.** The withdrawn dissociation
correction had it tied with water; with the store charged it is clear of water.
Recombination products: methane returns 52.6% as H2 and 43.3% as carbon, confirmed exactly by
the companion from heats of formation, with the remaining 4.2% the formation enthalpy that
never returns. **But most of that carbon comes back as gas-phase acetylene, not as soot** (see
**Acetylene is where the carbon store actually goes**). Ammonia returns 95.6% as gases
(3H->1.5H2 55.3%, 2N->N2 40.3%); hydrogen returns all of it as H2.
**The ladder charges every fluid the same conversion fraction and that is now known to be
wrong**, which is ask N12. See **Conversion is a chemistry result, not a nozzle constant**.
**Scoring convention, so the sets of numbers are not mixed.** The paper-side ladder was solved
**without** ionisation, which keeps it a pure fluid comparison independent of chamber volume and
costs 0.5% at 10,000 K. Its `k` values were methane 18.96 / 17.94, ammonia 27.53 / 25.93, water
37.70 / 35.57, hydrogen 7.99 / 7.43 at 10,000 / 12,000 K. **The companion's solve carries
ionisation and the C+..C6+ Saha ladder and lands within 5% of all four**, which is the check that
both sides use the same energy ledger. Since the chamber now flies at
10,000 K too, **the flown numbers are the ladder's own** and there is no second solve to
reconcile. Ionisation is 0.5% at this temperature (`k` 18.96 against 18.86), below every other
uncertainty.
**The number worth staring at is water.** `k = 39.55` solved, on a wall, against the `k = 8.52`
the magnetic nozzle flies. Same fluid, same collision, 4.6x the slug, and the entire factor is
the temperature cap. It is the clearest single demonstration of what a wall costs.
Assumptions behind every entry: `w = 75` km/s, a 25 kg polyethylene impactor at 83.7 MJ/kg
atomisation, `eta_geom` swept 0.852 to 0.98 (N13), **`eta_chem` per fluid from the companion's
solved conversion** (this used to say "full recombination" and that was the error), `k` from the
companion's equilibrium solve, and effective Isp `= [(1+k)*eta_geom*u_e - w]/(k*g0)` charged
against the ship's slug only. That reduces to the paper's `w(eta*sqrt(1+k) - 1)/(k*g0)` when
`u_e = eta_chem * w/sqrt(1+k)`, so it is the same model with the chemistry no longer set to 1.
_Avoid_: presenting one fluid as the answer; the ordering by energy-at-the-wall-cap is the
result and the fluid falls out of it. Do not mix the ionised and un-ionised solves.

**The wall limits temperature, not energy (why the two nozzles want opposite fluids)**:
The cleanest statement of what `Wall-cap energy density` is really measuring. A chemical bond is
energy the propellant carries **without the wall ever seeing it as heat**. Methane hides
102.35 MJ/kg from the wall in bonds (the paper carried 103.7; the gap is a 0 K against a 298 K
reference state, not a disagreement); helium can hide nothing, so every joule it absorbs becomes
temperature, and temperature is the one thing the wall caps.
Held at 12,000 K: hydrogen 362.8 MJ/kg, methane 150.3, **helium 37.4**, argon 3.7. Methane holds
4.0x helium, and only 1.25x of that is particle count (5 atoms per 16 amu against 1 per 4). The
other 3.2x is the chemical store. **Helium has no loss mechanism at all and is still worse**: it
would need a **48,800 K** chamber to reach methane's slug ratio. Its Isp is 667 s against
methane's 1,154, and argon's is 232 s.
**The paper already chose the opposite fluid for the magnetic nozzle, and both choices are
right.** `sec:watering_it_down` picks argon because it is "25 mol against dissociated water's
166 mol, so the same energy has a sixth as many particles to share it among and the plume runs
hotter and further ionized." Running hotter buys conductivity and field grip when there is no
wall. It is fatal when there is one. **The wall is what flips the objective, so the thermal
nozzle cannot inherit the magnetic nozzle's slug.**
**Why adjusting `k` per fluid does not rescue helium.** `k` is already solved per fluid (helium
72.13, methane 17.94 at 12,000 K). The adjustment *is* the penalty. **The slug does two jobs at
once and they pull opposite ways**: it is the heat sink that holds the chamber under `T_max` and
it is the reaction mass. A fluid that absorbs more per kilogram lets you carry less, and
carrying less is what makes the exhaust fast, since `v ~ sqrt(E/m)` at fixed pulse energy.
Helium absorbs a quarter as much per kg, so it carries 4x the mass and the exhaust is 2x slower.
**Bonds hide energy from the pressure vessel too, and this is the sharpest form of the
argument.** Vessel mass is `1.5*nRT*rho/sigma`, and `nRT` is set by the **sensible** energy
alone; chemical storage contributes nothing to `pV`. Helium must contain all 70.3 GJ as
pressure, methane only the 21.5 GJ that is actually heat. Vessels: **9.9 t methane against
31.2 t helium**, with 2,274 bar against 724 and 2.5x the convective load.
**Corollary that kills the obvious workaround:** helium's chamber pressure is 2,274 bar at
*every* temperature, because all its energy is sensible so `nRT` is pinned by the pulse. Heating
it buys no pressure relief.
**Helium is nonetheless a real floor, and the section should say so.** Methane returns 1,154 s
with all chemistry and 452 s with nothing returning; the 880 s middle row is **withdrawn**,
because W9 shows only 5.2% of the budget is hostage to soot rather than 32%. Helium's guaranteed
667 s beats the bottom row. It is not reachable (H+H+M now carries a solved 2.16 decades of
Damkoehler margin, not the hand-estimated x3400), but it is the honest reason a monatomic option
cannot simply be dismissed.
**The transparency argument for helium gets a hearing and fails.** Monatomic, no bound-bound
below 20 eV, first ionisation 24.6 eV, so its *radiative* ceiling really is higher than
methane's. But it needs **48,800 K** to tie 1,154 s, and there its convective load is 10x worse
at the same pressure with four times the delta-T. Transparency buys some temperature, not a
factor of four.
_Avoid_: assuming a monatomic gas is safer because nothing can freeze. It is safer and much
worse, and the section should say both.

**The free-impactor benefit is `(1+k)/k`, it is already inside every Isp quoted, and the wall
dilutes it**:
Effective Isp divides the pulse impulse by the ship's own slug `k*m`, not by the ejected
`(1+k)*m`, so the impactor's mass is never charged to the vehicle. **Verified against the paper's
own form, which looks different and is not**: `eq:ve_general` divides by `(1+k)` and then
`eq:external_reaction_mass` applies `(1-m_rp)` inside the rocket equation, and
`(1-m_rp)/v_e_paper = 1/v_e_here` to six figures. These numbers therefore go into the
**standard** rocket equation, not the modified one, and drop into the paper's framework unchanged.
**The benefit is exactly `(1+k)/k` and shrinks as `k` grows**: hydrogen walled 12.9%, water on the
magnetic nozzle 11.7%, ammonia walled 3.5%, **methane walled 5.1%**, water walled 2.5%.
So **the wall charges twice**. It forces a higher `k`, which slows the exhaust, and the same high
`k` dilutes the free reaction mass that is this architecture's whole premise. At 20 kg of carried
slug per kilogram arriving, "the propellant comes from outside" is no longer most of the story.
Hydrogen is the only walled option that keeps it.
**It also rewards the light fluid twice**, which is why the ordering is not negotiable by nozzle
design. A fluid that soaks up the pulse in a small slug gets a proportionally larger free ride
from the impactor mass it never lifted, so low `k` is paid once in exhaust speed and again here.
_Avoid_: adding this as a bonus on top of the quoted Isp. It is a decomposition, not a charge;
the 571-716 s already contains the 5.1%.

**Partial dissociation corrects the headline (2026-09-09) -- WITHDRAWN THE SAME DAY**:
**Do not use anything in this entry.** It is kept because the mistake is instructive and
because two other entries still cite it. The companion solved the same equilibrium properly
on a nine-species EOS with NIST-JANAF thermochemistry and found the chamber **93 to 98%
dissociated at 10,000 K**, with the chemical store **95 to 99% charged**, not the 49 to 76%
this entry booked. See **The store is charged, and here is why the paper-side fit missed it**.
Methane returns to 1,120-1,133 s and the ladder returns to something close to the
full-atomisation ordering.
The withdrawn reasoning follows. Everything scored before this entry assumed the slug's
hydrogen fully atomises. At several hundred bar it does not, and the chemical store therefore
**charges and discharges with both temperature and pressure** rather than being the fixed
constant `A` the exponent derivation used. Free-H fraction of hydrogen nuclei:

| T | 100 bar | 200 | 400 | 636 | 1000 |
|---|---|---|---|---|---|
| 8,000 K | 59% | 46% | 35% | 28% | 23% |
| 10,000 K | 82% | 71% | 58% | 49% | 41% |
| 12,000 K | 91% | 84% | 74% | 65% | 57% |

(`todos/dissociation_equilibrium_probe.py`; the two-parameter fit reproduces the known 50.7% at
1 bar and 4,500 K.) Re-solved with real H2 equilibrium, methane gives **1,059 s at 200 m^3,
1,080 s at 400, 1,095 s at 673**, against the 1,132 s the full-atomisation solve returned. The
launch ledger falls from 1.110 to **1.04-1.07 GN.s per load**, widening the gap to the magnetic
nozzle's 1.225 from 10% to 13-15%.
**The whole ladder re-scored at 400 m^3** (`todos/ladder_dissociation.py`), which is where
ADR-0016 now carries it:

| slug | k | slug/pulse | p | H free | eff Isp | GN.s/load | vessel |
|---|---|---|---|---|---|---|---|
| **methane** | 21.59 | 540 kg | 314 bar | 67% | **1,080 s** | **1.059** | 8.6 t |
| water | 42.51 | 1,063 kg | 336 bar | 69% | 831 s | 0.815 | 9.2 t |
| ammonia | 43.58 | 1,089 kg | 411 bar | 61% | 823 s | 0.807 | 11.2 t |
| hydrogen | 11.02 | 275 kg | 451 bar | 55% | 1,356 s | 0.753 | 12.4 t |

**Ammonia loses its edge over water entirely** (823 against 831, now within 1%), because its
nitrogen re-forms `N2` and discharges its store further than methane's carbon does. Methane's
lead over both widens from 15% to 31%, so the 2026-09-09 flip to methane is reinforced rather
than weakened. The solve omits OH, CH, `C2` and ionisation.
**Two consequences.** The temperature exponent of 0.136 was too flat because it held the store
fixed; with the store responding it is about **0.23**. Still far from 0.5, so the "temperature is
a weak lever" conclusion stands, but the number was wrong.
**And chamber volume became an Isp lever running opposite to the thermal one.** Bigger chamber ->
lower pressure -> more dissociation -> more store charged, worth +3.4% from 200 to 673 m^3, which
is comparable to what 2,000 K buys. That fights the thermal case for a small chamber, so **N9 and
N10 are now one joint question rather than two.**
_Avoid_: quoting **anything in this entry**. The 1,059 / 1,080 / 1,095 s row, the 21.59
slug ratio, the 43.58 for ammonia, the +3.4% volume lever and the 0.23 exponent are all
withdrawn.

**The store is charged, and here is why the paper-side fit missed it (2026-09-09, W1)**:
At the flown 10,000 K the chamber is 93 to 98% dissociated and the store is 95 to 99% charged.
Solved `k`: **19.56 at 200 m^3, 19.11 at 400, 18.92 at 673**, at 642 / 321 / 190 bar.
**Why the paper-side estimate came out low.** `H2 <-> 2H` at 10,000 K has `D0/kT = 5.2`, so the
Boltzmann factor barely suppresses it and the equilibrium constant `n_H^2/n_H2` is `1.22e28
m^-3`. Half dissociation needs the hydrogen nuclei density to equal that constant, which for
methane is **81.5 kg/m^3 and ~14,000 bar**, thirty times the densest chamber on the table. Le
Chatelier pushes the way the paper argued; at 600 bar it is nowhere near strong enough to do
what was booked.
**Chamber volume is worth 1.2%, not 3.4%.** 1,120 / 1,129 / 1,133 s at 200 / 400 / 673 m^3, so
the Isp argument no longer separates the geometries and N9's choice is thermal and structural.
**The Isp column is NOT proportional to `sqrt(1+k)/k`, and the companion's W1 assumed it was.**
The paper's form is `w(eta*sqrt(1+k) - 1)/k`, and the `-1` is the drift term of
`eq:reflection_baseline`, which subtracts a velocity rather than scaling one. That is why W1's
two anchors disagreed by 3% and it says so. Applying the paper's own formula to the solved `k`
gives the three numbers above, between W1's two rows. `todos/ladder_companion_k.py` reproduces
all three sets so they can be told apart.
**A charge is not a return.** 95 to 99% charged is a **ceiling** on what recombination could
hand back. What the flown 7 m^2 throat actually returns is **22.6 to 26.2%** of the store, and
the gap is unfinished gas-phase recombination rather than freezing (see **The throat is the
lever**).
_Avoid_: using the charge fraction where the return fraction belongs; they answer different
questions and differ by a factor of four.

**Chamber temperature: stay at 10,000 K (decided 2026-09-09, confirmed by the companion)**:
Going **down** is worse than going up, which is the non-obvious half, and it is the one claim
from the withdrawn dissociation entry that the companion's proper solve upholds. Solved: 8,000 K
costs **6-12%**, 12,000 K gains **3.5-4.9%**. At 10,000 K the chamber sits where cooling
discharges the chemical store faster than heating charges it, so 10,000 K is a genuine optimum
rather than merely a cheap choice. The paper-side estimate had 5.8% and 3.6%, right in shape.
_Caution_: the 8,000 K row is the softest number in the companion's solve. Its C3 partition
function is treated harmonically where the bend is quasilinear, which costs 0.1-1.2% of the
store at 10,000 K but **3.4-9.9% at 8,000 K**, and in the direction of understating the charge.

**Chamber temperature: stay at 10,000 K (decided 2026-09-09)**:
The chamber runs at Rubbia's own ceiling and does not chase higher. Reasons, in order of weight.
The gain is **+3.5 to 4.9%** for +20% of temperature (the paper-side estimate was 2.5%), which
is still **smaller than the uncertainty in every other term in the section**: `eta_geom` is
swept, the convective wall flux is a Bartz-like guess carrying 80-90% of the load, and the
recombination fraction is now solved but the wall's is not. Raising T spends
certainty to buy noise. **10,000 K also has a citation** (`augelli2013project242`) where 12,000 K
is our own extrapolation past the only anchor we have. The **heat balance closes with margin**,
91% of the wall load absorbed at a 400 K jacket against 71% at 12,000 K. The **liner runs cooler**
at 3.2 um per pulse against 3.7. And it keeps the ladder and the flown point at the **same
temperature**, so the ionised and un-ionised solves no longer have to be told apart (ionisation is
0.5% at 10,000 K).
**Flown numbers** at 200 m^3 through the 7 m^2 throat, matched convention: `k = 19.56`, 489 kg
of slug per pulse, **571-716 s** effective, **0.560-0.702 GN.s per launch load**. Through a
2 m^2 throat instead of 7 it would be 710-876 s and 0.697-0.859, which is the upside N9 has to
price (see **The throat is the lever**). On the withdrawn full-recombination convention these
read 1,129 s and 1.107; do not quote those.

**Why +20% of temperature buys only +2.7%, derived rather than asserted.** The ideal nozzle law
`v = sqrt(2*cp*Tc)` is not being departed from. Our capacity is `A + B*T` rather than `cp*T`,
where `A` is the atomisation store and only `B*T` moves:

| methane | A atomisation | B*T sensible | capacity |
|---|---|---|---|
| 10,000 K | 103.7 MJ/kg | 38.9 | **142.6** |
| 12,000 K | 103.7 | 46.7 | **150.4** |

Hand check: `sqrt(150.4/142.6) = 1.027`. Taking logs,
`d(ln v)/d(ln T) = (1/2) * BT/(A+BT) = (1/2) * (sensible fraction)`. **This is a lower bound and
the companion's solve puts the true exponent near 0.26**, because holding `A` fixed is what the
derivation assumes and the store does charge a little with temperature. The conclusion is the
same either way. The 103.7 MJ/kg row is a 298 K reference state; the 0 K value matching the
companion's partition functions is 102.35. A classic thermal rocket has
sensible fraction 1.000 and exponent **0.500**, giving `sqrt(1.2)` = +9.5%. Methane's is 0.273
and its exponent is **0.136**, giving +2.5%. The ratio 0.136/0.500 is exactly the sensible
fraction; nothing else is hiding in it.
**Recombination is a level, not a slope.** It is worth **+91%** at 10,000 K (899 s sensible-only
against 1,722 s with the chemistry back) and it flattens the temperature response by exactly the
same token. The store that makes methane good is the store `T` cannot reach.
Shape of the curve, which is the persuasive form: **+5% needs 13,760 K, +10% needs 17,700 K,
+20% needs 26,140 K.**
_Avoid_: reasoning about this engine with `v ~ sqrt(T)`. That law holds when the chamber
temperature is *set* and the mass flow is free. Here the energy is fixed at 70.3 GJ, temperature
is the constraint, and the mass adjusts.

**Rubbia's ceiling does not transfer, for the same reason his recombination finding does not.**
His limit is optical emission escaping a transparent gas. Ours gets *more* opaque as it heats,
because ionisation adds free-free absorbers faster than `T^-3.5` removes them: tau runs 45 at
10,000 K and 105 at 15,000. The radiated share of the pulse is 0.1% / 0.2% / 0.6% at
10,000 / 15,000 / 20,000 K and never binds. The liner recoats at 0.36% / 0.77% / 3.11%
redeposition across the same range.
**What binds instead is heat rejection, and it is convection.** F_conv runs 123 to 281 MW/m^2
against F_rad's 16 to 75, and the propellant mass falls as T rises, so there is less coolant for
more heat. Closure depends on how hard the jacket superheats the methane before it cokes
(~800 K classical limit): at a 400 K jacket the sink covers 91% / 71% / 49% at
10,000 / 12,000 / 15,000 K; at 800 K it covers 100% / 100% / 91%. **The flown 10,000 K point has
the most margin of the three**, which is part of why it was kept.
**15,000 K is the prize if that jacket closes**, because it reaches 1,192 GN.s per load against
the magnetic nozzle's 1.225, a tie within 3%. Named as upside, not claimed.
_Avoid_: trusting the ceiling too far. Convective flux is a Bartz-like scaling off one anchor
and is 80-90% of the load, so it is the crudest number carrying the most weight. N9 item.

**Where the pulse energy sits, and what that means for what to argue about**:
Per 70.3 GJ pulse, methane slug, at the flown 10,000 K: **atomisation 51.0 GJ (72%)**, sensible
19.0 GJ (27%), **ionisation 0.32 GJ (0.5%)**. At 12,000 K it is 47.7 / 21.5 / 1.13 GJ.
Three consequences worth carrying. **Temperature is a weak lever** because it reaches only the
sensible quarter; a C-H bond costs the same to break at 10,000 K as at 20,000 K, which is why
+2,000 K buys 3.5-4.9% (W1; the paper-side estimate was 2.5%) and not 20%, and why the chamber
stays at 10,000 K. **Ionisation is extra storage, not a loss.** It is recovered
fast (Rubbia; and `sec:jovian_dive_open` makes the same argument for argon at `n_e^2` with a
`T^-4.5` coefficient), and switching it off raises `k` from 17.60 to 17.94 and costs 0.7%.
Stranding it entirely would cost 0.8%. It is irrelevant in both directions. **Atomisation is
the only chemistry worth arguing about**, at 68% of the pulse and the only store at risk:
molecular recombination for the hydrogen, nucleation for the carbon. That is N10.
**Why the sensible share is only ~31%, and why no design moves it.** The ratio is fixed per
atom. Breaking CH4 costs 1663 kJ/mol to liberate 5 atoms, so 332.6 kJ/mol or **3.45 eV per
atom**, against `(3/2)kT` = 149.7 kJ/mol or **1.55 eV** at 12,000 K. Heat would become the
majority store only above **26,670 K**, which no wall sees. Every molecular propellant lands in
the same band (methane 31%, water 33%, ammonia 34%, hydrogen 41%), because bond energies per
atom cluster between 2.2 and 3.5 eV.
**Hydrogen wins a third argument here.** Its bond is the cheapest per atom at 2.24 eV, so 41% of
its energy sits in the safe store. It is the highest Isp, the fastest recombination *and* the
least exposed to freezing. Only tank volume argues the other way.
**The floor is not a collapse, and it is much higher than 880 s.** That figure stranded the
whole 43% carbon store and is **withdrawn**: W9 puts only 5.2% of the pulse genuinely hostage
to nucleation, since 84% of the carbon returns as gas-phase acetylene. What replaces 880 s has
not been computed. The shape of the argument survives: helium's chemically risk-free **667 s**
and methalox's 380 are the comparisons, the only fluids that cannot freeze are monatomic, and
they are far worse.
_Avoid_: spending a paragraph on ionisation; it is under a percent either way. Do not describe
it as consuming the budget, which inverts its sign.

**Density is what saves every fluid on the ladder (solved 2026-09-09, W5)**:
The single mechanism the section rests on. Three-body recombination goes as `n^2`, and a wall
holds density up where a field lets the plume thin. **This is now run station by station down
the expansion rather than hand-estimated, and the verdict is equilibrium everywhere in the
bore.** The Damkoehler number never enters the freezing band. Margin at the flown point
(200 m^3, 7 m^2 throat) is **2.16 decades** against a rate uncertainty of 0.5, so it survives
its own rate error four times over. `sec:watering_it_down`'s water plume freezes at
0.02 kg/m^3 only because a magnetic nozzle free-expands it.
**The paper's two hand estimates were both wrong and both erred safe.** x3400 for H+H+M is
3.5 decades, more generous than the best case anywhere; x403 for N+N+M is the wrong reaction
for a methane chamber. Two findings push the same way. Hurle et al. measured H+H+M directly
over 2,500-7,000 K and found it **temperature-independent**, ~3x faster than the cold
evaluations extrapolate, so every margin is a floor. And **atomic hydrogen is the third body
here** (the chamber is 93-98% dissociated), which three shock tubes agree is 7-67x better at
stabilising the collision than argon.
**One corner is genuinely thin**: 673 m^3 at a 2 m^2 throat has 0.41 decades, less than the
coefficient's own uncertainty. 200 m^3 at the same throat holds 1.33. Narrow the throat on the
small chamber, not the large one.
**Nitrogen's "~8x slower" is not robust and must carry its spread** (W7). Byron 1966 (shock
tube) makes nitrogen **faster** than hydrogen at 6,000 K, ratio 0.6; Notey, Jo & Panesi 2025
(ab initio master equation) makes it 12.7. **The two disagree by 1.3 decades.** The 8x sits
inside the band only near the ab initio end, and ammonia's whole rung depends on it.
**Carbon is still a different mechanism, but it is much smaller than booked.** See **Acetylene
is where the carbon store actually goes**.
_Avoid_: arguing this fluid-by-fluid; it is one mechanism with three instances plus carbon,
which is a different mechanism and must not be folded in with them. Do not quote the arcjet
8x without Byron.

**Acetylene is where the carbon store actually goes (2026-09-09, W9)**:
The 43.3% of methane's atomisation locked in carbon was booked as hostage to soot nucleation.
**Most of it comes back in the gas phase and needs no nucleation at all.** The stoichiometry
is exact and needs no rate constant: **`2 CH4 -> C2H2 + 3 H2` returns 89.0% of full
atomisation**, against 52.6% for the H2 channel alone and 95.9% for H2 plus fully condensed
carbon. Acetylene is nearly as strongly bound per atom as methane was.
So the carbon store splits: **36.3 points of atomisation (84%) return as gas-phase acetylene**
and **7.0 points (16%) need actual condensation**. That is **5.2% of the energy budget** truly
hostage to soot, not the 32.4% that treating the whole carbon store as condensation-limited
implies. The two-phase lag exposure shrinks with it, since acetylene is gas and stays
momentum-coupled.
**And the flown nozzle collects almost none of it.** At the exit plane the expansion parks
**66-82% of the carbon in C3**, which has banked ~62% per carbon of what condensation would
give and is a long way from done. From the exit state to acetylene equilibrium is **59 points
of atomisation**; from acetylene to condensed carbon is **7**. The missing energy is unfinished
gas-phase recombination, not failed nucleation, and it is unfinished because the nozzle stopped
1,000-1,500 K too hot. Same conclusion as **The throat is the lever**, reached from the carbon
side.
**What is still open is kinetics, not thermodynamics.** The Damkoehler work prices H+H+M only,
so nothing shows the `C -> C3 -> C2H2` path keeps up during the expansion. It is ordinary
combustion kinetics (`C2H + H2`, `C2H2 + H`), not nucleation theory, and it is worth 59 points
against soot's 7. Two hazards: C3 is the companion's least trustworthy species (harmonic
treatment of a quasilinear bend) and it is now carrying most of the carbon; and the evaluated
literature has **one** measurement of `C + C + M` and **nothing** for `C + H + M`, so the
remaining 7 points cannot be settled by a rate coefficient the way the H2 channel was.
_Avoid_: quoting the 880 s carbon-frozen floor, which assumed the whole 43% was hostage.

**The throat is the lever (2026-09-09, W6)**:
The paper posed throat area as a chemistry knob, holding density up so recombination keeps up.
**Right knob, wrong reason, and it points the other way.** Chemistry is in surplus by two
decades. What limits the return is that the nozzle does not expand far enough: at `A/A* = 4.04`
the gas leaves at 5,300-5,600 K still holding 70-76% of its store, because at 5,500 K
*equilibrium itself* holds the bonds broken. The bore is fixed at 28.3 m^2, so the throat is
the only expansion-ratio knob there is.

| throat | A/A* | conversion | eff Isp | GN.s/load | turnovers | sets k? | blowdown |
|---|---|---|---|---|---|---|---|
| 7 m^2 | 4.04 | 0.406 | 571-716 s | 0.560-0.702 | 6.8 | **no** | 8.0 ms |
| 4 m^2 | 7.07 | 0.460 | **642-797 s** | **0.630-0.782** | 11.9 | yes | 14.0 ms |
| 2 m^2 | 14.14 | 0.523 | **710-876 s** | **0.697-0.859** | 23.8 | yes | 28.0 ms |

**Narrowing to 2 m^2 is worth 24-26% and does not close the gap**, reaching at best 70% of the
magnetic nozzle's 1.225 with the wall granted an `eta_geom` it has not earned. An earlier
reading of this table, on the full-recombination ladder, had 2 m^2 passing the magnet outright.
It does not. **Three independent arguments still converge on narrowing it**: the Isp gain, the
sealed-vessel turnover count that fails at 7 m^2 and passes at 4, and the freeze margin that
stays comfortable at 4 everywhere.
**The cost is blowdown and it is unpriced.** Choked flow goes as throat area, so the pulse
stretches 8 -> 28 ms while the throat passes the same power through a third of the area. Both
are N9 items 1-7 and neither has been run, so every number above is an **upper bound**. The
2 m^2 row also exits at 4,349-4,561 K, into the range where the companion's EOS omits condensed
carbon and stops being physical.
_Avoid_: quoting the 2 m^2 row as a result. It is what the chemistry allows, not what the wall
permits, and N9 has not priced the 28 ms pulse it needs.

**The two nozzles were never on the same convention (2026-09-09, and it is the largest
correction in the batch)**:
`sec:jet_efficiency` factors the paper's jet efficiency as `eta_jet = eta_chem * eta_geom`, and
the magnetic nozzle's **1,249 s uses 0.775 = 0.910 x 0.852**, where 0.910 is `eq:eta_chem`
charging water its bond energy at 75 km/s. **The walled ladder was scored at 0.852 alone**, with
this file's own assumptions line saying "full recombination" out loud. That is `eta_chem = 1`.
So the paper charged the magnet for its chemistry, charged the wall for none, and printed the
two side by side.
**The companion has now measured what the wall returns.** Through the flown 7 m^2 throat the
methane nozzle converts 0.406 of the chamber's internal energy into directed KE, returning 26.2%
of its store, so `eta_chem = sqrt(0.406) = 0.637`. On the paper's own impulse model,
`Isp_eff = [(1+k)*eta_geom*u_e - w]/(k*g0)` with `u_e` the companion's exit speed, **methane is
571 s rather than 1,120 s** at the magnet's own `eta_geom`.
**The loss is amplified because this is the head-on leg.** The drift term subtracts a fixed `w/k`
of arriving momentum, 3,834 m/s per kg of methane slug, so a 36% cut in efficiency becomes a 49%
cut in impulse. `sec:jet_efficiency` already documents that amplification: a 12.4% efficiency
drop costs 21.3% head-on and only 8.7% on the overtake.
**A second borrowed number pushes back and is now ask N13.** `eta_geom = 0.852` came from the
flown *water* case, meaning from a magnetic nozzle, where it collects divergence, speed spread,
radiative escape and **mass the field fails to grip**. A wall has no field to fail and its
divergence loss is a bell nozzle's, near 0.98. The two errors partly cancel: over-credit 1/0.637
on chemistry, under-credit 0.852/0.98 on geometry, net ~1.37 too high. Even granting 0.98
outright, methane reaches only 716 s.
**What it does to the headline.** The section claimed 1,129 s against 1,249 s, a 10% gap, "the
price of a device that exists." **Matched, the gap is 43-54%** and the ledger is 0.560-0.702
against 1.225. The wall is about half the magnet, not nine tenths.
_Avoid_: quoting any walled Isp without saying which `eta_chem` and which `eta_geom` it carries.
Never set a companion "total" or "effective" Isp beside a paper figure; neither carries
`eta_geom` or the drift term.

**Conversion is a chemistry result, not a nozzle constant (2026-09-09, W8; N12 answered)**:
The ladder used to charge every fluid the same conversion fraction. **The companion solved three
through identical geometry and they do not agree**: hydrogen 0.532, water 0.415, methane 0.406.
Hydrogen's store banks straight into H2; methane's parks in C3.
**N12 asked whether this overturns the fluid choice. It does not, it widens the margin.**
Hydrogen's Isp lead grows to 45-54%, but its launch ledger falls to 0.460-0.611 against
methane's 0.560-0.702, so methane wins by 15-22% where the full-recombination ladder had 32%.
The reason is the drift term: `w/k` is 9,653 m/s against hydrogen's small slug and 3,834 against
methane's large one, so lowering everyone's exhaust makes that fixed penalty bite hydrogen 2.5x
harder. **Hydrogen's advantage is real and its ledger is worse**, which is the same verdict the
section already reached on tank volume.
**The `1/sqrt(m_bar)` scaling cannot settle the ordering**, because that law assumes a common
conversion fraction and this is exactly where it fails.
_Avoid_: reading a fluid's Isp lead as a ledger lead on this architecture; the drift term
reverses them.

**Thermal nozzle citation ladder (and what each source does not do)**:
`\cite{bray1959recombination}` is the mechanism: a dissociated flow tracks equilibrium until
the expansion outruns the three-body rate, then freezes suddenly. That criterion **is** the
confinement argument. `\cite{gordon1994cea}` and `\cite{gorrell2024dissociated_h2}` give the
direction at flight scale only; flown H2/O2 chambers run near 3,500 K and Gorrell's KIWI-4BE
enters at 0.7% atomic hydrogen, so neither bounds a fully atomised 10,000 K chamber.
`\cite{augelli2013project242}` is the only anchor at our temperature and it **supports** the
claim once its arithmetic is read rather than its prose (see below).
_Avoid_: citing flown H2/O2 engines as evidence that recombination completes from full
atomisation; they are barely dissociated to begin with.

**Project 242 read in full (2026-09-08): its own number needs recombination**:
The PDF has been read. The prose is conservative and the arithmetic is not, and the arithmetic
is what the section should cite.
Their text says "plasma recombination is really fast, but **molecular recombination is not**"
and claims performance was computed without it at "of the order of a factor 1.2" against
equilibrium. Their carried baseline is 2700 s at 3200 N, and 0.5*F*ve = 42.4 MW against the
43 MW they state, so 2700 s is the number they flew the mission on.
**2700 s needs 351 MJ/kg of stagnation enthalpy.** Sensible-only hydrogen at 10,000 K supplies
206 (2071 s); with full dissociation returned it supplies 421 (2957 s). So their figure implies
**67% of the dissociation energy returns**, sits at 91% of equilibrium (a reduction of 1.10,
inside their own stated 1.2), and frozen-molecular would need a **17,000 K** chamber against
their own 9,500 K radiative ceiling. There is no reading in which 2700 s is a frozen number.
**SETTLED by the companion, 2026-09-09 (W2), and it is the strongest result in that return**,
because it is a published case reproduced and a stated contradiction resolved the way the design
needs. Equilibrium hydrogen at 10,000 K, both columns being ceilings on a perfect nozzle:

| p | Isp equilibrium | **Isp frozen** | store return 2700 s needs |
|---|---|---|---|
| 1 bar | 3,070 s | **2,229 s** | 0.52 |
| 10 bar | 2,992 s | **2,122 s** | 0.63 |
| 100 bar | 2,959 s | **2,085 s** | 0.67 |

**2,700 s is 24-29% above the frozen ceiling at every pressure in "a few bar."** No nozzle,
however good, reaches it without recombination, and it sits comfortably inside the ~3,000 s
equilibrium ceiling, so it is not absurd either. It needs 52-63% of the store back, bracketing
the paper's 67% estimate. The paper's supporting figures are right in shape and 5-10% low: 206
against a solved 217-239, 421 against 421-453. The 351 is exact.
**Why this matters more than a validation.** The section rests its case on running 139x Rubbia's
number density. That argument needs Rubbia's own case to *have* recombination in it, or the
density scaling starts from zero. It does.

**Why Rubbia cannot run dense, and we can**: fission fragments must stop in about
0.5 mg/cm^2 of gas. Range against density: 12.5 mm in his cold wall gas at 0.40 kg/m^3,
820 mm on his hot axis at 0.006, **4.7 mm in our 673 m^3 chamber and 1.4 mm in the 200 m^3
one**. At our density a fragment deposits inside the wall's own boundary layer, which is the
failure his geometry exists to avoid. **His density is set by his heat source, not by his
nozzle.** A 25 kg impactor at 75 km/s has no range to match and denser only helps it couple.
Ours runs 139x his number density, so about 19,000x on the three-body rate before the longer
residence is counted. That is the whole confinement argument, with his engine as the anchor
rather than as a counterexample.
Other numbers now pinned. 230 MW thermal of which **43 MW propulsive and 190 MW rejected
through a 3 t radiator, so 18.7%, not the 22% remembered**; fission-fragment extraction from
the foil 34% at 1 mg/cm^2 falling to 24% at 3. The **9,500 K radiative ceiling is Rubbia's
own** ("the required power to increase the temperature is diverging"), which is why 10,000 K
is the right operating point and now has a citation. He splits the radiation the way a single
optical depth cannot: **line radiation is absorbed in the gas and acts as added conductivity,
continuum radiation escapes to the walls**, so the wall load is the free-electron continuum
only. And **his wall protection is transpiration**, gas flowing radially inward through a
porous carbon--carbon wall with peak temperature on the tube axis, a far better precedent for
the film than the nuclear light bulb.
_Avoid_: repeating their prose about molecular recombination without their arithmetic; taken
alone it reads as a refutation of this section when it is the opposite.

**Chamber geometry (short and dense, methane numbers)**:
Keep the paper's 3 m bore from `eq:bore_from_length` and shorten the column. Methane carries
489 kg per pulse at 200 m^3 and 478 at 400, against ammonia's 714, so 514 kg total and about
8.7 t of carbon overwrap. **And the length is no longer a lever** (W3): the equilibration count
is `A_bore/(f A*)` and the column length cancels exactly, so the short column is admissible on
the same terms as the long one and the choice is thermal and structural. The table's pressures
are confirmed by the companion, 642 bar at 200 m^3 against 636 and 190 at 673 against 189.

| V | L | p | tau | MJ/m^2/pulse | C um/pulse | front contact | swept then | heat sink |
|---|---|---|---|---|---|---|---|---|
| **200 m^3** | **7.1 m** | **636 bar** | **45.0** | **0.42** | **3.2 um** | 6.5 m | **151 kg** | **73%** |
| 400 m^3 | 14.0 m | 318 bar | 16.0 | 1.13 | 8.6 um | 6.5 m | 77 kg | 52% |
| 673 m^3 | 23.8 m | 189 bar | 7.3 | 2.29 | 17.5 um | 6.5 m | 45 kg | 28% |

Pre-charge at 200 m^3 is **1.4 bar** of methane vapour at 111 K, and the same mass sits at
**0.70 bar in 400 m^3 and 0.41 in 673**, so at all three there is no bag, no membrane and no
atomiser. Quote the pre-charge with its volume; ADR-0016 quoted 1.4 bar without one. Smaller is
better on every thermal axis and the ordering is the same as it was for ammonia.
**One thing got worse in the flip.** Methane's regenerative sink is tighter, because its latent
heat is 511 kJ/kg against ammonia's 1371 and it carries 31% less mass per pulse. Where ammonia
absorbed 100% of the wall load at 200 m^3, methane absorbs 73%, leaving about 38 GJ over a
100 s burn, or ~380 MW of radiator. Superheating the methane past ~400 K before injection
closes it, and the classic limit on that is **coking in the cooling channels** -- which in this
engine is wanted rather than feared, since the same carbon is the liner. Unresolved.
**The short column is admissible only if a sealed vessel escapes the `sec:needle_through_fog`
coupling problem** (N9 item 0). Until that returns, 400 m^3 over 14 m is the conservative
middle.

**Sprayed graphite film, and why methane may retire it**:
A few microns of carbon-loaded spray laid on the wall between pulses, the trick
`sec:lightweight_pusher_plates` uses on the plate and GA-5009 used on Orion (~150 um of
antiablation oil on a 0.8-1.5 s recycle, against 3.2 um on a 0.5 s recycle here). It does the
opacity job, so the wall can be a thin non-load-bearing steel or nickel skin behind the
composite overwrap rather than a thick refractory liner.
**With methane the spray may be unnecessary.** The exhaust carries 376 kg of carbon per pulse
against a liner loss of 1.26 to 13.9 kg, so 0.34% to 3.7% redeposition makes the liner
self-healing. A water or ammonia exhaust carries nothing that could rebuild it. **Open**:
whether it nets positive, and whether carbon deposits in the **throat**, where a drifting area
is the one dimension a nozzle cannot tolerate. The throat is the hottest and fastest station so
it should self-clean. Both are N9 items now.
**The film is a front shield and a convective coolant, not a radiation shield.** Equilibrium
radiation is handled by the chamber's own optical depth. A thin film adds an optical depth near
0.03; being optically thick would take the whole slug. Where it earns its keep is the shocked
front, which at the 6.5 m contact station has swept 151 kg at 200 m^3 against 45 kg at 673.
_Avoid_: claiming the film shields equilibrium radiation; a reviewer will check the optical
depth.

**Thermal nozzle section scope (decided)**:
Self-contained subsection under `sec:jupiter_only_growth`, carrying its own ladder table, plus
one sentence in `sec:minimum_nozzle` pointing at a non-magnetic option on the head-on leg.
**Nothing existing is re-scored.** Deliberately declined: re-scoring the minimum-rocket
conclusion (the 8.7 t methane vessel against the magnet's 17.3-37.6 t of structure plus
conductor would move the 8-38%-of-a-100-t-craft headline) and re-scoring the growth chain at
571-716 s. Both are companion-repo asks and both stay open, and the second is now the one that
matters: forward thrust needs only `eta_jet > 1/sqrt(1+k)` = 0.219, which the wall clears at
0.543-0.624, but whether it returns the required fifteenth of liftoff is unrun and no longer
obvious.

**Hydrogen thermal nozzle**:
A walled de Laval chamber that catches the head-on PuffSat, lets it merge with a charge of
cold hydrogen gas, and expands the ~10,000 K product through a physical throat. The
non-magnetic alternative for the Earth-to-Jupiter departure burn (`sec:split_push`, the
head-on leg), and the only leg it is proposed for. Precedent is Rubbia's fission-fragment
engine, Project 242, which heats hydrogen to the same temperature continuously.
Hydrogen is not a preference but the only admissible working fluid: at the chain's slug
ratio `k = 8.52` and 75 km/s closing, hydrogen sits at 8,360 K where helium sits at 93,400 K
and nitrogen at 238,000 K. Holding 10,000 K takes `k = 7.99` of hydrogen against 86.7 of
helium or 63.4 of nitrogen, so every other gas blows the launched-slug budget. Two reasons:
992 mol of particles per kilogram after dissociation (4x helium, 14x nitrogen), and
214 MJ/kg parked in broken H-H bonds, which is storage that costs no temperature.
_Avoid_: "thermal rocket" alone (it is not reactor-heated); calling it a fallback for the
overtake push, which is a different leg with a pusher-plate option already priced.

**Confinement recovery (why a wall beats a field on chemistry)**:
The argument that earns the thermal nozzle its place rather than merely substituting for a
magnet. `sec:watering_it_down` finds the water plume freezes chemically because a magnetic
nozzle lets it free-expand: by the time it is cool enough to re-form it has thinned to
0.02 kg/m^3 and run out of time, stranding 19-47% of the dissipated budget. Three-body
recombination goes as `n^2`, and a physical throat does not let the gas thin. The walled
expansion crosses 3,500 K near 0.12 kg/m^3, six times denser and thirty-six times faster.
_Avoid_: presenting this as a TRL argument; the TRL point is secondary and weaker.

**Head-on effective Isp (hydrogen, the fork that decides the section)**:
Effective exhaust velocity charged against the ship's own hydrogen at `k = 7.99` and
75 km/s. **1,490-1,630 s if the exhaust recombines, 510-600 s if it freezes**, against
1,250 s for the water slug the paper already flies. 64% of the pulse energy sits in broken
H-H bonds, so the whole case rests on **Confinement recovery**. Owed to the companion impact
simulation: solve H+H+M along the de Laval expansion and report the frozen fraction.
_Avoid_: quoting 1,500-1,700 s without naming the recombination condition.

**Detachment (and magnetic drag)**:
The release half of plasma-field coupling, and the mirror image of `Rm`. **Magnetic drag** is
the failure mode: plume that does not let go of the diverging field lines follows them
outward, loses axial momentum and lands off-axis. Hoyt et al. (MACH2) find it is *the* primary
driver of steady-state nozzle efficiency; Cassibry & Wu give the release condition as the flow
crossing from **sub-Alfvenic to super-Alfvenic**, i.e. faster than `v_A = B/sqrt(mu0*rho)`.
Resolved 2026-09-03: **we clear it, and structurally rather than by luck.** Substituting the
standoff condition `B^2/2mu0 = p` gives `v_A = sqrt(2p/rho) = sqrt(2 R_g T / Mbar)` --
**density cancels exactly**, so the bag radius (tuned at length in `sec:watering_it_down`)
does not move this number at all. `M_A` = **1.63** at the coldest pulse, **2.06** at the
hottest, two independent routes agreeing to 3%. And since `c_s = sqrt(gamma R_g T/Mbar)`,
`v_A/c_s = sqrt(2/gamma) = 1.095` wherever the field stands off the pressure: **in a beta ~ 1
nozzle the Alfven surface sits ~10% past the sonic throat**, so a standoff-sized magnetic
nozzle releases its plume exactly where a de Laval nozzle wants release. Past the last coil
the margin only grows (`p ~ R^-5` against a vacuum field's `R^-6`). Probe:
`todos/alfven_detachment_probe.py`.
**Residence, not resistivity** (added 2026-09-03): the reason Schilling's plume dies is NOT
that his coupling is lossier. His hot metal plasma at 1e5 S/m runs `Rm` ~ 300 early to 3e4
late, against our 39-650 -- **his field grips more cleanly than ours, per interaction.** He
loses because his plasma cannot *leave*: (a) his field has **gaps** (Ampere on a loop inside a
32-strut cage encloses zero net current, so field lives at the struts) and he flew no liner or
plate behind them; (b) his **strongest field is at the closed apex**, a magnetic bottle, so
plasma driven up that gradient exits only back through the gaps. We share neither: a solenoid
winding is continuous (walled by field, not fenced), `sec:watering_it_down` puts a pyrolytic
graphite liner + aluminium shell behind it at a booked 4.9 kg/pulse, and the 20 T -> 5 T graded
profile has **no local minimum**, so every gram has a downhill path out and the plume is *born*
at the strong end rather than driven into it. A nearly lossless coupling still empties a plume
that never leaves.
_Avoid_: calling this a bound on `η_geom` (clearing a necessary condition is not computing a
value; three contributions remain, being divergence, speed spread and radiative escape);
treating the 2450 K `Rm = 1` cliff as "the field fails" (once super-Alfvenic, letting go is
the *intended* end state, and the floor that actually binds is the 3800 K leak limit); saying
our coupling is more conservative than his (it is not -- see residence above).

**Reflection baseline (`eq:reflection_baseline`)**:
What `η_jet` would be if the nozzle only *reflected*: reverses every particle whose LAB-frame
axial velocity points at the ship, loses every transverse component. The mirror acts on the
lab velocity, so **drift and thermal terms do not add** (getting this wrong was the
2026-09-03 error, corrected same day; the bad form gave 1.06 at `f_d = 0.5`). With
`f_d` the share of pulse energy in bulk drift,

    eta_refl = 1/(2*sqrt(1-f_d))   for f_d <= 1/2
             = sqrt(f_d)           for f_d >= 1/2

giving **0.500** drift-free (0.46 Maxwellian) and rising only slowly from there.

**The drift is small where we operate, and dilution spends it.** Only the projectile brings
kinetic energy, the slug brings mass, so `f_d = 1/(1+k)`:

| k | 1 | 3 | **8.5** | 24 | 30 |
|---|---|---|---|---|---|
| `f_d` | 0.500 | 0.250 | **0.105** | 0.040 | 0.032 |
| baseline | 0.707 | 0.577 | **0.529** | 0.510 | 0.508 |

So the collision geometry is worth **~3% at the k we fly**, not the factor of two first
claimed. Same magnitude for **overtake as for head-on** (`|−V+u*mu|` has the same
distribution), but the *burden* differs: head-on, a nozzle doing nothing still yields
`+sqrt(f_d)`; overtake, doing nothing yields `−sqrt(f_d)`, so the field must reverse the
drift too.

**NOT a ceiling, and this is what actually carries the argument.** A diverging field *turns*
flow as well as reflecting it, converting transverse momentum to axial. Every working nozzle
sits above its own baseline: published solenoids reach 0.65-0.85 collimation on drift-free
plumes, i.e. **130-170%** of their 0.50. Our 0.775 is **147%** of our 0.529 at k=8.5.
**We ask a solenoid for what solenoids deliver.** Schilling's strut cage returns 68% of his,
the only device in the comparison below a plain mirror, which indicts his topology rather
than pulsed nozzles. Probe: `todos/reflection_baseline.py`.
_Avoid_: calling it a ceiling or upper bound (a turning nozzle exceeds it, and ours must);
saying "the drift is the difference" (it is ~3% at flown k; the turning is the difference);
adding `sqrt(f_d) + (1/2)sqrt(1-f_d)` (wrong, exceeds 1); confusing it with **field's share**,
which is the mass-side argument and legitimately uses `f_d = 0.25` at the near-Sun 3:1 mix.

**`kappa` (rupture criterion)**:
`kappa = 12 pi E_p R0^3 / (mu0 |mu_d|^2) = E_p/E_M`, the cloud's **kinetic** energy over the
**dipole** field energy integrated **beyond** radius `R0` (the coil-to-target distance), with a
threshold separating *quasi-capture* (clean deflection) from *rupture* (plasma bursts the field
and leaks). From **Nikitin & Ponomarenko 1993**; the value **0.4**, for a cloud born **on the
field axis**, traces to **Vchivkov 2003**; Hyde's flown design at **0.2**; the one bench
measurement is **0.077** (Kawashima 2016, who call 0.4 an overestimate for their own one-sided
plume). **Our standoff sizing pins the bore-only ratio at `1/(gamma-1) = 1.5` identically**, a
tautology of the rule rather than a property of the magnet, since `E_field = pV` and
`U = 1.5 pV`. Counting bore-downstream plus exterior field brings it to **0.99-1.22**; counting
only field outside the plume's own volume gives **2.9-6.5**. Posture (ADR `0009`): **declined**,
because `kappa`'s denominator presumes a cloud small against the field structure, which our
bore-diameter plume is not, and because rupture is a bubble-bursting failure of an isotropic
ball born at a point. Exposure if wrong is quoted in the paper: hot-pulse structure 10-30 t
becomes **37-112 t**, which would undo `sec:mass_interest`'s single-Starship claim. Decided by
the `sec:solid_PuffSats` impact sim.
Probes: `todos/epsilon_b_probe.py`, `todos/field_energy_integral.py`.
_Avoid_: calling it `eps_b` (that is Zakharov's separate ion-Larmor-radius parameter, ~1e-4 for
us, and the mix-up was in the paper until 2026-09-03); crediting the criterion to Zakharov;
saying "inside a solenoid" for the 0.4 (it is a cloud on the field axis); quoting 0.99-1.22
without noting it is the flattering reading of an ambiguous denominator; calling the criterion
refuted (it is declined as non-transferring, conditionally).

**`E_B/E_p` (field-poor exposure)**:
The inverse of `kappa`, and the same argument arriving from performance rather than rupture.
Five sources put the nozzle optimum at field energy several times plasma energy: Nagamine 1999
and VISTA at **5**, Hyde's flown design at 5, Inatomi 2023 simulating at 5 to peak efficiency,
Saito 2018 **measuring** extraction saturation above **4.3**, Itadani 2018 **measuring**
`beta ~ 10`. **Our standoff sizing puts it near 1**, so the magnet is field-poor by ~4x, and
Inatomi's momentum efficiency at the optimum is **0.6-0.7** under our own `eq:eta_jet_def`
against the **0.775** `sec:methalox_rebuttal` requires. Posture (ADR `0010`): **conceded**, and
answered on **ionization**, not geometry. Every number was taken on a thin fully ionized plasma;
ours is 0.32 kg/m^3, 1.3 eV, **5% ionized**, and a neutral feels no field at any ratio.
_Avoid_: answering this the way `0009` answers `kappa` (Inatomi is a scaled solenoid, so the
geometry argument does not transfer); calling the ratio speculative because the field's impulse
magnitudes diverge 3-7x (a dimensionless optimum survives calibration error, and two of the four
sources are measurements); saying no published solenoid states `eta_jet` (Inatomi 2023 does).

**Driver power (what a pulsed nuclear engine pays and we do not)**:
Every pulsed nuclear concept must charge something to light the *next* pulse, at MJ scale on a
~1 s turnaround. Photovoltaics and heat cycles are too heavy at that duty, so VISTA, HOPE and
PuFF all take the energy back out of the exhaust with a **flux compression generator** (FCG):
the plasma shoves the field ahead of itself and the changing field drives current into
capacitors. That forces the magnet into two parts, superconducting **seed coils** holding the
field plus conducting **thrust coils** taking the induced current. Cost: Schilling's point
design is **35 t for 1.2 MJ**. **We build the identical two-part magnet
(`sec:watering_it_down`, citing Romanelli) for the opposite purpose**: the copper shell exists
to keep induced current *out* of the REBCO, and the 13.4 MW is dumped into argon, never
banked. Our pulse is not driven, since the energy arrives in the projectile paid for by the
orbit, so the only onboard power need is cryostats. That is **kW drawn steadily for years**,
exactly the shape solar plus a battery fits and an FCG does not. Stated in
`sec:epstein_drives` beside the neutron-shield argument, which has the same form.
_Avoid_: claiming the FCG harvest is what costs those designs their nozzle efficiency (VISTA
takes ~1% of available power, and Schilling's 0.34 is computed with no extraction at all);
proposing we harvest our own eddy current (13.4 MW is thousands of times the cryostat load).

**Field's share (of a pulse)**:
The fraction of each pulse's collision energy the magnetic nozzle's field must actually
catch and redirect, as opposed to energy that exits the open back unaided. Both the
virial floor and the standoff radius scale linearly with it. Working number **~1/2**
(band ~0.3–1), decided 2026-07-14: the 3:1 diluted fireball drifts at only Mach ~0.8
(155 km/s drift against ~200 km/s internal sound speed; ~75% of pulse energy
thermalizes), and the head-on stagnation region squirts radially into the field, so the
plasma is a slow explosion, not a collimated jet. Mini-Mag Orion's isotropic fission
burst has share ≈ 1. The only route below ~1/2 is the hybrid nozzle, where a sacrificial
low-Z absorber takes the bulk blast and the field stands the hot core off it. Posture
(revised 2026-07-14, same day): the paper's quoted numbers are the **pure magnetic case
at share ½**; the hybrid is mentioned as a conditional refinement (roughly 2× nozzle
mass saving at share ~0.15) whose viability hangs on an unverified wall-heating
fraction (f_wall ≲ 3e-4, an impact-sim deliverable), so it is not load-bearing for any
quoted mass.
_Avoid_: "the field only trims divergence" (pre-2026-07-14 wording; overstates
collimation); claiming a small share without invoking the absorber.

**Virial floor (magnet mass)**:
The minimum structural mass of any magnet holding field energy `E_B`:
`M ≳ (ρ/σ_eff)·E_B`, from reacting the Maxwell stress, independent of conductor
technology; chained through the standoff condition,
`M ≳ (ρ/σ_eff) × (field's share) × E_pulse`. `σ_eff` is **strain-throttled**, not the
material's tensile strength: structure at the winding radius stretches with the REBCO
tape (limit ~0.4% elongation), so it can only develop (modulus × 0.004). Adopted band
(2026-07-14) **0.4–1.2 MJ/kg**: standard carbon fiber plain build at 0.4; high-modulus
(M55J-class) fiber plus assembly pre-compression (~ −0.25% squash, widening the usable
window to ~0.65%) at 1.2. A Kevlar/aramid overwrap is an *implementation of
pre-compression* (its high elongation lets it be wound at high pre-tension), not an
escape from the strain limit; as plain stiffening its low modulus makes it worse than
carbon, and creep limits sustained pre-tension. Mini-Mag's 200 t at 340 GJ sits at or
below the strain-matched floor, so treat it as their claim, not a validated benchmark.
Verified against the sources 2026-07-14: AIAA 2003-4525 specifies the nozzle in one
sentence (5 coils over 11 m, 10 MA each, ~200 t total) with no conductor type, field
strength, structural material, or mass breakdown; Lenard & Andrews 2007 adds nothing on
the coil. The 200 t is an unengineered point-design allocation, and no shield fraction
can be extracted from it.
_Avoid_: sizing winding structure by tensile *strength* (strain compatibility throttles
it); framing the constraint as cryogenic material survival (cold mildly helps; the
stretch-together geometry is the constraint).

**REBCO tape term (conductor mass)**:
Second term of the two-term nozzle mass model. Ampere-turns ≈ `2RB/μ₀` regardless of
conductor quality, so tape mass ∝ `R²B/I_tape` ∝ `(share·E_pulse)^(2/3)·B^(−1/3)`.
It falls more slowly than structure as pulses shrink, so **tape dominates small
nozzles**. At the adopted 20 T / 20 K anchor (SPARC-class working point, 300–600 A per
4 mm tape) with the scenario's own pulse energy (477 GJ for 2.5 kg at 618 km/s closing,
share ½): 100 g pulse ≈ 18–36 t tape vs ≈ 8–24 t structure (total ~26–60 t, replacing
the paper's "single-digit tonnes"); 2.5 kg pulse ≈ 150–310 t tape vs ≈ 200–600 t
structure (total ~350–900 t). Those tape figures assume standard 3.5 g/m tape; the
adopted policy is thin-substrate/thin-copper tape (30 µm Hastelloy + 5 µm Cu/side,
~1.5 g/m, a commercial product) wherever tape is dominant or comparable, cutting totals
to ~16–40 t (100 g) and ~265–730 t (2.5 kg). The copper floor is quench protection, not
resistance. Full derivation in `todos/nozzle_rewrite_plan_2026-07-14.md`, destined for
a new paper appendix with the math inline (closed-form, hand-checkable; the main text
quotes only the thin-tape band totals and points there). A calc-repo module is optional
follow-up for a sweep figure, not a gate (revised 2026-07-14 from "repo first").
This term is the concrete identity of the former
"minimum-coil-size floors". Model lives in the calc repo with the `rebco_tapes`
(Senatore 2024) current-scaling relations.
_Avoid_: "conductor mass is negligible with REBCO"; the pre-2026-07-14 "single-digit
tonnes" claim.

**Minimum-rocket conclusion (two anchors + ship classes)**:
How sec:minimum_nozzle states its bottom line (decided 2026-07-14): quote both nozzle
totals at the adopted thin-tape architecture (2.5 kg pulse ~265–730 t; 100 g pulse
~16–40 t), quote bands rather than single best-case points, and translate each into its
ship class: a multi-thousand-tonne vehicle for the big pulse (the former "better still
more than a thousand" is now a requirement, not a preference), and roughly
Starship-class at the light end (~65–400 t, nozzle a tenth to a quarter of the ship)
for the small pulse. The main text carries only these headlines plus a pointer to a new
appendix holding the full model and worked arithmetic. Propagation (decided 2026-07-14): the only downstream edit is
the methalox section's "vehicle carrying hundreds of tonnes or more" (line ~647), which
becomes thousand-tonne-and-up; the cascade's cost arithmetic is ratios and is untouched.
The cooling-system floor stays named but qualitative (pulsed heat into a 20 K magnet,
each absorbed watt costing tens of watts of plant); no invented absorbed-fraction
number, since that input waits on the impact simulation. The fission-vs-plasma radiation
contrast stays qualitative too: neither Mini-Mag source publishes a shield mass to cite.
_Avoid_: "single-digit tonnes"; leaving the ship-class implication implicit; quoting a
cryoplant power number.

**Standoff radius**:
The radius where the expanding pulse plasma's pressure meets magnetic pressure,
`R ~ (2μ₀ · share · E_pulse / B²)^(1/3) ∝ B^(-2/3)`: a stronger field gives a physically
smaller nozzle at the same virial mass. The ceiling on `B` is itself mechanical (REBCO
windings are strain-limited near 0.4%), so material strength limits the field and field
pressure limits the radius.
_Avoid_: reading a smaller radius as a lighter nozzle (virial mass tracks contained
energy, not size).

### Heliocentric re-intercept (solar-dive return)

**Earth re-intercept**:
The requirement that a boosted solar-dive projectile arrive *where Earth actually is*,
not merely cross `1 AU` somewhere. The boosted orbit is hyperbolic and crosses 1 AU only
once, about 0.2 yr after launch, roughly 136° of heliocentric longitude from Earth. The
projectile whips ~295° around perihelion while Earth advances only ~70°, so the miss is
set by the whip-around, not by Earth's drift. Re-aiming at periapsis is prohibitive
(~5.4 km/s per degree at the 309 km/s, 4 R☉ periapsis speed).
_Avoid_: "interception" (reserved for the near-term LEO terminal-guidance sense below);
treating "crosses Earth's orbit" as if it meant "hits Earth."

**Phasing loop**:
A pre-dive maneuver that delays the deep dive until Earth reaches the fixed crossing point,
so the return re-intercepts Earth. Every boost is a PuffSat collision, not carried
propellant, so any of these can supply the impulse. Three realizations:
(1) *Two-impulse loop* (periapsis-lowering shallow dip, then deep dive): the two retrograde
boosts are colinear, so it is free in total impulse (~24 km/s, same as a direct dive) and
holds the doubling factor at two. It needs a second PuffSat boost node at 1 AU, off Earth,
where the loop returns; a mature network fields it, an early one may not. First resonance
~0.82 yr. Apoapsis-raising is the wasteful direction (opposing boosts, ~+7.6 km/s,
~1.82 yr).
(2) *Single-impulse resonant dive* (inject outbound to ~1.9 AU aphelion): needs only the
Earth boost node, but the boost grows ~24 → ~37 km/s (the direct dive's ~24 km/s retrograde
component plus a ~28 km/s outbound radial component), which spends more PuffSats and drops
the doubling factor below two. ~0.85 yr; the aphelion is the knob that closes the geometry.
(3) *Gravity-assist resonant return* (Venus/Earth flyby): impulse-free phasing, ~1--2 yr,
constrained by flyby timing.
(4) *Split dive* (fly (2)'s outbound ellipse, but pay only part of the boost at Earth and
the rest out at aphelion): cheaper on impulse and on launched slug than (2), at a longer
clock, and it needs a second node out at ~1.96 AU. See **Split dive** below.
_Avoid_: calling phasing impossible or requiring a "rocket burn" (PuffSat collisions
provide all impulses); presenting apoapsis-raising as the default; rotating the argument of
periapsis for a *fast* dive (no in-plane solution when launching from the aphelion of a
deep diver).

**Split dive** (`sec:split_dive`):
The **phasing loop**'s fourth realization. Fly the **single-impulse resonant dive**'s
outbound ellipse, but spend only part of the Earth boost there and take the rest out at
aphelion, where the vehicle is slow and reshaping the orbit is cheap. Parametrised by the
**outbound perihelion** `q`, the perihelion of the ellipse the Earth burn buys; at
`q` = 4 R☉ the far burn is zero and the family reduces exactly to the single-impulse dive.
Injecting 1 AU to 4 R☉ is a 54:1 radius ratio, far past the ~15.6:1 where bi-elliptic always
wins: 24.09 km/s direct, 16.94 through 3 AU, floor `(sqrt 2 - 1) v_earth` = 12.34.
_Avoid_: presenting the outbound leg as the novelty (the single-impulse dive is *already* a
raise-then-drop, aphelion 1.9259 AU, boost 28.80 radial + 24.07 retrograde; only the
*splitting* is new); confusing it with the **two-wave departure**, which splits an
Earth-orbit burn across days for an arrival-angle reason, not a heliocentric one across
months for an Oberth reason.

**Partial split** (`q` ~ 0.4918 AU):
The interior optimum on the Earth re-intercept closure curve: doubling 0.2969 yr against the
paper's 0.3048, and 1.536 kg of launched slug per delivered kg against 2.365, at `k` = 30,
`eta_jet^2` = 0.60 and node survival 0.60. It is the family's **rate optimum before delivery
is charged**, and that is the only way to describe it. **The dominance claim is retired, not
lifted** (companion ADR 0025 second addendum, worklist S1; `docs/adr/0008`). The ledger
charged the impactors *consumed* at both nodes and nothing for **delivering them to
1.96 AU**, which the returning beam misses by ~110 deg on this member of the family. Charged
at the **far-node delivery price**, 1.536 kg/kg becomes **3.552** against the paper's own
dive at 2.365, so it no longer beats what it was said to dominate. The pure bi-elliptic end
of the same family (`q` = 0.99 AU) is 6% *worse* on doubling than the paper's dive, so the
family punishes the intuition that a cheaper injection must be a better one twice over.
_Avoid_: "dominates", "free" or "costs nothing" at all; quoting 1.536 kg/kg without its
missing delivery; reading S1 as a cost that merely trims the margin (it reverses the
verdict); scoring the partial split as though it were phased — the *phased* closures of
`sec:far_node_colocation` are beam-fed and do not carry this cost.

**Far-node delivery price**:
What it costs to feed the **partial split**'s outer node, which cannot eat the returning
beam's leftovers. **The far node does not need mass at 1.9649 AU, it needs mass moving at
153.35 km/s there**, against a vehicle doing 13.45 — a Hohmann delivery arrives nearly
co-moving and is worth nothing as an impactor. Buying that speed from 1 AU costs **113.20
km/s of Earth departure excess** (co-linear, the cheapest arrival the geometry allows and
therefore a bound; 125.80 for the perpendicular arrival the beam actually makes), against
the payload's own 19.12, and delivers **1.0%** of what is launched (0.6% perpendicular).
The structural point: the returning beam carries 153.0 km/s past the far node for nothing,
being a climb-out from the dive, and **the cheap way to make fast mass is to drop it down
the Sun's well first**. So the phased closures' leftovers are not a convenience but the only
affordable source.
_Avoid_: pricing a delivery on *arrival* rather than on *arrival speed*; quoting the
co-linear number as the answer rather than as a bound.

**Split pad crossing**:
The depth at which the **split dive** stops earning its own launch on the committed
`0.25 * chain * survival` floor of 1/15: **5.58 R☉**, bisected, with node survival derived
rather than held. So "the cheaper injection buys the pad" is **true at 4 R☉ and false by 6**
— margin 1.179 against the direct route's 0.657 there, but 0.306 against 0.237 at 22.93 R☉.
Its edge shrinks 1.80x → 1.29x → 1.09x from 4 to 22.93 to 32 R☉, so the architecture that
buys the pad buys it only where the thermal case is worst. **At the recommended shallow end
neither architecture earns its launch**; the choice is between two failures, one 29% less bad.
_Avoid_: quoting the pad claim without its depth; confusing this with slug per delivered
kilogram (0.875 vs 2.365), a different currency and the one ADR 0023's claim was made in.

**Stated versus derived node survival**:
The paper's depth-dial ledger holds node survival at **0.60 at every depth**; derived from
the boost it is `exp(-boost/exhaust)`. At 4 R☉ the two agree (0.5895 vs 0.60), which is why
it went unnoticed, but the node's exhaust speed collapses with the arrival speed (68.09 km/s
at 4 R☉ to 22.38 at 32), so derived survival falls to **0.2589 at 22.93 R☉ and 0.1629 at 32**
and doubling rises 0.3075 → 0.6570 → 0.9484 yr. Held at 0.60 the same three depths give
0.3048 / 0.3431 / 0.3091, **non-monotone and inside 13%** — that spurious flatness is what
made backing the dive out look nearly free. In the paper as `tab:derived_node_survival`.
_Avoid_: reusing the stated 0.60 at any depth but 4 R☉, which a shallow-dive comparison
invites; reading this as a correction to the published 4 R☉ headline (there the gap is 1.009x).

**Node-depth admissibility** (`sec:node_depth_admissibility`):
The rule that **every trajectory in the architecture -- payload, opposing stream, and any
projectile stream feeding a node -- must have a perihelion no lower than the dive node's
depth**. Nothing in the system may pass inside the node. Adopted 2026-09-02; see
`docs/adr/0008`. It disqualifies the **plunger node** outright: a zero-angular-momentum drop
has perihelion `r = 0`, so it does not skim the Sun but enters it, and the share the node
fails to consume is on a Sun-impacting trajectory. An architecture that backs the payload out
to 23 R☉ for thermal reasons while aiming its ammunition at the Sun's centre has moved the
exposure, not escaped it. **The tell** is that the radial placement is priced *flat at
Earth's own 29.78 km/s at every depth* -- a depth-independent cost means the trajectory is
not aiming at a depth; contrast the payload column, 24.09 falling to 14.62 km/s, which is.
**The trap that closes it**: forcing the plunger to bottom out at the node means carrying the
tangential speed a perihelion there requires (15.16 km/s at 32 R☉), which *is* the payload's
own prograde injection, so it would arrive alongside rather than across and there would be no
collision. "Plunger" and "bottoms out at the target depth" are mutually exclusive. So
**retrograde placement is the only admissible head-on arrival**, which makes the bi-elliptic
route load-bearing rather than convenient: injected at one far node, payload and opposing
stream fly the *same ellipse* in opposite senses, arrive together at 180 deg with no tuning
knob, and neither leg ever goes closer to the Sun than the node.
_Avoid_: rejecting the plunger on its 135 deg geometry alone (true at `k` = 30, but it is
inadmissible before it is inefficient); "fixing" the plunger by giving it a perihelion at the
node; treating the rule as a caveat rather than a constraint -- the companion repository now
*enforces* it, because the plunge is the cheapest-looking of the three placements and a rule
left to judgement is a rule left to lose.

**Plunger node**:
The dive node with the opposing stream arriving on a zero-angular-momentum drop instead of
head-on. It arrives at **135 deg, not 90** -- both bodies reach perihelion within a percent of
the same speed, so their relative velocity bisects the axes -- and the closing speed falls by
exactly 1/root 2 at every depth (612.0 to 432.7 km/s at 4 R☉). But `beta` *rises*, because the
`cos psi` debit is the impactor's own momentum arriving backwards and a 135 deg arrival pays
only 0.707 of it. **Plunger Isp toll**: the debit is `k`-independent while the useful term
grows as `sqrt(k)`, so the plunge keeps 0.960 of head-on exhaust speed at `k` = 1, 0.864 at 3,
0.802 at 8.5 and **0.757 at 30**. Both readings in circulation are wrong -- it costs neither
the full root two nor nothing. What it would have bought is a clean **halving of collision
heat at every `k`**, worth about a factor of two read as depth (a plunger at 4 R☉ collides as
gently as a head-on node at 7.86 R☉). Collision term only; the node's solar flux still goes as
`1/r^2`. In the paper as `sec:arrival_angle`.
_Avoid_: treating it as a live option -- **node-depth admissibility** rules it out before any
of this trade applies, and what survives is only the record of why it would have lost anyway;
quoting the toll without its `k`; comparing its heat relief against the *solar* flux.

**Off-head-on arrivals under admissibility** (open):
A consequence the companion does not draw and the paper now states. Any trajectory bottoming
out at the node carries the local near-parabolic speed there, tangentially, so **a coplanar
admissible arrival is co-moving or head-on with nothing between**. An intermediate angle has
to be bought with an **inclined placement**, an out-of-plane orbit rather than one with its
angular momentum removed, giving closing speed `2 v_p sin(theta/2)`. `eq:ve_angle` still
prices any angle. **What a plane change costs on a placement leg appears nowhere in this
paper**, and it is now the only surviving route to an off-head-on arrival.
_Avoid_: quoting the appendix's old "a flown fleet would arrive across a spread of angles" as
though the spread were free.

**Opposing-stream placement routes**:
The two ways to put the dive node's *second* arrival where it has to be. They differ by 3-4x,
so **always name which architecture is meant**. *Earth-direct*: reverse Earth's own 29.78 km/s
from 1 AU, **35.48 km/s at 4 R☉ rising to 44.94 at 32** -- the only route open to the
**single-impulse resonant dive** and to the **split dive**, neither of which visits Jupiter.
*Via Jupiter*: a one-way tangential launch at **11.06-11.83 km/s** of Earth excess, bent
retrograde by an unpowered flyby -- open only to the **Jovian dive cycle**, and 0.95-1.09x
that cycle's own departure rather than three times it. Co-locating the arrival with the
payload in longitude *and* time costs a further 13-38 m/s; excess above the **dive-placement
floor** sweeps the perihelion-longitude gap through a full 360 deg over ~50 m/s, so a root
always exists and the solutions are **discrete**, like the **synodic closure**. The stream
leaves Earth 6.7 d before the payload at 4 R☉ and 40.5 d after it at 32. The **Jupiter-only
chain** owes nothing at all: its retrograde return is flown only from the Jovian bend to the
1 AU crossing, its perihelion is never reached, so it has no dive node and no second arrival.
_Avoid_: quoting 35.48-44.94 as "the" placement cost; assuming the Jovian route transfers to
the split dive (that architecture is Earth-only).

**Opposing-stream charge**:
What placing the second arrival costs once it is actually billed, and the answer to deferred
item S3. **No ledger in the paper charges it**, which is a real omission. Charged: growth
ledger **1.0014x doubling at 4 R☉ to 1.0075x at 32** for the Jovian cycle, 1.0063x to 1.0112x
for the paper's dive; pad ledger 0.45-2.00% of returned mass, **flipping no verdict**. It is
small because of *mass*, not impulse: at `k` = 30 the node wants only 0.17-0.49 kg of opposing
stream per impactor kilogram of payload, so even a 44.94 km/s placement through a nozzle
delivering a fifth still lands near 1%.
_Avoid_: promoting the two-leg asymmetry to `sec:split_dive`'s spine on the strength of it --
it is a result about impulse and node geometry, and the growth effect is a rounding error
(this is why `docs/adr/0007`'s planned restructure was retired); quoting the bound for the
**split dive**, whose far node has to be *fed* as well as reached (**far-node delivery price**).

**Re-intercept cycle floor (~0.82 yr)**:
The shortest Earth-to-Earth solar-dive cycle that actually re-intercepts Earth, set by the
first phasing resonance. Supersedes the paper's earlier implied ~0.5 yr ("6 month") cycle.
At one payload doubling per cycle, a millionfold scaling takes ~16 yr, not under a decade.

### Jovian dive cycle (`sec:jovian_dive_cycle`)

**Jovian dive cycle**:
The growth cycle in which Jupiter places the solar dive *every* cycle, not just the first
one (`sec:jupiter_gravity_initial` places only the first). Depart Earth for Jupiter, let an
unpowered flyby drop perihelion to the chosen depth, take the Oberth boost there, cross 1 AU
where Earth is waiting. Because the Earth-side collision only has to buy a Jupiter transfer,
its push target falls from the **single-impulse resonant dive**'s 39.11 km/s at 200 km to
15.24 km/s (4 R☉) or 16.66 (32 R☉). That substitution is the whole prize.
_Avoid_: "Jupiter-only cycle" (that is `sec:jupiter_only_growth`, which has no solar node at
all); calling it a variant of the **phasing loop** (it replaces the phasing, it does not
phase).

**Three-synodic closure (3S)**:
The clock the Jovian dive cycle runs on. The loop must take a whole number of Earth--Jupiter
synodic periods so the next cycle sees the same geometry, and **three is the only multiple
that closes**, bracketed on both sides: 1S is short 101.38° of Jovian bend, 2S short 6.84°,
and 4S needs 4.368 yr against a 3.661 yr ceiling on any zero-revolution direct transfer.
3S is 3.2761 yr, with +58.80° of bend margin at 4 R☉ and +54.48° at 32.
_Avoid_: treating 2S as merely worse (no perijove burn closes it at any magnitude or sign;
only a maneuver off the flyby does, at ~2 km/s wherever it is placed). Also avoid reading
this **2S** as the Jupiter-only chain's: see **synodic lock** below, where 2S is routine and
a 2.00 S total is a phase fixed point. Three senses of "2S" live in this document and only
this one is a bend-feasibility claim.

**Depth dial**:
Perihelion read as a continuous knob rather than a choice between two designs. Every
node quantity moves monotonically along it, and the **cycle time does not move at all**
(3.2761 yr at every depth), so depth trades collision violence against growth and nothing
else. 4 R☉ against 32 R☉: solar flux 64x, equilibrium temperature 2.83x, node closing speed
2.87x, energy thermalised per kilogram 8.2x, rendezvous timing tolerance 2.87x.
_Avoid_: presenting the shallow node as the safe default; it is the marginal one, and depth
wins on three independent axes (Oberth leverage, node exhaust speed, and departure cant).

**Two-wave departure** (**split push**):
The Earth-side departure charged from the pad and flown as two pulses about **5 days**
apart, because its halves want opposite geometries. An **overtaking push** from the
3.60 km/s ballistic lob to a 5-day parking orbit at 10.861 km/s runs at `theta` = 0 where
the impactor's momentum *adds* (`beta` = 3.39 at `k` = 8.5); the **canted departure leg**
must leave along the aim the three-synodic closure demands (`beta` = 1.67 at 124.8°). The
**apoapsis re-aim** between them costs `2 v_apo sin(cant/2)`, flown on methalox because no
stream is present at apoapsis. 5 days is a saturation point, not a tuned one: it captures
95% of what 40 days offers while Earth advances 4.93° instead of 39.43°, and below half a
day the re-aim eats the whole advantage.
_Avoid_: quoting the free-parking-orbit figures (0.513 / 1.094 yr doubling), which start the
burn at Earth escape and charge nothing for reaching it; assuming one canted push is
equivalent (it costs 1.4x the growth at 32 R☉); using "split push" in prose now that the **split dive** and the Jupiter-side
**growth wave / departure wave** split exist, since
the two split different burns for different reasons (days in Earth orbit for an arrival
angle, against months in heliocentric space for an Oberth saving). The section label
`sec:split_push` stays, so cross-references do not move.

**Dive-placement floor**:
The minimum Jupiter-arrival excess speed that can place an opposing stream at a given
perihelion, since an unpowered flyby rotates the arrival vector but never rescales it.
Prograde / radial / retrograde: 11.96 / 13.06 / 14.16 km/s at 4 R☉, spreading to
9.98 / 13.06 / 16.14 at 32. **Neither cycle's own arrival reaches its retrograde floor**
(12.17 and 10.95 km/s), so the opposing stream cannot ride the payload's cycle at either
depth. It needs its own departure energy (11.83 km/s of Earth excess, tangential) and its
own schedule.
_Avoid_: the retired claim that one departure energy serves both streams; that was a
statement about the floors, not about a closed cycle.

**Depth conduction crossing**:
The depth at which the **single-impulse resonant dive**'s Earth departure stops conducting,
because that burn aims ~31 deg off the arriving stream and so runs *away* from what feeds it,
cooling itself through the burn. **Quote it with two conditions or not at all.** Expansion
margin: 19.80 R☉ at 1.5, 27.40 at 1.25, 40.72 at 1.0. Perihelion burn, which matters more:
5.58 R☉ at 20 km/s, 19.80 at the paper's 35.98 tuning, 26.04 at 40, ~1.9 R☉ per km/s. The
**split dive**'s Earth node has no crossing in 4--48 R☉ at any of these settings, because its
burn is 3.93 km/s rather than 21.6, and its far node cannot cool itself at all (it thrusts
within a few degrees of perpendicular to a radial beam, so closing speed moves 153.50 to
153.17 across a 10.26 km/s burn).
_Avoid_: reading the crossing as "the split is required to fly shallow" -- that reading is
retired, see **conducting burn**; pairing it with the Jovian pad ledger's 22.93 R☉ to make a
window, since those two edges come from different architectures and the window is empty anyway.

**Conducting burn**:
The cheapest perihelion burn that keeps the **self-cooling departure** above the conduction
floor at a given depth. **38.10 km/s (1.059x the paper's 35.98 tuning) holds the direct
departure conducting out to the 22.93 R☉ pad floor**, and the cycle still grows there: 2.505
per pass, doubling 0.657 yr. So **the direct route can fly shallow**, and the **depth
conduction crossing** is a statement about the tuning rather than about the architecture.
The extra 6% of burn costs 7.4% of node survival and ~1% of clock, and the clock moves the
*helpful* way, since a hotter perihelion burn climbs out faster. Depth itself is the
expensive part: at 19.80 R☉ with no extra burn at all, doubling is already 1.93x the 4 R☉
value (**stated versus derived node survival**). Answers deferred item S2; lifts
`sec:self_cooling_departure`'s held paragraph, and lifts it *against* the split.
_Avoid_: the stronger reading ADR 0023 gave the crossing; claiming a depth window for the
split -- at 38.10 km/s the crossing (23.01 R☉) rises *above* the pad floor (22.93), so the
band the split was said to open is empty at that tuning.

**Expansion floor** (**conduction reserve**):
The requirement that the plume still *conduct* when the expansion is finished, not merely
ignite when the blob merges. A magnetic nozzle works by letting the plume expand, which
cools it, so a blob sitting on the ignition window's upper root lights and then falls out of
conduction the moment the field takes work out of it. Written as a ceiling,
`eta_jet^2 <= (k/(1+k))(1 - reserve/eps_th)`. The **reserve is a bracket, and the companion
repo's 15,000 K default is not this paper's requirement**: `sec:watering_it_down` puts the
`Rm = 1` cliff at 2450 K and the binding leak limit at 3800 K, and the 15,000 K figure is the
plume's *state* at the coldest Jupiter pulse rather than a floor. Water reserve runs 84.41
MJ/kg at 15,000 K, 61.31 at 3800.
_Avoid_: reading 15,000 K as a nozzle requirement; charging argon's ionisation as a frozen
toll (three-body electron-ion recombination goes as `n_e^2` with `alpha ~ T_e^-4.5`, giving
nanoseconds at 0.32 kg/m³ against a ~100 µs expansion, so it *accelerates* as the plume
cools and the energy returns inside the nozzle).

### Interception navigation (near-term LEO)

**Common-mode error**:
An error shared by every PuffSat in the train, which slides the whole block together and
is cancelled by re-aiming.
_Avoid_: bias (overloaded with the optical calibration bias below).
_Aliases (informal, OK in prose)_: block-miss, block-slide.

**Per-unit scatter**:
How individual PuffSats differ from *each other*. Cannot be re-aimed away; must fit
inside the catch radius.
_Aliases (informal)_: spread.

**Centroid retarget**:
Shifting the swarm's collective aim point (up to about ±2 km) to absorb common-mode
error.

**Catch radius**:
The largest miss the projectile can still correct in the final seconds (about 475 m).
Set by engine thrust (a control/authority limit), *not* by sensing.

**PuffSat GNSS cross-check** (accepted 2026-08-20 grill, supersedes the 2026-08-12
blanket rejection):
A GNSS receiver on each PuffSat, differenced against a base receiver on the target, used
as an **independent cross-check** on the optical terminal chain. The optical chain stays
load-bearing; GNSS never becomes primary. Scope is the near-Earth LEO cycle only, and
within it the last ~13 minutes of the descent.
_Window_: the descent crosses the ~20,200 km GNSS shell 73 min before interception and
reaches near-terrestrial geometry (~3,000 km) 13 min out. The full-authority divert
horizon is ~487 s (½at² for 475 m at 4 mm/s²), so **GNSS arrives about 5 minutes before
the correction horizon closes**. That margin is the feasibility argument.
_Topology_: the target is the base and broadcasts; PuffSats receive and solve. This keeps
the no-transmitter-on-the-PuffSat commitment intact.
_Achievable grade_: **~18 mm**, the RSS of the GNSS terms alone (no troposphere at
altitude, and ephemeris/clock/most ionosphere cancel over a 5 km baseline).
_Spin phase is self-solving, not an input_ (resolved 2026-08-20). A tip-mounted antenna
rides a 12.5 m circle at 9.25 m/s, which writes a clean 0.118 Hz tone into the carrier
phase of every satellite. Measuring a 12.5 m amplitude at 1--2 mm carrier-phase precision
gives spin phase to ~0.005°, against the 0.09° that 2 cm needs. Ninety-two revolutions fit
inside the 780 s window, orbital motion has no content at 0.118 Hz, and a constant integer
ambiguity cannot affect a sinusoid, so this works on time-differenced phase without fixing
integers. Same principle as multi-antenna GNSS attitude determination, with the baseline
swept in time by one antenna instead of realized in space by two.
_Inertial package supplies the model, GNSS supplies the anchor_ (2026-08-20). The two are
complementary and **neither closes 2 cm alone**.
- The ADR-0002 accelerometer triad delivers the *geometry*. It reads `ω²r` directly, so
  with `r` known it gives ω to δa/2a = 7e-4 at a 1 mg floor, calibrating a 1--3% gyro
  scale factor down by 20--40x. It also resolves tether-pull direction to ~0.16 mrad with
  1 s of averaging against the 6.8 m/s² tip field, a factor of 10 inside the 1.6 mrad that
  2 cm needs. ADR-0002 already sized this leg at 8 mrad; 1.6 mrad is a 5x tightening, not
  a redesign.
- What the inertial package **cannot** supply is absolute azimuth about the spin axis. A
  gyro reads rate, an accelerometer reads specific force, and neither has an inertial
  azimuth reference on a spinning body. Dead-reckoning 780 s (33,072° of rotation) to 0.09°
  needs ω to **2.7 ppm**; the best accelerometer-calibrated figure is 7e-5, giving 2.3°.
  No MEMS part is within 25x. The shortfall is inherent to integrating a rate, not a
  matter of part selection.
- The split also runs in time. **Between burns** the arm is a clean circle and GNSS anchors
  phase. **During burns** the geometry is ADR-0002's 2.9 m kink and the triad carries it.
  The transverse tether mode at ~11.8 Hz (~100x spin) sits far above the estimation band.
_Paper scope_ (decided 2026-08-20): **one sentence**, in the redundancy-layer paragraph of
`sec:sensor_architecture` (near line 460), covered by that paragraph's existing "none of
this layer is simulated" closer. Everything below stays here, not in the paper, because
GNSS clears Tier 1 by orders of magnitude and a cross-check that is not load-bearing does
not earn a paragraph.
_Why the constellation cannot serve interception_: not link budget, geometry. A focused
beam closes the power side easily (a 3,300 km stream at 150,000 km needs 22 mrad = 1.26°,
worth ~44 dBi, from a 0.52 m Ka dish or 0.28 m at 60 GHz). But perigee and apogee sit at
opposite ends of the major axis with Earth between them. At the 200 km interception
altitude the true anomaly is 17.6°, putting the apogee direction **16.9° from nadir against
Earth's 75.8° angular radius**. The constellation is behind the planet, and no antenna gain
beams through a planet.
_The handover is forced, and it is clean_: occultation begins at ν ≈ 76° (r = 10,089 km),
**15 min before interception**. GNSS is available from the shell crossing at 73 min and
reaches good geometry at 13 min. So there is a **58-minute overlap and no gap**, and
neither number was designed.
_Downlink_ (decided 2026-08-20): **modulate the existing beacon**, 0 g. The blink pattern
is already read in every gated exposure by the target-side array, so no RF hardware, no
antenna, and line 446's no-transmitter commitment survives. Bandwidth is a few bits/s, set
by the tracker frame rate, which carries a disagreement flag and a coarse residual but not
raw observables.
_Mass and cost_: ~20 g for a purpose-built receiver (patch antenna dominates; DLR's Phoenix
flew PRISMA's cm-class relative nav at ~20 g, 0.85 W), i.e. **8% of the 250 g dry budget**.
Power is a non-issue (1.03 Wh over the full 73 min against ~3 Wh in a 5 g primary cell).
Cost is NRE, not per-unit: **do not buy space-qualified** ($10--50k each × 900 is
prohibitive). A 1.35-day, two-belt-crossing life is ~50x milder than the five-month park
CONTEXT already calls "deliberately cheap electronics", so commercial automotive silicon
serves. Budget ~$1--5M one-time for firmware (COCOM removal, ±60 kHz Doppler) and $50--500
per unit at volume.
_What the cross-check buys_: 2 cm at the co-flyer's 150 km standoff bounds the optical
angular error at **0.13 µrad**, 12x below the assumed 1.6 µrad fusion floor, from a single
unit with no averaging. This settles the flagged-open "is the 1.6 µrad floor noise or
bias?" question with flight data rather than a bench test.
_Antenna_: boresight **along the spin axis**, tip-mounted. The sky view is then fixed and
the antenna merely translates on a known circle at 9.25 m/s. Carrier phase wind-up (one
cycle, 19.03 cm on L1, per 8.5 s revolution) is deterministic and largely common across
satellites, so the receiver clock absorbs most of it.
_Avoid_: fusing the ~1 m GNSS vector into the ~1.6 cm optical estimate (it moves the answer
by nothing); assuming it helps anywhere off Earth (the Jupiter, solar-dive, lunar and
Parker cycles have no GNSS); assuming it reaches the gas-momentum centroid (it measures the
dry package, same as the beacon); a commodity receiver (COCOM cuts out above 515 m/s and
18 km, and L1 Doppler here runs to ±60 kHz).

**Cross-track knowledge** (`σ_θ · R`):
The projectile's lateral position error relative to the target, equal to angular
precision `σ_θ` times range `R`. The binding constraint on success, limited by a fixed
optical *calibration bias*, not by random noise.

**Plate capture**:
The mission-success criterion: a PuffSat landing anywhere within the ~5 m plate
(≥99 % probability), not hitting a precise point.
_Avoid_: "centimetre centring" as the *committed* requirement (see Flagged ambiguities).

**Feasibility tiers**:
The three confidence levels the interception claim is carried at, kept deliberately
separate. Tier 1: a 5 m plate capture, closed-loop simulated (companion repo
`puffsat_control_simulation`). Tier 2: a ~10 cm plate, *sized* (**surveyor-anchored
centring**, ADR 0022: nominal ~5.8 cm, 10 cm robust), not simulated; its binders are
bench characterizations a Monte Carlo cannot produce. Tier 3: a near-Sun/Parker
extension, an architectural sketch with open numbers. Only Tier 1 is a simulation
result. The tiers answer *different questions*, not one question at different
confidence: Tier 1 proves the closed-loop dynamics and nav grade (the committed
requirement); Tier 2 shows the metrology can center inside the funnel Tier 1 already
proved (capability). Neither demotes the other (2026-07-02 grill, provisional:
recommended framing adopted while Seth was away).

**Off-board nav assets (LEO)**:
The interception's support hardware, redistributed from the paper's original single
**coordinator node** into the three roles below. No dedicated per-mission co-flying
coordinator satellite is needed for LEO; the tracking-and-relay role is carried by
permanent infrastructure plus assets already in the architecture (the target, the reused
launch rocket).

**Apogee nav constellation**:
A permanent ~150,000 km Ka-band, authenticated *one-way broadcast* network that pins the
PuffSat's coast/apogee position; the PuffSat is a passive receiver. Sized to *match* (not
beat) the coast accuracy the corrector needs; ~3 members suffice. Clock/transponder
placement (ADR 0020, reconfirmed 2026-07-02 grill): precise clocks live on the
*constellation members*; the PuffSat carries a sub-gram verify-only receive ASIC, no
transmitter, and solves its clock bias from ≥4 members like a GNSS receiver; the target
and co-flyer rockets carry the full two-way crypto-nanosecond echo transponders.
_Avoid_: "GNSS at apogee" as the baseline (GPS side-lobe fixes have reached ~150,000+ km
on NASA's MMS, but they are weak, unauthenticated, and geometrically poor there; the paper
acknowledges MMS and explains why the dedicated constellation wins — resolved 2026-07-02
grill); "coordinator node" (this is permanent infra, not a co-flyer); putting an echo
transponder or precise clock on the PuffSat; treating a PuffSat **GNSS receiver** as a
*replacement* for the apogee constellation or for the optical terminal chain (it exists
only below the ~20,200 km GNSS shell, and only near Earth; see **PuffSat GNSS
cross-check**).
_Superseded_: the flat 2026-08-12 rejection of a PuffSat GNSS receiver. Two of its three
reasons do not survive the 2026-08-20 reframing. Range collapse does not apply to a
differential baseline, and phase-centre variation binds only at Tier 2. The lock-loss
reason assumed a radially-pointing antenna. See **PuffSat GNSS cross-check**.

**Target-side tracker array**:
The load-bearing terminal sensor: several (~5) independent, separately bench-calibrated
detectors on the target that image each PuffSat's optical beacon against a reference-star
field. Fusing them beats one detector by √N down to a common-mode floor (~1.6 µrad),
against a ~3.2 µrad requirement. Fallback (ADR 0019, paper alignment resolved 2026-07-02
grill): if bench calibration proves optimistic on the vibrating vehicle, about a dozen
cruder 10 µrad detectors average back to the required grade; the paper states both, in
these roles.
_Avoid_: calling it a coordinator node; expecting *ranging* to sharpen the lateral (angle
does the cross-track work); presenting the dozen-crude-detector fallback as the committed
configuration.

**Co-flying tracker**:
The *role* of a quiet off-board vantage holding the measurement from PuffSat deployment down
to the 2--3 s handover of ADR-0003, where it fuses with and yields to the **target-side
tracker array**. It is a role, not a vehicle: which vehicle fills it depends on the cycle.
- LEO cycle (`sec:starship_safelaunch`): the reused launch rocket.
  _Avoid_ treating it as a dedicated new satellite *there*; it is the launch rocket, reused.
- Staged crewed launch (`sec:periapsis_challenges`): the **tracker platform**, decided
  2026-08-12. The staged path has no launch rocket to reuse, because the PuffSats come from a
  **staging carrier** already in the ellipse and the crew vehicle's reusable ground launcher
  (line 752) never reaches the 10.9 km/s needed to fly alongside.
Sub-decisions: **plate-beacon differencing**, and a star channel decoupled from the 1 ms
beacon gate.
_Note_: this entry previously read "UNRESOLVED" and described the co-flyer as a redundant
hedge not required for the 5 m verdict. Both were stale as of ADR-0003; corrected 2026-08-12.

**Tracker platform**:
The permanent, refuelable sensor vehicle that fills the **co-flying tracker** role on staged
crewed launches. Parked in the **staging ellipse** at the same 2.7 d period as the carriers, so
phasing holds once set. Distinct from a **staging carrier**, which is a cheap tank that empties;
carriers proliferate as waves double each cycle, and the platform is the one asset worth
amortizing across many of them.
_Avoid_: coordinator node (legacy term for the rejected per-mission co-flying brain; the
platform is shared infrastructure, like the **apogee nav constellation**, which is the side of
the 2026-06-30 decision that was *accepted*), co-flyer satellite, tug.
_Budget_: parks at ~1000 km perigee to clear drag across the **storage interval**, drops to a
~200 km operating perigee for the push and returns, about 26 m/s each way, call it 50--100 m/s
per flight all in. Under 3% of vehicle mass per flight at methalox exhaust velocity, so roughly
30 flights per propellant load equal to dry mass. It never leaves the ellipse.
_Vantage_: the 200 km operating perigee against the PuffSats' 50 km disposal perigee is a
150 km **radial** offset bought for ~5 m/s at apogee, which must be paired with a comparable
along-track offset to satisfy the **miss plane** geometry. A purely radial offset is blind in
the radial miss axis.
_Refuelling_: the propellant rides up as a *dedicated consignment* in the **staging carrier**'s
payload, not scavenged from the PuffSat fill. Decided 2026-08-12. What matters is that it
arrives free with every wave, so there is no Earth tanker chain and no depot, which is the last
thing the Lagrange proposal was reaching for. Scavenging the carrier's water and running
**on-demand electrolysis propellant** was considered and set aside: it works, but it buys a
water plant and a several-kW array to avoid carrying a tank that costs a rounding error.
Every chemistry is affordable, because the platform's whole per-flight budget is 50--150 m/s
against the ~850 t a single crewed launch consumes (line 198):
- cold-gas propane (`sec:cold_gas_fluid_choice`), Isp ~70 s: ~2.4 t/flight for a 10 t platform,
  0.3% of a wave. Stores indefinitely, self-pressurising, no catalyst.
- peroxide/propane bipropellant (`sec:peroxide_propane_biprop`), Isp ~250--300 s: ~0.6 t/flight.
  Note the **storable PuffSat** exclusion of peroxide does *not* transfer here: that ruling was
  about 60% H₂O₂ inside a 250 g thin-skinned balloon, and bulk tankage with a real vent path and
  thermal control is a different problem.
_Preferred mechanism_: swap the tank rather than transfer fluid. The carrier brings a full one
and takes the empty. It needs no fluid interface, and it caps peroxide age at one wave interval
rather than at platform lifetime.
_Open_: which chemistry. Both close on mass; the decision is shelf life against dry mass.

**Plate-beacon differencing** (provisional, 2026-08-12 grill):
If the terminal measurement moves off the target, it must be a *differential angle*:
a strobed beacon on the plate rim is centroided in the same frame as the PuffSat
beacon, and only their angular separation is reported. This makes the co-flyer's
absolute position cancel to first order, leaving `miss ≈ θ_sep · D` with `D` the
scalar co-flyer-to-target range. Without it, an absolute line-of-sight measurement
must be registered to the plate through a separately-known co-flyer-to-target vector,
which the paper prices at ~2 m (GNSS, `sec:sensor_architecture`) and which alone
consumes the whole Tier 1 tolerance.
_Avoid_: assuming a co-flyer measurement is automatically referred to the plate. The
**target-side tracker array** gets that registration free by being bolted to the plate;
a co-flyer must buy it.

**Miss plane**:
The plane perpendicular to the PuffSat-target relative velocity, containing the two
error components that actually cause a miss: **radial** (altitude) and **cross-track**.
The third component, along the relative velocity, is *timing*, not miss. A tracker's
blind axis is its own line of sight, so vantage choice decides which miss component is
unobservable: a co-flyer directly overhead is blind in radial (bad), one offset purely
cross-track is blind in cross-track (bad), one offset **along-track** is blind only in
timing (good). For an offset with altitude `h` and along-track distance `x`, the radial
error is `(h²+x²)/x · σ_θ`, minimised at `x = h` (45° elevation) to give `2·h·σ_θ`.
_Avoid_: reading "closer is better" off `σ_θ · R` alone. Closest approach is exactly
when an overhead co-flyer is blind in radial. Range and observability fight.

**Differential astrometry** (star-differencing, the "Gaia trick"):
Measuring a beacon's bearing relative to reference stars in the *same* exposure, so the
focal-plane distortion common to beacon and nearby stars cancels. This is what "star maps"
buy: they attack the binding **cross-track knowledge** error, which is a fixed optical
*calibration bias*, not random noise.

**PuffSat self-homing** (redundancy layer, not yet simulated):
An optional autonomy layer: each PuffSat also carries a few-gram camera to image a bright
target beacon against stars and run its own terminal guidance, fused with the target-side
measurement. Strengthens the no-co-flyer story; costs a little non-volatile dry mass to
dispose of before impact. The sim modeled only the target-side path, so this is a
speculative addition, not a simulation result. Extended (2026-07-02 grill) to cover
inter-PuffSat bearing as part of the same optional layer: a camera pointed *backward*
images the follower's strobed beacon (pulsed LED or Q-switched laser plus narrowband
filter) against dark sky, exploiting the short inter-unit range; forward staring into the
impact flash is avoided per the sim's anchor-as-surveyor rule.
Cameras may be carried in threes for two-of-three majority voting: fault containment
(a systematic defect in one camera is rejected as an outlier), *not* a √3 precision
gain, which shared-batch distortion forbids (ADR 0019 independence rule).
_Avoid_: presenting it as the load-bearing baseline (the **target-side tracker array**
is); promoting inter-PuffSat bearing into Tier 1; claiming √N bias averaging across
same-batch cameras.

**Coordinator node** (fallback option, superseded as baseline for LEO):
The paper's original picture: a co-flying satellite that tracks each PuffSat and uplinks
commands. Superseded for LEO by the **off-board nav assets** above. The rewrite landed
2026-07-02: `sec:sensor_architecture` now holds the consolidated sensor/nav architecture,
with the coordinator node as its closing held-in-reserve paragraph, and
`sec:coordinator_node_dry_mass_disposal` retains only dry-mass disposal (label kept so
existing cross-references resolve).
_Avoid_: using it for the new architecture (name the specific asset instead).

**Surveyor-anchored centring**:
An optional metrology upgrade (a sacrificial "surveyor" projectile measured by an
independent instrumented gate, plus strobed beacons on each unit) that shrinks the
plate from 5 m toward ~10 cm without changing the baseline architecture. Now *sized*,
not just argued (sim repo `centering_budget.py`, ADR 0022, folded into the paper
2026-07-02 grill): the plate is the RSS of two legs, the hoop precision σ_hoop and the
camera scatter σ_θ·v/f. Nominal point ~5.8 cm (1 cm hoop ⊕ 3 µrad camera at the 2 Hz
link); 10 cm tolerates σ_hoop ≤ 2.9 cm; 5 cm needs *both* legs tightened. A Q-switched,
coarse-pointed beacon (~100 kW peak, few-hundred-mW average) plus narrowband filter and
matched gate keeps the intra-train link distortion-limited, not photon-limited.
Thermal-distortion hierarchy (ADR 0022 §5, reconfirmed 2026-07-02 grill): differential
astrometry is the *primary* lever (thermal figure error is smooth, so star-differencing
cancels it); thermal modelling with software correction (Gaia precedent) and a
reflective narrowband front element with edge-cooled diamond conduction (gyrotron
practice) are *backup/margin*, load-bearing only near the Sun.
_Avoid_: "achieved" (binders are unmeasured bench characterizations; right next rigor
is a bench test, not a sim); putting the diamond filter in the load-bearing LEO role.

**Beacon lever arm** (spinning tethered pair only, resolved 2026-08-11 grill):
The vector from a strobed beacon to the point guidance actually cares about, the center
body, which the tip packages of `sec:spinning_tension_detail` straddle at roughly ±12.5 m
on the 25 m bundle. Its length follows from the tether design; only its *direction* is
open. Scoped as a **refinement-only** error: 2 m of tolerance across a 12.5 m arm is
160 mrad (9.2°), which a taut tether never reaches, so the 5 m capture verdict does not
depend on it; the ~10 cm centring refinement needs 8 mrad and does.
_Avoid_: "the beacon is on the dry mass" as the statement of the problem. A beacon is
always dry mass (LED, battery, driver). The live choice is *which* dry mass carries it,
a tip package or the center body.

**Tip-beacon pair** (resolved 2026-08-11 grill):
Both end packages strobe, and the target-side array averages the two bearings. At near-equal
range the mean bearing *is* the bearing to the chord midpoint, with no range knowledge, no
package attitude, and no tether model, at σ_θ/√2 (~1.1 µrad). The 25 m separation subtends
417 µrad at 60 km, hundreds of times the precision, so the pair always resolves; blink-pattern
IDs already distinguish them. Chosen over inferring the lever arm from tip accelerometry,
which stacks gyro drift, a tip-tangent-vs-chord mode assumption, and a 12.5 m extrapolation.
Costs a few grams on the counterweight and doubles the beacons the tracker must associate.
_Avoid_: treating it as a complete solution. It cancels **antisymmetric bend** (S-curve, tips
swing oppositely) and is *blind to* **symmetric bow** (C-curve, tips stay put and the center
displaces), which is exactly what a transverse force on the center body produces. Detecting
that bow is the residual job left to accelerometry.

**Center-body kink** (the dominant deflection; ADR 0002, sized 2026-08-11 grill, not yet in the
companion repo):
Under thrust the 25 m bundle is not a bow but a shallow V, with the kink at the center body,
which the two half-tethers have to drag along. Force balance at the center gives
`sin θ = F / 2T`, half-angle θ, total thrust F, tether tension T. At F = 400 mN and
T = 0.85 N: **θ = 13.6°, putting the center body 2.9 m off the tip-to-tip chord.** Modulates
over the spin period, full amplitude when the tether axis is perpendicular to thrust and
zero when parallel (there the load is a tension differential, not a kink), so it is a
spin-synchronous signal with known phase. Proportional to thrust, so 3% thrust knowledge
buys 10 cm; the triad measures θ directly at ~0.15 mrad. Assembly integrity needs `2T > F`,
about 4x margin here. Disposal geometry survives: tips stay 12.15 m off the impact axis
against a 5 m plate.
_Avoid_: locating the deflection at the *thrusting tip* (a tip thruster firing in a fixed
body direction is a torque, not a bend; coordinated thrust from both tips cancels the torque
and translates cleanly, leaving the tethers radial at the tips); treating it as a **bow**,
which the **tip-beacon pair** would partly see, when a symmetric kink is exactly its blind spot.

**Tip-pull bend** (the small, benign companion term):
Each tip must be accelerated at the assembly's rate by its own half-tether, giving
`a_assembly / (ω²r)` = 2.4 mrad at 400 mN, 0.1 mrad at 17 mN drag cancellation.
Baseline: ω ≈ 0.74 rad/s (isobaric ceiling at a ~0.18 m charge radius), r = 12.5 m, tip
centrifugal 6.8 m/s², spin period 8.5 s. The tip sits ~70x further from the axis than the
charge, so the layout buys tension without touching the isobaric ceiling. Bare 100 µm bundle
drag at 200 km adds 0.09 mrad; the bundle weighs 0.27 g over 25 m and breaks at ~45 N against
0.85 N working load, so it is sized by handling and redundancy, not by load.
_Avoid_: comparing raw thrust to tether tension (off by the 200:1 assembly/tip mass ratio);
using the 400 mN figure as a drag number (tex:376 says it is actuator authority; the
simulation's drag is 17 mN).

**Quasi-static tether response** (resolved 2026-08-11 grill):
The fundamental transverse mode of each 12.5 m half-tether is `c/2L` with `c = √(T/μ)`,
about **11 Hz** for a 100 µm bundle (3.5 Hz for ten redundant strands), far above any
throttled-thrust bandwidth. So the tether tracks commanded thrust quasi-statically with no
ring to outlast, and **throttled thrust can run continuously to impact with no quiet period**.
Deflection is then a commanded quantity to subtract, not a transient to wait out. Solid-charge
impulses are the exception (step response overshoots ~2x and rings at 11 Hz), so they stay
early in flight.
_Avoid_: the "pendulum after thrust cutoff" model, which assumes a mode near the spin rate;
the real mode is ~100x the spin frequency.

**Accelerometer triad** (role settled 2026-08-11 grill):
Three co-located 3-axis MEMS parts (~1 g) on the **sensing** package, not the thruster package
(a 400 mN thruster on a 125 g tip is 3.2 m/s² of self-induced specific force against a
0.016 m/s² signal, a 200:1 swamp; the paper's existing thruster/sensor split gives this free).
Load-bearing, not a bound check: the **center-body kink** is the **tip-beacon pair**'s blind
spot and at 2.9 m overruns even the 2 m tolerance, so nothing else measures it. Three units
vote 2-of-3 against a silent bias, reusing the camera-triad logic of tex:443.
_Avoid_: justifying the count by signal strength (averaging buys only √N, 1.7x for three, which
one better part buys outright) or by the centrifugal gradient (`a₂−a₁ = α×r + ω×(ω×r)`, which
needs *spread* units and is already covered better by the gram-class MEMS gyro over the
few-second window, at ~0.17 mrad of drift); spreading them into an actual triangle, since a
vote wants identical inputs, not a baseline.

**Kink downlink** (resolved 2026-08-11 grill):
θ goes to the target-side estimator over the **low-bandwidth radio** already in the 250 g
budget, not encoded in the beacon blink pattern. 11 bits at the ~2 Hz link cadence is 22 bps,
so bandwidth is never the issue. Chosen because the optical channel goes dark whenever an
impact saturates the tracker's rearward view (tex:439), and a separate radio keeps the kink
data flowing through those gaps rather than losing it with the beacon; it also leaves the
beacon pulses purely metrological, undisturbed by data modulation that would have to share
the matched gate and the centroid.
_Avoid_: assuming the radio's current sizing covers this. It is budgeted for housekeeping
across a multi-day coast; this is a hard-real-time terminal duty cycle, live and pointed
through the last seconds.
Open: whether a command uplink already exists that would let the PuffSat do the arithmetic
onboard instead, making any downlink unnecessary. Not confirmed.

**Isobaric ceiling ⇒ kink is unavoidable** (ADR 0002; resolved 2026-08-11 grill; universal
across variants):
Holding θ ≤ 8 mrad at 400 mN without measuring needs T ≥ 25 N, so ω = 4 rad/s, which puts
0.29 g on the charge, 7x past the 0.04 g mark where the isobaric gradient is already 10%.
The sensitization chemistry caps ω, ω caps T, T sets the kink, so **measurement is mandatory,
not a convenience**. This is the number CONTEXT's "a fast-spinning variant needs rechecking"
was waiting for. Decided to hold ω = 0.74 rad/s and fly the triad on *all* variants rather
than let non-explosive units spin faster: a variant-dependent spin rate means two tether
designs, 20 g tips, a fatter bundle (25 N against a 45 N break is only 1.8x), and it opens
cavitation-sphere stratification on liquid payloads.
_Avoid_: reusing CONTEXT's buoyancy dismissal for a *liquid* payload. That is computed for
the 50 Pa·s emulsion; in bulk water at 10⁻³ Pa·s the same Stokes creaming runs ~50,000x
faster, so a 100 µm cavitation sphere migrates tens of metres over a multi-day coast even at
0.01 g and fully stratifies to the spin axis. A frozen payload is immune.

**Sheath stripping** (resolved 2026-08-11 grill):
The inflatable bumper / nitrogen tube of `sec:spinning_tension_detail` deflates or is jettisoned
before the drag phase, having served as Whipple protection through the coast. A 3 cm sheath over
the 25 m bundle is 0.75 m² broadside and, being light with its own area, is not divided down by
assembly mass: ~24 mN of drag against 0.85 N of tension, a **28 mrad quasi-static bow** (0.35 m
of center displacement), 300x the bare bundle and the largest single bow term if retained.
Stripping it also changes what accelerometry has to do, from tracking a slow DC drift against
MEMS bias instability to band-passing a clean ~0.7 Hz post-burn transient.
_Avoid_: keeping the sheath through descent on the grounds that its drag is "a modest price";
that holds for the coast, not for the drag phase. Open: the PETN variant loses its grain-strike
bumper exactly when the tether is most loaded.

### Near-Sun navigation

**Transverse-node differential ranging**:
Lateral knowledge obtained from a coordinator node placed off to the side of the line of
flight, measuring distances only to the controlled projectile and a reference, and using
the difference.

**GDOP** (geometric dilution of precision):
How anchor geometry converts range precision into lateral precision,
`σ_lateral ≈ σ_range / sin θ`. A transverse node gives good GDOP (`sin θ ≈ 1`); an
in-line anchor gives terrible GDOP (`sin θ → 0`).

**Deterministic-coast correction**:
Two-tier control (a gross early correction of ~tens of m/s plus a fine, late ~mm/s nudge
about 1 s before impact) that defeats the `v²` homing-miss floor by nulling a known,
pre-measured offset rather than chasing fresh navigation noise.

### Economics

**Momentum-amplification cascade** (in the paper as `sec:methalox_rebuttal`, "Moneyball Meets Methalox"):
The chain that answers the obvious skeptic ("how can heat-tolerant, formation-flying
projectiles beat a tank of methalox?"). Fast, expensive reaction mass transfers momentum
to progressively larger amounts of slow, cheap mass at each collision, so cost per kg falls
by roughly the mass-amplification factor at every stage. For the 4 R☉ transport case:
a retrograde projectile (worst-case ~\$3200/kg, projectile-cost-dominated, early generation,
aviation-scale manufacturing but pre-breeding) is mixed 3:1 with cheap prograde mass
(÷4 → ~\$800/kg reaction mass at effective exhaust u_eff ≈ 155 km/s), boosted ~34.5 km/s at
periapsis to a 150 km/s Earth crossing (propellant fraction e^(34.5/155)−1 ≈ 25%, ÷~4 →
~\$200/kg at 150 km/s), then at Earth its kinetic energy is spread over ~24× cheap onboard
water/plastic (u_eff ≈ 25 km/s exhaust, ÷25 → ~\$8/kg of exhaust) which lifts ~2.6 kg to LEO
per kg exhausted (e^(8/25)−1 ≈ 0.38) → **~\$3/kg to LEO**, competitive with methalox even at
the worst-case anchor. Doubling for return-trajectory launches keeps it well under methalox;
the costly fast-cycling ship amortizes because PuffSats decelerate and recover it in Earth
orbit. The terminal number is only as firm as the mixing-chamber efficiency (the **fudge
factor** `f` / f-sim frontier); the magnetic nozzle is legitimate here despite being an
Earth-arrival stage because a 150 km/s collision is fully ionized (near-Sun-class energy),
unlike the weakly-ionized 8 km/s LEO PuffSats.
_Avoid_: quoting the ~\$3/kg output without the mixing-efficiency caveat; presenting it as a
cost model rather than an order-of-magnitude rebuttal; conflating the worst-case ~\$3200/kg
projectile anchor with the optimistic ~\$80/kg materials build-up (the latter, blended with
~90% cheap bulk to ~\$8/kg fleet cost, feeds the Straw Way power economics of
`sec:strawway_economics`, not the transport rebuttal: the \$8/kg retrograde fleet dilutes
~16× en route to Earth (÷4 from 3:1 prograde mixing, ÷4 from spreading over 4× its mass of
thrown payload, the same 25% propellant fraction as the transport chain) to ~\$0.50/kg,
i.e. ~\$0.16/MWh raw at 150 km/s (3.1 MWh/kg), quoted in the paper as "comfortably under
\$1/MWh" after conversion losses, against a 1¢/kWh ($10/MWh) price.

**Mass interest** (`sec:jupiter_only_growth`, a `\subsubsection` placed after the growth
paragraph and before "Inner Planet Assist Alternatives"; title "Mass Interest Is Paid In
Kilograms, And The Early Buyer Wins". Renamed from "space mortgage" 2026-09-02):
A **mass-denominated equity stake** in the Jupiter-only growth fleet, not a launch slot and
not a loan. The customer buys kilograms of PuffSat fleet mass; the holding compounds at the
chain's annual growth rate (companion ADR `0013`) for as long as it stays in the loop; the
customer redeems it as delivered payload whenever they choose to stop compounding. The name
is load-bearing in both of its ordinary senses. An *interest* is a fractional ownership claim
(a majority interest, a working interest in a well), and *interest* is what a holding earns
by compounding. Seed launches toward Jupiter are financed against those subscriptions on the
operator side, with the in-transit fleet as the appreciating collateral. Early buyers win
because their kilograms compound through more cycles, and because the data their cycles
return raises **recovery** (`e`) for everyone after them. At the reference point
(`e = 0.6`, `f = 0.8`) a kilogram bought into cycle 1 is a x83,070 claim by 2055 against
~x20 for one bought into cycle 8, at the same price.
_Avoid_: calling it a forward contract or a prepaid launch slot (those are the rejected
alternatives, and they make the exponential decorative rather than load-bearing); any debt
instrument name (**mortgage**, **bond**, **coupon**), all rejected 2026-09-02 because debt
caps the upside, cannot return zero without meaning default, pays the same rate to cycle 1
and cycle 8, and puts the *operator* in the borrower seat where "early buyer wins" loses its
referent; **security** as part of the name (a regulatory category, not a name, and it
collides with the aerospace sense of the word); quoting a compounding multiple without naming
both `e` and `f`. First use in the paper takes the appositive "an ownership stake denominated
in kilograms rather than dollars", which is what answers "is this a financial instrument?".

**Redemption is withdrawal** (the conservation caveat the multiples rest on):
In the two-wave ledger the parked payload splits into **craft** and **slug** and *both* go back
to Jupiter. That is where the growth comes from. So a kilogram taken as delivered product is a
kilogram not reinvested: the fleet grows at `r − d` for redemption rate `d`, and **x83,070 is
the no-redemption number**. The section states this in two sentences and names a compounding
phase followed by a harvest phase. Far from weakening the pitch, it is what makes "first-time
buyers win" literally true rather than a slogan: the valuable claim is the one with the most
cycles left ahead of it.
_Avoid_: presenting the multiples without the reinvestment assumption; promising delivery on
demand during the compounding phase; adding an optimal-harvest crossover number (not computed
in the companion repo, and quoting one would need new code in `two_wave_growth.py` first).

**Register (Mass Interest only)**: deliberately plainer than the surrounding paper. Target is
an AP-Physics student for the propulsion parts and an interested layperson for the investment
parts. Short sentences, everyday words, the arithmetic shown rather than asserted. This is a
local exception, not a change to the paper's voice elsewhere; the stylebook in `CLAUDE.md` still
applies in full (no em-dashes, no colon-welded sentences, no rule-of-three, quantify don't hedge).

**Numbers printed**: the multiple compounded over the **11 flown cycles / 28.3930 yr**
(2026-11-09 to 2055-04-02), *not* ADR 0013's 30-year projection. The thirty-year framing is
gone with the mortgage name (it was a caption clause justifying the round number); every
printed figure is ephemeris-verified. At the reference point
(`e = 0.6`, `f = 0.8`) that is **x83,070**, against x157,700 if the rate is extrapolated the last
1.6 yr. _Avoid_: printing the projection; deriving the table from ADR 0013's rounded e-folding
column (regenerate from `two_wave_growth.py` / `ChainGrowth.mass_after(28.3930)` instead, worth
~1.4% at the top corner: my derived reference cell reads x83,184 against the ADR's x83,070).

**Citation**: `\cite{Katz_aim_is_all_you_need_2025}` only, as everywhere else in the paper. The
ADR number is deliberately *not* named in prose and gets no deep-link bib entry, for consistency
with the paper's other twelve companion-repo cites. Decided 2026-08-20 against the alternative.

**The table, as it goes in the paper** (regenerated 2026-08-20 from `python -m src.two_wave_growth`
in the companion clone, `total_growth` column; reproduces ADR 0013's reference cell exactly).
Multiple of launched mass compounded over the 11 flown cycles, 28.3930 yr, 2026-11-09 to
2055-04-02:

| `e` | f = 0.5 | f = 0.6 | f = 0.7 | f = 0.8 |
| ---: | ---: | ---: | ---: | ---: |
| 0.25 | x0.0953 | x0.311 | x0.816 | x1.83 |
| 0.30 | x1.28 | x4.54 | x12.8 | x30.5 |
| 0.40 | x40.2 | x161 | x506 | x1,328 |
| 0.50 | x363 | x1,587 | x5,371 | x15,100 |
| 0.60 | x1,676 | x7,827 | x28,060 | x83,070 |
| 0.70 | x5,182 | x25,460 | x95,480 | x2.94e5 |
| 0.80 | x12,350 | x63,180 | x2.46e5 | x7.83e5 |
| 0.90 | x24,590 | x1.30e5 | x5.21e5 | x1.71e6 |

Two cells carry the argument. **`e = 0.25, f = 0.5` returns x0.0953**, nine and a half cents on
the dollar, the underwater case. **At `f = 0.8`, `e = 0.4` grows 28.83%/yr to x1,328 and
`e = 0.9` grows 65.76%/yr to x1.71e6** — roughly twice the annual rate for **1,284x** the mass.
That ratio is the compound-interest intuition the **mass interest** name exists to carry.
The chain-optimal slug ratio `k` runs 4.53 to 9.52 across the table and is interior to the
search box everywhere.

**Supersedes**: the existing growth paragraph's ADR 0009 claims are rewritten in the same edit.
The perijove burn no longer buys the two-wave split (real orbits give the Lambert pair a free
encounter time; 8 of 11 cycles pay under 1 m/s, chain mean 0.179 km/s), and "the chamber recovers
80\% of the ideal thrust" was attached to a 1.7-1.8 yr doubling that is really the `e = 0.6` row
(`e = 0.8` doubles in 1.45 yr).

**Jupiter-cycle nozzle scaling** (new paragraph in `sec:minimum_nozzle`, pointed to from Mass
Interest):
`sec:minimum_nozzle`'s "hundreds of tonnes of payload, better still more than a thousand"
amortization floor was drawn for the **near-Sun** pulse and does not bind the Jupiter-only
outbound leg. At `k = 8.53` the arriving kilogram vaporises 8.53 kg of slug, so the reduced
mass is 0.895 kg and a 75 km/s closure carries **2.52 GJ**, against **477 GJ** for 2.5 kg at
618 km/s. A factor of **189**. On the section's own rule that coil mass scales with contained
energy, and the Mini-Mag anchor of ~200 t for 340 GJ, that is **~1.5 t of coils** against
~281 t. The nozzle is then 14.8% of a 10 t craft, **4.9% of a 30 t craft**, 1.5% of a 100 t
one, so the seed vehicle is Starship-class rather than thousand-tonne-class. This is what makes
the **mass interest** fund something buildable.
Ionization check, at AP-Physics register and verifiable in one line: specific kinetic energy
`½v²` spread over carbon atoms gives ~**4 eV/atom at 8 km/s** (below carbon's 11.26 eV first
ionization, matching the paper's "weakly ionized" low-orbit gas) and ~**350 eV/atom at
75 km/s**, about 31x over it. The outbound leg is therefore firmly on the ionized side of the
paper's own dividing line, so a magnetic nozzle is legitimate there.
_Provenance_: derived in the 2026-08-20 grill session, not in the companion repo. It is one
division against a cited anchor (`ewig2003minimag`, `lenard2007minimag`), so it needs no new
code, but it is a **linear extrapolation** and the paragraph must say so.
_Avoid_: quoting the 1.5 t without the linear-scaling caveat; letting `sec:minimum_nozzle`'s
thousand-tonne sentence stand unqualified once this paragraph exists; reusing the *lighter
impactor* radiative caveat here (this pulse is lighter by **speed**, not by impactor mass, so
its plasma is cooler and less radiative, not more).

**Overtake leg vs head-on leg** (`sec:jupiter_only_growth`; first decided 2026-08-20 grill,
**verdict reversed later the same day** after the companion two-leg sweep was regenerated):
Which device catches the growth push. Superseded content: the earlier version of this entry
argued the plate wins on *payload delivered per kilogram launched off Earth* (plate 1.000 vs
nozzle 0.700) and turned on the claim that a plate simply *is* a no-slug nozzle. Both are
retired. The launched-mass metric charges the nozzle for its slug and never charges the plate
architecture for its own ground launch, and it omits the per-PuffSat side where the nozzle wins.
The `k = 0` identity is arithmetic only (see below).

**The geometry still stands, and is why leg 2 has no choice.** The two legs face opposite ways.
- **Earth boost (leg 1)**: an **overtake**. The returning PuffSat catches the craft from behind
  and pushes it from rest into the parking orbit. The arrival's momentum already points where the
  craft is going, so a plate only has to reverse it. Ideal impulse `1 + sqrt(1+k)` times the
  arriving momentum.
- **Jupiter departure (leg 2)**: **head-on**. The arrival's momentum points backward, so a plate
  would *brake* the craft. Ideal impulse `sqrt(1+k) - 1`, which is zero at `k = 0`. Vaporizing a
  slug is the only mechanism there, not an optimization of one.

**The `k = 0` identity is formal, not physical.** As `k -> 0` the nozzle's parked-mass term goes
to the plate's with `e1` in the role of `f`. But a magnetic nozzle steers a **conductor**, and a
vanishing slug dissipates nothing in the merge, so there is no plasma to grip. `k = 0` sits
*below* the plume ignition window. The two are genuinely different devices. Do not write "a
pusher plate is what a magnetic nozzle becomes when it carries no slug" as a physical claim.

**Constraints on `k`, in the order they bind:**
1. **Plume ignition window** (two-sided). Only the dissipated share `k/(1+k)` of the arrival's
   kinetic energy heats the blob, spread over `1+k` kg, so `eps_th = w^2 k / (2(1+k)^2)`. That
   peaks at `k = 1` and falls on **both** sides, giving a closed interval, not a ceiling. Too
   little slug dissipates nothing; too much spreads a fixed energy too thin.
2. **Evaluated at the coldest instant of the burn.** The push runs the craft 0 -> 10.95 km/s, so
   `w` *falls* through the burn as the craft catches up. The last pulse is the coldest and sets
   the ceiling.
3. **Fleet-wide intersection.** One nozzle loading flies all eleven cycles, so the admissible set
   is the intersection over cycles, and the slowest cycle wins.

**2S vs 3S cadence** (regenerated 2026-08-20, 10-day split; the ADR 0013 default is 20 days and
gives ~1.7 km/s higher, so always pass `split_days=10`):

| cadence | cycles | growth-wave `v_b` | departure burn | cold end | `k1` ceiling | plate ratio at `f=0.8` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 synodic | 7 | 61.83-65.13 (mean 63.02) | 6.84-7.17 | 50.88-54.18 | 13.26-15.32 | 8.21-8.69 |
| 3 synodic | 4 | 56.53-57.43 (mean 57.17) | 5.32-5.54 | 45.58-46.48 | **10.21**-10.70 | 7.43-7.56 |

Both follow from one cause: squeezing Earth -> Jupiter -> Earth into two synodic periods forces a
more energetic transfer, which costs more to depart on *and* comes home faster. The 3S cycles are
the cheap-to-leave, slow-to-return ones, and they cap the fleet at `k1 = 10.21` where the best 2S
cycle alone would allow 15.32.

**Growth wave vs departure wave** (`sec:jupiter_only_growth`, `sec:split_tail`; named in the
2026-09-02 grill):
The Jupiter-only chain's departing batch splits **at Jupiter** into two waves that reach Earth one
parking-orbit period apart. The **growth wave** arrives first and pushes the newly lofted payload
from rest into the parking orbit (leg 1, the overtake, recovery `e1`). The **departure wave**
arrives one parking orbit later and is fed to the magnetic nozzle to throw that payload back to
Jupiter (leg 2, head-on, recovery `e2`). The gap between them **is** the parking-orbit period.
Pulling the growth wave that far ahead of the departure wave costs the **separation burn**.
_Avoid_: calling this a "two-wave split" or "split push" in prose. **Two-wave departure**
(`sec:split_push`) is a different maneuver in a different cycle, the Jovian dive's *Earth*
departure flown as two pulses ~5 days apart. Also avoid the companion's name **nozzle wave** for
the second one: both legs of this chain run a magnetic nozzle, which is exactly why
`tab:two_leg_growth` sweeps `e1` and `e2` separately.

**The split gap is 10 days in this chain, 20 in the wider architecture** (settled 2026-09-02 after
the paper was migrated to 20 days and reverted):
`two_wave_growth.DEFAULT_SPLIT_DAYS` is **10** per companion ADR 0013, and the paper carries 10.
`astro_constants.PUFFSAT_CYCLE_ORBIT_PERIOD` is **20 days**, and `sep_split_correction` defaults
to 20. Both are real; they belong to different cycles. 10 and 20 days are within 0.7% on doubling
(1.737 vs 1.749 yr), because a longer parking orbit buys a cheaper apoapsis re-aim and pays for it
with a larger separation burn.
_Avoid_: moving the paper to 20 days. It looks like a three-number edit and is not. The split gap
only reshapes the **growth wave**, so at 20 days its collision speeds rise (2S 61.83-65.13 ->
63.56-66.77; 3S 56.53-57.43 -> 58.44-59.29), the coldest growth push goes 45.58 -> 47.49 km/s, and
that cold end is the design point for the **entire plume and bag thermal chapter** in 11 places
(liner load, radiative share, `tab:axial_bag`, ionization history, field leak, `eta_chem`, the
shocked-layer 1040 MJ/kg, and two appendix tables). A hotter pulse ignites more easily but
radiates as `T^4`, so the thermal margins move the *wrong* way. Departure-wave figures do not move
at all (`v_b` 54.49-63.31, departure burns 5.32-7.17).

**The split tail, and why low thrust cannot buy it** (`sec:split_tail`; landed 2026-09-02 from
companion ADR 0026, re-run at the paper's 10-day gap because the ADR published only 20-day figures):
The separation burn's cost is **bimodal**. Eight cycles buy the head start for under 0.3 m/s; three
pay 398.5, 556.0 and 1011.3 m/s, all three with the growth wave pinned at the 1.056 `R_J` perijove
floor. The residue is an **angle**, not a speed mismatch, so on two of the three no flyby change
helps at all. Worst total correction 1029.8 m/s (2036-09-07), 26% of the wave as methalox.
**Pay the tail, do not dodge it.** A stricter cadence that also refuses 2S when the growth wave
would pay holds every correction under 1.51 m/s and doubles in 1.863 yr against 1.737, so dodging
costs **7.3% of the clock**: it fits 10 cycles into the same 28.39 yr where the flown rule fits 11,
and a cycle is worth ~2.9x.
**The propellant flips which cadence wins**, which is the finding. Never-fall-back is worst on
methalox (2.270 yr, corrections to 5.04 km/s leaving a fifth of the wave) and best on argon
(1.501); charged for its 7.7 MW array it loses the lead again by 20 kg/kW.
**Low thrust cannot buy the tail.** `a = 2 eta P / (m v_e)`, so at eta = 0.5 acceleration is
specific power over exhaust speed: 1 W/kg buys 5.1e-5 m/s^2 at 1 AU. The worst cycle needs
8.02e-5, i.e. **1.57 kW per tonne of wave**, 0.79 MW at the 500 t reference, ~60 flight-class
12.5 kW Hall thrusters. The array fraction is scale-invariant, 2.4% at 15 kg/kW. Net of its own
array argon is worth **1.1%** in doubling, and the departure wave's array is still uncharged.
_Avoid_: saying the split spacing "pushes us to the 3S cycle" -- that is the policy the work
**rejected**, not the finding. Benchmarking the array against small deep-space probes (Psyche,
Dawn): the blocker is **absolute** power, ~0.8 MW built and expended every 2.18 yr, not W/kg.
Quoting ADR 0026's 8.2x shortfall, 1.61 MW, 2089 m/s worst cycle or 3.7% argon gain: those are its
**20-day** run and do not describe the chain the paper flies.

**Fly-and-park** (`sec:jupiter_only_growth`; companion `src/fly_and_park.py`, its
`docs/paper_corrections_fly_and_park_2026-09-07.md`, named in the 2026-09-08 grill):
Flying the Jupiter-only chain's loop **shorter and hotter than its synodic window** and parking
the payload in its bound near-escape cycle orbit for the remainder, so flight plus park is an
exact integer of synodic periods. At the best 3S phase: flight 2.735 S against an exact-3S
cycle's 2.99, park 0.265 S (~104 days), departure burn 6.74 km/s against 5.56, arrival `v_b`
**68.7 km/s against 61.3**. The park is nearly free: stretching the cycle orbit from 20 days to
~100 moves the push target `v_rf` 10.9503 -> ~10.99 km/s, 0.2% on the mass ratio.
**What parks is the payload, not the impactor.** The arriving mass is consumed in the collision
on arrival, so **the mass cannot wait** (companion ADR 0010) still holds unchanged. Fly-and-park
lengthens a coast the architecture already flies; it stores nothing.
_Avoid_: reading it as warehousing returned mass, or as lifting ground mass early into LEO (the
model represents **no ground resupply whatsoever**); saying it shortens the cycle (the padding
exists precisely to hold the clock at an exact integer, and the companion retires that claim by
name); expecting a `(68/61)^2` energy gain (the impulse law is **linear** in closing speed).

**Synodic lock (2S lock, 3S lock)** (named in the 2026-09-08 grill, to keep three senses of
"2S" apart):
The property **fly-and-park** buys: because flight plus park sums to an exact integer of
Earth--Jupiter synodic periods, the cycle **returns to its own departure phase** and repeats with
no steering. A cycle that lands at 2.09 S does not, which is why the chain search could reach one
and never hold it: each drifting cycle hands its successor a worse phase.
This is the **third** distinct sense of "2S/3S" in this document and they do not interchange:
* **Three-synodic closure (3S)**, above, is the *Jovian solar dive*'s bend feasibility. 2S there
  is short 6.84 deg and **does not close** unpowered at any perijove burn.
* **2S vs 3S cadence**, above, is the *Jupiter-only chain*'s return policy. Both are routine;
  the flown 11-cycle chain takes seven 2S returns and four 3S.
* **Synodic lock** is a *padded total*, and the thing being claimed is phase repeatability.
_Avoid_: writing bare "the 2S cycle" anywhere near `sec:jovian_dive_cycle` (a reader taught the
closure sense first will read it as the 6.84 deg bend deficit being solved, which nothing here
does); calling the 2S lock a new trajectory, which it is not (see below).

**2S lock: pinned, and it is the resonance we already had** (2026-09-08 grill, pinned same day
by companion ADR 0031 and asks S5-S8; **in the paper at `sec:synodic_lock`**):
The 2.00 S lock exists, and padding is not what builds it. It sits at departure phase **0.8082**,
flight 1.9497 S, park **0.0503 S (20.06 days)**, `dv` **8.613 km/s**, `v_b` **63.35 km/s**, and
that is `fixed_points()`' own two-synodic resonance to every digit. Its park is the mandatory
coast plus about ninety minutes, so there is no remainder for fly-and-park to pad.
**The park cannot go below the coast.** The push lands at one periapsis and the departure burn
lights at the next, so the park is the 20-day cycle orbit *lengthened*. The first construction
here wanted a 9-day park and that is not a trajectory; asking the question found the companion's
`MINIMUM_PARK` at 0.02 S, 2.5x under the coast it stood for. Charging it cost +3.5% of clock.
**The trade, and it is the reason 2S does not simply win.** Doubling **0.873 yr** against 3S's
**1.189** at Isp 2214 (**1.082** against **1.377** at Isp 1200), bought by giving back launch
window: **26 of 73 phases against 73 of 73**. 2S at the top exhaust speed is still narrower than
3S at Isp 1200's 44 of 73. Present them as **two operating points with the trade stated**, never
as 2S superseding 3S. On methalox nothing pads to 2.00 S; 3S is reachable from 12 of 73 at
3.641 yr.
**The flown chain needs none of this.** All eleven cycles are already exact locks, drift under
1e-4 S. What forces its four 3S fallbacks is ADR 0011's perijove floor (45 of 91 windows over
200 years clear 4,000 km), not phase drift, so the lock retires a problem the architecture did
not have.
_Avoid_: quoting the 0.84 yr / phase-0.781 / 9-day-park construction, which is superseded;
counting "phases offering a lock" off the **usable-phase** fraction, which is a looser test and
is what made an earlier cut of ADR 0015 read 28 of 73 against a 73 of 73 from a different test;
presenting the 2S lock as a new trajectory or as fly-and-park's product.

**Departure phase, sweet phase, usable phase** (companion `src/fly_and_park.py`; the paper must
define all three before using any fly-and-park result):
**Departure phase** is where Earth and Jupiter stand relative to each other when the payload
leaves, as a fraction of the 1.0923 yr synodic period, so phase 0 and 1 are the same geometry.
**Sweet phase** is where reaching Jupiter is cheapest, located at **0.726** rather than assumed;
the cheapest available departure burn runs **4.41 km/s there to 38.49 at the worst phase**, an
8.7x swing. That swing is the *mechanism* behind the integer-synodic clock the paper already
reports but never explains: a stage that cannot afford the dear phases is pinned to the cheap one.
**Usable phase** is one from which some closing cycle actually grows the payload. Reachability
never changes with exhaust speed; usability does.
_Avoid_: treating phase as a calendar date (circular, coplanar, relative epoch); conflating
reachable with usable.

**Departure-burn accounting seam** (companion ADR 0030 and its CONTEXT.md; **unresolved**):
Two models charge the *same* Earth departure burn differently. `jovian_cycle_phasing.py` charges
**methalox** (Isp 380 s, `v_e` = 3.727 km/s); ADR 0009/0012 and `circular_resonance_impulse.py`
drive it with the returning stream through the **head-on nozzle** at `v_e` = 19-22 km/s at
`k` = 3, which is Isp ~1940-2240. The paper already carries both ends at line ~857 as the 4.0 yr
chemical doubling against 3.0 yr for the head-on catch.
**The seam need not be resolved to publish fly-and-park**, because the result is a *sweep across*
it, reported as a continuum in departure Isp. What the exhaust speed moves is growth per cycle
and the launch window, **not the clock**: the 30-yr chain picks ~3.00 S and holds phase under
either accounting, because a 2.09 S cycle has the better instantaneous rate and a worse successor.
**Two thresholds, and they are not the same number.** Fly-and-park clears its own exchange rate
at **Isp 1200 s** (3.13 km/s budget against a +1.04 km/s cost, ~3x headroom, winning at 17 of 30
phases). Continuous departures need **Isp 1900 s**. Both sit under the departure-nozzle ledger's
own 2214 s.
**Methalox is where fly-and-park fails, by about 5%**: 0.99 km/s of budget against the same
+1.04 cost, winning at 1 phase of 11 for a best gain of 1.002. It is not an idea chemistry nearly
supports.
_Avoid_: quoting either model's clock or `v_b` preference as settled; quoting the 1200 s gate for
the launch-window claim or the 1900 s gate for the exchange rate.

**Usable launch window is one contiguous arc** (computed 2026-09-08 in the grill; **owed back to
the companion repo, which publishes the fractions but not the layout**):
The usable phases do not scatter around the circle, they form a **single window** widening about
the sweet phase at every exhaust speed tested: **71 days of 399 at methalox, 241 days at Isp
1200, the whole 399 at 1900**. So the launch-cadence claim is "one window, 3.4x wider" rather
than "a set of windows", which is both simpler and the stronger operational statement.
_Avoid_: calling the Isp 1200 case continuous (it is 60% of phases, and only 1900 s reaches
100%); inferring **pad** throughput from it. This says when the vehicle may leave Earth orbit.
Whether it eases ground-launch congestion depends on fleet resupply, which **nothing in either
repository models**, and it must be labelled as inference wherever the paper says it.

**Ignition bill**: 84.41 MJ/kg for water with a 1% potassium seed at 15,000 K. Atomisation
(H2O -> 2H + O) is **59.7%**, translational 36.7%, vaporisation 3.5%, seed ionisation **0.13%**.
The intuition that ionisation dominates is wrong once you seed. Hand check for the AP-Physics
register: atomisation costs 9.50 eV per molecule, heating the 3 atoms to 15,000 K costs
`4.5kT` = 5.82 eV, so chemical beats thermal by 1.63x; **the two cross at 24,500 K**. _Avoid_:
quoting 68% or any figure above 63.2% (that is chemical *including* vaporisation); forgetting the
model charges **no** water ionisation, only the seed, which is what pushes the bill down (5% of
hydrogen ionised takes it to 94 MJ/kg and drops `k1` to 8.94).

**Ground-launch ledger**: 2/3 of liftoff is launcher propellant, 1/4 of the remainder is launcher
dry mass, so **1/4 of liftoff reaches intercept**, and the loop must return **1/15 of liftoff**.
Applied per flown cycle. **This is what actually binds**: across the 8x8 grid it is active in
**56 of 64 cells** while the plume window is active in **one**. 15,000 K is a low bar for a
46 km/s impact; what stops `k` is that the water has to be launched.

**The verdict (reversed 2026-08-20): lead with the nozzle winning, at matched recovery.**
Comparing a nozzle at `e1` against a plate at `f = e1`, both over the flown chain:

| matched `e = f` | nozzle | plate | ratio |
| ---: | ---: | ---: | ---: |
| 0.25 | 0.000133 | 0.000309 | **x0.4 (nozzle loses)** |
| 0.30 | 0.0295 | 0.0291 | x1.0 (tie) |
| 0.40 | 13.2 | 6.96 | x1.9 |
| 0.60 | 6.63e4 | 7,827 | **x8.5** |
| 0.80 | 2.83e7 | 7.83e5 | x36.2 |
| 0.90 | 3.35e8 | 4.79e6 | x70.0 |

The advantage **switches on near `e = 0.3`** and only then compounds; below it the launch floor
crushes `k1` onto the window's lower root (~0.1) and the nozzle degenerates toward a plate while
still paying to launch slug. What breaks the tie in the nozzle's favour is that **`f = 0.8` is
the least defensible number in either architecture**: it was swept at 3.2-16 km/s
(`sec:mass_fraction`) and this leg runs 45-65 km/s. Nothing rebounds elastically at 46 km/s.
Against that `f = 0.8` specifically the crossover is `e1 ~ 0.6` at a good departure leg, rising
to ~0.7 at a mediocre one, and the paper states that number so a skeptic has it.

_Note the currency_: the companion writeup's "~25%" is a **growth-rate** advantage
(e-foldings/yr). In delivered mass over the 28.3930 yr chain the same cells are x4 to x70.
Always say which.

**Assumptions the verdict rests on, both directions:**
- Wrong-way bulk drift the overtaking nozzle must reverse is only `1/(1+k1)` of the blob energy,
  **8.9%** at the fleet ceiling. Argues `e1 ~ e2`. **In the nozzle's favour.**
- The overtake puts impactor entry and exhaust exit at the **same end** of the vehicle, so each
  arriving PuffSat flies up the previous shot's plume. Argues `e1 < e2`, possibly strongly, and is
  **unmodelled**. ADR 0014 calls it probably the largest missing effect. The head-on leg has no
  such problem (in the front, out the back). **The one thing that could reverse the verdict, and
  the paper must name it.**
- Impactor and slug both given water's caloric properties. Fine for `k >= 3` (blob is >75% slug);
  the window's lower root is indicative only.
- Water fixed **by choice, not by optimisation**: the impulse law has no molar-mass dependence, so
  the model would always pick whatever is cheapest to ionise per kg (Xe) and reject what a real
  nozzle wants (Li).

_Provenance_: regenerated 2026-08-20 from the companion clone at `23ceb9b` via
`python -m src.two_leg_nozzle_sweep` (reproduces ADR 0014 exactly) plus per-cell
`price_chain_two_leg(...).total_growth`. **ADR 0014 concludes the opposite** ("the plate stays"),
because it compares against `f = 0.8` rather than at matched recovery; a draft **ADR 0015**
reversing the verdict on the same arithmetic is to be written locally and pushed by Seth.
_Avoid_: quoting the ~25% rate figure as if it were mass; claiming the nozzle wins below
`e ~ 0.3`; claiming one nozzle could serve both legs as-is (leg 1 must exhaust back out the
aperture the arrival entered, leg 2 passes front to back, so same coils, different topology).

**Watering It Down, Literally** (new `\subsubsection`, decided 2026-08-20 grill; sits *before*
the plate-vs-nozzle subsection because it establishes why the slug is water and seeded):
Why the growth cycle's slug is seeded water rather than a cheaper-to-ionise species. Four
arguments in this order, and the ordering matters because each one answers the objection the
previous raises.

**Bag material: high-strength polyethylene fiber** (decided 2026-08-21 grill). The film-mass
coefficient is `(3/2) x rho_f Rg T / (M sigma)`, so what matters is **specific strength**
`sigma/rho`, not strength. Handy identity: **tenacity in cN/dtex x 0.1 = specific strength in
MJ/kg, exactly**, so the Toyobo table reads off directly.

| fiber | GPa | g/cm^3 | MJ/kg | melts |
| --- | ---: | ---: | ---: | ---: |
| PBO (Zylon AS) | 5.8 | 1.54 | 3.77 | 650 C |
| **HS polyethylene** | **3.5** | **0.97** | **3.61** | **150 C** |
| p-aramid (HM) | 2.8 | 1.45 | 1.93 | 550 C |
| polyester (HT) | 1.1 | 1.38 | 0.80 | 260 C |

All four verified from `toyobo_zylon` (datasheet fetched and text-extracted, not recalled).
Coefficient at half the quoted strength for weave and seams: **`4e-4 x T`**, giving 1.3% of slug at
Jupiter and 4.2% at Earth.
- _Why PE and not the cheaper fibers_: HT polyester and HT polypropylene both sit at 0.7-0.8 MJ/kg,
  so the bag is 12.5 kg instead of 2.8. **Delivering the extra 10 kg costs ~$50k at the near-term
  fare; the feedstock gap between commodity fibers is ~$100.** Two to three orders of magnitude, so
  the paper argues the *gap*, not the prices (UHMWPE $20-60/kg, aramid ~$15/kg, polyester a few
  dollars -- volatile, and deliberately **not** cited in the paper).
- _Why the 150 C melting point is not the usual disqualifier_: the mist runs 306 K (Jupiter) and
  **328 K (Earth boost, the binding case), leaving 95 K of margin**. The cold-mist decision is what
  legalises PE here; a 1000 K bag would have melted it. Creep, its other standard objection, needs
  sustained load and this bag is loaded for seconds. `sanborn2014dyneema` measured SK76 from 1e-3 to
  1e3 /s with failure strength *rising* to a plateau near 1/s, so fast loading is favourable.
- _Why it also wins on chemistry_: pure C and H, so no halogen, sulfur or metal in the plume.
  Consistent with the existing chlorine, lead and halogenated-plastic refusals, and it is the **same
  polyethylene** already chosen for the airlock pipe and the pusher-plate slab. **Avoid a metallized
  barrier film** (aluminium in the plume, and the upper-atmosphere metals-loading objection); the bag
  holds only 4.9 kPa for seconds, so a plain PE liner suffices and weave and barrier weld as one
  polymer.

**Conductivity and the droplet-bag question go to `puffsat_impact_simulation`** (routed 2026-08-21;
spec in `todos/impact_sim_conductivity_and_bag.md`).

_Study 1, `sigma(T, rho, x_K)`._ Routed there because `sigma` is a **transport coefficient**, shares its
Saha solve with **opacity** (which that repo needs for the eight deferred radiation-transport items),
and consumes `T(t)`/`rho(t)` which that repo owns.
- **My "factor of 28" was mostly my own error.** The 569 S/m figure counted only the potassium seed and
  omitted **water's own ionisation, 5.9% at 15 000 K by Saha, which is 38x more electrons than the
  seed**. The seed is *not* the dominant electron source above ~5000 K. Corrected blend gives ~6 950
  S/m at 15 000 K against the ~15 900 that `Rm` = 361 implies, so 2.3x not 28x.
- **The residual gap is worst exactly at the cliff**: 68 S/m modelled against ~405 implied at 3000 K, a
  factor of 6, running in the direction that makes the cliff worse.
- **Both sides are weakly sourced.** The paper's `Rm` column has no published `sigma`, no stated `v` or
  `L`. My model is a two-limit series blend with `Q_en` = 1e-19 m^2 hand-picked and `ln(Lambda)` coming
  out **2.5**, marginal for Spitzer.
- **The validation data is already in `references.bib` and has never been used.** Open-cycle MHD power
  generation measured potassium-seeded conductivity at **2000-3000 K, which is the cliff regime**:
  `kerrebrock1964nonequilibrium`, `rosa1968mhd`, `messerle1995mhd`. Likely the best-measured physics in
  the paper. Kerrebrock also raises an unasked question: **if electron temperature decouples from gas
  temperature, the cliff may not exist.**
- _Paper corrected_: "four hundred times more conductive" conflated the **electron-density** ratio with
  the **conductivity** ratio. Conductivity saturates once Coulomb collisions dominate; the real factor
  is ~100x against the cool end.

_Study 2, the droplet bag._ **"Is the bag needed at all" is the wrong question.** The bag does two jobs
and only one depends on the leak:
- absorbing waste heat -- evaporates if the plume stays above 4000 K;
- **spreading 213 kg over 660 m^3 so the field can hold it -- survives regardless.** Without it the
  field goes 4.1 T at 5.4 m to 21 T at 1.8 m.
So the bag **survives as a different object**: a droplet cloud at 0.32 kg/m^3 in a container under **no
pressure**, where `eq:bag_film_mass` stops applying and the film is set by deployment and tear
resistance. `tab:bag_state` already has it two thirds to nine tenths liquid, so this is a smaller change
than it sounds. The hydro question that repo owns: **does a projectile couple to a droplet cloud the way
it couples to a vapour**, i.e. does `k = 8.5` still describe it, given droplet breakup time against the
~2.3 ms snowplow transit.
_Avoid_: saying the bag becomes unnecessary; quoting the electron-count ratio as a conductivity ratio.

**The field leak IS `1/Rm`, and it sets the seed window's floor** (found 2026-08-21 grill; the
sharpest result of the session). `tau_d / t_exp = mu0 sigma L^2 / (L/v) = mu0 sigma v L = Rm`, so the
share of stored field energy that soaks into the plume per expansion is **`1/Rm`**. `tab:seed_window`
has been carrying the leak schedule in its third column all along, and `tab:bag_state`'s 4.4% was being
quoted as if unrelated. **They are the same quantity.**

| plume T | `Rm` | leak `1/Rm` | vapour `x` at `E_B` = 12.2 GJ | |
| ---: | ---: | ---: | ---: | --- |
| 15 000 K | 361 | 0.28% | -0.21 | slug never finishes melting |
| 6 000 K | 400 | 0.25% | -0.22 | slug never finishes melting |
| 5 000 K | 238 | 0.42% | -0.17 | slug never finishes melting |
| 4 000 K | 76.5 | 1.31% | 0.05 | bag nearly unnecessary |
| 3 000 K | 9.2 | 10.9% | **2.48** | **exceeds the whole slug** |
| 2 000 K | 0.1 | 1000% | -- | field is gone |

**Amended 2026-09-05** (`aim_is_all_you_need` ADR 0027): the `x` column above is charged the whole
122 K-to-room-temperature ladder, 0.653 MJ/kg. Only warming the ice and fusing it **gate** melting,
0.570 MJ/kg; the liquid warming that follows competes with boiling for the same surplus. No verdict
in this table flips, but the onset threshold it is read against is the 0.570 gate, not the ladder.

- **There is a cliff between 4000 K and 3000 K and the design sat on it.** Above ~5% leak, `x` passes 1
  and what fails is not the bag but the **confinement**. My earlier "3.7 kg vs 31 kg" framing was too
  gentle; 31 kg is the 4.4% case, and 4.4% implies `Rm ~ 23`, between those two rows.
- **The window floor is ~3300 K, not 2500 K.** The paper said potassium condensation closes it; the
  leak binds ~800 K earlier. Recombination is unaffected (`tab:seed_window` has water recombined by
  4000 K). Paper corrected 2026-08-21; `tab:seed_window`'s caption now states the `Rm > ~25` bound too.
- **Seed fraction is not a lever.** For a trace alkali, Saha gives `n_e ∝ sqrt(n_K)`, so
  `Rm ∝ sqrt(seed)`. Lifting `Rm` at 3000 K to its 4000 K value needs **69x the potassium**, i.e. most
  of the slug.
- **This kills the need for an MHD code.** The `1/Rm` identity means the open question is a *residence
  time*, "how long does the plume linger below 4000 K while the field works", not a field solve. So:
  **`puffsat_impact_simulation` owes `T(t)`; `aim_is_all_you_need` does the quadrature.**
- _Unreconciled_: my electron-neutral estimate gives `sigma` = 569 S/m at 15 000 K against the ~15 900
  S/m that `Rm` = 361 implies. Factor of 28. Does not change the shape of the calculation.

**Repo routing for the whole backlog** (added 2026-08-21 to
`todos/companion_repo_calculations_2026-08-21.md`). Three destinations: `aim_is_all_you_need` for
closed-form solves and sweeps, `puffsat_impact_simulation` for anything needing the collision or
expansion actually simulated (densities, cooling histories, opacities, LTE checks), and a third bucket
for what neither has. Of the 13 items, 10 are `aim`, 3 are split, and **only ideal-MHD stability (RT /
minimum-B) has no home** and is the least load-bearing. The doc also disaggregates the paper's eight
deferrals to "the radiation-hydrodynamic calculation", which are really six different calculations
needing four different capabilities.

**Jupiter nozzle mass was wrong by 3-20x and is now a band** (found and fixed 2026-08-21 grill).
`sec:minimum_nozzle` computed the pulse for **one arriving kilogram** (reduced mass 0.9 kg -> 2.5 GJ)
and scaled Mini-Mag's 200 t by `2.5/340` to get **1.5 t**. The adopted anchor is a **25 kg impactor on
a 213 kg slug**, so `mu = 25*213/238` = 22.4 kg and the pulse is `(1/2) mu w^2` = **62.9 GJ**. The
paragraph predated the anchor and never followed it. The stated "factor of 189" against the near-Sun
477 GJ was also comparing a per-kilogram figure against a whole-pulse one; the real factor is **7.6**.
- Corrected linear Mini-Mag rule: **37 t**. Virial floor on `E_B`: **3.7-11 t** cold pulse,
  **10-30 t** hot. **We take the virial figures**, because the linear rule charges the magnet for
  energy that never pushes on it: the field stands off *pressure*, pressure is translation only, and
  dissociation plus ionisation carry none. Paper now says **tens of tonnes** and quotes the band.
- Downstream repaired: "5% of a 30 t craft and 1.5% of a 100 t one" -> **a tenth to a third of a 100 t
  craft**; `sec:mass_interest`'s "on the order of a tonne" -> "tens of tonnes". The Starship-class
  conclusion survives; the nozzle is a serious fraction of the ship rather than a rounding error.
_Avoid_: quoting 1.5 t; quoting the 189x factor; applying the linear Mini-Mag rule to `E_B`.

**Companion-repo calculation backlog** (`todos/companion_repo_calculations_2026-08-21.md`, written
2026-08-21). Inventories all ~43 new numbers from 2026-08-19..21, filters to **13 that belong in
`aim_is_all_you_need`**, gives the method for each, and lists the modules, `make` targets, regression
tests and ADRs owed. Three rules were decided in that grill:
1. **Filter: solves and sweeps only.** Code it if it is an iteration/sweep/root-find, or if a whole
   table's cells move when one upstream constant changes. Printed algebra and datasheet lookups stay
   in the paper with their existing cites.
2. **Code the chain in the paper's order with its hand-cuts intact**, so every digit reproduces and the
   cite is honest; add a *separate* fixed-point check that reports the convergence gap as a number.
   The three cuts are named in the doc.
3. **Citation mechanism: a reproduction line in each computed table's caption** naming a `make` target,
   extending ADR 0015's own "Reproducing:" convention. The 26 existing bare cites stay untouched.

**WRITTEN INTO THE PAPER 2026-08-21.** Everything in the three blocks below is now in
`templateArxiv.tex` and builds clean. Do not re-derive it; edit it.
- New `\subsubsection{A Needle Through Fog}` (`sec:needle_through_fog`), between `sec:watering_it_down`
  and `sec:two_leg_nozzle`: aperture argument, `eq:bore_from_length`, `tab:axial_bag`, plug sizing via
  `birkhoff1948lined`, ice vs PE on CO scavenging, corrected sublimation via `marti1993ice`, graded
  20 T -> 5 T field via `creely2020sparc`.
- `eq:bag_film_mass` now carries shape factor `F`; `eq:bag_shape_factor` added; coefficient restated as
  `2.6e-4 F x T` (was `4e-4 x T`, which had `F = 3/2` baked in).
- Line ~874's sweep claim replaced with the areal-density arithmetic (27 g of 213 kg).
- Field-energy invariance restated from `PV = n Rg T` rather than hand-waved; ionisation-thermostat
  paragraph added; `tab:bag_sizing` gained a **Field, ionized** column (M = 3.3 g/mol) beside the
  neutral one, and the caption now says it is a *volume* sweep, shape-independent.
- End of `sec:two_leg_nozzle`: the two topologies, the loss-cone-does-not-apply argument
  (`chen2016plasma`), `eq:rt_efolds` for Rayleigh-Taylor (`chandrasekhar1961hydrodynamic`), plug
  position per leg (56 T vs 7.6 T), one-geometry-two-current-sets, and the pre-compression argument
  against a reshapable magnet.
- `sec:two_leg_nozzle` line ~977 rewritten: closing speed vs impact speed, the slugged plate.
- New bib entries: `birkhoff1948lined`, `chen2016plasma`, `creely2020sparc`, `marti1993ice`.
**Two same-day reversals, both now in the paper. Do not re-derive from the earlier notes.**

1. **The plume state is set by energy AND Saha together, and the paper's 15000 K is the COLD-END
   answer.** An earlier note here said "four fifths ionised at 15000 K"; that was wrong, because Saha
   at 0.32 kg/m^3 allows only **5.9%** at 15000 K. The gas cannot dump 180 MJ/kg into a channel that
   narrow, so `T` climbs until it opens. Solving both together (two-line root find, energy
   `1.5 N(1+f) k T + f N chi` against dissipated minus ~54 MJ/kg vaporise+dissociate):

   | closing speed | dissipated | T | f | P/P0 | B/B0 | E_B |
   | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
   | 75 km/s | 265 MJ/kg | 26 200 K | 0.573 | 2.75 | 1.66 | 12.2 GJ |
   | 65 | 199 | 22 400 K | 0.371 | 2.05 | 1.43 | 9.1 GJ |
   | 56.53 | 150 | 19 400 K | 0.217 | 1.58 | 1.26 | 7.0 GJ |
   | 45.58 | 98 | 14 700 K | 0.053 | 1.03 | 1.02 | 4.6 GJ |

   **The last row validates the paper's original assumption**: at the coldest pulse the fleet flies,
   15000 K with negligible ionisation is the answer, not a guess. `tab:bag_sizing`'s two columns are now
   labelled coldest/hottest pulse, at 1.02x and 1.66x. Ignores O's second ionisation (35.1 eV).

2. **A slugged pusher plate gains NOTHING, so `tab:equivalent_plate` was fair all along.** An earlier
   note here said a slugged plate "may dominate both entries". Wrong. The plate is pushed by what it
   reverses: `(1+k) m x w/(1+k) = m w`. **The two factors cancel exactly**, so a slugged plate delivers
   `2 f m w`, identical to an unslugged one, because the slug was at rest and brought no momentum.
   Carrying 8.5 kg/kg buys a gentler impact and zero thrust. The nozzle benefits because it is pushed by
   the *dissipated* energy `(1/2) mu w^2` with `mu = mk/(1+k)`, which climbs with k. **The slug is the
   nozzle's food and the plate cannot eat it.** `sec:two_leg_nozzle`'s own `k -> 0` identity already said
   so. The 46 km/s objection to the plate therefore stands as originally written; what was corrected is
   that the *nozzle's* surface sees 11-23 km/s too, so its advantage is collecting the thermal three
   quarters, not surviving a speed the plate cannot.

- **`tab:bag_state`'s leak line is bracketed, not rescaled.** Stored energy is now pinned and rises to
  12.2 GJ, but the leak *fraction* is an integral over two regimes: while the fireball is at 26 000 K and
  57% ionised, water supplies ~1.7 e-/molecule against the seed's 0.005, so it is ~400x more conductive
  than the seeded estimate and barely leaks; the seed only governs later, in the 3000-6000 K window where
  `Rm` approaches 1. Which regime dominates is unresolved. **The upper bound matters**: hold the fraction
  at 4.4% and scale only `E_B` and waste heat hits 2.62 MJ/kg, 5/6 of the slug flashes, the mist runs
  352 K, and the bag is **31 kg instead of 3.7 kg** (PE survives with 71 K margin). The paper states that
  bound explicitly as a gate on the radiation-hydro calculation.

**The slug bag is axial with an ice plug, not a sphere** (decided 2026-08-21 grill). The bag is a
capsule ~23 m long with a ~3.0 m bore, not a 5.4 m sphere, and its front carries a solid ice plug that
the compact impactor hits first.
- _Why the bore matters_: standoff volume is invariant (`E_B = P V`, and the field stands off
  `(gamma-1)E/V`), so `r_bore = sqrt(V/pi l)` falls as `l^(-1/2)` while REBCO tape goes as `B r l`,
  i.e. as `l^(1/2)`. **Bore and conductor trade inversely, one for one: halve the bore, double the
  tape.** Virial structure mass does not move at all, because contained energy does not move.
- _Where we stop_: **`l` = 23.7789 m, V = 660 m^3, bag radius 2.97236 m, aspect 4**
  (P20 accepted 2026-09-05, ADR-0014). Cross-section 27.7557 m^2, density 0.322727 kg/m^3.
  Costs +21% tape relative to the equal-volume sphere in the cylindrical sizing model.
  **The winding is not the bag.** It flares 3.50 m -> 5.17 m to follow the plume's bounding flux
  tube (ADR-0011 as amended by ADR-0012's cap), so `sec:mass_interest`'s "coils ~7 m across clear
  a Starship fairing assembled" holds at the chamber and **fails at the 10.3 m flare exit**. The
  paper now concedes this: the magnet ships in sections and is joined once.
- _Film cost_: pressure-vessel film mass is `F rho_f P V / sigma` with `F` a pure shape number,
  **1.5 for a sphere (hoop stress `PR/2t`) and 2.0 for a cylinder (`PR/t`)**. Capsule
  `F = (2L+2r)/(L+4r/3)`. At aspect 4, `F` = 1.9091 in the existing cylinder-bore/capsule-film approximation.
  **Earth pressure film 4.85 kg -> 6.17 kg, +1.32 kg on a 213 kg slug.**
  The design membrane is 444.09 m^2; 12.7 um polyethylene weighs 5.19 kg.
  The whole penalty is bounded at 4/3 and most of it is paid by aspect 2.
  **The `P V` form is a trap, and it caught R14** (2026-09-05, `aim_is_all_you_need` ADR 0029).
  `P` and `V` are not independent factors here. The film sizes a vessel holding `P V = n R_g T`, so
  a bigger bag drops `P` by exactly what it adds to `V` and the product does not move. R14 adopted
  the sim's 672.9 m^3 over 659.6 and scaled `tab:axial_bag`'s film column by the 1.0202 volume
  ratio; multiplying the model by that ratio reproduces every cell R14 printed, to the digit, which
  is what identifies it as a double charge rather than a disagreement. The V-free form is
  `eq:bag_film_mass` itself, `F x rho_f R_g T / (M sigma)`, and the paper's own derivation says
  every factor of `R` cancels.
  _Avoid_: scaling any film mass by a volume ratio. Volume reaches the film only through `T`, since
  the same vapour spread 2% thinner saturates 0.4 K colder and the film is linear in `T`. That is a
  tenth the size and runs the other way, taking the sphere row from 4.850 to 4.844 kg.
- _Water cost: zero_. `k = 8.5` comes from the ignition window and the launch budget, not bag shape.
- _Why a compact impactor cannot hit a mist_: the column's axial areal density is only
  `0.322727 x 23.7789` = **7.7 kg/m^2**. A 5 cm ice rod is 3183 kg/m^2. Newtonian drag over the full traverse
  is `rho v A l` = 3300 kg m/s against its 1.4e6, so it loses 0.24% of its momentum and exits, having
  swept **58 g of the 213 kg**. A rod is a needle through fog.
- _So the plug is load-bearing, not a convenience_. The alternative is a footprint-matched puff, which
  needs an aperture as wide as the bore, so the front is a hole the size of the chamber and there is no
  forward mirror at all. **Compact impactor: 0.15 m aperture into a 3.0 m bore, 0.25% open.** Given
  `tab:two_leg_growth` makes `e2` 0.6 -> 0.8 a factor of 14, this dominates every other consideration here.
- _Plug sizing_: **~1.5x the impactor mass, ~37.5 kg**, not half. Hydrodynamic penetration is
  `P = L sqrt(rho_p/rho_t)`, which for ice on ice is just `L`, so the plug must be at least as thick as
  the impactor is long; at matched footprint that means at least as massive. A 25 kg ice rod at 0.1 m
  radius is 0.87 m long.
- _The plug is thermally free_: it may melt, just not vaporize, so it absorbs 0.653 MJ/kg on the way to
  liquid. 37.5 kg soaks 24.5 MJ of the 138 MJ waste-heat bill, a sixth of it. From Earth storage vapor
  ends at 28.9 kg against a 39.3 kg baseline and the mist falls from 316 K to 310 K; PE keeps 113 K of
  melt margin. From cold storage the plug is what keeps the bag dry at all.
- _Not a foam column_: the mist runs 0.322727 kg/m^3 and the closed-cell PE foam of `sec:icy_puffsat` is
  30 kg/m^3. Two orders of magnitude, so it is mist or nothing.
- _Impactor material_: mostly ice, PE structure; it is a hybrid and the question is the ratio. PE-only
  costs ~9% of the ignition budget, because 25 kg of PE is 1.78 kmol of carbon that scavenges an equal
  1.78 kmol of oxygen into **CO, whose 11.1 eV bond is the strongest in diatomic chemistry** and will
  not release it on a 100 us expansion, so 15% of the slug's oxygen never re-forms water and that much
  of the 50.4 MJ/kg recombination loan is never repaid. Ice's only problem is cruise, and the corrected numbers are
  (an earlier note here understated the shaded loss by many orders of magnitude): a bare ice body at
  1 AU cools until `sigma T^4 + L * sublimation` balances 340 W/m^2 averaged, which lands at **194 K**,
  where ice's vapour pressure is 0.064 Pa (`marti1993ice`, log10(P/Pa) = -2663.5/T + 12.537) and free
  evaporation runs **7.4 kg/m^2/day**. A 25 kg rod is ~55 kg/m^2, so bare it is gone in a week. Behind
  the detachable sunshade of `sec:lox_puffsat` at 150 K it loses **0.58 kg/m^2 over a two-year cruise,
  ~1.4% of the rod**. Affordable, not free.
- _You cannot funnel a wide puff into a narrow bore_. The arriving cloud is cold neutral droplets at
  122-200 K with `Rm` far below 1. The field has nothing to grip until after the collision.
- **Graded field, adopted 11 T peak and retained 5 T exit** (P18/P19 accepted;
  ADR-0013 amends ADR-0012). The protected surface is the graphite liner, not the
  bag. The companion model uses a constant 3.50 m wall, giving contact at 3.83 m
  and demand 10.95 T at the binding 1.9x spreading bracket. Since the liner flares
  outward from that radius, this is conservative for contact within the prescribed
  front/profile model. The sound-speed-only result is 7.29 m / 8.25 T and is not
  the adopted cap. These are not the old paper-side full-flare 4.14 m / 10.59 T
  and 8.50 m / 7.71 T estimates.
  Swept area is capped at the bag boundary by construction; changing the reporting
  wall radius does not alter the front integration. Lateral feedback remains unresolved.
  **Retain 12 T reference calculations and mass budgets.** The 3.50--5.17 m
  envelope, conductor prices, expansion efficiencies, and coil-count sweep have not
  been rerun at 11 T or ADR-0014's corrected bag dimensions. P13 corrects the old
  claim that the 12 T cap leaves efficiency unchanged: eta_exp improves by
  0.045--0.155 over the 20 T reference cases. Original 0.88x energy and 0.96x tape
  figures remain first-order estimates for 12 T, not new 11 T savings.
  P19 confirms that 5 T was also bag-referenced standoff. Whole-profile regrading
  is deferred; the unrun 8.44 T peak / 2.87 T exit option and its `B ~ 1/r`
  conductor savings are not adopted. Source: impact sim `6fe8cf3`, P18/P19,
  `front.py`, ADR-0042.
  _The old entry, for reference_ (decided 2026-08-21 grill):
  Front-loading the collision means the fireball sweeps the mist as a snowplow, and the pressure it
  needs stood off falls down the bore: ~20 T at 1 m, 12 T at 3 m, 9 T at 6 m, 5 T at exit. That is a
  genuine converging-diverging magnetic nozzle profile, which the spherical bag never gave. Stored
  energy is dominated by the long low-field section, so a 20 T nose costs far less than 20 T everywhere,
  and 20 T is the SPARC-class anchor already adopted above.
**The winding flares to follow the plume; `eq:bore_from_length` sizes the bag, not the magnet**
(decided 2026-09-04 grill on the impact sim's nozzle answers; ADR-0011). `A/A*` is one ratio read
two ways: `alpha_exit = 1 - (1-alpha_0) B_exit/B_start` converts the pancake, and
`r_exit/r_start = sqrt(B_start/B_exit)` is the radial spread that buys it. **They are the same
number, so conversion cannot be bought without spread.**
- _The flare_: `r(z) = 3.02 sqrt(B_chamber/B(z))` + clearance. At ADR-0012's 12 T cap that is
  **3.50 m at the chamber to 5.17 m at the throat**, costing **1.18x conductor** against the
  original straight 3.5 m winding at the flown field (5.2/8.5 t at 500 A; the "under about 8 t"
  floor becomes ~9.4 t; flare exit 10.3 m across). At the uncapped 20 T profile it was 6.50 m and
  1.50x. **The cap and the flare pull against each other and the cap wins**, because a lower
  chamber field expands the flux tubes less. The bag stays a 3.02 m x 23 m cylinder **inside** it.
- _Why not a cylinder_: 12.9% of the plume, ~27 kg/pulse, misses a straight 3.5 m winding against
  the **4.9 kg/pulse (2.3%) the ablation budget books**. A 6x rebooking.
- _Why not regrade the column field_: self-defeating. Flat 20 T buys `eta_geom` 0.67-0.83 but
  throws **58.2%** of the plume at the coils and costs 4.92x field energy (49-148 t structure,
  past the 37-112 t ADR-0009 refused).
- _`eta_geom` with both terms_: **0.48-0.64**, across P3's 1.44-2.00 exit-radii detachment
  window (it peaks at 0.53-0.66 at 0.95 radii, but detachment is not ours to choose). Clears
  `sec:mass_interest`'s floor `1/sqrt(1+k)` = 0.324; **does not reach the swept 0.775**. The
  impact sim's P2 quotes 0.70-0.88 because `jet.py` models conversion without the spread, and
  lumps one `A/A*` over mass that is really spread along the column. Probes:
  `todos/fluxtube.py`, `todos/station_weighted_alpha.py`, `todos/regrade_full.py`. First order
  (paraxial field, uniform mass, one detachment surface) and owed back to the companion repo.

**A diverging section still pushes on the vehicle at high supersonic Mach** (checked 2026-09-04,
user's question; settled, no companion ask needed). The worry is that flow at Mach 5-7 is "moving
too fast to push". It confuses two things: **supersonic means information cannot travel upstream,
which says nothing about local normal stress.** A wall feels static pressure wherever gas touches
it. The axial force has a closed form with no angle in it: `dF_z = p sin(th) 2 pi r ds` with
`ds = dz/cos(th)` collapses to **`p 2 pi r dr`, pressure over the projected annulus**, which is
why vacuum bells are large.
- _Numbers_, from the magnet-exit state (0.7 MPa, 0.0251 kg/m^3, Mach 2.35, `mdot` 27 800 kg/s so
  238 kg takes 8.6 ms): at the binding 7.45x expansion the wall collects **45.8 MN**, the exhaust
  leaves **19% faster**, and the section delivers **16% of the total impulse** at an exit Mach of
  5.79. Confirmed two ways, pressure integral and momentum balance, agreeing to the digit.
- _Vacuum helps rather than hurts_: separation needs wall pressure to fall below ambient and there
  is no ambient, so a longer bell always adds, with diminishing returns and no cliff.
  Over-expansion is a sea-level problem. `Kn` ~ 1e-6 at the 12.8 m exit, so continuum throughout.
- _Do not add this to `eta_geom`'s gain_. Wall pressure is **how** a diverging section converts
  thermal motion to directed motion, so the 16% and the rise in `alpha` are one effect counted
  twice. The same holds for R11's magnetic extension, where the force lands on the coils as
  `j x B` instead of on a bell as `p`.
Probe: `todos/bell_thrust2.py`.

**`mu` conservation is the wrong framework for this plume; it is a collisional fluid**
(2026-09-04). `jet.py`'s docstring lists its own assumption, "the expansion is collisionless
enough for `mu` to mean anything", and the paper's own Knudsen number violates it: **`Kn` = 5e-8
in the bag, 4e-7 at the magnet exit, 1e-6 at an extension exit**, and this `CONTEXT.md` already
says "mean free path ~1 um against a 3 m bore ... **this is a continuum fluid**". `mu` is a
single-particle invariant; a parcel here collides millions of times crossing the bore.
- _The right model_ is an ordinary de Laval nozzle with **magnetic walls** (the paper's own
  "walled by field rather than fenced by it"). At `beta` = 0.013-0.073 the field exceeds plasma
  pressure 15-75x, so it *is* the wall. **This changes no hardware.** The flare stays magnetic and
  nothing physical is needed at the throat.
- _Gas-dynamically_, `eta_geom = cos(theta)/sqrt(1 + 3/(gamma M^2))`:

| station | Mach | thermal left | spread term | `cos th` | `eta_geom` |
| --- | ---: | ---: | ---: | ---: | ---: |
| magnet exit, no extension | 2.35 | 24.6% | 0.868 | 0.883 | 0.767 |
| extension 2.63x | 3.83 | 10.9% | 0.944 | 0.983 | **0.928** |
| extension 7.45x | 5.79 | 5.1% | 0.974 | 0.983 | **0.958** |

- **The binding term is divergence, not speed spread.** At the magnet exit the spread term is
  already 0.868 and `cos th` = 0.883 from free fanning is what costs.
- _Supersedes_ the 0.48-0.64 above, which was built on `mu`. Sent back as a correction to R1.
Probe: `todos/framework.py`.

**Everything computed so far is a WATER slug; argon pays neither toll** (2026-09-04, user's
catch; ask is R13). `sec:watering_it_down` line 1074: "A bare atom has no bonds to break, so the
50.9 MJ/kg goes away and so does the toll `eq:eta_chem` charges for it." Ionisation is not a
frozen toll either (three-body recombination in nanoseconds against a ~100 us expansion), so
**`eta_chem` -> ~1 and `eta_jet` = `eta_geom`**.
- **Water's cold leg is capped at `eta_jet` <= 0.731, below the paper's own 0.775 target, before
  any nozzle exists.** The cold-leg shortfall is a chemistry problem, not a nozzle problem.
- With argon the binding cold leg clears at **0.928 on the short 10.9 m extension**; R11's 30.3 m
  case is not needed.
- _The risk that could take it back_: argon is 25 mol/kg against dissociated water's 166, so the
  plume "runs hotter and further ionized". Radiated power goes as `T^4`, and that share multiplies
  every liner-load and gate figure (R12's shield count, the ablation booking, P5's margin).
  **Argon may swap a chemical constraint for a thermal one.** Unquantified.
_Avoid_: quoting `eta_chem` = 0.731/0.910 or `tab:mass_interest_growth`'s "0.78 to 0.91" without
saying they are water figures.

**The throat field can be reduced by moving the throat downstream** (raised 2026-09-04 by the
user; ask is `docs/nozzle_replies_to_impact_sim.md` R11, and **it may retire R8**). P9 forbids
flaring the same 23 m harder, because that weakens the field where the snowplow is still at the
wall. **It does not forbid extending the magnet past the bag**, where the front has stopped
sweeping mass and its pressure is falling. The 5 T exit field is a *collision* requirement;
nothing downstream of z = 23 m inherits it, and the field is already 15-75x over-strength for the
expansion there.
- _What it takes_: `M_A = M sqrt(gamma/2) sqrt(beta)` climbs on both factors as the flare opens,
  so `M_A` = 1 needs only **2.63x more area on the hot leg (10.9 m extension, 34 m total, 1.32x
  conductor)** and **7.45x on the binding cold leg (30.3 m, 53 m total, 1.61x)**. Peak field
  stays 12 T; the extension runs under 2 T so it is cheap per metre. The 3x spread between legs
  is entirely P3's `beta` range.
- _What it buys_: not conversion (`alpha` 0.86 vs 0.91) but **where detachment happens**. Free
  fanning releases the plume along field lines spreading at 40-50 deg (`<cos th>` = 0.665); a
  controlled 15 deg flare releases it pointed the right way (`<cos th>` = 0.983).
  **`eta_geom` 0.72-0.91, `eta_jet` hot 0.66-0.83, which clears the swept 0.775 for the first
  time.**
- _Why it may retire the staged bell_: it is the bell's benefit obtained magnetically, with no
  wall for plasma to push against. It also **restores `sec:jet_efficiency`'s original claim that
  detachment happens inside the nozzle** (the claim was right, the number was wrong).
- _The gate_: our figures are 1-D isentropic area-Mach with a cone-average divergence, cruder
  than the flux-tube model behind the 0.48-0.64. **Nothing enters the paper until R11 lands**
  (user's call). Probes: `todos/extension.py`, `todos/extension2.py`.

**The staged nozzle is parked, gated on the sub-Alfvenic wall question** (raised 2026-09-04 by
the user; ask is `docs/nozzle_replies_to_impact_sim.md` R8). Magnet to `A/A*` = 4 where the
collision needs it, then a **physical bell** outside the winding for the rest of the expansion,
with no field to weaken and no coil to protect.
- _Why it is worth asking about_: it targets the **divergence** term, which is the largest single
  loss in the chain. `<cos theta>` = 0.63-0.70 across the detachment window is what holds `eta_geom` to
  0.48-0.64 against a directed bound near 0.88. A bell sets exhaust direction mechanically and does not care what the
  field lines do. Chemical bells run ~0.98 divergence efficiency at 15 deg half-angle.
- _Thermally it is nearly free, and this is the non-obvious part_. Pulses are ~1 ms at 2 Hz, so
  **duty cycle 0.2%** and the time-averaged flux is 500x below peak. Pyrolytic graphite conducts
  1700 W/m/K along its sheets, so a 1 ms pulse penetrates 1 mm and the surface spike from
  44.6 MW/m^2 is **31 K**. **Steady-state radiative balance is the wrong model for a pulsed wall
  and overstates the load by ~1000x.**
- _Where the bell can start_: **7 m radius**, one metre outside the magnet exit, survives both the
  frozen and equilibrium branches. Only the exit plane itself (6.03 m) is too hot, and only on the
  equilibrium branch. A bell **holds** the plume rather than chasing it; left alone the plume
  follows flux tubes to 26 m radius by detachment.
- _The gate_: at the magnet exit the plume is **sub-Alfvenic** (`M_A` 0.35-0.58) and low-beta
  (0.013-0.073), so a wall there pushes against the field, not against free plasma. Favourable
  argument, uncalculated: a wall keeps `rho` up, which lowers `v_A` and raises `M_A`, so it may
  detach the flow sooner. **Nothing enters the paper until R8 lands** (user's call, 2026-09-04).
Probe: `todos/staged2.py`.

**A magnetic trap is judged by depth, not existence, and P1 sets the threshold** (2026-09-04).
`sec:jet_efficiency` claims the graded profile "has no local minimum anywhere along it, so nothing
can sit in it". The impact sim's P8 tests that off-axis and answers ">= 36 coils". **Both ask the
wrong question.** A mirror holds a particle when `sin^2(theta) > 1/R`, so the threshold is
`R > 1/(1 - alpha)`:
- isotropic (`alpha` = 1/3): traps once `R` > **1.50**
- **the measured column (`alpha` = 0.088): traps once `R` > 1.096**

**The pancake is trapped by a mirror five times weaker than an isotropic plume would need**, so
P1 makes P8 harder and neither item notices. Against it, shallow ripple minima are harmless: on
our own crude re-run over the flared, capped winding, 18 coils leaves one minimum at `R` = 1.023
(below threshold, traps nothing) and 24 coils is clean. **Take the criterion, not our count** (our
per-coil currents are a rough local-field match, not a winding solve). Asked back as R10.
_Carry a caveat_: the 12 T flat shelf has **no background gradient to swamp ripple**, so minima
will appear there that the old steep chamber profile suppressed. Believed ~1e-4 deep, but that is
exactly where depth has to be checked rather than assumed.
_Avoid_: stating the residence claim as "no local minimum" (it will be literally false on a flat
shelf, and harmlessly so); quoting P8's ">= 36 coils" as current (it predates the flare and cap).
Probe: `todos/winding.py`.

**The same coils must present opposite mirror topologies on the two legs** (2026-09-04, from
P10 and R10 together). `sec:two_leg_nozzle` already says the legs "ask for opposite shapes", and
the mirror-ratio threshold makes that quantitative. The threshold is `R > 1/sin^2(theta)` and the
plume's pancake sets `sin^2(theta)`:
- **leg 2, departure** (a tube open at both ends): ripple minima **trap** the plume once
  `R` > 1/(1 - alpha) = **1.096**. Unwanted. This is R10's criterion.
- **leg 1, overtake** (a cup closed at the ship end): the mirror **reflects** the plume once
  `R` > **1.449** with the drift included. Wanted, and P10 confirms it is not binding, since the
  graded column approaches nothing like that.

Same hardware, re-energised per leg, so a mirror ratio is a defect on one leg and the mechanism
on the other. P10's arithmetic checks: `f_d` = 0.10526, `sqrt(f_d)` = 0.3244 against a 0.529
baseline, so the nozzle supplies 0.205 head-on and 0.853 on the overtake, **4.17x the work**
(the impact sim says 4.18).

**Historical R14 adoption, superseded by ADR-0014/P20 on 2026-09-05.**
The current geometry is 660 m^3 / 23.7789 m / 2.97236 m radius. The impact simulation
keeps its original 3.0 m radius and 23.8 m length until rerun.

**Column length resolved in the companion repo's favour** (2026-09-04, the answer document's
"unreconciled; pick one"). The paper *states* 23 m and 660 m^3, which give a 3.022 m bore and a
28.7 m^2 cross-section. But the paper *quotes* a **3.0 m bore and 28 m^2**, and those match the
sim's **23.8 m / 672.9 m^3 exactly** (r = 3.000 m, 28.3 m^2). So the paper is internally
inconsistent by ~2% and its quoted bore is already the sim's. **Adopted 2026-09-04 and applied
to the paper**: 23.8 m, 672.9 m^3, 3.00 m bore. Aspect also favours it (3.97 against 3.81 for
the stated pair, against a quoted "4"), so **three round figures the paper prints match the sim's
pair and none match its own stated pair**. Also `k` = **8.52**, not 8.5 (213/25).
_Owed back_: `tab:axial_bag` was recomputed **by hand** from the model its caption states, after
reproducing all five printed rows at 660 m^3 as a check (`todos/bag_geometry_converge.py`).
`make bag-state` in the companion repo has not been rerun, so table and generator now disagree.
Pair it with the `tab:bag_state` recompute already owed. Sent as R14.

**P3's `M_A` correction is confirmed, and its consequence is blocked on R8** (2026-09-04).
The paper's `M_A` = 1.63 / 2.06 divides the **exit speed** (10.8 km/s) by an Alfven speed built
from the **bag** density (0.323 kg/m^3) and field (4.1 T). The plume thins 13x between those
states and `v_A ~ rho^-1/2`, so the figure is inflated by `sqrt(0.323/0.0251)` = 3.59; the sim's
0.58 x 3.59 = 2.08 reproduces the printed 2.06. The paper's "two routes agree to 3%" is not
corroboration either: working standoff for rho = 0.323 at 15165 K and `Mbar` = 5.7 g/mol gives
4.24 T, so `tab:bag_sizing`'s 4.1 T **is** the standoff field and both routes evaluate `beta` = 1.
**`M_A` never crosses 1 inside the column; the crossing is 1.44-2.00 exit radii downstream.**
_The consequence, deferred_: the paper retires **magnetic drag** from `eta_geom` on that number
(line 2291, citing Hoyt). Magnetic drag and R1's divergence term are the same physics, so if the
plume stays field-guided the retirement is void and the term costs `<cos theta>` = 0.63-0.70. A
physical bell would make the retirement genuine. **Nothing changes in the paper until R8 lands**
(user's call). _Avoid_: listing "magnetic drag" and "divergence" as separate contributions to
`eta_geom`; they are one term.

**Paper edits applied 2026-09-04** (the unblocked half of the impact sim's P1--P10). Six landed
in `templateArxiv.tex`, and the paper builds:
1. **Line 773 and `sec:minimum_nozzle`**: the `1e-4` gate is attached to the **near-Sun** burn,
   the Jupiter chain is given its own (79x less power, about **5%** of pulse energy allowed), and
   the sky fraction is corrected from the bag's tenth to the bore's **88%**, with the ceiling set
   by **graphite at 3900 K (13.1 MW/m^2)** rather than structure at 1500 K. The passage now warns
   that mixing the two pairings is wrong by 8x either way.
2. **`sec:watering_it_down`, the liner**: a vacuum gap is not insulation. Bare surfaces put the
   shell at liner temperature (~2600 K against aluminium's 933 K), so the gap wants **low
   emissivity**, with refractory foil shields if `phi` turns out high.
3. **`eq:reflection_baseline`**: a new paragraph states `alpha` = **0.088** for the flown column
   against 0.360 for the sphere, names shape as the whole cause, and says a launch-fairing choice
   retired the isotropy the baseline rests on. Drift-free baseline 0.46 -> **0.237**.
4. **`sec:two_leg_nozzle`**: the drift enters with opposite signs, so the overtake nozzle does
   **four times** the work; plus the mirror-ratio reading (1.45 wanted on leg 1, `R` = 1.10 a trap
   on leg 2).
5. **The liner-ablation appendix**: the 42.6 MW intercepted flash is corrected to about
   **380 MW**, the conduction figures move to 878 kW/m^2 and a 1254 K gradient, and the shell
   comparison from 3x to **28x**. Flagged as an upper bound pending `phi` (R12).
6. **`k` = 8.52** noted once where the slug ratio is defined, with 8.5 kept as the round figure.

**A second pass landed later the same day**, clearing the decided-but-unapplied backlog:
7. **Historical bag adoption, superseded by ADR-0014/P20:** 23.8 m / 672.9 m^3 / 3.00 m bore. `tab:axial_bag`'s sweep
   volume and all five rows move; the design row becomes 23.8 m / 3.00 m / 449 m^2 against the
   old 23 m / 3.02 m / 437 m^2. The last stray "23 m" and its 7.4 -> 7.5 kg/m^2 areal density go
   with it.
8. **ADR-0012's 12 T cap** is now in `sec:needle_through_fog`. The graded profile is derived as
   before, then flattened upstream of wall contact into a 12 T shelf meeting it at 3.12 m, with
   the front-geometry reason stated and the 1.6--1.9x bracket answered. The SPARC 20 T citation
   is demoted in place to a comfort rather than a requirement.
9. **ADR-0011's flare** is now in `sec:minimum_nozzle`. `eq:bore_from_length` is said outright to
   size the bag and not the magnet; the winding runs 3.50 m -> 5.17 m; conductor moves 4.4/7.2 t
   -> **5.2/8.5 t**, the 300--1000 A band 7.3/2.2 t -> **8.6/2.6 t**, and the floor "under about
   8 t" -> **about 9.4 t**.
10. **The fairing claim** is conceded where the row is chosen: 7 m across at the chamber fits an
   8 m fairing, the 10.3 m throat does not, so the magnet ships in sections.

_Not applied, deliberately_: everything gated on R8, R11 or R13.

**P5's passive-structure gate is right at the bottom line and wrong twice on the way there**
(2026-09-04). The gate at line 1584 sizes what the structure can shed as "a few thousand square
meters at **1500 K**, about a gigawatt". Two inputs are not the flown hardware:
- **1500 K** is an alloy temperature, but the surface taking the flash is **pyrolytic graphite,
  good to 3900 K**, which sheds 13.12 MW/m^2 against 1500 K's 0.29. **45x looser.**
- **"a tenth of the sky"** is the bag's solid angle, but the liner wraps the plume at **82%**
  (ADR-0011's flared bore). **8.2x tighter.**

Over the real 631 m^2 wall the ceiling is **8.28 GW**, the Jupiter gate product is **6.6e-2**, and
the allowed radiated share is **8.0%**. The impact sim's P5 gets 7.95% by scaling the near-Sun
1500 K ceiling with burn power at a tenth of the sky. **The two errors cancel to within 1%**, so
its number is usable and its reasoning is not. _Avoid_: fixing one of the two and not the other,
which lands you off by 8x in either direction. Probe: `todos/gate.py`.

**The liner and the shell are radiatively coupled across their gap; not touching is not enough.**
`sec:watering_it_down` stands the pyrolytic graphite liner off the aluminium shell "on pads of
insulating carbon foam with a vacuum gap over the rest". A bare vacuum gap between two blackbodies
is not insulation, it is a clear radiative path, and the shell equilibrates at **liner
temperature**: 1033 K at the coldest case and 2607 K at the hot pulse, against aluminium's 933 K
melting point. **The shell melts in every case, including the coldest.** The fix is emissivity,
not separation. Blocking the backside makes the liner run hotter (3101 K rather than 2607 K at
the hot pulse, still inside graphite's 3900 K), which tightens the requirement to
**`eps_eff` <= 0.0082**. Conventional MLI is useless here: **aluminised mylar dies at ~400 K and
the shields themselves run 2206-2888 K**, so they must be **polished refractory foil** (tantalum
3290 K, tungsten 3695 K, or graphite). How many depends on `phi`:

| branch | `phi` = 0.1 | 0.2 | 0.5 | 1.0 |
| --- | ---: | ---: | ---: | ---: |
| cold, 1.2% | none | none | none | none |
| hot, 3.6% solved | none | none | 1 | 3 |
| hot, 13.25% equilibrium | 1 | 2 | 5 | liner itself ablates at 4300 K |

The alternative is a refractory **shell**: tungsten survives a bare gap at 3101 K but is 7.1x
aluminium's density, and molybdenum (2896 K) is marginal. The foil stack is far lighter.
_Avoid_: reading "the liner does not touch the shell" as thermal isolation; calling the gap
filler MLI (it is refractory foil). Probes: `todos/liner.py`, `todos/shield.py`.

**`tab:bag_state`'s flash row is a bag number and lines 2740/2743 reuse it for the liner**
(the answer document's P4, resolved 2026-09-04). The row books "1.2% radiated, a tenth of the sky"
and is **correct for the bag**, a film balloon in free space with structure over a tenth of its
sky. The **liner wraps the plume**: an optically thick plume filling the bore can only radiate out
through the wall (436 m^2) or the two open ends (57 m^2), so the wall covers **88% of the sky**,
82% once ADR-0011's flare widens the exit. So the booked **42.6 MW is low by ~8.8x on solid angle
alone**, and P4's second route (~453 MW) is the right order. Every corrected figure carries `phi`,
the share of total radiated energy emitted **before the plume clears the exit plane**, which is
computable from `data/results/cooling_history.csv` and is not yet asked for.
_Still open_: how the paper states this. Probe: `todos/p4_ledger.py`.

**Current nozzle terminology (P22 accepted).** `chamber` is the strong-field end;
`exit` is the downstream weak-field opening. `throat` is reserved for the sonic
station, where flow reaches sound speed, at the chamber in the expansion model.
This supersedes R7's proposed `throat = exit` convention. The companion renamed
`expansion.THROAT_RADIUS` to `CHAMBER_RADIUS`; historical entries above may retain
the earlier vocabulary. The paper now uses `exit` for the downstream hardware and
`chamber` for the ship-facing pressure-support region. Chemical-thruster sonic
throats retain their standard name.

_Avoid_: quoting `tab:bag_sizing`'s single 4.1 T as if the field were uniform; calling the impactor a
compact rod that "sweeps the column" (it does not, the plug is what couples it); reading a smaller bore
as a lighter nozzle (it is bought with conductor, at one-for-one); **reading `eq:bore_from_length`'s
`r` as the magnet's radius (it is the bag's); quoting `eta_geom` = 0.70-0.88 from the impact sim's
P2 (it omits the divergence term and the station weighting); calling the graded field's `A/A*`
a free lever (every factor of conversion is a factor of sqrt in radius)**.

**The nozzle field is static within a pulse** (decided 2026-08-21 grill, user-asserted and
self-consistent with the paper). No travelling, switched or otherwise time-varying coil topology is
admissible. Two independent reasons:
- _The paper already forbids it_. `sec:watering_it_down` (line ~828) builds the whole quench
  architecture on keeping induced current **out** of the superconductor: a copper shell between plume
  and coil takes the transient, the coil supplies a persistent seed field, per
  `romanelli2017pulsed_fusion_nozzle`. A deliberately time-varying coil field breaks that design.
- _Energy_. At 4.4 GJ stored, changing even a tenth of the topology per pulse at 90% switching recovery
  dumps 44 MJ, and at 20 K each absorbed joule costs tens of joules of plant, so ~1 GJ of plant energy
  per pulse against a 39 GJ pulse. Persistent-mode fields cost nothing to hold.

**Leg 1 (overtake) is a reflector, not a nozzle** (decided 2026-08-21 grill). Follows from the static
constraint. The blob's net momentum is prograde and the exhaust must leave retrograde, so the device
reverses momentum rather than expanding it; `sec:two_leg_nozzle` already half-says this (`k -> 0` in the
overtake gives exactly 2, a perfect bounce).
- _Only one static topology works_: a **single-ended mirror at the ship end**. A two-ended static mirror
  leaks preferentially through its weaker end, and on leg 1 that has to be the ship end once enough
  field sits at the far end to contain the birth fireball, so the plume would vent onto the bus. This is
  a loss-cone geometry argument, not a mass argument, so it survives better numbers.
- _Field needed_: the blob reaches the mirror having swept the column, 238 kg at 5.88 km/s through
  660 m^3. Static 10.6 MPa, ram-to-static `M v^2 / ((gamma-1) E)` = 1.17, total ~23 MPa, **~7.6 T**.
  Compare **~55 T** if the plug sits at the mirror end instead (62.5 kg at 22.4 km/s, ratio 6.7), which
  is why the plug must NOT be at the mirror end on this leg.
- _A free term_: the fireball born at the far end expands at 27 km/s against a 22 km/s drift, so ~9% of
  it leaves retrograde immediately in the correct direction with no field involved.
- **Leg 1 keeps the axial bag** (revised later the same day, superseding an earlier note here that it
  did not). The compact rod enters through the open throat at R, hits a plug **at R**, and the fireball
  snowplows the full 23 m prograde before meeting the mirror. That run is exactly what makes 7.6 T
  sufficient rather than 55 T. The blob then travels back out and exits at R. Round trip ~4 ms, which
  caps pulse rate near **250 Hz** and gives `sec:two_leg_nozzle`'s "flies up the previous shot's plume"
  worry its first concrete number.
- _The loss cone does not apply_. At 0.32 kg/m^3 the number density is 1.07e25 /m^3, ~40% of sea-level
  air, mean free path ~1 um against a 3 m bore, **Kn ~ 3e-7**. This is a continuum fluid, so
  `1 - sqrt(1-1/R)` is the wrong formula and mirror ratio buys nothing. For a fluid the field is a
  pressure wall and the condition is just `B^2/2mu_0 > P_static + rho v^2`.
- _What does leak_: resistive diffusion (already priced at 4.4%) and **Rayleigh-Taylor flute modes**,
  the classic axisymmetric-mirror failure. Speed cancels out of the growth arithmetic:
  **e-foldings = sqrt(4 pi d / lambda)** for stopping distance `d` and mode wavelength `lambda`. A 30 cm
  mode grows 11 e-folds over a 3 m stop and 4.6 over a 0.5 m stop, so **gentler is worse**. Minimum-B
  (Ioffe / baseball) geometry is the proven fix and costs axisymmetry.
_Avoid_: proposing any switched, travelling or pulsed coil field **within a pulse**; invoking loss-cone
or mirror-ratio confinement for this plume.

**One geometry, two current configurations** (decided 2026-08-21 grill). The ship carries a single
23 m graded bore with independently-fed coils. For leg 2 the currents make the monotonic 20 T -> 5 T
profile; for leg 1 the current is concentrated at the P end and the rest left near zero, making a
single-ended mirror in the same hardware with no moving parts.
- _Why this is allowed_: the static-field rule above is **static within a pulse**, not static forever.
  The legs are one to three years apart, so recharging a persistent magnet over a day of cruise costs
  nothing against a pulse. Do not over-read the constraint.
- _Why not physically reshape the magnet_ (the option to rule out with a number): `CONTEXT.md`'s own
  virial band already says the 1.2 MJ/kg end is **bought with assembly pre-compression** (~ -0.25%
  squash, widening the strain window from 0.4% to ~0.65%), not with a material property. Pre-stress is
  created at assembly and destroyed by disassembly, so a re-formable coil comes back at the plain-build
  **0.4 MJ/kg**, a factor of 3 on the dominant mass term. Two fixed magnets cost ~1.6 `M_2` (leg 1 is
  the smaller job); one reshapable magnet at 0.4 costs ~3 `M_2`. **Two fixed win by ~1.9x**, before
  mechanisms and joints. So the ordering is one-geometry-two-currents, then two fixed magnets, then
  reshapable last.
- _On REBCO deformability_: it is a **winding-time** property. The tape bends about its thin axis and
  cannot stretch past ~0.4% strain, the same limit that throttles `sigma_eff`. Demountable REBCO joints
  belong to the **ARC** power-plant concept (sector maintenance), not SPARC, and are a maintenance-shift
  operation rather than a flight reconfiguration. Verify before citing.

**Leg 1's plate comparison is against the wrong speed** (found 2026-08-21 grill, affects
`sec:two_leg_nozzle` line ~977). That line defends the nozzle by saying `f = 0.8` came from a
3.2-16 km/s sweep while "this leg runs between 45-65 km/s". Those are **closing** speeds. The impactor
merges with the slug before anything reaches the reflector, so the reflector sees `w/(1+k)` =
**5.88 km/s** of bulk drift, inside the measured band. The argument holds only because the plate in
`tab:equivalent_plate` carries **no slug**. A **slugged plate** is not a row in that table and may
dominate both entries. Its remaining exposure is ablation from the ~27 km/s internal expansion, not the
drift. Rework the line before it is quoted again.

**RESOLVED 2026-08-21 (was flagged OPEN the same day; the flag was my arithmetic error, not the
paper's).** `tab:bag_sizing` is not `(gamma-1)E`. It is the **ideal-gas pressure of the slug at an
assumed temperature**:

  `B = sqrt(2 mu_0 rho Rg T / M)`, with `T` = 15000 K and `M` = 6 g/mol

`M` = 6 g/mol is fully dissociated water, three particles per 18 g. Every published row reproduces to
three figures: 21.34/7.87/4.11/2.01/0.70/0.35 T against the table's 21.3/7.9/4.1/2.0/0.70/0.35, and the
densities match too. And **`E_B = P V = n Rg T` = 4.43 GJ**, which is why line 876's invariance claim is
true: field energy is the plume's `PV`, and `PV` is fixed by mass and temperature alone, with no volume
in it. That is a cleaner statement than the `(gamma-1)E` framing and should be how the paper says it.

**What is genuinely open is the assumed 15000 K, and the answer is an ionisation buffer.** The collision
delivers `(1/2) k w^2/(1+k)^2` = **265 MJ/kg** at 75 km/s (150 at 56.53, 97.8 at 45.58), while the
85.1 MJ/kg ignition budget only buys vaporisation + dissociation (50.4) + thermal to 15000 K
(`(3/2)(Rg/M)T` = 31.2). The excess at 75 km/s is 180 MJ/kg. It does **not** mostly raise `T`, because
singly ionising water's three atoms costs `(2 x 13.598 + 13.618)` eV per molecule = **219 MJ/kg**, and
180/219 = **0.82**. Ionisation is a thermostat, the way boiling is for a pot of water.
- _But it doubles the particle count_. At ~80% single ionisation, `M_eff` falls from 6 g/mol to ~3.3, so
  `P` and `E_B` rise ~1.8x and **`B` rises ~1.34x**: 4.11 T -> ~5.5 T at 5.4 m, `E_B` 4.43 -> ~8 GJ.
- _So `tab:bag_sizing`'s fields are low by roughly a third_ and should be restated with the ionisation
  term, or the 15000 K row relabelled as the fully-dissociated-but-neutral case.
- Saha closure for the ionisation fraction: `hansen_kawaler_trimble_stellar_interiors` is already in the
  bib. High-temperature EOS: `zeldovich_raizer`, also already cited.

**Solar power at Jupiter, and why the cold end is an asset** (added 2026-08-21 grill). The ship
must hold **two temperatures at once**: electronics fail well below 122 K, coils want colder than
that. MLI zones a warm bus against a cold magnet; the warm side needs power.
- _Flux_: inverse square puts 5.2 AU at 1/27 of 1361 W/m^2, **~50 W/m^2**.
- _Flight proof, no RTG_: **Juno** is the one that has actually operated on solar at Jupiter. Three
  9 m arrays, 18,698 cells, **~14 kW at Earth, ~500 W at Jupiter** (`bolton2017juno` for the
  mission, `jpl_juno_solar_record` for the numbers; JPL release verified by direct fetch). Galileo
  used RTGs. **JUICE and Europa Clipper are still in cruise as of 2026-08** -- do not write them up
  as having operated there.
- _Concentrators_: **SCARLET** on Deep Space 1, line-focus silicone Fresnel lenses at ~8x, ran the
  bus and the ion engine for the mission's 38 months (`stella2000scarlet`, NTRS 20000057570,
  verified). Prefer **non-imaging** mirrors where pointing is disturbed by pulses: forming no image
  buys a wider acceptance angle, hence looser Sun-pointing.
- _The payoff that makes this more than housekeeping_: Carnot work to lift a joule from 77 K is
  `(T_h - T_c)/T_c`, so **2.9 J against a 300 K radiator but 0.95 J against Jupiter's ~150 K one**.
  Cryogenics is **3x cheaper at Jupiter** than at Earth. The distance that endangers the electronics
  is what makes the magnet affordable to keep cold.
_Avoid_: quoting SCARLET's W/m^2 or W/kg figures (seen only in secondary summaries, not verified
against the primary); giving Galileo's RTG wattage (same reason).

**Copper takes the eddy currents, not the superconductor** (added 2026-08-21 grill). Two layers,
in this order.
- _Outside the coil_: a **normal-conducting copper shell** between the plume and the coil is the
  lower-impedance path for a rapidly changing field, so the induced current flows there and warms
  copper at mount temperature instead of the cold mass. **Precedent is in this exact application**:
  Romanelli, Mignone & Cervone's multi-coil parabolic pulsed-fusion chamber gives each ring a
  superconducting **seed** coil plus a separate conducting **thrust coil** that carries the current
  the expanding plasma induces (`romanelli2017pulsed_fusion_nozzle`, Acta Astronautica 139:528-544,
  2017, verified via Crossref).
- _Inside the conductor_: **copper stabilizer** on the REBCO tape. Marchevsky: normal zones spread
  slowly in REBCO so voltage-based quench detection is hard, and raising stabilizer cross-section
  **0.16 -> 0.40 mm^2 halved hot-spot temperature** in current-dump tests on insert coils
  (`marchevsky2021quench`, Instruments 5(3):27, 2021, verified via OSTI).
- _Why the shell comes first_: stabilizer copper carries no supercurrent, so more of it costs
  engineering current density. The shell costs none.
- _The number that motivates both_: removing a joule at 77 K against a 300 K sink costs 2.9 J at
  Carnot and **~20 J with a real cryocooler**. Keeping the loss out of the cold mass is worth ~20x.

1. **The nozzle must be cooled, and radiators are heavy.** Two heat sources. (a) **Edge currents**:
   the plume is diamagnetic and excludes the field with a surface current layer, which dissipates
   resistively because the plasma's conductivity is finite. Magnetic diffusion time
   `mu0 sigma L^2` is ~1.6 ms at `sigma = 574 S/m`, `L = 1.5 m`, against a ~200 us expansion, so
   the field holds but leaks at the percent level per pulse. A pulsed field also drives AC losses
   in the coils, which for a superconductor must be removed at cryogenic temperature. (b) **An
   opaque plume radiates as a blackbody**: 15,000 K gives **2.87 GW/m^2**.
2. **Water is the heat sink that replaces the radiator.** 300 K liquid to 1000 K steam absorbs
   **3.88 MJ/kg**, against 1.16 for LN2 and 1.38 for dry ice. Latent heat is **2.26 of that 3.88
   (58%)**, so the comparison already counts the phase change; water wins because its `h_fg` is 11x
   nitrogen's, not because the others were denied theirs.
   **And the heat is not spent, it is recycled**: energy put in as waste heat is energy the
   collision no longer supplies, taking the ignition bill 85.1 -> **81.3 MJ/kg** and the `k1`
   ceiling 10.10 -> 10.69.
   Water also **stores passively** across the whole trajectory (278 K at 1 AU, 122 K at Jupiter).
   LN2 boils at 77 K and needs active cryo at both ends of a 2.18-3.28 yr cycle; CO2 has a ~40 bar
   vapour pressure at 278 K and needs a pressure vessel.
   **BUT 3.88 MJ/kg is a ceiling the bag cannot buy** (resolved 2026-08-21 grill, see *Bag film
   mass* and *The bag runs as a cold mist* below). Everything above the latent heat is sensible heat
   of hot steam, and sensible heat is exactly what pressurises the bag. The matched operating point
   is **0.31 MJ/kg**, not 3.88, and it **exceeds the demand by construction rather than by 15x**.
   _Avoid_: quoting "1.49% of the pulse energy at `k = 4`" as the delivered figure (that is the
   1000 K ceiling at an illustrative `k`; the flown chain runs `k ~ 8.5` and 0.31 MJ/kg); framing
   the competitor as LN2 or dry ice at all. **The competitor is a radiator**, and the figure of
   merit is not MJ per kg of coolant but **MJ per kg of hardware carried**, where the slug's
   hardware is its bag film: `h_fg / (9.7e-4 T)` ~= **7,700 MJ per kg of film** at 311 K,
   independent of slug mass, bag radius and vapour fraction. No radiator is within three orders of
   magnitude. That is the buried advantage the original wording missed.
3. **Potassium carbonate, 1.77% by mass, gives 1% potassium.** The nozzle steers a *conductor* and
   water at 3000-6000 K is not one. Why the carbonate: it dissolves, and the slug *is* water, so the
   seed distributes itself with no feed system and no settling over a multi-year cruise. **KCl is
   rejected for chlorine** (ozone-catalytic), consistent with the paper already rejecting lead
   primaries at line 243 for atmospheric reasons. K metal is pyrophoric in water, KOH caustic,
   KNO3 an oxidiser. Cost: the extra carbonate adds **0.36 MJ/kg, 0.42% of the bill**.
   **Solubility is not the binding constraint** (corrected 2026-08-21 grill). 1.77% K2CO3 by slug
   mass is **1.80 g per 100 mL**, against ~110 available: a **61x margin**. _Avoid_: rejecting
   **K2SO4 as "barely soluble"** -- sulfate needs 2.27 g/100 mL against ~12 at 25 C, a 5.3x margin,
   so it dissolves fine. Reject sulfate for **putting sulfur in the plume**, the same stratospheric
   logic that already retires chlorine. Carbonate stays the delivery form regardless: cheaper and
   easier to handle than metallic K.
   **The carbonate does not evaporate, and the vent is a separation step** (resolved 2026-08-21
   grill). K2CO3 has no meaningful vapour pressure below its ~1170 K decomposition, so **dry steam
   would arrive carrying no seed at all** and the "distributes itself, no feed system" claim above
   would be defeated by the very venting step that follows it. The mist is what rescues it: at
   `x = 0.13` **87% of the slug never leaves the liquid phase**, so the droplets carry the seed,
   enriched only by `1/0.87 = 1.15x`. **Decision: droplets only, no separate seed feed.** Rejected
   alternatives -- a two-stream clean-steam-plus-brine-spray (redundant once the mist exists; the
   skin-only-seeding saving it would buy is ~0.2% of the bill); dry powder entrained into the vapour
   as open-cycle MHD does (K2CO3 is hygroscopic, cakes over a 2-3 yr uninspectable cruise, and a
   caked seed is a dead pulse); a small metered trim feed for in-flight re-seeding (attractive
   because `tab:seed_window`'s 2500 K cold edge is exactly what a flight measures, but it is a
   second fluid system on a ship that otherwise has none).
   **Why potassium and not cesium**: at *equal mass* K beats Cs above ~3,800 K, because Cs ionises
   more easily but weighs 3.4x as much, so once ionisation saturates you carry fewer atoms per kg.
   `Rm` at 5,000 K is 238 (K) against 138 (Cs). Cs wins only below ~3,500 K, and by 87 K.
   Same trade that standardised open-cycle MHD on K2CO3.
4. **The payoff: the seed lets the plume recombine while staying steerable.** Recombination
   window and `Rm` at 1% seed by mass, `rho = 1 kg/m^3`, `L = 10 m`, `v = 50 km/s`:

| T | K ionised | `Rm` | water chemistry |
| ---: | ---: | ---: | --- |
| 2,000 K | 0.01% | **0.1, field lets go** | recombined |
| 3,000 K | 1.14% | 9.2 | recombined |
| 4,000 K | 10.95% | 76.5 | recombined |
| 5,000 K | 38.03% | 237.8 | mostly recombined |
| 6,000 K | 70.12% | 400.2 | dissociating |
| 15,000 K | 99.90% | 360.7 | fully dissociated |

**Coldest grip at `Rm = 10`, 1% by mass**: Cs 2,942 K, **K 3,029 K**, Rb 3,061 K, Li 3,396 K,
Na 3,461 K. Sodium works but needs **2.5% at 5,000 K, 5.4% at 4,000 K, 12.7% at 3,000 K** to match
1% potassium.

**The bag runs as a cold mist, and its state is derived rather than chosen** (resolved 2026-08-21
grill). Three results, in dependency order.

_Bag film mass._ A spherical film at working stress `sigma` holding an ideal gas obeys
`m_bag/m_slug = (3/2) rho_f Rg T / (M sigma) ~= 9.7e-4 * x * T` at `rho_f = 1400 kg/m^3`,
`sigma = 1 GPa`, where `x` is the vapour fraction. **The radius cancels.** This is a *second*
invariant sitting beside the stored-field-energy one already recorded below: a bigger bag changes
neither the coil mass nor the film mass. What it changes is peak field and radiative loss.
Consequence: **1000 K steam costs ~1 kg of film per kg of slug**, destroyed every pulse. That is
what kills the 3.88 MJ/kg operating point.

_In vacuum the steam runs cold, and the floor is its own saturation curve._ 373 K is where water's
saturation pressure hits 1 atm, and there is no atm. The floor is set by the **bag's own density**:
dew point is 395 K at 1.0 m, 355 K at 1.55 m, 321 K at 2.5 m for a 5 kg slug. **A bigger bag is a
colder bag.** _Avoid_: saying vacuum makes the steam *easier to contain* -- containment is strictly
harder, because the film carries the full differential with nothing outside to balance it. On Earth
a bag of saturated steam at ambient carries **zero** differential.

_The heat balance derives `x` and `T`; nothing is chosen._ The ship has no radiator, so **all** waste
heat must boil water, and `x = Q / (m_slug h_fg)` with `T` following off the saturation curve.
Using line 972's own recipe (radiated share x sky fraction x pulse energy, coils filling ~a tenth of
the sky) at the **213 kg** anchor:

| term | per kg of slug |
| --- | ---: |
| radiated (1.2% at 5.3 m, scales as `M^-1/3`) | 1.02 MJ |
| intercepted at a tenth of the sky | 0.102 MJ |
| field and coil dissipation (~1% of 20.8 MJ/kg stored) | 0.21 MJ |
| **demand Q** | **0.31 MJ** |
| **-> x = Q/h_fg** | **0.13** |
| **-> T (dew at `rho_vap` = 0.13 x 0.32)** | **311 K** |
| **-> P** | **~4 kPa** |
| **-> film** | **3.9% of slug (8.3 kg)** |

**The mist is a thermostat**, and this is the sentence the section was missing. Two-phase water is
pinned to its saturation curve, so a thermal overrun converts into **vapour fraction, not
temperature**: the bag boils a little more and holds 311 K. A single-phase coolant would run hotter
and raise bag pressure with it. The mist also **keeps the seed in suspension** (see point 3 above),
so two independent arguments land on the same design.

_Avoid_: presenting `x` or `T` as design choices; quoting a bag temperature without saying which
slug mass it came from.

**Bag sizing, bounded on both sides** (5 kg slug at 15,000 K -- **illustrative only; the flown chain
carries ~213 kg, see the anchor-mass entry below**). Venting the slug as steam into a bag
lowers density, hence pressure, hence the field needed to stand it off (`B ~ R^-3/2`). But
blackbody loss grows as `R^2`, and the plume must stay optically thick (`tau = kappa rho 2R >= 1`)
or it radiates volumetrically instead of from its surface:

| radius | density | `B` at `beta = 1` | radiated in 200 us | share of `E_th` |
| ---: | ---: | ---: | ---: | ---: |
| 0.5 m | 9.55 | 22.3 T | 2 MJ | 0% |
| 1.0 m | 1.19 | 7.9 T | 7 MJ | 2% |
| 1.55 m | 0.32 | 4.1 T | 17 MJ | 4% |
| 2.5 m | 0.076 | 2.0 T | 45 MJ | 11% |
| 5.0 m | 0.010 | 0.71 T | 180 MJ | 43% |
| 8.0 m | 0.002 | 0.35 T | 462 MJ | 109%, cannot sustain |

**Sweet spot ~1 to 2.5 m radius at 2-4 T.** Optical depth agrees: max radius 1.09 m at
`kappa = 0.5 m^2/kg`, 3.45 m at `kappa = 5`. A third bound is a **matching condition, not a cap**
(resolved 2026-08-21 grill): the bag and the arriving cloud want the *same frontal area*. A bag
wider than the cloud leaves slug unswept; a cloud wider than the bag spills impactor mass past it.
Both mismatches cost, so the correct statement is match, not "keep the bag small". **On the nozzle
legs the footprint is a free knob**, unlike everywhere else in the paper: line 511 pins the *plate*
footprint at about half the plate radius, squeezed between a facesheet cliff (342 MPa against a
400 MPa limit; 0.3 R takes it to 1470 MPa and destroys the plate) and the `eta_capture` rim spill,
but a magnetic nozzle has no facesheet to over-pressure and no rim to spill past, and its own scale
length (`L = 10 m`) sits well above the 1-2.5 m bag. The cloud is therefore sized *for the bag*,
using the atomization-timing knob the fleet already flies (CONTEXT **impulse trim**, knob 2). The
impactor is already a gas cloud before arrival (line 86), so this is a sizing choice, not a new
capability.
_Avoid_: saying a bigger bag makes the plume **hotter** (temperature is `eps_th = w^2 k/2(1+k)^2`,
which has no volume term; a bigger bag is the *same* temperature at lower pressure); claiming the
bag makes the nozzle **lighter** (stored field energy is invariant at 103.8 MJ by the virial
theorem, so `sec:minimum_nozzle`'s energy-scaling rule gives the same coil mass -- the win is peak
field and hoop stress, which goes as `B^2`); worrying about particle magnetisation (`r_L/L` stays
under 3.5e-5 across the whole range).

**Anchor mass for the growth leg: 25 kg impactor, 213 kg slug** (decided 2026-08-21 grill). This
exposes a units mismatch in `sec:minimum_nozzle`. **Line 968 quotes the growth-leg pulse *per
arriving kilogram* (2.5 GJ) and then sizes the nozzle from it as though that were the whole pulse**,
while the near-Sun figure it is compared against (477 GJ) is the whole 2.5 kg projectile. At a 25 kg
impactor the pulse is **63 GJ** and the Mini-Mag rule returns **~37 t**, not 1.5 t. An independent
check agrees: the virial bound for a self-supported magnet, `M >= rho_struct E_field / sigma`, with
the paper's own invariant field energy (20.8 MJ per kg of slug -> **4.4 GJ** at 213 kg) and REBCO
structure at 1 GPa / 8000 kg/m^3, gives **35 t**. Two routes, same answer, so the number is not an
artifact of the Mini-Mag ratio.
_What breaks_: line 790's "masses on the order of a tonne rather than hundreds of tonnes" and line
968's "about 5% of a 30 tonne craft and 1.5% of a 100 tonne one". Both become **tens of tonnes and a
few Starship loads**.
_Why 25 kg anyway_: **bigger pulses radiate less.** Radiated share goes as `M^-1/3`, so the 25 kg
pulse loses ~1.2% where a 1 kg pulse loses ~4%. By line 972's own square-root rule that is worth
roughly 3 points of `e2`, and `tab:mass_interest_growth` pays orders of magnitude for points of
`e2`. A 37 t nozzle that recovers better beats a 1.5 t one that does not. It is also the same
argument line 819 already makes in reverse ("a smaller fireball cools and radiates faster, so a
scaled-down shot returns a recovery that does not carry over to flight").
_The one lever not yet priced_: `beta = 1` is required **at the throat**, not through the whole
plume volume, and the stored-field invariant assumes the field fills the sphere. A throat-only field
would contain less. Unquantified; belongs with the radiation-hydrodynamic calculation already owed.

**Dry-mass plug ring** (decided 2026-08-21 grill):
A dense ice or plastic annulus at the *front face* of the vented slug bag, held **off the ship's
axis**, that catches a **softened** dry-mass discard so the PuffSat's <=250 g of non-volatile
solids couple into the pulse instead of leaving as a **Heliocentric package**.
*Why it needs its own part*: the package arrives with roughly 25 kg/m^2 of areal density against
the bag's ~1 kg/m^2 through the centre at the sweet spot, so the steam alone couples only a few
percent of it. *Sizing*: ~0.1 m of ice, ~3 kg, about 1.5% of the ~200 kg slug a 25 kg PuffSat
carries at `k ~ 8.5`. *Payoff*: under 1% of the pulse recovered (dry mass is <1% of PuffSat mass
at the same arrival speed), but the larger win is retiring the **upper-atmosphere metals loading**
objection the 2026-08-11 grill left open as "the objection a reviewer is most likely to raise",
by consuming the solids rather than shedding them. Metals help rather than contaminate here:
Al ionises at 5.99 eV and Si at 8.15 against ~12.6 for water, the opposite of the LOX-plate case
at line 279 where the same metallisation was landing on a physical surface.
*Why a ring, and why softened rather than replaced*: **discard stays fail-safe**. The shaped
charge's kick is tuned down from "clear the target radius" to "clear the ship's silhouette", so a
plug that misses or under-performs sends debris *past* the hull rather than through it. Both legs
otherwise point the dry mass down the ship's axis (head-on it enters the front, on the overtake it
enters the back), and an on-axis plug replacing the discard would be fail-dangerous: ~700 MJ at
75 km/s relying on 10 cm of ice.
_Avoid_: presenting the plug as a **mixing aid for the gas plume** (the volatilised plumes mix on
their own; the plug exists only for the non-volatile remnant); calling it **ship protection** (the
discard is what protects the ship and is retained); sizing it against the **5 kg bag-table slug**
(wrong scale -- that table is a small-unit illustration, and dry mass belongs to a 25 kg unit).
_Open_: the aim spec on the softened kick; whether the **departure leg** (head-on, ~75 km/s) has
any dry-mass resolution in either repo, since the **Heliocentric package** covers only the Earth
encounter on the growth push.

**The PuffSat/slug asymmetry, worth one sentence in the paper**: line 250 atomises the PuffSat's
water into droplets *because* that "requires much less energy than vaporization", while the slug is
deliberately boiled. Not a contradiction. The PuffSat has no waste heat to spend; the ship has a
nozzle it must cool anyway.

**Recombination is assumed recovered** (decided 2026-08-20 grill, on the physics above):
The ~50 MJ/kg locked in `H2O -> 2H + O` is **a loan, not a cost**. Three-body recombination time
scales as `1/n^2`: 0.01 us at 1 kg/m^3 and 1 us at 0.1, against a ~200 us expansion, so it
completes with orders of magnitude to spare. It freezes only **below ~0.01 kg/m^3**, which is the
one condition the paper must name. Two supporting facts: dissociation energy carries **no
pressure**, so a dissociated plume holds 84 MJ/kg while pressing with only its 31 MJ/kg of
translation and returns the rest during expansion where the field is weaker; and the frozen-flow
bound `e1 <= sqrt(1 - phi)` (0.675 at `k = 10.21`, 0.870 at `k = 4.02`) is therefore the
**pessimistic** limit, not the expected one.
_Provenance_: derived in the 2026-08-20 grill, not in either repo. Saha + electron-neutral
conductivity at a fixed 1e-19 m^2 cross-section, so the >=6,000 K rows overstate `sigma` (Coulomb
collisions take over above ~30% ionisation); the 3,000-5,000 K rows carry the argument and are
electron-neutral limited. **The fireball density is uncomputed in both repos and decides this**,
the same gap `sec:minimum_nozzle` already defers to a radiation-hydrodynamic calculation.
_Avoid_: extending `e`'s definition to cover frozen chemistry without saying recombination is
assumed (`eta_jet` at line 1521 already lists "frozen ionization or dissociation energy", `e` at
line 793 does not, and that asymmetry is now deliberate).

**Carry-over to the near-Sun case, prograde only** (raised 2026-08-20 grill; belongs in this
subsection with an `\autoref` to `sec:solid_PuffSats` and `sec:jupiter_gravity_initial`):
The same "slug doubles as coolant" argument plausibly applies to the **prograde** three quarters of
the near-Sun split (`sec:dv_effective`, prose at line 734), where the reaction mass rides aboard a
shielded rocket and never sees the Sun directly. The prograde vehicle can carry a heat shield over
its payload, so water is admissible there and brings the same radiator-replacing heat sink to a
chamber running far hotter than the Jupiter cycle's.
**It does not carry over to the retrograde quarter.** Those projectiles are released and fly their
own Sun-grazing retrograde orbit unshielded, so they must survive close solar approach on their
own. That is exactly why `sec:solid_PuffSats` specifies low-Z carbon and ceramic solids from the
Parker Solar Probe's thermal protection lineage, with a little iron for X-ray opacity. Water would
be lost long before periapsis.
_Avoid_: presenting this as a priced result (it is an observation, and no near-Sun slug/coolant
budget has been computed); implying the prograde and retrograde legs differ in **periapsis** (they
share it) rather than in **whether the mass rides behind a shield**.

**References, verified and added 2026-08-20** (all four checked against primary sources, not
memory; `crc_handbook` already existed and is reused for K2CO3 solubility):
- `kerrebrock1964nonequilibrium` -- alkali seeding / two-temperature conduction. **My recalled
  citation was wrong**: it is *AIAA Journal* **Vol 2, No 6, 1072-1080, 1964**, not Vol 3 (1965).
  Confirmed off the scanned page header. Its worked example is argon plus potassium at 2000 K.
- `rosa1968mhd` -- Rosa, *Magnetohydrodynamic Energy Conversion*, McGraw-Hill 1968.
- `messerle1995mhd` -- Messerle, Wiley 1995, UNESCO Energy Engineering Series.
- `molina1974ozone` -- Molina & Rowland, *Nature* **249**(5460), 810-812, 1974. Cited for why the
  seed is a carbonate and not a chloride.
_Avoid_: citing Kerrebrock as 1965 or Vol 3 (a real error I made from memory and corrected).

**Applied to `templateArxiv.tex` 2026-08-20** (builds clean, 104 pp, 0 errors):
- `tab:mass_scenarios` row for `sec:jupiter_only_growth` now reads **56.5--65.1 km/s** and
  **7.4--8.7**, with a note that 69.270 is the *unphased* retrograde Hohmann arrival the phased
  chain never reaches.
- The **three** (not four, as first miscounted) 9x prose claims are now "about 8 times": lines
  785, 790, 1616. There was no such claim at line 157.
- Line 1616's "about 69 km/s" -> **61** (chain mean), and line 828's "69 km/s return velocity"
  -> the 56.5--65.1 range.
- `tab:mass_interest_growth` top two rows refloored to **0.011/0.022/0.039/0.059** and
  **1.0/3.2/7.7/15**; caption now states the 1/15 ground-launch floor and that it binds only in
  those two rows. Prose at line 817 updated from `x0.095` "under ten cents" to **`x0.011`, about a
  cent on the dollar**. Everything at `e >= 0.40` is unchanged, so the **1,284x** headline stands.

**Both subsections are now in the paper** (2026-08-20, builds clean at **107 pp**, 0 errors, all
five cites resolving):
- `sec:watering_it_down` ("Watering It Down, Literally") and `sec:two_leg_nozzle` ("Two Nozzles
  Beat a Nozzle and a Plate") sit between Mass Interest and Inner Planet Assist Alternatives,
  as `\subsubsection`s. New tables: `tab:seed_window`, `tab:bag_sizing`, `tab:two_leg_growth`,
  `tab:equivalent_plate`.
- The old line-794 paragraph is replaced by a two-sentence pointer to both.
- **`e -> e_2` relabel done**, 10 occurrences across `sec:mass_interest` including the
  `tab:mass_interest_growth` header; the caption now says why. No bare `$e$` remains in that
  subsection, and there were no `e^` exponentials in range to catch by accident.
- Citations wired: `kerrebrock1964nonequilibrium` + `rosa1968mhd` + `messerle1995mhd` on the
  alkali-seed sentence, `crc_handbook` on the K2CO3 solubility, `molina1974ozone` on chlorine.

**Outbound-leg ground-test gap** (`sec:jupiter_only_growth`, the Mass Interest argument):
Why **recovery** (`e`) on the Jupiter-only outbound leg can only be measured by flying, which
is what makes early cycles an asset rather than a cost. Four commitments, in this order:
1. *Energy is explicitly conceded not to be the wall.* 70 kg at 70 km/s is 171.5 GJ, about
   41 t TNT equivalent; 1 kg at 75 km/s is 2.81 GJ, about 0.67 t. Both are conventional-test
   scale. **Do not claim the pulse is nuclear-scale** — a reader with a calculator catches it.
   (A defensible nuclear sentence exists but is about *power density*, not yield: only a
   nuclear device can dump 2.81 GJ into a kilogram fast enough, the Casaba-Howitzer wall
   Orion hit. Optional, currently not used.)
2. *Acceleration is the wall.* `a = v²/2L` to 70 km/s: 2.5e6 g over 100 m, 2.5e5 g over 1 km,
   **2.5e4 g even over 10 km**, 2.5e3 g over 100 km. No guided projectile carrying a slug
   survives that, and no evacuated 10 km launcher exists.
3. *Delivering the energy is a second wall.* 171.5 GJ against Sandia Z's ~20 MJ stored is
   ~8,600x, before launcher efficiency (the 1 kg case is still 141x).
4. *The path must be evacuated.* ~6 GPa stagnation pressure at 70 km/s in sea-level air. The
   range is therefore a km-scale vacuum tube, i.e. the **Straw Way** — downstream
   infrastructure the working cycle has to pay for first. Worth one sentence of circularity.
Backstop that closes the sub-scale loophole: `e` is **not scale-invariant**, by
`sec:minimum_nozzle`'s own radiative-escape argument (a 100 g pulse cools and radiates faster,
so it returns an `e` that cannot be extrapolated to flight).
Ground anchor already in the bibliography: First Light Fusion's two-stage gas gun at
\SI{6.5}{\kilo\meter\per\second} (`firstlight2022fusion`, cited in `sec:epstein_drives`);
its shaped target drives *target material* past 70 km/s, but only as a mm-scale converging
implosion, never a free-flying kilogram.
_Needs citation before use_: the kilogram-class launcher record near 11 km/s, and Sandia Z's
milligram flyer plates near 45 km/s. Both currently unsourced.
_Avoid_: leading with energy or treaty language; asserting untestability without conceding
what *is* groundable (the nozzle magnet itself scales to ~1.6 t of coils at this pulse energy,
against Mini-Mag's 200 t for 340 GJ, so the driver is the unbuildable half, not the magnet).

**Launch-cadence asymmetry (E2E critique)**:
The 2026-07-17 grill's framing for the launch-cadence disadvantage of Starship
Earth-to-Earth in `sec:200_mile_high`. Four commitments. (1) *Mechanism is closure, not
blast*: helicopters are excluded from the shore-to-platform corridor because every launch
and reentry closes the surrounding airspace and sea lanes against a possible vehicle
failure (range safety), and at SpaceX's own projected cadence the closure windows tile the
operating day; "rocket blast makes helicopters unsafe" is the rejected wording. (2) *Cadence
anchor is SpaceX's own number* (Shotwell's dozens of E2E flights per day), matching the fare
section's use-their-optimism discipline; the hub-traffic derivation is the fallback only.
(3) *Pad spacing is grounded on the LC-39 precedent* (LC-39A/B sited ~2.7 km apart for
Saturn V, a smaller propellant load than Starship's), not a bare "1 km" figure.
(4) *Boomerang guard*: the paper concedes 2.5x launch capacity in `sec:fare_comparison`, so
the critique is stated as a **city-end** asymmetry: PuffSat cadence lands at a few remote
dedicated spaceports on infrastructure schedules (formations pre-placed), while E2E runs its
full cadence, exclusion zones, and multi-pad sprawl at every served city. Placement: the
closure argument extends the existing Logistical Inefficiency bullet; pad sprawl is one new
bullet; the asymmetry sentence lives in the rocket-plane paragraph, not in a bullet.
_Avoid_: blast-hazard wording for the helicopter point; quoting a cadence band SpaceX never
claimed; adding the disadvantage without the city-end guard sentence.

### Intercity rocket plane (`sec:200_mile_high`)

**Takeoff**:
The rocket plane's departure: an ordinary runway takeoff from an existing urban airport on
air-breathing engines. There is no launch anywhere in this architecture.
_Avoid_: "launch" for anything the rocket plane does. That word belongs to Starship, and the
whole community-noise argument rests on the two being different events.

**Transit leg**:
The subsonic cruise from the departure airport out to the **ignition point**. Flown on
turbofans, carries no orbital-mechanical meaning, and is therefore free to dogleg away from
the great circle. About ten minutes at the 150 km baseline.

**Ignition point**:
Where the rocket engines first fire: roughly \SI{12}{\kilo\meter} altitude, one **ignition
standoff** from the nearest populated area. The only loud event in the architecture, and the
only one whose position is a free variable.
_Avoid_: conflating it with the airport. The formation's orbital plane must contain the
ignition point and the destination, *not* the departure airport. That decoupling is the
argument.

**Ignition standoff**:
Horizontal distance from the **ignition point** to the nearest populated area. Baseline
\SI{150}{\kilo\meter}, chosen because two Raptors there read as about one wide-body departure
in A-weighted sound exposure, which is the claim Table 1 already makes. Continuously
adjustable, so a single town under the track is cleared by lengthening it rather than
doglegging.

**Community-noise asymmetry (E2E critique)**:
The 2026-08-13 grill's framing for the noise disadvantage of Starship Earth-to-Earth,
sibling to the **Launch-cadence asymmetry** entry above and carrying the same boomerang
guard. Five commitments. (1) *The distance anchor is Musk's own*: ~20 miles / 30 km offshore,
which he named and tied explicitly to "frequent daily flights." Do not assert a distance he
never claimed; the 2026-08-13 session opened with "20 km," which is wrong. (2) *Levels are
measured, not modelled*: Gee's BYU group, 1.0--35.5 km, Flights 5/6/9. 145.7 dB at 1 km,
125.2 dB at 10 km, 115 dBA sound exposure at 10 km (= 1000 wide-body departures), flyback
boom 9 psf at 10 km and 1.5x Concorde loudness at 20 km. (3) *Cadence is argued from
institutional precedent, never from DNL* -- see the Flagged ambiguity below. (4) *The
rocket-plane counter-case is the movable standoff, not a quieter source*: an offshore
platform must be passenger terminal and ignition point at once, and those want opposite
distances from shore, which is what pins Musk at 30 km. Splitting the roles costs ten
minutes of cruise. The corollary is reach: offshore platforms can only ever serve coastal
cities, while rural overland ignition opens Phoenix and Chicago. (5) *Boomerang guard*: the
architecture burns ~2.5x the launch capacity (`sec:fare_comparison`) and is therefore louder
in total. The claim that survives is that the noise is relocated off the passenger schedule
and away from cities, not that there is less of it. Concede this inside the bullet.
_Avoid_: claiming the rocket plane is quieter per passenger; claiming its ascent boom
vanishes (it is Falcon-9-class, ~1.90 psf max and mostly under 0.5 psf, and it still travels
150 km); presenting the Starbase suit as findings rather than allegations.

### Cryogenics, thermal, and ISRU propellant

**Passive standoff sunshade**:
A JWST-style detachable multilayer (aluminized Kapton) shade carried in front of a
cryogenic PuffSat to block sunlight, distinct from the conformal solar-white coating on
the skin. Tune the layer count to the target temperature (more layers, colder). Jettisoned
a short time before impact so it does not foul the gas plume or have to survive the
collision. Not retained as reaction mass: the benefit is sub-kg, and its metallization
(Al, doped Si) would contaminate the non-combustible LOX pusher plate.
_Avoid_: calling it a "heat shield" (that evokes the near-Sun ablative chamber and the
Parker-class sunshade, which are different hardware).

**Passive-shielding temperature law**:
A shaded radiator equilibrates with the attenuated sunlight, so its temperature scales as
`T ∝ r^(−1/2)` with heliocentric distance `r`. Anchored at JWST's ~40 K at ~1 AU, this
gives ~24 K at Ceres (2.77 AU) and ~13 K at Saturn/Phoebe (9.6 AU). The 40 K reach is
colder than LOX wants (oxygen freezes at 54.4 K), so for LOX use a lighter shade (~60–80 K);
the full reach is the lever for storing LH₂ farther out.

**Passive-LH₂ threshold**:
The heliocentric distance (~1.5 AU) beyond which passive shielding can hold hydrogen below
its 33 K critical temperature, so liquid hydrogen becomes storable. Inside it (Moon,
Mercury) no shield keeps H₂ liquid at any pressure; outside it (Ceres and beyond) LH₂ is
storable at modest pressure (a few bar at Ceres' ~24 K). This is why LOX/methalox serve the
inner system and LH₂/LOX is a Ceres-and-out option.

**On-demand electrolysis propellant**:
Store water (not a pressurized cryogen) and electrolyse it with onboard solar power into
hydrogen and oxygen at the moment of use, feeding either a chemical thruster (Imperial
ICE-Cube) or a Hall-effect thruster (Imperial WET-HET). The closer-in alternative to stored
LH₂/LOX, sharing the "make propellant on demand, no pressurized tank" principle with the
PuffSat fine-control thrusters.

**Effervescent (carbonation) atomization**:
Dissolving CO₂ into the icy PuffSat's meltwater so exsolving gas helps shatter it into
droplets on release, supercharged by the vacuum pressure ratio. A speculative assist that
trims the micro-explosive load, viable only where carbon is abundant (icy moons such as
Ceres and Phoebe), not on the carbon-poor Moon. Clathrate storage is rejected: its
endothermic, self-preserving dissociation releases gas too slowly for millisecond
atomization and over-pressurizes the liner if it dissociates while confined.

**Centrifugal stirring geometry** (`sec:spherical_water_thermal`, `sec:tethered_ring`):
Which convection architecture a spinning water body needs depends on whether it is
centered on the spin axis. A **centered** body (the baseline 100 kg sphere, and the hub
bag of the tethered ring) sees `omega^2 s` pointing cylindrically outward, which vanishes
along the whole spin axis. Its coldest surfaces, the spin poles, sit exactly on that null,
so they cannot be stirred and are instead prevented from getting cold with aluminum-out
low-emittance caps. An **off-axis** body (the ten ring bags at R = 2 m) sees a nearly
uniform `omega^2 R` outward, varying only ~6.5% across a 0.129 m bag and vanishing nowhere.
Its permanently dark caps (facing along the spin axis) then sit broadside to the field,
which is a side-heated cavity with no critical Rayleigh number, so it convects at any dT
and needs no polar caps. Off-axis bags are also stirred ~12x harder at the same spin rate (`omega^2 R` at 2 m against
the volume-mean `omega^2 <s>` = 3*pi*a/16 = 0.17 m inside a 0.29 m sphere).
Rests on the bags co-rotating rigidly with the ring. **Co-rotating means one turn per lap, same
face to the hub: tidally locked in geometry, like the Moon to Earth, though by hardware rather
than by tidal friction.** Circling the axis and spinning about one's own center are separate
motions; the spoke compels only the first. Locked to the HUB is fine (the Sun still sweeps past
once per rotation, and the flux-average argument shows the inward and outward faces collect
identical mean flux anyway). Locked to the STARS is the failure, since that bakes one hemisphere.
A spoke ending at a single point pulls
through the bag's center and exerts zero torque, so a bag is torque-free and simply keeps the
spin it was deployed with. The failure is spin-up after the spokes are taut: the bags never
start turning, stay fixed in inertial space while orbiting the axis, and park one bumper
hemisphere in permanent sun (~150 C) with the other permanently dark, which kills the
light-and-shade cycling the thermal balance needs. Fix is a 3-line bridle per spoke, which
only ever carries spin-up and disturbances, never a steady load.
_Note_: centrifugal gravity is always perpendicular to the spin axis, so the
Chandrasekhar `g || Omega` rotational suppression of onset never applies to either case.
But that only frees the *threshold*, not the *speed*. At omega = 1 rad/s the Ekman number is
~7e-6 and the Rossby number ~0.02, so Coriolis dominates: convection organizes into columns
aligned with the spin axis, columnar onset sits orders of magnitude above the plane-layer
1708 (margin of tens, not tens of thousands), and overturn is minutes to tens of minutes, not
the tens of seconds a non-rotating free-fall estimate gives. Still fast against a 15 d coast.
Bonus: axis-aligned columns carry little flow *along* the axis, a second reason the spin
poles of a centered body are the worst-mixed points.
_Sun-angle independence (off-axis only)_: an off-axis bag stays side-heated at **every**
Sun angle, not just at the baseline perpendicular attitude. Decompose the Sun direction in
the bag's co-rotating frame: the component along the spin axis is constant, and the
in-plane component turns once per rotation. Averaging the Sun *vector* is not the argument,
since a facet of normal n absorbs as `max(0, n.s)`, which is nonlinear in s. Average that
instead: over one rotation s sweeps a cone about the spin axis, so the mean depends on n only
through its angle to that axis. The bag's outward and inward faces share that angle, so they
collect identical mean flux and no mean gradient forms along the field. Verified numerically
to 1e-11 across Sun angles 0, 0.6, pi/2 rad.
The stagnant case, a hot cap parked on the "ceiling" with warm fluid buoyantly stuck, would
need the Sun over the bag's inward-facing cap, and that direction sweeps a full circle in
inertial space once per rotation, so no fixed source can sit there. Only the **centered**
hub bag can get a permanently stagnant hot cap, and only when the axis points at the Sun.
_Sun at the hub's equator is the good case_: the hub bag straddles the axis, so it has its
own field, zero on the axis but rising to omega^2 a = 0.13 m/s2 at its equator (about 0.45x
the 100 kg body, 26x weaker than a ring bag). In the thermal attitude the Sun sits in that
equatorial plane, heating lands where the field is strongest and sweeps once per rotation,
warm water at the rim is hot-at-the-bottom and overturns, and the cold poles are handled by
the aluminum-out caps. Only the axis-at-Sun attitude is bad. Do NOT say the hub bag has no
centrifugal drive; the drive vanishes only ON the axis, not throughout the bag.
_How bad is that cap_: bounded by transient conduction, not steady state. The cap is stuck
because warm water floats toward the axis and the sunlit pole already sits on the axis.
Steady conduction would give ~33 K, but that is never reached: crossing the bag takes
a^2/kappa = 32 h against a 3 h hold, so heat stays in a sqrt(kappa t) = 4 cm skin and the
surface rise is 2q sqrt(kappa t/pi)/k. That is 6 K on the lit-hemisphere mean
(76 W/m^2) and 11 K at the sub-solar point for a cos-theta distribution. Both ignore the
vapor-space heat pipe and the ~0.5 W/K by which net intake falls as the cap warms, and the
cos-theta case is pessimistic since the water sees the bumper's inner face, not the Sun.

**Thermal attitude vs impact attitude** (`sec:tethered_ring`, `sec:spin_reorientation`):
The two directions the ring's spin axis is asked to hold. The **thermal attitude** is
perpendicular to the Sun-line, wanted by centrifugal stirring. The **impact attitude** is
along the closing velocity, wanted so the ring plane arrives square to the pusher plate.
Mission geometry decides whether they agree; worst case is 90 deg apart. Resolution: hold
the thermal attitude through the coast, re-point in the last hours. Cost of the worst case
is ~63 N.s, an equivalent 0.63 m/s on the 100 kg assembly. Firing time depends on how the
400 mN of `sec:fine_control_thrusters` is read: it is a whole-vehicle drag figure, so the
conservative split is 200 mN per end, a 5 N.m couple, 150 rotations, 942 s. Sizing each
package for the full 400 mN halves that to 471 s. Impulse and propellant unchanged either way.
Against the propellant: the drag leg of `sec:estimate_cold_gas` is only 18 N.s before margins
(20 mN x 300 s + 400 mN x 30 s), so the re-point is ~3.5x that leg; the 500 g tank holds
123 N.s at the pessimistic Isp = 25 s and 211 N.s at the flown 43 s, so the re-point is about
half the tank on the first figure and under a third on the second.
_Key scaling_: `dv = 2 sin(theta/2) * omega * k^2 / r`, where `k` is the radius of gyration
and `r` the thruster moment arm. Cheap only because the water stays compact at R = 2 m
while the thrusters ride at the 25 m tether bundle's ends (r = 12.5 m). Putting the same
100 kg out at 25 m radius instead costs ~41 m/s on the arc formula the appendix actually uses
(an earlier note said 37 m/s, which was the chord lower bound), which is why that variant is
not the architecture.

### Energetics and sensitization

**Chemical gassing (nitrite gassing)**:
Sensitizing an emulsion explosive by injecting sodium nitrite (NaNO₂), which decomposes in
the acidified aqueous phase and nucleates nitrogen bubbles in situ. Those bubbles are the
**hot spots**. The canonical sensitizer for the PuffSat emulsion of `sec:explosive_puffsat`,
because it is added late in flight, which is the safety property line 230 already claims.
_Avoid_: "sodium nitride" (Na₃N, a different and essentially non-existent compound, and not
what any energetic formulation uses); confusing it with sodium azide (NaN₃), which
`sec:cold_gas_generators` explicitly rejects for its silicate slag.

**Hot spot**:
A small gas-filled void that heats by adiabatic compression when a shock passes, initiating
the surrounding matrix. Must contain a **non-condensable** gas. A void filled with water
vapor condenses under compression instead of heating, so it is a poor hot spot even at the
correct void fraction. This is the constraint that sets the charge fill pressure.

**Charge fill pressure (~5 kPa)**:
The explosive PuffSat's emulsion is held a few kPa above vacuum, not at one atmosphere and
not vacuum-referenced. Chosen as the lowest pressure keeping bubble contents nitrogen- rather
than steam-dominated: the supersaturated AN phase sits near 1 kPa of water vapor at 290 K, so
5 kPa is ~80% nitrogen, and ~94% if the charge runs at 273 K. Stays inside line 232's "very
thin layers" (membrane stress `Pr/t`), where a full atmosphere would demand a real pressure
vessel. Nitrite dose scales down with pressure, which is the same dose-against-head
calculation mining already does down a borehole, extrapolated the other direction.
_Avoid_: "low vapor pressure environment" for the flight condition. Vapor pressure is a
property of a liquid at a temperature. The environment is low **ambient** pressure, and the
mechanism runs the opposite way from what that phrase suggests.

**Sensitizer-set thermal band (273--300 K)**:
The explosive PuffSat's thermal-trim target, squeezed from both sides by the gassing
chemistry. Below 273 K the nitrite reaction is too slow to finish inside the pre-intercept
window and the supersaturated ammonium nitrate phase risks crystallizing out. Above 300 K
aqueous vapor pressure crowds the nitrogen fill and the matrix coarsens. Held passively by
the louver of `sec:louver_thermal_trim`, which currently lists a target for every variant
*except* the explosive one. Means colder is **not** strictly better for a gassed charge,
qualifying line 232's reflective-liner argument.

**Isobaric charge (low-gravity advantage)**:
In free fall the charge has no hydrostatic head, so bubble size, density, and sensitivity are
uniform throughout. A 10 m borehole carries ~137 kPa of head and must be dosed against depth.
Holds to within a few percent for any acceleration below ~0.01 g; near 0.04 g the gradient is
back to 10%, so a fast-spinning variant needs rechecking. The paired cost is **mixing**: an
emulsion matrix is a yield-stress paste (~100 Pa) that neither convects nor settles, so
gassing must happen during a chamber-to-chamber transfer where shear distributes the reagent.
Buoyancy itself is a non-issue at this timescale. Stokes creaming of a 100 µm bubble in
50 Pa·s matrix is 0.6 µm/s at *full Earth gravity*, or 2 mm over the whole gassed window.

**Bubble populations (four, do not conflate)**:
The paper uses "bubble" for four distinct things doing different jobs.
(1) **Gassing bubbles**, nitrite-generated N₂ in the emulsion, are hot spots that initiate the
explosive (`sec:explosive_puffsat`).
(2) **Cavitation bubbles**, pre-formed gas-filled plastic spheres in the bulk water, shape what
the shock does to the water and cap droplet size (`sec:icy_puffsat`, line 239).
(3) **Effervescent bubbles**, exsolving dissolved CO₂, stretch ligaments during late breakup
(see **Effervescent (carbonation) atomization**).
(4) **Crevice nuclei**, gas trapped on unwetted foam-strand surfaces, seed cavitation in the
water (line 245).
(1) initiates the charge; (2), (3), and (4) act on the water after it fires.

### Materials

**Halogen-free vaporizables rule**:
Any material expected to vaporize, decompose, or ablate in flight, ice-wire coatings, the
airlock's sacrificial plastic, and (see **Second-surface radiator skin** below) balloon
PuffSat outer skins, must be halogen-free, no fluoropolymers (PTFE/FEP/Teflon) or other
halogenated plastics. Rationale, stated twice already in the paper for other components:
halogenated combustion/decomposition products are toxic in the near term (HF,
perfluoroisobutylene-family compounds) and persistent in the long term (PFAS chemistry),
and the paper's own fleet-scale argument for aluminum reentry debris (small per-event,
real in aggregate at billions-of-disposals cadence) applies at least as strongly here.
Prefer polyethylene (airlock plastic) or polyimide/Kapton (thermal-control skins) even
where a fluoropolymer would otherwise be the obvious choice for UV durability.
_Avoid_: FEP Teflon or any PTFE-family polymer anywhere in flight hardware that vaporizes
on orbit or on impact.

**Second-surface radiator skin** (superseded by **passive louver thermal trim**, `sec:louver_thermal_trim`):
The formerly-resolved thermal-control construction for balloon/water-bag PuffSat outer skins: a
clear, halogen-free, UV-tolerant polymer (Kapton, matching the paper's existing JWST
sunshade citation) faces the sun, with aluminum vapor-deposited on its *inner* face rather
than the outer one. Sunlight still reflects off the aluminum (low solar absorptivity
preserved), but the surface radiating to space is the polymer's own, with IR emissivity
around 0.6–0.8 versus bare (first-surface) aluminum's 0.02–0.05. This fixes an
unfavorable α/ε ratio: an isothermal sphere with bare first-surface aluminum (α≈0.1–0.2,
ε≈0.03–0.05) equilibrates near 330–450 K at 1 AU, at or above water's boiling point,
independent of any internal conduction scheme. The second-surface construction drops that
estimate to roughly 186 K, trading an overheating problem for a large cooling margin that
can be dialed back down (partial coverage, material choice) rather than fought from a
deficit. Kapton's UV durability is worse than FEP's over a multi-year mission, but a
PuffSat's exposure is a multi-day coast, not years, so the margin FEP would buy is likely
unnecessary. Not yet backed by a citation for Kapton's or aluminum's exact α/ε values;
flagged for verification before this goes in the paper.
_Avoid_: "metallized skin" without specifying which face carries the aluminum,
first-surface (outward-facing metal) and second-surface (metal on the inner face of a
transparent polymer) give very different emissivity and are not interchangeable.

**Passive louver thermal trim** (in paper, `sec:louver_thermal_trim`, replaces **second-surface
radiator skin** above):
The resolved thermal-control mechanism for all PuffSat variants (icy/water, LOX, balloon), each
at a different target temperature. A movable louver flap adds fine control on top of a body's
baseline reflective coating, driven by one of two passive, self-triggering (no electronics)
actuator technologies: a bimetallic strip, with real flight heritage from Pioneer 10/11's
louvers and Goddard's Dellingr CubeSat, or a nitinol shape-memory wire drawable to single-digit
micron diameters. The actuator senses the PuffSat's own body temperature rather than the flap's
sun-facing side, so a short pull cable separates actuator from flap instead of integrating them.
Both actuator and flap stay light enough, the wire especially so, that neither is a major
shrapnel risk against the pusher plate on its own; a spin-stabilized PuffSat can additionally
reel the whole assembly clear on its tension tether before impact (see **spinning tethered
pair**, `sec:spinning_tension_detail`). Thermal trim also simply stops in the last ~10 minutes
before impact: extended flaps add drag that perturbs the terminal trajectory at low altitude,
and unshaded absorption over that interval only raises a water body's temperature by a few
tenths of a kelvin, negligible against the margin already banked.

### Straw Way vacuum pumping (`sec:vacuum_tube_details`)

**Straw Way wall stack**:
Metallized plastic carrying a roughly 100 nm aluminum inner layer, sized for mass rather than for
vacuum performance (settled 2026-08-19 grill).
_Avoid_: heavy-metal liner, tantalum liner (see Flagged ambiguities; tantalum is not merely
unnecessary here, it breaks the pumping mechanism).

**Reflector skin**:
A few nanometers of iron over the projectile nose, present so that argon has something heavier
than itself to bounce off. Argon is 40 amu, so it cannot backscatter from carbon (17.5 deg maximum
single-collision deflection), oxygen (23.6), aluminum (42.5) or silicon (44.7). Iron, titanium,
calcium, tantalum and tungsten all permit backscatter.
_Avoid_: conflating with the **high-Z cap** of `sec:solid_PuffSats`, which exists for opacity;
defaulting to tungsten (iron is cheaper, and its lower `E_d` costs only window ceiling).

**Displacement threshold (`E_d`)**:
The minimum energy an incoming atom must hand a lattice atom to knock it permanently out of its
site. Below `E_d` the incoming atom bounces off the lattice acting collectively; above it, the
atom displaces its way in. Orientation-averaged values: Al 25 eV, C 30, Fe 40, Ta and W 90.
Directional minima run roughly 40% lower (Fe near 17-20 eV, Al near 16 eV), so every window edge
below carries that spread.
_Avoid_: treating `E_d` as a sharp cliff; it is a threshold with real orientation spread.

**Reflector window**:
The projectile-speed band in which argon reflects off the **reflector skin** and then implants in
the **Straw Way wall stack**. Its floor is set by the wall (the rebounding argon must clear
aluminum's `E_d`) and its ceiling by the skin (the incoming argon must *not* clear iron's `E_d`).
Argon transfers 96-97% of its energy head-on to either Al or Fe, so both edges are sharp in speed:
**6.2 km/s to 14.1 km/s** for an iron skin, rising to 27.2 km/s for tantalum or tungsten. Earth
escape speed at the 200 km interception altitude is **11.01 km/s**, so every bound-orbit arrival
sits inside the iron window automatically, with 28% of margin, and needs no per-source analysis.
Direct interplanetary arrivals do not: Ceres Hohmann lands at 12.70 km/s (inside), Jupiter prograde
Hohmann at 14.09 (at the edge), Saturn at 15.08 (outside iron, inside W).
_Avoid_: quoting the ceiling as a hard number without the `E_d` spread; taking iron's directional
minimum drops it to about 10 km/s, which would put the 11 km/s case just outside.

**Captured-either-way (the claim the paper makes)**:
The robust form of the pumping argument, chosen over the window itself because it survives the
`E_d` spread. Argon is removed from the tube on both sides of the reflector ceiling, only by
different pumps. Below it, argon reflects and implants about 1.5 nm into the aluminum wall. Above
it, argon displaces skin atoms and buries itself in the projectile, which carries it out of the
tube. **Both outcomes occur at every speed** (settled 2026-08-19): backscatter off a heavy cap is
kinematically allowed at any energy, and sub-threshold trapping in the skin happens at low speed
too. Closing velocity shifts the odds between the two, it does not switch between them. The single
genuine failure mode is falling below the **floor**, where the rebound is too soft to enter either
material and the argon rattles around indefinitely. That floor corresponds to a drop from about
3250 km apogee, which nothing in the architecture approaches.
_Avoid_: presenting the two regimes as success and failure, or as mutually exclusive. Reflection
coefficients are probabilities, not switches.

**Noble-gas ladder**:
Which NEG-immune gases the projectile mechanism can bury. Two criteria, and they split the gases
differently. By **displacement** (clearing aluminum's `E_d` on rebound) the minimum projectile
speeds are Xe 4.0 km/s, Kr 4.4, Ar 5.6, Ne 7.8, He 25.9, so only helium fails below Earth escape
speed (11.01 km/s at the 200 km interception altitude). But displacement is the wrong criterion
for a small atom, which can enter **interstitially** without moving anything. Against aluminum's
59 pm octahedral site, He (31 pm) and Ne (38 pm) fit; Ar (71 pm), Kr (88) and Xe (108) do not.
So Ar/Kr/Xe must displace and the `E_d` criterion governs them, while helium has a second door.
_Avoid_: calling helium capture impossible below 25.9 km/s (see Flagged ambiguities; corrected
2026-08-19). The `E_d` criterion bounds displacement, not entry.

**Rebound ceiling (`2V`)**:
Reflection off a body moving at `V` bounds the rebound at `|v_out| <= 2V + |v_in|`, and that bound
does not compound. After one hit an atom moves down-tube faster than the projectiles, so it cannot
be overtaken and struck on the nose again; the next encounter is with a receding tail, which slows
it. Reversing axially needs wall bounces, and those outnumber projectile hits about 66 to 1 even at
1 ktonne/s, so accommodation drains energy faster than projectiles add it. A 4000-atom Monte Carlo
over 10 s peaked at 12.2 eV against helium's 55.6 eV requirement.
_Avoid_: appealing to the tail of the velocity distribution to rescue helium. Thermal spread needs
a 38-sigma tailwind; there is no Fermi-style ratchet to supply the rest.

**Blunt-nose condition**:
Argon reflects specularly, so a local surface normal at angle `theta` to the flight axis returns it
at `2 v cos(theta)` and `cos^2(theta)` of the energy. Wall implantation therefore needs the normal
within about **59 deg** of the axis, i.e. a cone **half-angle above about 31 deg**. A hemispherical
nose delivers about 74% of its swept argon above threshold; a slender needle delivers none. Costs
nothing, since these projectiles transit in hard vacuum.

**Sweep-limited pumping speed**:
`(mdot / projectile areal density) x tube length x capture probability`. Independent of projectile
size, since halving the projectile doubles the count. At 1 kg/s of traffic and 1% capture it is
10^3 L/s, a large turbomolecular pump; at the 1 ktonne/s of `sec:death_star` it is 10^9 to 10^11
L/s. Argon crosses a 3 m bore thermally in 7.5 ms, so successive projectiles sample a fresh draw
rather than re-sweeping a cleared channel. Rate is not what limits this mechanism.

### Lunar disposal (`sec:handling_space_debris`)

**Disposal package**:
The sub-250 g dry-mass remnant of a spent PuffSat, steered to a lunar impact instead of reentry.
_Avoid_: waste, garbage, trash, debris (reserve **debris** for the ejecta it throws).

**Disposal site**:
One of a handful of fixed lunar impact points, spread in longitude so one always sits near the
low-$\Delta V$ approach geometry as the Moon rotates.

**Ejecta trap**:
A roofed disposal site (sintered enclosure or lava tube) whose small aperture subtends a narrow
cone from the impact point.
_Avoid_: baffle, shield. Contrast with **open pit**.

**Open pit**:
An unroofed disposal site, natural crater or excavation, whose rim blocks ejecta launched below
$\arctan(H/R)$ and whose slope relaxes to the 35° angle of repose if unbonded.
_Avoid_: open crater, baffled crater.

**Latitude separation**:
Siting disposal at the lunar equator while settlement stays polar, so 2729 km of arc separates
them.
_Avoid_: geographic separation, polar standoff, antipodal siting (the separation is 90°, not 180°).

**Pole-reach threshold**:
1.53 km/s, 64% of lunar escape speed, the slowest ejecta that can fly equator-to-pole; raised to
1.57 km/s by a 35° rim, and to escape (route closed) by a 67° one.

**Azimuth window**:
The ±5° of launch azimuth about the meridian that reaches latitude 85°+ from an equatorial site,
5.6% of all azimuths; the actual protection **latitude separation** provides.

**Fast tail**:
The ejecta mass fraction launched above the **pole-reach threshold**, the only material that can
reach a polar settlement at all.

### Heliocentric disposal, Jupiter cycle (`sec:jupiter_only_growth`)

**Heliocentric package**:
The dry-mass remnant shed by a Jupiter-cycle PuffSat at the Earth encounter. It keeps the
PuffSat's incoming orbit almost unchanged, because at 60--69 km/s Earth's gravity barely bends it
and the discard kick is metres per second: retrograde, Jupiter-crossing, perihelion *inside* 1 AU,
aphelion at or beyond Jupiter, period 5--9 yr. The Earth encounter is a crossing, not a tangency;
the package arrives with a large inward radial component and continues to a perihelion well below
1 AU. Exact $q$, $Q$, $P$ not yet pinned from the companion repo.
_Avoid_: **disposal package** (reserved for the Earth-orbit remnant steered to a lunar impact; the
heliocentric one is never disposed of), **debris** (reserved for lunar ejecta), "widely dispersed
debris".

**Dispersal ratio**:
The volume argument that excuses the Jupiter cycle from the disposal machinery the LEO cycle needs.
LEO packages stay gravitationally bound inside a shell of order $10^{21}$ m³, the same volume
satellites occupy. Heliocentric packages are unbound and spread through a torus of order
$10^{35}$ m³, about $3 \times 10^{14}$ times larger. That ratio, not the word "dispersed", is the
argument.

**Satellite-collision metric**:
The hazard the heliocentric package population is judged against, chosen 2026-08-11 over two
rejected alternatives (Earth-impact hazard, which is a harmless 70 km/s meteor, and upper-
atmosphere metals loading). At $10^8$ t/yr of PuffSats and a 1% dry-mass fraction, so $10^6$ t/yr
and ~4 billion packages a year, a century of accumulation gives ~$7 \times 10^{-24}$ packages per
m³ near 1 AU: one hit per $10^9$ years on a 100 m² spacecraft, ~0.04 hits/yr across the whole
in-transit fleet. Ignoring the population is the baseline.

**Jupiter phasing**:
The optional route that clears the population instead of ignoring it. The orbit already crosses
5.2 AU twice a revolution, so this is a *timing* problem, not a shape problem, and timing is set by
orbital energy. The burn therefore belongs at **perihelion**, not apoapsis: $\Delta E = v \cdot
\Delta v$, and the package moves 9--18x faster at perihelion than at aphelion. Target is Jupiter's
gravitationally focused capture disk, ~205,000 km radius at a ~22 km/s $v_\infty$, so arrival must
land inside a ~6 hour window.
_Avoid_: "phasing burns at apoapsis" (imports the wrong folklore; apoapsis is cheap for changing
perihelion and plane, not period).

**Sunlight trim**:
The propellantless actuator for **Jupiter phasing**. Sunlight only pushes outward, so a fixed area
cancels itself over a symmetric pass; asymmetric deployment between the inbound and outbound legs
does not. A single flap, of the kind `sec:louver_thermal_trim` already flies, gives a 250 g package
at 0.08 m²/kg about 7 m/s of radial impulse per deep perihelion pass, worth ~3--4 m/s of tangential
perihelion burn and ~5 days of Jupiter-arrival shift. Two orders of magnitude more authority than
needed, so the design problem is throttling it down. Must be **commanded**, not passively
hysteretic: a one-way drift only reshuffles a phase sampling that is already near-random at ~80°
per revolution, so it concentrates no probability on Jupiter and collapses back into ignoring the
population.

### Staged crewed launch (`sec:periapsis_challenges`, closing paragraph)

**Staging carrier**:
The unmanned vehicle that holds *undeployed* PuffSat mass between a Parker-return delivery and the
crewed launch it will feed. It is the "unmanned payload" of the closing paragraph of
`sec:periapsis_challenges`, named. Being uncrewed, it absorbs the full 3.7 g of an 11 km/s solar-dive
push, which is the whole point of staging.
_Avoid_: depot (implies a fixed station), tanker, tug.

**Staging ellipse**:
The 50 km x 150,000 km orbit (`v_p` = 10.916 km/s, period 2.7 d, apogee speed 0.45 km/s) that the
solar-dive PuffSats deliver the **staging carrier** into, and where it parks. Same orbit the PuffSats
themselves fly in `sec:starship_safelaunch`, so no injection burn is ever needed.
_Avoid_: "apogee at lunar distance" (that is the `tab:mass_scenarios` row description; the operational
orbit of line 1444 and the companion sim is 150,000 km. Both happen to give `v_p` ~ 10.916 km/s).

**Arrival-declination floor**:
The lowest inclination a **staging ellipse** can be given for free, equal to the declination of
the solar-dive carrier's incoming hyperbolic asymptote. Choosing where perigee falls around that
asymptote selects the inclination at zero cost, and the same PuffSat collisions that deliver the
boost do the aiming, so upstream aiming beats a plane change. Decided 2026-08-12. Solar-dive
returns run near the ecliptic, so the floor sits near the 23.4° obliquity: every inclination from
there up is free (Cape Canaveral 28.5°, Baikonur 51.6°), and near-equatorial ones are not
(Kourou 5.2°). The paper should state the constraint rather than leave a reader to find it.
_Fallback, priced_: turning the plane at apogee costs `2 v sin(Δi/2)` at v = 0.45 km/s, so 218 m/s
for 28°. Negligible on the 10 t **tracker platform** (~0.6 t) and expensive on a loaded carrier
(~6% of an 850 t wave, ~52 t, every delivery). The asymmetry is the point: let the platform turn,
never the carrier.

**Perigee arming**:
Dropping the parked carrier's perigee from its drag-free parking value back to the 50 km deployment
perigee when a crewed launch is scheduled, and raising it again after. About 31 m/s each way at
apogee, because the carrier is crawling at 0.45 km/s there. This is the "very small rocket" the
Lagrange proposal wanted, and it is small only because the carrier never left the ellipse.

**Storage interval**:
Months, worst case ~0.8 yr, set by the **re-intercept cycle floor**: solar-dive mass arrives in waves
about 0.82 yr apart while crewed launches draw it down continuously. Decided 2026-08-12. It is the
number that binds lunisolar perigee drift, propellant shelf life, and cryogenic boiloff.

**Storable PuffSat**:
The variant qualified to sit in a **staging carrier** across the **storage interval**: water-ice or
ANFO fill, cool gas generator thrusters (`sec:cold_gas_fluid_choice`, line 419), no 60% peroxide
bipropellant and no LOX fill. Decided 2026-08-12. It retracts, for staged flights only, the line 424
premise that "PuffSats are single-use and operate for only half of a single orbit", which is what
licensed the paper to ignore shelf life everywhere.
_Rationale_: ice and ANFO keep indefinitely; airbag generants (guanidine nitrate with basic copper
nitrate) are qualified for ~15 yr of thermal cycling and sit *unpressurized* until fired, so the
storage phase carries no pressurized tank at all. Peroxide is excluded because the paper itself names
"catalytic decomposition and oxygen buildup in a closed volume" as the governing in-flight hazard,
which over months is a slow loss of oxidizer. LOX is excluded because holding 60--80 K through ~50
perigee passes of Earth albedo and IR is a different problem from holding it at 1 AU.
_Sustained-flow debt, discharged_: line 395 makes sustained flow, not total impulse, the binding
cold-gas requirement across the 300 s drag pass, and a gas generator is a one-shot device. The
T³µPS architecture already cited resolves this: generators charge a **plenum** and the plenum meters
sustained flow, firing more generators as pressure falls. The pressurized volume then exists only
during the half-orbit of use, never during storage, which preserves the exact property the storage
case wanted.
_Open_: belt dose. The **staging ellipse** crosses the Van Allen belts twice per 2.7 d period, so a
five-month park is ~100 crossings against deliberately cheap electronics. The mitigation is that
stowed PuffSats are shielded by the carrier hull and by each other, so only the outer layer of the
rack takes full dose. Unsized.

## Relationships

- A **PuffSat** strikes the **pusher plate** (or the **Medusa-style sail**); plate and
  absorber obey the **buffer invariant**.
- **Common-mode error** is cancelled by a **centroid retarget**; only **per-unit
  scatter** must fit inside the **catch radius**.
- **Plate capture** is the success criterion. The claim runs in **feasibility tiers**:
  Tier 1 (5 m) is simulated; **surveyor-anchored centring** is the Tier 2 (~10 cm) path,
  argued not simulated.
- For LEO, the **apogee nav constellation** pins the coast; the **target-side tracker
  array** (plus the **co-flying tracker**, and optionally **PuffSat self-homing**) does
  terminal homing via **differential astrometry**. Together these are the **off-board nav
  assets** that replace the dedicated **coordinator node** of the original paper.
- Near the Sun, lateral knowledge comes from **transverse-node differential ranging**
  with good **GDOP**; control is **deterministic-coast correction**. The **apogee nav
  constellation** does double duty here, since an Earth-to-Sun transfer departs from Earth.
- Straw Way argon pumping runs skin-then-wall: the **reflector skin** bounces argon, the
  **Straw Way wall stack** absorbs it, and **displacement threshold (`E_d`)** sets both edges of
  the **reflector window**. Earth escape speed sits inside that window, so **capture into a bound
  ellipse first, then drop through the straw** turns any interplanetary source (lunar, Ceres,
  Jupiter-cycle secondary payloads) into a guaranteed in-window arrival. The returning Jupiter
  PuffSats themselves arrive retrograde near 69 km/s and are six times outside it.
- Heliocentric distance sets the cryogen via the **passive-shielding temperature law**:
  LOX/methalox inside the **passive-LH₂ threshold** (~1.5 AU), LH₂/LOX beyond it; where a
  stored cryogen is unwanted, **on-demand electrolysis propellant** carries water instead.

## Example dialogue

> **Author:** "If a stochastic atmosphere scatters the whole salvo by a kilometre, doesn't
> that blow the **plate capture** budget?"
> **GNC expert:** "Only if it's **per-unit scatter**. A shared atmosphere is mostly
> **common-mode** — it slides the block as one, and a **centroid retarget** cancels it for
> free. What has to fit the **catch radius** is how the units differ from each other."
> **Author:** "And the catch radius is a sensing limit?"
> **GNC expert:** "No — it's the engine. The sensing limit lives in the **cross-track
> knowledge**, `σ_θ · R`, and that's a calibration bias, not noise."

## Flagged ambiguities

- **Does argon implantation in the tube wall work at the low arrival speeds of lunar, Ceres and
  Jupiter-cycle payloads? - RESOLVED 2026-08-19 (grill): yes, and the mechanism in the paper is
  currently attached to the wrong case.** `sec:vacuum_tube_details` claims argon rebounds off the
  150 km/s projectiles and implants in the wall, citing the sputter-ion pump. Two errors:
  - At 150 km/s argon meets the projectile at 4.66 keV, far above every `E_d`, so it does not
    rebound at all. It buries 5.9 nm into the skin and rides out of the tube. The projectile is
    the pump; the wall gets nothing. A "few nanometers" of iron is a window at this energy, not a
    mirror.
  - At 11 km/s argon meets the skin at 25 eV, below iron's `E_d`, so it does reflect, and reaches
    the wall at up to 100 eV, above aluminum's `E_d`, so it does implant. The paper's stated
    mechanism happens **only** in the low-speed case.
  Depth also needs restating. "A few nanometers" is about right at 100 eV (1.5 nm in Al) but
  understates the fast case by an order of magnitude (34 nm in Al at 18.6 keV). Decision: state
  **captured-either-way** as the claim and use the **reflector window** as supporting detail.
- **Does helium break the pumping story? - RESOLVED 2026-08-19 (grill): no, but not by
  implantation.** Helium needs a 25.9 km/s projectile to clear aluminum's `E_d`, and the
  **rebound ceiling (`2V`)** makes that unreachable below escape speed by any route, including the
  velocity tail. **Corrected later the same session:** that does not make helium capture
  impossible, only uncertain. `E_d` bounds whether an atom can *make* a hole, not whether it can
  *fit through* one, and helium's 31 pm radius clears aluminum's 59 pm octahedral interstitial
  site. Tungsten fuzz forms under 20-60 eV helium plasma, where helium can deliver at most ~5 eV
  against tungsten's ~90 eV threshold, so sub-displacement helium retention is experimentally
  established. Tunneling is not the route (4.5 pm de Broglie wavelength against 286 pm spacing).
  The retained *fraction* stays unknown, since helium is also highly mobile in metals. What saves
  the argument is influx, not pumping. Leak-driven helium sits 5e6 inside a budget
  of 1e-7 mbar per monthly refurbishment cycle. Permeation would dominate through bare polymer
  (bare 50 um PET needs a barrier improvement factor of 123x, Kapton 368x), but a single metallized
  layer buys 100-1000x. Cited in the paper via `baldwin2008helium` (60 eV He loads into W below
  the physical sputtering threshold) and `kajita2009tungsten` (fuzz threshold above 20 eV). Decision: **no dedicated helium pump**; the refurbishment cycle absorbs it,
  and the 100 nm aluminum layer is the helium barrier. Consequence: that layer now carries four
  jobs (atomic-oxygen/UV barrier, magnetic-steering conductor, argon absorber, helium barrier), and
  three of the four require it to stay *continuous*. The refurbishment driver is therefore pinhole
  growth from micrometeorites and sputtering, not bulk erosion, which is not close to binding
  (2.4e21 Ar impacts/m2 to sputter 100 nm away, against 1.8e14 per tube-fill).
- **Should the tube carry a tantalum liner to suppress argon instability? - RESOLVED 2026-08-19
  (grill): no, and the existing sentence must be cut.** `sec:vacuum_tube_details` recommends a
  heavy-metal liner such as tantalum on the sputter-ion-pump analogy (cathode-to-ion mass ratio,
  `vaumoron1970argon`). It fails twice here. It contradicts the mass budget, which wants
  metallized plastic over roughly 100 nm of aluminum. And tantalum's `E_d` of 90 eV exceeds the
  59 eV a 100 eV argon atom can transfer to it, so a tantalum wall would **reflect** the argon
  instead of trapping it, breaking the pumping mechanism outright. Aluminum is both the lighter
  and the better absorber, for the same reason: it is lighter than argon. The `vaumoron1970argon`
  cite was kept, reframed: the cathode-to-ion mass ratio runs the *unfavorable* way for an aluminum
  wall, and what offsets it is the low rebound energy at slow speeds plus the fact that fast
  projectiles carry their argon out rather than leaving it in the wall. The instability worry
  that motivated tantalum also mostly evaporates at low speed, since the Ar-on-Al sputter yield at
  100 eV is 0.05 against a 32 eV threshold, versus 2.5 at 18.6 keV.
- **Does the 3:1 prograde/retrograde optimum survive a real magnetic nozzle? — RESOLVED
  2026-08-17 (grill): no, it is the loss-free endpoint; the paper keeps it and names the
  parameter.** `sec:dv_effective` derived 3:1 assuming the merged fireball leaves as a single
  collimated jet, which is the momentum-maximizing bound for a given mass and energy, not an
  approximation. Reframed via **jet efficiency (`η_jet`)** the optimum is `(4/η_jet²) − 1`,
  moving to ~5:1 at `η_jet = 0.8` and ~7:1 at 0.7. Decision: **keep 3:1 as the stated result**,
  because it answers the idealized question, because the peak is flat (holding 3:1 costs ~1% of
  achievable thrust at `η_jet = 0.9`, ~6% at 0.8, ~18% at 0.7), and because the downstream
  mission numbers already assume a lossy nozzle at that mix. A ~5:1 minimax split would stay
  within 4% across `η_jet ∈ [0.7, 1.0]`, so the *design* bias runs prograde even though the
  *derivation* stays at 3:1. Two corrections fell out and were applied:
  - The center-of-mass motion of the merged fireball does **not** need re-thermalizing. It
    carries a fraction `m_rp` of the energy (25% at 3:1), already points retrograde, and its
    momentum exactly equals the incoming projectile's, so alone it yields **zero** net thrust.
    All thrust comes from collimating the thermal `1 − m_rp` share. That is the nozzle's job,
    and roughly half of that heat starts out moving *toward* the ship and must be mirrored.
  - `sec:methalox_rebuttal` conflated `v_g` with `v_e` at the Earth step, assuming 25 km/s
    where the head-on ideal ceiling is 24. Corrected; the headline ~$3/kg survives at
    `η_jet = 1`, but break-even against methalox now sits at `η_jet ≈ 0.89`.
  - A later review found that the cost cascade had inserted `v_e`, defined per total collision
    mass, into a conventional rocket equation even though the retrograde share arrives
    externally. The corrected mass ratio is `eq:external_reaction_mass`. It is strictly below
    `exp(Δv/v_e) − 1` at any `m_rp` in `(0,1)`, so the correction **lowers** the collision mass
    a burn needs and makes every cascade step cheaper. At full precision the ideal one-way cost
    falls from $3.32/kg to $3.20/kg, and break-even falls from 0.9007 to 0.8906. Any restatement
    of this correction that shows the cost *rising* is comparing a rounded old number against a
    full-precision new one.
  _Still open_: (1) no nozzle model supplies `η_jet`; the required 0.89 at the pessimistic
  anchor is asserted as a requirement, not estimated. (2) The magnetic pressure needed at the
  throat to mirror the ship-facing half of the fireball is uncomputed, and belongs with the
  deferred radiation-hydrodynamic calculation of `sec:solid_PuffSats`. (3) What published
  magnetic-nozzle results say about 0.89 was checked 2026-08-17: Ahedo & Merino
  (`ahedo2010magnetic`, already cited) report plume efficiency 0.63-0.83. Its square root gives
  a divergence-only ceiling near **0.79-0.91**. The 0.89 the pessimistic anchor needs sits near
  the top of that band. This reopened the 5:1 option (its six-fold rather than four-fold dilution
  of the expensive retrograde mass moves methalox break-even to `η_jet ≈ 0.80`) and the
  decision was **reaffirmed at 3:1**, because 0.89 is a rhetorical break-even at a $3200/kg
  early-generation projectile price, not a physics or architecture requirement. Recorded as
  `docs/adr/0006-three-to-one-split-stays-at-the-loss-free-optimum.md`.

- **Where does staged PuffSat mass park between delivery and use? — RESOLVED 2026-08-12
  (grill): the staging ellipse, not a Lagrange point.** The proposal was to park incoming
  PuffSat mass (and the reusable co-flyer carrying it) at Sun-Earth or Earth-Moon Lagrange
  points, with small rockets pushing it into the deployment orbit when needed. Rejected on
  angular momentum. The **staging ellipse** and the Earth-Moon Lagrange points sit at nearly
  the same *energy*, so the entire cost of moving between them is angular momentum: the
  ellipse crawls through apogee at 0.45 km/s while the Lagrange points sweep around Earth at
  0.87 (EML1) to 1.02 km/s (EML4/5). Round-trip costs, two-body coplanar, from the ellipse:
  - EML1/EML2 halo: ~0.88 km/s in, ~0.65 km/s out, ~1.5 km/s round trip, roughly 35% of the
    loaded carrier as methalox. Buys lunar-ISRU propellant access and a quiet thermal
    environment.
  - EML4/EML5 (the stable pair of `sec:handling_space_debris`): ~0.83 km/s each way plus a
    phasing wait, since departure is locked to 60° from the Moon.
  - Sun-Earth L1/L2: ~90 day transits, so ~2 flights/yr per carrier. Cadence is the killer.
  - Staging ellipse: 0 m/s to insert (it is already there), ~31 m/s of **perigee arming**
    each way, and it returns to apogee every 2.7 days for free.
  The reusability the proposal wanted therefore comes free from the ellipse's own period.
  Note the paper's Lagrange numbers in `sec:handling_space_debris` (0.5 km/s to EML1, 0.18 km/s
  to EML4/5) are computed for a package *falling from the 900,000 km turnaround* and do not
  transfer to a departure from the staging ellipse.
  _Shell crossings, answered 2026-08-12_: the ellipse's one real defect is that it sweeps the
  LEO and GEO belts every 2.7 days with a loaded carrier, and `sec:handling_space_debris`
  line 543 sells the lunar disposal route on precisely the opposite property ("never descends
  through the low Earth orbit and geostationary belts"). The reconciling distinction, which the
  paper does not yet draw and should: **line 543 is an argument about *uncontrolled* objects.**
  Disposal packages are inert, uninstrumented, and arrive billions per year, so they can never
  participate in conjunction avoidance. Carriers and the **tracker platform** are few, tracked,
  and maneuverable. Precedent for long-duration eccentric orbits crossing both belts is Molniya
  (perigee ~500 km, apogee ~40,000 km, twice daily, decades, dozens of spacecraft) and every
  GTO ever flown. Priced and held in reserve if the population number comes out badly: raising
  the parking perigee above the LEO debris shell to ~2500 km costs ~75 m/s each way (per-flight
  budget 50 -> 150 m/s, still ~20 flights per load); parking clear of LEO at ~10,000 km costs
  ~247 m/s each way (~5--6 flights per load, and it still crosses GEO).
  _Still open_: (1) the steady-state carrier population, which is the number the controlled-vs-
  uncontrolled argument owes. (2) Lunisolar perigee drift across the **storage interval**,
  unsized: at 150,000 km apogee the carrier sits at 39% of lunar distance, and months of
  third-body tugging moves perigee by an amount nobody has computed. It sets the parking
  perigee margin, so it also sets the per-flight budget above.

- **Should the load-bearing terminal sensor move from the target to the co-flyer? —
  RESOLVED 2026-08-12 (grill): split by phase, fused, handover at 2--3 s to impact.**
  The co-flyer is load-bearing from deployment down to roughly 2--3 s before impact; the
  **target-side tracker array** takes over inside that, and the two are *fused* rather than
  switched. Motivation for reopening: the target is disturbed by propellant slosh, repeated
  PuffSat impacts, and its own RCS/gimbal corrections between pulses, while the co-flyer is a
  quiet platform. What decided it:
  - The target-side array looks straight down the approach corridor, so its blind axis is the
    **miss plane**'s *timing* component. Both real miss axes are observable at every instant,
    with no singular geometry, by construction. A co-flyer never has this.
  - `σ_θ·R` collapses for the target because `R → 0` at impact, and does not for the co-flyer
    whose standoff `D` is roughly fixed. The target-side array at its nominal 1.6 µrad beats a
    50 mas co-flyer inside 45 km. The terminal phase *is* those last seconds.
  - The target's degraded conditions and its relaxed requirement coincide. Impact gating only
    exists once impacts are happening, which is when `R` is already small enough that the
    existing grade delivers centimetres. A **10× platform degradation still delivers 10 cm with
    0.57 s to spare.** This is a far stronger defence of the current architecture than the
    shock-isolator-and-Copperhead argument the paper actually makes, and it should replace it.
  - 2--3 s is simultaneously the metrology crossover and roughly the *control* horizon (a 10 cm
    divert takes 0.3--0.6 s to execute), so nothing is lost by handing over there.
  Sizing that falls out: the handover time pins the co-flyer at **~25--35 mas**. Below ~30 mas
  the co-flyer is **registration-limited** by the cm-class body-beacon-to-plate chain, not
  optics-limited, so Gaia-class metrology buys nothing. Build the 30 mas scope and spend the
  rest on absorber metrology.
  _Avoid_: the paper's current claim that the co-flyer "shortens `R`" for *terminal* homing.
  True in mid-course, false in the terminal phase where the target is nearer by construction.
  Also settled along the way:
  - The measurement must be **plate-beacon differencing**, not absolute line-of-sight
    (registration to the plate is otherwise ~2 m and eats all of Tier 1).
  - The **star channel decouples from the 1 ms beacon gate** (10–100 ms free-running star
    exposure on its own detector, gyro bridging to each beacon epoch). This is the actual
    reason a quiet platform wins: star *photons*, not vibration immunity. It is impossible
    on the impact-hammered target and easy on the co-flyer.
  - Vantage must satisfy the **miss plane** geometry: primarily along-track offset, with
    `x ≈ h`. A purely radial offset (the "350 km vs 200 km periapsis" idea) is blind in the
    radial miss axis unless paired with a comparable along-track offset.
  - Sizing: `σ(radial) = 2·h·σ_θ`. At `h` = 150 km, Tier 1 (~2 m) passes at any grade
    considered; Tier 2 (~10 cm) needs `σ_θ ≤ ~69 mas`, so the paper's current 330 mas fails
    and the premise 100 mas also fails. ~50 mas closes it. A half-metre-aperture, ~2–5 m
    focal-length scope reaches ~5–8 mas on rough photon-budget grounds, i.e. Tier 2 is not
    metrology-limited once the co-flyer exists.
  - The co-flyer's overflight singularity is real geometry but operationally harmless. Riding
    the PuffSat orbit at 10.8 km/s past a target accelerating 0→8 km/s, it sweeps ~2040 km of
    along-track offset per 300 s push and must transit `x = 0`, where the radial axis goes
    singular for ~50 s (~150 of ~900 units). It does not matter, because the mid-course only
    has to deliver into the **catch radius** (475 m against a 224 m entry spread), and even the
    worst overflight moment gives ~1 m.
  - Which disturbances actually threaten a 1 ms exposure, by frequency: **slosh (~0.9 Hz) does
    not** (0.33° of phase across the exposure, so constant rate, which centroids at mid-exposure
    and differences away like a rigid shift). RCS ringing (5--100 Hz) and impact ringing
    (hundreds of Hz) do. Slosh instead lands on the body-beacon-to-plate registration leg, which
    matters more now that the beacon has moved onto the body.
  Still open: the co-flyer's station-keeping and phasing against an accelerating target, and
  the migrated error terms below.
- **Terms that bind once `σ_θ·D` drops under ~1 cm — NONE ARE SIZED ANYWHERE
  (raised 2026-08-12 grill).** Listed in rough order of how badly they are neglected:
  *PuffSat beacon to gas-momentum centroid.* Tier 2 assumes "the PuffSat's position" is
  meaningful at 10 cm. The PuffSat is a balloon that atomises, the plate receives a gas
  cloud's momentum centroid, and the beacon rides on the dry-mass package that detaches or
  passes through the plate aperture before impact. `sec:spinning_tension_detail` already
  concedes the beacon sits off the aim line and fixes it with an accelerometer reading
  tether-pull direction, but that fix is sized for metres.
  *Loop latency.* At 11 km/s, 1 µs = 1.1 cm and light-time alone from a 1000 km standoff is
  3.3 ms = 37 m. Tolerable only because the measured state is ballistic and predictable, but
  that shifts the requirement from position knowledge to *velocity* knowledge.
  *Light-time lead.* The beacon appears displaced by `v_rel/c` ≈ 7.57 arcsec, independent of
  range. Deterministic, but needs `v_rel` to 0.027% to leave 1 cm.
  *Differential stellar aberration.* ~130 mas per degree of field angle at 10.8 km/s, i.e.
  larger than the whole 100 mas premise. Deterministic given co-flyer velocity to ~1%.
  *Differential distortion across the dichroic.* The paper's star-differencing argument says
  "the same front optics" cancel distortion, but beacon and stars land on **different
  detectors through different back-end paths** behind the splitter. Only the front element is
  common. Plausibly the true floor; unsized.
  *Plate-beacon to plate-centre structural/thermal flex.* mm–cm class, unmeasured.
- **Is the 1.6 µrad floor noise or bias? — OPEN (raised 2026-08-12 grill).** The paper
  insists it is a fixed calibration bias ("a bent ruler", averaging cannot help), while this
  glossary describes it as a "common-mode floor" reached by "√N" fusion, which is noise-like
  language. A rough photon budget (10 cm aperture, 1 ms exposure, ~20 stars) lands near the
  same few-hundred-mas value, which suggests the paper's own floor may be star-photon shot
  noise mislabelled as bias. If so the paper is *understating* its margin, since noise
  averages and bias does not. Needs decomposing in the companion sim.
- **Jupiter-cycle dry mass: which hazard? — resolved 2026-08-11 (grill).** The metric is
  **satellite collision**, and by that metric the population is ignorable by many orders of
  magnitude (see **satellite-collision metric**). Two alternative framings were raised and set
  aside. Earth impact is a harmless 70 km/s meteor. Upper-atmosphere metals loading is *not*
  obviously ignorable: if $10^{-4}$ to $10^{-3}$ of the population eventually reenters, that is
  100--1000 t/yr of mostly-aluminium ablation against a natural aluminium influx near 600 t/yr, on
  top of the burden `murphy2023metals` already measures. Deliberately out of scope for this
  paragraph; it is the objection a reviewer is most likely to raise, and the reentry fraction is
  the single number that would decide it. Salvage (a cislunar depot) is closed: the packages arrive
  at 40--70 km/s relative to everything near Earth, so the Moon and the Lagrange points are
  unreachable for them, unlike for the Earth-orbit **disposal package**.
- **"centimetre centring" vs "plate capture"** — resolved: **plate capture** (about 2 m
  on the 5 m plate) is the *committed* requirement; centimetre precision is achievable
  *capability* and an optional later tightening (surveyor-anchored centring), not the bar
  the baseline must clear.
- **"coordinator node" — resolved 2026-06-30 (grill).** No dedicated per-mission co-flying
  coordinator satellite is needed for LEO. The role is redistributed into the **off-board
  nav assets**: a permanent **apogee nav constellation** (one-way broadcast) for the coast,
  and a **target-side tracker array** + reused-rocket **co-flying tracker** for terminal
  homing, optionally backed by **PuffSat self-homing**. The companion control sim closed
  this at the 5 m (Tier 1) level. "Coordinator node" is now a *legacy* term for the original
  co-flying-brain framing; name the specific asset instead. The rewrite landed 2026-07-02
  as `sec:sensor_architecture` (grill session; see the **Apogee nav constellation**,
  **Target-side tracker array**, and **PuffSat self-homing** entries for the decisions).
- **Medusa "behind" = tension** was a slip; the behind-mounted sail is in
  **compression**. Real Medusa (front-mounted) is tension.
- **"hydrolyze" → "photodissociate"** (resolved 2026-06-30, §8 ozone subsection
  `sec:ozone_policy`). Water released by PuffSats at ~200 km is destroyed by
  **photodissociation / photolysis** (solar UV splits H2O into H + OH, the H escapes to
  space), *not* hydrolysis. Use "photodissociate" for any upper-atmosphere water-breakup
  claim. The ozone it could threaten sits in the stratosphere at 15--35 km, far below the
  200 km release.
- **"launch" applied to the rocket plane — RESOLVED 2026-08-13 (grill): it never launches, it
  takes off.** Every rocket-plane departure is an ordinary runway takeoff from an existing
  urban airport; the rockets first fire at ~12 km, one **ignition standoff** downrange. The
  distinction is load-bearing, not cosmetic: the liftoff roar (full thrust at zero altitude
  over a hard reflecting pad, radiating for tens of seconds at close range) is what dominates
  the complaint record at Starbase and Vandenberg, and this architecture has no such event at
  all. Reserve "launch" for Starship. Use **takeoff**, **transit leg**, **ignition point**.
- **Can the E2E noise critique be made on cumulative exposure (DNL)? — CLOSED NO, 2026-08-13
  (grill).** Tempting, because Musk tied his own 30 km figure to "frequent daily flights," and
  the FAA regulates residential compatibility at DNL 65 dB. The blocker is propagation
  uncertainty past 10 km. Gee's group describes the decay beyond 10 km as "sporadic" and
  meteorology-driven, and reports A-weighted sound exposure at 35 km coming in **18 dB below**
  the FAA Environmental Assessment model. Carrying that spread through the DNL arithmetic at
  30 km gives **7.8 events/day** to reach DNL 65 under naive spherical extrapolation and
  **491 events/day** under the full 18 dB haircut. A 63x swing settles nothing, and any
  referee who knows these papers will say so. The paper therefore argues cadence from
  institutional precedent instead: the California Coastal Commission rejected **50 Falcon 9
  launches per year** at a site with a 15 km buffer (overridden federally), against Shotwell's
  projected dozens per day. No estimate required. Reopen only if measured SEL-vs-distance
  data past 20 km is published; the figure exists in the Flights 5/6 comparison paper but the
  numbers were not extractable from the open-access text.


## P21 radiation accounting accepted after the nozzle handback review

The current paper uses the companion's in-nozzle energy integral directly.
`radiance.py` at impact-simulation revision `6fe8cf3` integrates each parcel's
emission over its transit. It retains `AREA_RATIO_EXIT = 4.0`, chamber radius
3.0 m, field length 23.8 m, and the original water histories. These are not the
12 T capped expansion calculations, the adopted 11 T nozzle, or an argon solve.
Radiative cooling is not fed back into the flow.

| Closing speed | Frozen emission, MJ/kg | Equilibrium emission, MJ/kg |
| --- | ---: | ---: |
| 45.58 km/s | 0.99 | 3.55 |
| 56.53 km/s | 1.77 | 12.03 |
| 65 km/s | 2.19 | 6.10 |
| 75 km/s | 2.65 | 4.35 |

For 238 kg per pulse at 2 Hz, multiply by 0.476 to get GW emitted inside the
nozzle. Frozen power is 0.47--1.26 GW; equilibrium power is 1.69--5.73 GW.
The largest case emits 2.863 GJ per pulse at 56.53 km/s, against 35.750 GJ of
dissipated collision energy (reduced mass 25*213/238 kg). Its share is 8.009%,
not P21's 4.55% from using a common 62.9 GJ denominator. That denominator belongs
to the 75 km/s case. Do not multiply already-in-nozzle energy by `phi` again.

Emission is not absorbed liner power. The 585 MW booked ablation capacity covers
all intercepted radiation in the maximum case only below about 10.2% absorption.
This does not preclude radiative heat rejection, but neither the integral nor a
wall-area ratio establishes a liner temperature or a shield count. Supersedes
historical claims in this file that the corrected 380 MW is an upper bound or
that all radiation leaves with the booked carbon. The appendix retains 380 MW as
an assumed conduction load and 1150 K as a separate assumed gap-radiation example;
neither is a computed water/argon state. The 449 m^2 reference area gives about
4.4 MW gap exchange at graphite/aluminium emissivities 0.85/0.1, or about 13 MW
if aluminium emissivity is 0.3, neglecting its temperature as in that example.


## P23 mission objective and loading policy clarified

Accepted in the paper review, from `aim_is_all_you_need` at `b4ddcf0`.
`two_wave_growth.price_chain` maximizes compounded growth across the flown chain
with a common departure ratio. `two_leg_nozzle_sweep.price_chain_two_leg` permits
separate ratios for the two legs, holds each fixed across cycles, and maximizes
sum(log(cycle growth)) subject to ignition and launch-return constraints. Neither
optimizes a pulse-by-pulse loading schedule. This answers P23's objective question;
it does not adopt a new slug ratio or schedule.

At fixed other loss factors, the chemistry-only gross-momentum factor is
`sqrt((1+k) - 2 E_a (1+k)^2/w^2)`. With E_a=50.9 MJ/kg and w=45.58 km/s,
its optimum is k=9.20401; k=8.52 is 0.224927% below the maximum. Moving to k=5.2
reduces that gross momentum by 7.812997%, even while eta_chem rises. These figures
are not mission growth optima. Pulse-speed fractions and the expansion/ship-frame
efficiency mapping remain separate open questions.
