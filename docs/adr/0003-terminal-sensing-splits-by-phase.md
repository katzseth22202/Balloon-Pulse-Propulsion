# Terminal sensing splits by phase: co-flyer to 2-3 s, target-side array inside that

Status: proposed (the co-flyer's ~30 mas grade and the whole registration chain are
estimates from the 2026-08-12 grill; none are bench numbers)

The paper puts the load-bearing terminal sensor on the target
(`sec:sensor_architecture`), and the obvious objection is that the target is the worst
platform on the mission. It sloshes, it is struck at a few hertz by hypervelocity gas,
and it fires its own RCS and gimballed main engine between pulses to trim torque. The
co-flyer, the spent carrier that deployed the PuffSats near apoapsis, is quiet by
comparison. We decided **not** to move the load-bearing measurement to the co-flyer.
Instead the co-flyer carries it from deployment down to roughly **2 to 3 seconds before
impact**, the target-side array carries it inside that, and the two are **fused rather
than switched**. The reason is not sensor quality. On raw angular precision the co-flyer
wins by an order of magnitude. It loses on geometry and on range collapse, and both are
structural rather than fixable.

This needs recording because the obvious future "fix" is to finish the job and take the
sensors off the target entirely, which quietly gives up a non-singular vantage and a
`1/R` advantage that no optic can buy back.

## Why the target-side array cannot be retired

**Observability.** Miss lives in the plane perpendicular to the relative velocity, which
holds two components: radial (altitude) and cross-track. The third component, along the
relative velocity, is *timing*, not miss. Any tracker is blind along its own line of
sight. The target-side array looks straight down the approach corridor, so its line of
sight is parallel to the relative velocity and **its blind axis is the timing axis**.
Both real miss components are observable at every instant, with no singular geometry,
by construction. No off-board vantage has this property.

**Range collapse.** Cross-track knowledge is `sigma_theta * R`. The target's `R` goes to
zero at impact; the co-flyer's standoff `D` does not. At the paper's existing 1.6 urad
the target-side array delivers 1.6 cm at 10 km and 0.16 cm at 1 km. A co-flyer at a
150 km standoff needs 10 mas to reach 1.45 cm and can never do better than its
registration floor.

**The disturbance and the requirement relax together.** The 1 ms exposure is forced by
impact gating, and impact gating exists only once impacts are happening, which is exactly
when `R` is small enough that the existing grade already delivers centimetres. A **tenfold
platform degradation, to 16 urad, still delivers 10 cm with 0.57 s to spare.** This is a
stronger defence of the target-side array than the shock-isolator and Copperhead argument
the paper currently makes, and it should replace it.

## Why the co-flyer is nonetheless load-bearing for the other ~297 seconds

The co-flyer's advantage is **integration time, not immunity to shaking**. On the target,
the star channel and the beacon channel are both locked to the 1 ms impact gate, so the
reference star field is built from a millisecond of photons. On the co-flyer the two
channels decouple: the beacon channel stays 1 ms and gated, while the star channel runs
free at 10 to 100 ms on its own detector, with a gyro bridging to each beacon epoch.
Star photons scale as `1/(D * sqrt(t))`, so this is worth a factor of 10 to 40 and it is
simply impossible on an impact-hammered mount. Aperture compounds it: a spent stage can
host one 0.3 to 0.5 m aperture at 2 to 5 m focal length where five distributed detectors
on a mass-critical target cannot.

## Sizing that falls out

- Handover at 2 to 3 s pins the co-flyer at **~25 to 35 mas**. A 0.3 to 0.5 m aperture at
  2 to 5 m focal length reaches roughly 5 to 8 mas on a photon budget, so this is not a
  stretch.
- **Below ~30 mas the co-flyer is registration-limited, not optics-limited.** Its estimate
  must be referred to the plate through a cm-class chain, so at 2 cm registration a 30 mas
  co-flyer totals 4.8 cm and a 3 mas co-flyer still totals 2.05 cm. **Gaia-class metrology
  buys nothing here.** Build the 30 mas scope and spend the rest on absorber metrology.
- Optimum vantage is `x = h` (45 degrees elevation), giving `sigma(radial) = 2 * h *
  sigma_theta`. A purely radial offset, such as flying at 350 km periapsis over a 200 km
  interception, is blind in the radial miss axis unless paired with a comparable
  along-track offset.
- 2 to 3 s is also roughly the **control** horizon. A 10 cm divert at 0.5 to 2 m/s^2 takes
  0.3 to 0.6 s to execute, and `sec:sensor_architecture` already concedes that block
  corrections take seconds. Knowledge keeps sharpening past the point the PuffSat can act
  on it, so nothing is lost by handing over there.

## Considered options

- **Co-flyer takes the terminal role outright, target sensors removed. Rejected.** Loses
  the non-singular vantage and the `1/R` collapse. The target-side array at 1.6 urad beats
  a 50 mas co-flyer inside 45 km, which is the whole terminal phase.
- **Two co-flyers offset in along-track, to cover the singularity. Rejected as
  unnecessary.** The singularity is real but harmless (see below), and a second
  instrumented carrier with its own phasing and cross-registration is a large cost for it.
- **Status quo, target-side load-bearing throughout with the co-flyer as an explicit
  hedge. Rejected.** It leaves the decoupled-exposure gain unclaimed, which is the largest
  free margin in the sensor architecture.
- **Absolute line-of-sight from the co-flyer plus separate registration. Rejected.** The
  paper prices the co-flyer-to-target vector at roughly 2 m by GNSS, which alone consumes
  the entire Tier 1 tolerance. The measurement must instead be a **differential angle**
  against a beacon on the target, so the co-flyer's absolute position cancels to first
  order and only the scalar range `D` is needed.
- **Beacon on the plate rim. Rejected.** `sec:lightweight_pusher_plates` sprays about
  0.1 kg/s of ablative onto the plate every pulse, 25 to 50 kg over the mission, onto the
  surface being struck by design. The beacon goes on the vehicle body forward of the plate
  instead. The absorber stroke is longitudinal and the miss is lateral, so several metres
  of stroke costs almost nothing to first order.
- **A dedicated 50 g GNSS receiver on each PuffSat. Rejected.** Considered as an
  independent non-optical leg rather than for precision. 50 g does close a dual-band
  carrier-phase receiver, but **antenna phase-centre variation caps it at centimetres**:
  a 20 to 40 g patch has 5 to 20 mm of PCV across its hemisphere, and sub-mm PCV is what
  kilogram-class choke-ring antennas exist for. There is no mass-efficient version. Three
  further problems. The PuffSats **spin** at up to 0.74 rad/s, so a hemispherical antenna
  sweeps each GNSS satellite below its own horizon every ~8.5 s, and carrier-phase integer
  ambiguity resolution needs minutes of unbroken lock, so spinning units fall back to
  code phase at metres. Usable geometry exists only in the last few minutes of descent,
  since the PuffSat is above the constellation for nearly all of its two-day coast. And the
  leg is **weakest exactly where it would be called on**: at R = 1 km the target-side array
  gives 1.6 mm against GNSS's 2 cm, while the coast, where GNSS would be competitive,
  already has a non-optical leg in the Ka-band apogee constellation. Cost avoided: 50 g
  across ~900 units is 45 kg more non-volatile hardware per mission to dispose of, a 20%
  increase on the 250 g dry mass. Note that baseline length was **not** the objection.
  GRACE determines a 220 km baseline to ~1 mm with dual-frequency GPS, so 10 km inter-unit
  spacing is comfortably within demonstrated practice.
- **Chaining relative positions unit-to-unit instead of measuring each against the target.
  Rejected.** Unnecessary if every unit has an absolute fix, and harmful otherwise: ~900
  hops random-walk as `sqrt(N)`, reaching 3 cm even at 1 mm per hop and 30 cm at 1 cm per
  hop. The chain also still needs an absolute anchor at one end, which is the target, so it
  relocates the weak link rather than removing it.
- **Radio echo transponder plus multi-band ranging on each PuffSat. Rejected.** At the
  recommended 45 degree geometry neither miss axis is blind, so there is no gap to fill.
  If the line-of-sight axis is ever wanted, the **optical beacon is already a ranging
  signal**: the PuffSat's clock is disciplined by the apogee constellation, so its pulse
  emission epoch is known and the co-flyer timing arrival gets one-way range directly.
  That needs no transmitter, no transponder, and no reversal of the receive-only PuffSat.

## Consequences

- The target gains a **strobed reference beacon on the body forward of the plate**, and
  the shock absorber gains **stroke and lateral-pose instrumentation** so the body-to-plate
  vector is known. Multi-metre stroke at cm accuracy is routine for LVDT or magnetostrictive
  sensors, so this is cheap, but it is new hardware that does not appear in the paper.
- Slosh moves from the metrology budget to the **registration** budget. At about 0.9 Hz it
  advances only 0.33 degrees of phase across a 1 ms exposure, so its rate is constant over
  the exposure and it centroids at mid-exposure and differences away like a rigid shift.
  It is the wrong worry for the camera. It is a real worry for body-to-plate structural
  flex. What does threaten a 1 ms exposure is RCS ringing at 5 to 100 Hz and impact ringing
  at hundreds of Hz.
- **The co-flyer's overflight singularity is accepted.** Riding the PuffSat orbit at
  10.8 km/s past a target accelerating from 0 to 8 km/s, it sweeps about 2040 km of
  along-track offset per 300 s push and must transit `x = 0`, where the radial axis goes
  singular for roughly 50 s, about 150 of some 900 units. This does not matter, because
  mid-course only has to deliver into the 475 m catch radius against a 224 m entry spread,
  and even the worst overflight moment gives about 1 m.
- **The paper's claim that the co-flyer "shortens `R`" for terminal homing is wrong and
  must be fixed.** It is true in mid-course and false in the terminal phase, where the
  target is nearer by construction.
- The co-flyer stops being a hedge, so `CONTEXT.md`'s "not required for the 5 m capture
  verdict" no longer holds for the mid-course. Tier 1 should be re-checked with the
  co-flyer removed to confirm the fallback still closes.

## Open (unverified inputs)

1. **The ~30 mas co-flyer grade** is a photon budget over assumed aperture, focal length,
   pixel pitch and star density. Not a bench number, and not simulated.
2. **Differential distortion across the dichroic.** The star-differencing argument says the
   shared front optics cancel distortion, but beacon and stars land on different detectors
   through different back-end paths. Only the front element is common. Plausibly the true
   angular floor. Unsized.
3. **The registration chain** from body beacon through instrumented absorber to plate
   centre. Assumed cm-class. Unsized, and it is what caps the co-flyer.
4. **Plate rock.** Off-centre impacts up to 2 m torque the plate on its absorber. A crude
   estimate gives 2 to 18 cm of lateral plate-centre shift depending on strut torsional
   stiffness, which is not specified anywhere. Self-stabilising in the good regime, since
   tighter centring means smaller off-centre hits, but it sits directly on the 10 cm budget.
5. **Whether the 1.6 urad floor is noise or bias.** The paper calls it a fixed calibration
   bias that averaging cannot improve. `CONTEXT.md` describes it as a floor reached by
   `sqrt(N)` fusion, which is noise language. A rough photon budget for a 1 ms star field
   at 10 cm aperture lands near the same value. If it is noise, the paper understates its
   own margin.
6. **What "the PuffSat's position" means at 10 cm.** The beacon rides the dry-mass package
   that detaches or passes through the plate aperture before impact, while the plate
   receives a gas cloud's momentum centroid. ADR 0002 already measures the tether kink for
   this, sized for metres. Nothing sizes it for centimetres.
7. **Co-flyer station-keeping and phasing** against a target whose orbit changes every pulse.
8. **Light-time lead and differential aberration.** Both deterministic and both currently
   unmodelled: the beacon appears displaced by `v_rel/c`, about 7.57 arcsec independent of
   range, and differential stellar aberration runs about 130 mas per degree of field angle
   at 10.8 km/s, larger than the whole measurement budget.

## Numbering note

`CONTEXT.md` cites ADR 0019, 0020 and 0022, but `docs/adr/` holds only 0001 and 0002.
Those decisions currently exist as glossary prose. This file takes 0003, the next free
sequential number, rather than guessing at the cited scheme.
