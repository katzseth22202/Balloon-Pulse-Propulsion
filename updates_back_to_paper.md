# Updates to fold back into the paper

Working checklist of edits to reconcile into `templateArxiv.tex`. Check items off
as they land in the paper. Organized **by paper destination** (sections in the
paper's own order, each headed by its `\label{}`).

**Legend** — each item carries a provenance tag:

- `[SIM]` — closed-loop simulation result (control sim, Rungs A–D, closed out
  2026-06-15/16). Hard numbers, not sizing.
- `[sizing]` — order-of-magnitude or hand derivation (Medusa/plate trades,
  periapsis nav, near-Sun option menu).
- `[raw]` — quick reconciliation note, rough idea not yet worked through.
- `[decision]` — a choice to make before the edit can be drafted. See the
  "Decide before editing" box; dependent items are flagged `(blocked on Dn)`.

Convention: a finding is a parent checkbox (headline + tag + `→ sec:label`),
nested sub-checkboxes for its discrete edits, and the full prose indented beneath.
Short `[raw]` notes are single checkboxes. Prose is preserved verbatim from the
original handoff notes; style cleanup happens when each lands in the paper.

---

## When you sit down to write

Standing instructions for turning a checked item into paper prose. These are *how*
we edit; the items below are *what*.

- **Voice — define, then use.** Pair each technical term with a plain-language gloss
  on its *first use*, then keep the precise term and the math. The goal is a
  blog-readable explanation that loses no rigor (e.g. "periapsis, the orbit's low
  point where the probe skims closest to the Sun and moves fastest"). Applies to
  prose we add and to any paragraph we are already editing — not to untouched
  sections.
- **Citations — chase them, for outside-world facts.** When a claim is about the
  external world (a prior mission, a physical constant, a cost, a date, a material
  property), find a real source and cite it. Do *not* attach citations to our own
  sizing/derivations or `[SIM]` numbers; those point to the companion calc repo
  (`katzseth22202/aim_is_all_you_need`) or stay labelled as speculative. If no
  credible source exists, leave an inline `% TODO-CITE: ...` marker — never
  fabricate one. No Wikipedia (see the `CLAUDE.md` bibliography rules).
- **AI smells — see `CLAUDE.md`.** The writing-style blocklist (no em-dashes in the
  paper, banned vocabulary, no rule-of-three, short sentences, quantify don't hedge)
  lives in `CLAUDE.md`. Follow it there; do not duplicate it here.
- **Match the claim to its tag.** This is a *speculative* white paper, so keep the
  epistemic status visible: `[SIM]` → "the closed-loop simulation shows",
  `[sizing]` → "a first-order estimate gives", `[raw]` → "we expect / we speculate".
  Never let a sizing argument read like a measured result.
- **Use the canonical terms.** Draft with the canonical names from `CONTEXT.md` and
  avoid the listed aliases — "PuffSat" not "pellet"; "plate capture" (≈ 2 m on the
  5 m plate) as the committed bar, not "centimetre centring".
- **Figures — only where a drawing beats a paragraph.** Suggest one sparingly, with a
  one-line note on what it must show. Highest-value candidates already visible:
  - front-vs-rear overtaking geometry + fail-safe shielding (why the buffer rides
    behind the rocket);
  - common-mode block-slide (cancelled by a centroid retarget) vs per-unit scatter
    that must fit inside the catch radius;
  - transverse-node GDOP near the Sun (anchor off to the side; σ_lateral ≈
    σ_range / sin θ).
- **Build before you check the box.** After an edit lands, run `./build.sh` and
  confirm it compiles before marking the item done.
- **Mark where each item landed.** When you check a box, append where it went
  (`→ sec:foo`, short commit ref) instead of deleting the prose, so this file stays
  an audit trail of what changed and where.

---

## Decide before editing  (gates the edits below)

These four are choices only Seth can make. **All four resolved 2026-06-16** in a
grilling session; resolutions recorded below. Downstream items flagged
`(blocked on Dn)` are now writable per these answers.

- [x] **D1 — Appendix: one or two?** → **TWO separate appendices** (overrode the
  "one" lean). Appendix X = rigid pusher plate (invariant, 1/f², ripple, two-stage
  absorber); Appendix Y = Medusa sail + struts (invariant restated, long stroke,
  buckling). *Consequence:* the unifying "sail and rigid plate are the two ends of
  one `m·s`" sentence moves to the **body**, at the point in
  `sec:lightweight_pusher_plates` where the sail is introduced alongside the plate,
  since neither appendix now owns both ends.
  - **SUPERSEDED 2026-06-29 (grill).** Appendix X is killed: the rigid-plate
    invariant, ripple, and two-stage absorber **fold into the body** as two compact
    paragraphs (see the rewritten body item below). Reason: the rigid-plate headline
    (`m·s ∝ 1/f²`) is a one-line result, and its two trade tables + full worked
    example were detail dressing a one-liner. Appendix Y (Medusa sail + struts) is
    **deferred** to a later Medusa-focused grill, not resolved here. So D1's "two
    appendices" is now **zero for the plate, Y pending** — there is no shared
    appendix preamble to write.
- [x] **D2 — Front-vs-rear safety argument: body or appendix?** → **Short body
  paragraph, ≤4 sentences, no figure** (matches lean). Body carries the rear-mount
  fail-safe rationale (external reaction mass ⇒ approach from behind; rear sail
  shields crew; misses fly off behind; silhouette ≥ craft). The `1/L²` buckling
  *cost* stays in Appendix Y.
  - **REFINED 2026-06-29 (Medusa grill).** Appendix Y is killed, so the `1/L²` buckling
    cost no longer goes there: it stays in the body as a qualitative one-liner plus ONE
    rescued mitigation clause (sailboat-mast bracing + telescoping), all strut numbers
    dropped. Also keep one buffer-invariant unification sentence and a half-sentence
    concave-face cross-ref to §Mass Fraction. The LEO-drag idea was considered and dropped
    (~3 N at the 200 km boost altitude).
- [x] **D3 — Worked example (4 Hz / 4.6 m / 3.2 t): body anchor or appendix-only?**
  → **One-line anchor triple in the body** (refined past the "appendix-only" lean).
  Body gets only the `(f, stroke, plate-fraction)` triple as a parenthetical
  anchoring the 1/f² / ~10%-of-craft claim, e.g. "(at 4 Hz a 4.6 m stroke holds the
  plate near 3.2 t, ~10% of a 32 t craft)". Full worked example (235 kN·s, 73 m/s,
  60 g, 128 kg/m², survivability margin) stays **appendix-only** in Appendix X.
  - **SUPERSEDED 2026-06-29 (grill).** With Appendix X killed, the full worked
    example is **dropped**, not relocated. What survives into the body is the triple
    *(4 Hz, 4.6 m, ~3.2 t ≈ 10% of a 32 t craft)* plus **one** honesty clause: the
    survivability floor (~10–50 kg/m², far below Orion's regime) sits several × below
    the worked plate, so dynamics — not survival — set the ~10%. Everything else
    (235 kN·s, 73 m/s, 60 g, 128 kg/m²) goes.
- [x] **D4 — Reframe committed text (explicit OK given).** In
  `sec:formation_challenges_current_missions` (the `\SI{5}{\centi\meter}` std-dev
  centring claim) and the related `sec:lightweight_pusher_plates` centimetre claim:
  change "~5 cm required" to "**~2 m required laterally on the 5 m plate**". **State
  capability as ~10 cm robust / 5 cm stretch with metrology aids — NOT bare "cm
  achievable"** (bare "cm" would contradict Item 9-optional's 10 cm-robust /
  5 cm-stretch / 2 cm-not-claimed commitment). The body must also (a) state the
  torque cost (a 2 m miss buys more RCS authority + plate inertia, per the appendix
  off-center-torque note) and (b) say *why* the number changed: the earlier text
  conflated achievable **capability** with the binding **requirement** (plate
  capture). This unblocks Part-1 Item 1 criterion, Part-D.1 precision tiers, and the
  walk-before-run staging.

---

## §How PuffSats Work → PuffSat Design (`sec:lox_puffsat`, `sec:icy_puffsat`)

Two additions to the gas-generation subsections. The first gives LOX PuffSats a
flight-proven passive-cooling option (JWST-style detachable sunshade) and sets up the
cryo-fuel reach used by the Ceres item below. The second is a short speculative note on
carbonation as an atomization aid for icy PuffSats. Both resolved in a grilling session
(2026-06-30); the cryo physics is shared with the `sec:ceresly_good` ISRU-propellant item.

### `sec:lox_puffsat` — JWST-style detachable sunshade as a deep-cryo option

- [x] **Add the detachable standoff sunshade as a flight-proven cryo option beside the solar-white coating** · `[sizing]` → `sec:lox_puffsat` *(landed 2026-06-30: two paragraphs after the solar-white-coating para in `sec:lox_puffsat`. Build clean, all 3 cites resolve. SI-wrapped all figures; L2 glossed ("just beyond Earth's night side"); LH₂ forward-ref points at Ceres context only since the `sec:ceresly_good` LH₂ item [L830] isn't folded yet.)*
  - [x] Cite JWST: a five-layer aluminized Kapton sunshield cools the cold side passively to ~40 K at ~1 AU (Sun-Earth L2). Flight proof that passive standoff shielding reaches deep cryo at Earth distance. Cites `jwst_sunshield`, `gardner2023jwst_mission`.
  - [x] Frame as existence-proof + headroom (decided): 40 K is *colder* than LOX wants (oxygen freezes at 54.4 K; liquid range 54–90 K), so for LOX tune a lighter shade to ~60–80 K (fewer layers). The full 40 K reach is the lever for LH₂ farther out (see the `sec:ceresly_good` ISRU-propellant item). *(O₂ phase points cited to new `nist_webbook_oxygen`; NIST WebBook + archive.org both sandbox-blocked, values confirmed via search across multiple cryogenic refs.)*
  - [x] Keep it an **option alongside** the existing solar-white coating + thick-skin design (decided 2026-06-29). Do **not** rewrite the "thicker skins for elevated internal pressure" claim; this is an addition, not a D4-style reframe. *(thick-skin para untouched)*
  - [x] Detach handling (decided): the shade jettisons a short time before atomization, because it would foul the gas plume and a floppy multilayer cannot survive the collision. One-line aside on why we do *not* let it ride in as reaction mass: the benefit is sub-kg (~1–3% of a 25 kg PuffSat), and its Al/Si metallization would contaminate the non-combustible LOX plate; the case is worst at the cool ~3.2 km/s end, where the film may not fully self-vaporize and arrives as a short-pulse peak load. *(short-pulse-peak-load detail trimmed for brevity; contamination + "may not fully vaporize" kept)*
  - [x] Thermal-margin note: "short time" is set by plume geometry, not boiloff. A reflective-coated ~25 kg LOX PuffSat unshaded at 1 AU absorbs only ~10–15 W, so it takes hours to warm 20 K; seconds-to-minutes of unshaded coast is thermally trivial.
  - [x] Disposal: ultralight Kapton (high area/mass) deorbits fast, like the existing ice-wire coatings, or goes via the dry-mass disposal channel (`item:discard_before_impact`).

  The JWST sunshield is five layers of aluminized Kapton (the two sun-facing layers also
  doped-silicon coated) and cools the observatory's cold side passively to about 40 K at
  Sun-Earth L2 (~1.01 AU). That is direct flight evidence that a passive standoff shade
  reaches deep cryogenic temperatures at Earth distance, with no active cooling. For a LOX
  PuffSat it is an option beside the conformal solar-white coating already in the section.
  The 40 K reach is actually colder than LOX needs, since oxygen freezes at 54.4 K and is
  liquid only between 54 and 90 K, so a LOX shade is tuned lighter (fewer layers, ~60–80 K);
  the full 40 K capability matters because it is what lets hydrogen stay liquid farther from
  the Sun (the Ceres item). The shade is jettisoned a short time before the PuffSat is
  atomized, both because a floppy multilayer cannot survive the collision and because it
  would scatter the gas plume. We do not keep it as reaction mass: a 1–3 m² shade is only
  ~0.2–0.6 kg (about 1–3% of a 25 kg PuffSat), and its aluminium and doped-silicon
  metallization would contaminate the non-combustible LOX pusher plate, worst at the cool
  ~3.2 km/s lunar end where the film may not fully vaporize on contact. The "short time"
  before impact is set by plume geometry, not by thermal urgency: unshaded, the
  reflective-coated PuffSat absorbs only ~10–15 W at 1 AU and takes hours to warm by 20 K,
  so a coast of seconds to minutes barely touches the LOX. The discarded Kapton has a high
  area-to-mass ratio and deorbits quickly, or it leaves on the existing dry-mass disposal
  path (`item:discard_before_impact`).

### `sec:icy_puffsat` — carbonation as a speculative effervescent-atomization assist

- [x] **Mention dissolved carbonation briefly as an atomization aid for icy moons** · `[raw]` → `sec:icy_puffsat` *(landed 2026-06-30: two-sentence note after the icy atomization para, before `sec:lox_puffsat`. Cited `marchi2019_ceres_carbon` (Ceres ~20% carbon) and `phoebe` (Cassini CO₂ ice); `% TODO-CITE: effervescent atomization` left inline. Clathrate-rejection sentence dropped to honor "one or two sentences / do not develop the storage trade".)*
  - [x] Keep it brief (decided 2026-06-30): one or two sentences, do not develop the storage trade.
  - [x] Mechanism: dissolved CO₂ (soda model) exsolves on rupture and the expanding gas helps shatter the water into droplets, supercharged by the vacuum pressure ratio. Frame as a fourth mechanism that *trims* (does not replace) the micro-explosive load already in the section.
  - [x] Scope: viable only where carbon is abundant (Ceres ~20% carbon, Phoebe's CO₂ ice), **not** on the carbon-poor Moon. The exsolved CO₂ is biocompatible, a minor reaction-mass bonus. *(biocompatible/reaction-mass-bonus clause omitted for brevity.)*
  - [ ] Rejected (do not propose): CO₂ clathrate hydrate. Its dissociation is endothermic and self-preserving, so it releases gas too slowly for millisecond atomization and can re-freeze the spray (the ice-crystal failure the section already warns about), and full dissociation while still confined over-pressurizes the liner. *(dropped from the paper per the brevity decision; kept here as rationale of record.)*
  - [x] Cite an effervescent-atomization reference when this lands (e.g. a Lefebvre atomization text): `% TODO-CITE: effervescent atomization`.

  Where carbon is abundant, the icy PuffSat's meltwater can be lightly carbonated, so that
  on release the dissolved CO₂ comes out of solution and the expanding bubbles help atomize
  the water into fine droplets, an effect the vacuum pressure ratio makes strong even at a
  soda-like gas load. This is a speculative assist that would trim the micro-explosive load
  rather than replace it, and it is only free on the icy moons (Ceres is roughly 20% carbon
  and Phoebe carries CO₂ ice), not on the carbon-poor Moon. Storing the CO₂ as a clathrate
  hydrate was considered and rejected: clathrate dissociation is endothermic and
  self-preserving, too sluggish for millisecond atomization, and it over-pressurizes the
  liner if it lets go while still sealed.

---

## §How PuffSats Work → Mass Fraction Of Rocket To PuffSat Mass (fudge-factor `f`)

The fudge-factor passage (paper subsection "Mass Fraction Of Rocket To PuffSat Mass":
the `f` definition and the "Project Orion's findings justify a high `f`" paragraph;
derivation in `sec:PuffSat_ratio_approximation`). This **reframes committed text**, so
treat it like a D4 edit: it changes what the paper already says about Orion, not just an
addition. Cross-links to `sec:radiative_differences` (Orion's shaped charges) and
`sec:lightweight_pusher_plates` (curved plate, Medusa).

- [ ] **Disentangle `f`: opacity sets restitution, plate/source shape sets direction** · `[sizing]`
  - [ ] Split the two roles `f` currently bundles. Restitution (the 0.5→1 axis: how elastic the bounce is, energy kept as kinetic vs lost to heating the plate) is what opacity governs (Kramers' law). Direction/capture (what drops `f` below 0.5: whether the rebounded momentum goes forward vs scatters sideways or spills past the plate) is pure geometry. The current text pins Orion's high `f` on opacity alone, which conflates the two.
  - [ ] Fix the Orion claim. Opacity only buys restitution; turning that into ~2× forward thrust needs the rebound collimated. A flat plate reflects efficiently only near normal incidence, so Orion was forced to collimate the source with shaped charges (the paper already says this in `sec:radiative_differences`). Orion's `f` was high, but the directionality came from flat-plate-plus-shaped-charge geometry, not from opacity. Do not write this as knocking Orion.
  - [ ] State Medusa's geometric advantage. A dished sail wrapping around the blast (concave toward the explosion, convex from the payload side) catches a large solid angle of the divergent spherical expansion and reflects each element forward, with no shaped charge. That curvature matching the blast shape is a real design advantage of Medusa.
  - [ ] State the PuffSat thesis. A gas puff is divergent, so a flat plate would scatter and spill (`f` < 0.5). Because PuffSat pulses are orders of magnitude gentler than nuclear blasts, we can afford to curve either plate style (rigid plate or Medusa-style sail) to collimate the rebound geometrically, getting directionality from a divergent puff without aggressive source-shaping. This raises the effective `f` for both styles.
  - [ ] Cite-check the outside-world facts when folding in: Orion's plate was flat, Medusa's pusher was a dished/parachute sail, and Orion used shaped charges to direct the plasma. The shaped-charge fact is already cited (`balcomb1970nuclear`, `dyson2002project_orion`); find sources for the plate shapes.
  - [ ] Note the shared lever with the down-push item under `sec:lightweight_pusher_plates`: the same curvature that collimates the rebound forward (raising `f`) is what lets the rebound carry the descending PuffSat's downward momentum out. One plate-shape decision, two payoffs.

  The paper's `f` quietly bundles two independent things. The first is restitution: how
  elastic the impact is, set by whether the impact energy stays kinetic or is lost to
  heating the plate. This is the 0.5-to-1 axis, and it is what opacity (Kramers' law)
  governs, for Orion and for PuffSats alike. The second is direction and capture: whether
  the rebounded momentum actually goes forward, or scatters sideways or spills past the
  plate edge. This is what pushes `f` below 0.5, and it is pure geometry. The current text
  pins Orion's high `f` on opacity alone, which is the slip to fix.

  Opacity only buys restitution. Turning a near-elastic bounce into ~2× forward thrust
  needs the rebound collimated, and there are two ways to get it. Orion collimated the
  source: a flat plate reflects efficiently only near normal incidence, so Orion shaped the
  blast into a directed jet with shaped charges (already stated in
  `sec:radiative_differences`). Its `f` was high, but from flat-plate-plus-shaped-charge
  geometry, not from opacity. Medusa instead shaped the plate: a dished sail wrapping the
  blast catches a large solid angle of the divergent expansion and reflects it forward with
  no shaped charge, a genuine advantage of that design. PuffSats follow Medusa's route
  cheaply. A gas puff is divergent, so a flat plate would scatter and spill, but because
  PuffSat pulses are orders of magnitude gentler than nuclear blasts we can curve either
  plate style to collimate the rebound geometrically, raising the effective `f` without
  aggressive source-shaping. The same curvature also carries the descending PuffSat's
  downward momentum out (the down-push item under `sec:lightweight_pusher_plates`), so it
  is one plate-shape decision with two payoffs.

---

## §Sorry, I Don't Need ISRU → `sec:solid_PuffSats`

The "Like Proba-3, we target millimeter-scale precision" claim (paper line at
`sec:solid_PuffSats`) and the headline mm claim near the Proba-3 mention
(`sec:formation_challenges_current_missions`) both need the scale correction and
the walk-before-run framing below.

- [ ] **"Like Proba-3" needs a scale correction: mm at 300 km is not angular metrology** · `[sizing]`
  - [ ] State Proba-3's mm is at ~144 m (≈ 7 µrad), an easy optical-metrology angle
  - [ ] State that at a 300 km baseline 1 mm = ~3 nrad, which astrometry cannot reach
  - [ ] Conclude the precision lever here is **ranging**, not angle (full case under `sec:periapsis_challenges`)

  Proba-3 achieves millimetre relative precision at a separation of **~144 m**, where
  1 mm corresponds to an angular precision of **~7 µrad** — easy for an optical
  metrology instrument. For prograde/retrograde projectiles converging at Parker-class
  periapsis, the geometry the precision must be established over is **hundreds of km**,
  not 144 m. At a 300 km baseline, 1 mm corresponds to **~3 nrad**. That is *not*
  reachable by angular measurement (astrometry / star tracker):

  | target angular precision | diffraction-limited aperture (λ = 500 nm) |
  |---|---|
  | 5 µrad (≈ 1 arcsec, ordinary star tracker) | ~12 cm |
  | 1 µrad | ~0.6 m |
  | 100 nrad | ~6 m |
  | **3 nrad (= 1 mm at 300 km)** | **~200 m** |

  A 200 m telescope on a projectile is absurd, and star-referenced astrometry is in any
  case capped by a focal-plane **distortion floor** (a ~µrad-class systematic that more
  photons cannot beat). So at this scale the precision lever **cannot** be "like
  Proba-3" angular metrology. It must be ranging.

- [ ] **Walk before run: meter-class near Earth (near-term), mm near the Sun (later)** · `[sizing]`  (blocked on D4)
  - [ ] Add a scoping sentence near the headline mm claim (the Proba-3 mention) that mm precision is a *later-stage* near-Sun requirement, not needed for Section 2 near-term work
  - [ ] State the counterintuitive point: tight precision is feasible where the environment looks most extreme (no atmosphere near the Sun ⇒ deterministic orbital mechanics)
  - [ ] Name the genuinely hard regime as near-Earth low-periapsis (drag, gravity anomalies, sensor dropouts), which is why the near-term requirement stays loose

  This reframes the paper's navigation-accuracy claims. We can walk before we run, and
  the order is counterintuitive: the near-Earth near-term work needs only meter-class
  precision, and the tight millimeter precision belongs to the later near-Sun stages,
  where the dynamical environment is actually cleaner.

  *Later architecture (near-Sun direct collisions: no-ISRU rocket, World Set Free,
  interplanetary highways).* Here we switch from gas puffs hitting a plate to solid
  projectiles colliding head-on directly (`sec:solid_PuffSats`), at very high speed
  (100 to 250 km/s effective-exhaust regimes). This *does* demand millimeter precision,
  and `sec:solid_PuffSats` already says so. The burden is shared, not all on the
  projectile: the main rocket's sensors and RCS make the terminal adjustments to meet a
  slightly-off-target incoming retrograde projectile (consistent with the software
  guidance sketch in `sec:neural_navigation`). So millimeter precision is the
  closing-gap requirement of the rocket-plus-projectile pair, not a standalone
  per-projectile miracle.

  *The framing to add (walk before run).* Make explicit, wherever the paper invokes
  millimeter precision, that:
  * Millimeter precision is a *later-stage* requirement (near-Sun direct collisions),
    not needed for the Section 2 near-term work, which runs on meter-class tolerances.
  * Counterintuitively, the tight precision is feasible precisely where the environment
    looks most extreme. Near the Sun there is no atmosphere, so no drag perturbations;
    radiation pressure is large but can be modeled, and the orbital mechanics are
    deterministic. It is thermally and radiatively brutal, but navigation is predictable.
    The paper already makes this point locally (`sec:periapsis_challenges` "corona's low
    perturbation environment", and `sec:ceresly_good` for Ceres); state the general
    principle once and tie it to the walk-before-run order.
  * The genuinely hard navigation environment is the near-Earth low-periapsis regime,
    where atmospheric drag, gravity anomalies, and sensor dropouts bite. That is exactly
    why we keep the near-term requirement loose (meters) and do not ask for millimeters
    there.
  * One-line summary for the paper: we demand only meter-class precision where the air
    is thick (near Earth, near term), and we earn millimeter precision later where the
    vacuum is clean (near the Sun). Walk, then run.

---

## §Sorry, I Don't Need ISRU → `sec:periapsis_challenges`

The near-Sun navigation chapter. Two layers: the **core sharpening** (a worked
derivation of the transverse-node ranging lever) and an **expansion-options menu**
(A–F) of what else the chapter can use. Both target this section. Status:
order-of-magnitude sizing, not a simulation result (derived in a design grilling
session 2026-06-15).

### Core sharpening (detailed derivation)

- [ ] **The lever: differential ranging from a transverse node (good GDOP)** · `[sizing]`
  - [ ] Replace any "angular metrology" framing with a transverse coordinator node measuring distances only
  - [ ] Explain GDOP: `σ_lateral ≈ σ_range / sin θ`; transverse node gives θ ≈ 45–90°, in-line anchors give θ → 0
  - [ ] Explain differential: node ranges the controlled projectile *and* a reference, differencing out the node's own position/clock error
  - [ ] State the inversion vs ordinary close-formation flying: here ranging is practical, angle is not

  The right architecture is a coordinator node placed **off to the side** (transverse
  to the line of flight, e.g. ~300 km off-axis) measuring **distances only** (laser or
  carrier-phase two-way) — not a star map, not angles.

  - **Why transverse.** Lateral position error from a range is
    `σ_lateral ≈ σ_range / sin θ`, where θ is the angle the anchors subtend at the
    target — the *Geometric Dilution of Precision* (GDOP). Anchors nearly **in line**
    with the target (an along-track stream, or two head-on projectiles ranging each
    other) give θ → 0 and `1/sin θ → ∞`: range is blind to the lateral. A **transverse**
    node gives θ ≈ 45–90°, `1/sin θ ≈ 1`: a millimetre range becomes a millimetre
    lateral. The node offset should be comparable to the sensing range for good GDOP.
  - **Why differential.** The node ranges *two* things at once — the controlled
    projectile and a reference (the chamber beacon, or the opposing projectile) — and
    uses the difference. This cancels the node's own position/clock error. (Near the Sun
    there is no GNSS to pin the node absolutely; differencing makes that irrelevant.)
  - **Why ranging wins here when angle wins elsewhere.** Range precision (~mm via laser
    carrier phase) is essentially **range-independent** and needs only a laser +
    retroreflector, *not* a 200 m aperture; angular precision is distortion-floored and
    aperture-limited. So at the mm / long-range scale the conclusion **inverts**
    relative to ordinary close-formation flying: ranging is the practical lever, angle
    is the impractical one. The work is **relative orbit determination over the
    approach arc** (the geometry rotation builds the lateral), not a last-moment
    snapshot.

- [ ] **Why ~mm ranging at hundreds of km is realistic (carrier phase)** · `[sizing]`
  - [ ] Note raw carrier-phase precision is ~1% of a cycle (~0.1 mm at Ka-band), range-independent
  - [ ] Explain integer-ambiguity resolution: code range, dual-frequency wide-laning, geometry rotation over the arc, continuous phase tracking
  - [ ] Note differential processing cancels clock/hardware biases (CDGPS / SLR heritage)
  - [ ] Cite flight precedent: GRACE/GRACE-FO (~1 µm at ~220 km), SLR (mm-class), LLR (cm at 3.8×10⁵ km) — requirement is ~3 orders of magnitude inside demonstrated capability

  The architecture rests on ~mm-class *range* precision over hundreds of km, by
  carrier-phase ranging. This is not a stretch — it is well inside flight-proven
  capability, and the deep-space environment makes it *easier* than its terrestrial
  form:

  - **Raw phase precision is a small fraction of the wavelength, and range-independent.**
    A carrier-phase observable is typically measured to ~1% of a cycle. At Ka-band
    (~30 GHz, λ ≈ 1 cm) that is ~0.1 mm; at optical (laser, λ ≈ 1 µm) it is far finer.
    Precision degrades only through SNR with range, not through range itself — so
    hundreds of km is a link-budget question (solved with modest gain + a
    retroreflector/transponder), not a precision wall.
  - **The integer-ambiguity problem is resolvable here, several ways at once.** Carrier
    phase gives range modulo the wavelength; the whole-cycle integer must be fixed. It is
    pinned by (a) a coarse **code / time-of-flight** range to within a few candidates,
    (b) **dual-frequency wide-laning** (a long synthetic wavelength makes the integer
    trivial, the fine carrier then supplies precision), (c) the **geometry rotation over
    the approach arc** (the "500 measurements" over-determine the integers jointly with
    the relative trajectory, as in kinematic GNSS / orbit determination), and (d)
    **continuous phase tracking** once locked — the ambiguity is fixed *once* at
    acquisition and then merely cycle-counted.
  - **Differential processing cancels the biases.** Single- and double-differenced
    carrier phase (node-ranges-two-targets, differenced) removes clock and hardware
    biases — the same CDGPS / satellite-laser-ranging heritage that delivers mm
    relative positioning operationally.
  - **No atmosphere — the dominant terrestrial error sources are simply absent.** The
    ionospheric and tropospheric delays that limit ground carrier-phase ranging do not
    exist in the coast regime or near the Sun. The corona carries some dispersive plasma,
    but it is tenuous and dual-frequency-removable. Vacuum is the *friendly* case.
  - **Flight precedent (the decisive point).** GRACE / GRACE-FO perform inter-satellite
    ranging at ~220 km separation to ~1 µm (microwave K-band) and ~nm (the GRACE-FO
    laser interferometer); satellite laser ranging routinely reaches mm-class to
    spacecraft at hundreds–thousands of km; lunar laser ranging reaches cm-class at
    ~3.8×10⁵ km. So **mm at hundreds of km is roughly three orders of magnitude inside
    demonstrated inter-spacecraft ranging** — the requirement here is conservative, not
    aggressive.

- [ ] **Control: two-tier, deterministic-coast — not terminal homing** · `[sizing]`
  - [ ] State the homing-miss floor `σ_θ² v² / a_max` makes classical homing hopeless at ~400 km/s
  - [ ] Gross setup early (~50 m/s Δv lateral authority); authority is not the binding constraint
  - [ ] Fine touch late: ~mm/s execution ~1 s before impact (include the t_go table)
  - [ ] Explain why this beats the v² floor: nulling a known, measured offset, not fighting nav noise

  At ~400 km/s head-on closing, classical terminal homing is hopeless: the homing-miss
  floor scales as `σ_θ² v² / a_max`, so hitting mm would demand ~25 nrad nav. The escape
  is exactly the paper's own argument — the **predictable** corona environment lets the
  push be set up in advance:

  - **Gross setup, early.** A light (few-kg) projectile has ample lateral authority
    (~50 m/s of Δv) to place itself in the path of the incoming opposing projectile.
    Authority is *not* the binding constraint.
  - **Fine touch, late, fine precision.** The residual lateral miss is
    `≈ δv_lateral · t_go`. So the *final* correction must be both **late** and executed
    to **fine velocity precision**:

    | final correction at t_go | required δv precision for 1 mm |
    |---|---|
    | 1 ms (≈ 400 m out) | 1 m/s |
    | **1 s (≈ 400 km out)** | **1 mm/s** |
    | 10 s | 0.1 mm/s |

    i.e. ~mm/s execution (a micro-thruster impulse bit) applied ~1 s before impact —
    *not* the ~1 m/s that suffices for the gross setup.
  - **Why this beats the v² floor.** That floor assumes fighting *nav noise* in the
    endgame. In a deterministic environment you are instead nulling a **known,
    slowly-evolving offset** that the differential-ranging arc has already measured to
    mm. The binding number becomes `(mm/s execution) × (~1 s reaction) ≈ mm`, and the
    high closing speed stops being the enemy.

- [ ] **SRP near the Sun: huge in absolute terms, irrelevant to the collision** · `[sizing]`
  - [ ] Quote the absolute number (~470× the 1 AU value, ~75 mm over a 100 s arc) and put it in the trajectory model
  - [ ] Argue common-mode cancellation: both projectiles share sun-facing geometry, residual scales with ~1% A/m mismatch
  - [ ] "Track, don't predict": ranging measures the actual relative trajectory; only the brief final coast must be modelled
  - [ ] Flag the one non-cancelling term (velocity-dependent / Poynting–Robertson) as deterministic, bakeable

  Absolute SRP at Parker periapsis (~9.86 R_sun ≈ 0.046 AU) is ~470× the 1 AU value:
  ~15 µm/s² on a 1 kg projectile (A/m ≈ 0.005 m²/kg) → ~75 mm of displacement over a
  100 s arc. That is large and must be in the trajectory model. But what the collision
  cares about is the **relative** SRP between the two converging projectiles, and that
  stays sub-mm:

  - **Common-mode cancellation.** Both projectiles share the same heliocentric position
    (same flux, same outward SRP direction) and — for thermal survival — must point heat
    shields sunward, so they present the *same* sun-facing geometry. The absolute SRP
    cancels in the difference; the residual scales with the *mismatch* (A/m,
    reflectivity), ~1% at matched manufacturing → ~0.15 µm/s² → ~7.5 µm over 10 s,
    ~0.08 µm over the 1 s final coast. The near-Sun environment that makes SRP large
    also *enforces* the symmetry that cancels it.
  - **Track, don't predict.** Continuous differential ranging measures the actual
    relative trajectory (incl. ablation-driven drift); only SRP during the short final
    coast must be modelled, and over ~1 s even the *full* SRP moves <10 µm.
  - **Flux gradient** over the inter-projectile gap is negligible (~22 µm over 100 s
    even at 1000 km separation; nothing at the meters-apart endgame).
  - **The one non-cancelling term** is velocity-dependent SRP (aberration /
    Poynting–Robertson): prograde and retrograde velocities are opposite, so the
    ~(v/c)·SRP tilt *differences* rather than cancels — ~2×10⁻⁸ m/s² → ~0.1 mm over
    100 s. It is **deterministic** (fixed by known velocity), i.e. exactly the
    "relativistic effects are predictable but must enter the trajectory calculations"
    already flagged — bakeable, not a stochastic risk.
  - An on-board solar-intensity detector (sub-gram photodiode) is a useful third layer,
    but its higher-value role is as a **sun sensor for attitude** (attitude sets A_eff,
    the term that does *not* auto-cancel); the SRP-prediction problem itself mostly
    dissolves under cancellation + tracking.

- [ ] **Net architecture for the chapter (the summary paragraph)** · `[sizing]`

  - **Lateral knowledge** → differential ranging from a transverse node (good GDOP),
    *not* astrometry (which would need a ~200 m aperture at 300 km).
  - **Control** → two-tier (gross ~50 m/s early + ~mm/s fine at ~1 s t_go),
    deterministic-coast, defeating the v² homing floor.
  - **Dominant residual risk** → SRP on the long arc (tracked out) + projectile
    attitude/area matching (engineered); unpredictable solar luminosity is a ~0.1%-TSI
    effect, smaller than the chapter currently implies.

  This is sharper and more defensible than "like Proba-3, mm precision": at the 300 km
  scale Proba-3's *angular* metrology cannot reach mm, so the precision lever is
  transverse-node differential **ranging** with good GDOP, with control made tractable
  by the deterministic-coast / early-correction structure the predictable corona allows.

### Expansion-options menu (A–F)

Menu of architectural options to expand the chapter — what else the near-Sun case
can use, and where the LEO logic inverts because there is no GNSS anchor and the
projectiles' *spread* relative to each other becomes the whole game.

- [ ] **Option A — transverse-node differential carrier-phase ranging (the baseline)** · `[sizing]`

  Restate as the chapter's baseline: lateral knowledge near the Sun comes from a
  coordinator node placed **off to the side** of the line of flight, measuring
  **distances only** to both the controlled projectile and a reference, and using the
  difference.

  The geometry term is **GDOP — geometric dilution of precision** — and it is the crux.
  *In plain terms: a distance measurement tells you a lot about sideways position only
  if the measuring station is off to the side; a station straight ahead or behind tells
  you almost nothing sideways, the way one eye gives poor depth perception.* A
  transverse node converts millimetre ranging into millimetre *lateral* knowledge;
  differencing two ranges from the same node cancels the node's own position and clock
  errors, which matters precisely because near the Sun there is no GNSS to pin the node
  absolutely. This is the option the chapter should lead with, because at the 300 km
  scale ordinary angular metrology would need an absurd ~200 m telescope.

- [ ] **Option B — a VLBI-style coherent-aperture swarm (precision boost)** · `[sizing]`

  Offer as an upgrade path: several projectiles acting as one **synthetic aperture**
  (the radio-astronomy "very-long-baseline interferometry" trick) can in principle
  sharpen the relative-position fix beyond a single ranging node.

  *In plain terms: many small antennas spread out and combined can see as sharply as
  one impossibly large one.* This is the only option that could genuinely *beat* the
  single-node precision rather than merely match it. It is included here, rather than in
  the LEO chapter, for two honest reasons that the text should state: in LEO it would be
  insurance against a failure that the entry-limited capture analysis says does not
  bind, and its precision depends on knowing the **baseline orientation** between units
  to high accuracy — which ranging alone does not give (ranging measures baseline
  *length*, not its sideways tilt). Near the Sun, where relative geometry *is* the
  mission and there is no anchor floor, the trade is more attractive, so it belongs in
  this chapter as a stretch option.

- [ ] **Option C — optical LED-beacon cameras layered on RF ranging (close endgame)** · `[sizing]`

  Offer as the terminal collision sensor: in the final approach, **strobed LED beacons
  + small cameras** between the converging projectiles can supply the last-instant
  relative bearing, on top of the RF differential ranging that does the long-range work.

  Here the LEO logic **inverts**, and the chapter should say so explicitly. In LEO,
  inter-projectile cameras were the *wrong* tool — they measure how the swarm is spread
  relative to itself, which is already handled, and are blind to the block-slide that an
  external anchor must fix. *Near the Sun there is no external anchor, and the spread
  between two converging projectiles is exactly the quantity that decides the
  collision* — so the very sensor that was redundant in LEO becomes useful as the
  close-in collision sensor. *In plain terms: when two objects must hit each other and
  there is no outside referee, they are best off watching each other directly through
  the last stretch.* This is a layered backup to ranging, not a replacement for it.

  On power, the watt-class beacon budget that closes the formation-scale centring case
  (the surveyor-anchored item under `sec:formation_challenges_current_missions`) does
  *not* carry over to this geometry. At hundreds of km of closing range and against
  coronal glare, a 1 W omnidirectional beacon puts under one photoelectron per strobe
  on the camera. Bearing from the beacons becomes usable only once the gap has closed
  to formation scale, which at ~400 km/s is the last few milliseconds. The long-range
  work stays with ranging; the optical layer is a very-late-endgame add, not a
  hundreds-of-km sensor.

  - [ ] **UV-C beacon for relative orbit determination at ~300 km, seen against the
    coronal glare** · `[sizing]` — move the beacon and the camera's bandpass into the
    deep ultraviolet (UV-C, ~250–280 nm), where the scattered-light coronal background
    is dimmer than the visible glare that washes out a near-IR beacon. Use case is
    relative orbit determination between PuffSats ~300 km apart at low relative velocity,
    not the last-millisecond terminal sensor of the parent option. (This re-scopes the
    optical layer: it is a ~300 km metrology aid, so the parent's "last few milliseconds"
    framing does not apply to it.)

    **Does the corona pass UV-C? Yes, for propagation.** The coronal plasma cannot block
    it. Even at a generous n_e ~ 10⁹ cm⁻³ near the coronal base, the plasma cutoff is
    f_p ≈ 8.98×10³·√n_e ≈ 284 MHz, against ~1.13×10¹⁵ Hz for 265 nm light — higher by
    ~4×10⁶ (more than six orders of magnitude), so the refractive index is 1 − ~3×10⁻¹⁴:
    no cutoff, no meaningful bending. Thomson scattering off the free electrons over a
    300 km path is optically thin to τ = σ_T·n_e·L ≈ 2×10⁻⁸ and is wavelength-flat, so
    it costs nothing. The gas is fully ionized, so neutral photoabsorption is negligible.
    UV-C crosses 300 km of corona essentially loss-free. (Real densities at a near-Sun
    periapsis of several R_sun are lower than 10⁹ cm⁻³, so this is the conservative case.)

    **The open question is the background, not transparency.** "Solar-blind" works on the
    ground because ozone removes the solar UV-C; in space there is no ozone, and the glare
    here is the corona's own brightness. The scattered-light (K/F) corona follows the
    photospheric colour, which is genuinely down in the UV-C, so that piece is dimmer. But
    the corona is a million-K plasma that *emits* its own UV/EUV lines, so the chosen band
    (~255–265 nm) must dodge coronal and chromospheric emission lines. That needs the
    coronal UV surface-brightness spectrum, not just the photospheric continuum (needs a
    citation). Hardware also needs a real UV-C emitter, and there are three candidates with
    different trade-offs: an **AlGaN UV-C LED** (~255–280 nm, narrow-band and efficient, but
    low peak power per device, so an isotropic beacon wants an array); a **frequency-quadrupled
    solid-state laser** (266 nm from the 1064 nm Nd:YAG line, high peak power and a single
    clean line good for beaming and for dodging a coronal emission line, but directional, so it
    must be pointed); and a **xenon flashlamp** (an intense broadband pulse reaching well into
    the UV-C through a UV-grade fused-silica envelope, inherently omnidirectional and high in
    peak power, the cheap rugged strobe option — at the cost of wasting most of its photons
    outside the solar-blind band and solarizing its envelope over time). All three need a
    citation on pulsed UV-C output and space-qualification. The flashlamp is the natural emitter
    for an *isotropic* artificial-star beacon meant to be seen by several nodes at once; the
    laser suits a *beamed* point-to-point link (see the artificial-star item below).

    **Link budget — is a few watts enough at 300 km?** Order-of-magnitude: a 3 W peak
    source pulsed 1 ms once per second puts 3 mJ ≈ 4×10¹⁵ photons (4.7 eV each) into each
    pulse. A 10 cm receive aperture at 300 km subtends a geometric fraction ~7×10⁻¹⁵ of a
    full sphere, so an *isotropic* beacon delivers ~28 photons/pulse — about 1–2
    photoelectrons after filter throughput (~0.3) and detector QE (~0.2): marginal. The
    relative geometry is known to far better than a degree at 300 km, so beam the beacon: a
    tens-of-degrees cone gives ~50–500× gain and ~10²–10³ photoelectrons/pulse, a strong
    fix in a 1 ms gate. *In plain terms: pick a colour the Sun is dim in, point the beacon
    at the partner instead of lighting the whole sky, and a few watts is plenty.* So a few
    watts closes the 300 km link **only if the beacon is beamed** (or the aperture is
    ~20 cm) with a solar-blind photon-counting detector; an isotropic few-watt beacon does
    not.

  - [ ] **Artificial-star UV-C beacons beyond the corona: a two-stage attitude reference
    for the Parker regime** · `[sizing]` — a second, distinct use for the UV-C beacon. The
    item above solves *relative* geometry between two nearby PuffSats at ~300 km. This one
    solves *absolute attitude* (which way a node is pointed) deep inside the corona, where a
    conventional star tracker is starved of stars. Put the references where they can survive
    and self-locate, and let the deep-diving nodes treat them as bright, known stars.
    (Cross-link `sec:neural_navigation`'s optical tracker array and the coordinator-node
    ranging fleet.)

    **The problem.** A star tracker fixes attitude by matching a field of faint natural stars
    (visual magnitude ~2–6) against a catalog. At a Parker periapsis of ~9.86 R_sun the
    diffuse K/F-corona surface brightness and stray light raise the background enough to wash
    those stars out, so the tracker's accuracy and update rate degrade right where the
    converging-collision geometry wants its tightest, fastest, *shared* angular reference.
    (Parker's own trackers do operate, shielded behind the heat shield, so the honest claim is
    degradation and insufficiency, not total failure — needs a citation on near-Sun
    star-tracker performance and on the coronal surface-brightness profile.)

    **The two-stage fix.** Stage one: a small constellation of beacon-sats parked *beyond* the
    bright inner corona, at a survivable distance — ~0.1 AU (≈ 21.5 R_sun) is a reasonable
    first guess. There the solar flux is ~136 kW/m² (~100 suns), against ~640 kW/m² (~470 suns)
    at Parker periapsis, so a Parker-class shield has large margin, and a star tracker pointed
    anti-sunward sees a sky dark enough to fix the beacon's own attitude. Each beacon-sat
    self-locates: its own star tracker gives attitude, and the ranging fabric (the same
    Ka-band / laser nodes already in the architecture) gives position. Stage two: the beacon
    pulses a bright UV-C flash — an *artificial star* — and broadcasts its own position and
    time. A deep node (the main spacecraft, a co-flyer, a coordinator node, possibly a PuffSat)
    measures the *direction* to each beacon on its solar-blind focal plane and, knowing the
    beacon's broadcast position and its own position, computes the attitude. *In plain terms:
    when the real stars are drowned out, fly your own brighter stars to a place where they can
    still see the sky, have them announce exactly where they are, and aim off them instead.*

    **Why UV-C, not an RF beacon.** Same band logic as the relative-OD item: UV-C sits ~6
    orders of magnitude above the coronal plasma frequency, so it suffers none of the
    refraction or scintillation that wrecks radio links near solar conjunction. The angular
    reference stays geometrically clean exactly where an RF one would be smeared. The
    solar-blind band plus a pulsed emitter (LED array, 266 nm laser, or xenon flashlamp; see
    the emitter note above) let a temporal/spectral gate pull the flash out of the coronal
    background.

    **Caveats, all resolvable.**
    - *Angle needs position, and it is a joint solve.* Turning a measured bearing into an
      attitude presupposes you know both the beacon's position and your own. Two non-collinear
      artificial stars give 3-axis attitude; a single one leaves roll about its line unfixed,
      so this is a *constellation*, not one beacon. With enough beacons of known position the
      node solves attitude *and* position together, GPS-style — which is why these beacons
      should be the *same* transverse ranging nodes already sized for GDOP, not a separate
      fleet.
    - *Light-time latency.* The beacon is tens of seconds away at light speed (~0.05 AU of
      separation ≈ 25 s one-way; a range round-trip is a minute or two). The *bearing* is
      instantaneous — you measure the photon's arrival direction now — but the broadcast
      position is stale by the light-time, so it must be propagated forward on the beacon's
      ephemeris. Near the Sun the dynamics are deterministic (the chapter's recurring theme),
      so propagating a known heliocentric orbit over a minute to well under a kilometre is easy.
    - *Aberration.* At ~190 km/s (Parker periapsis) stellar aberration tilts every bearing by
      ~130 arcsec, far above the µrad target; at ~400 km/s closing it is ~270 arcsec.
      Artificial stars do not escape it. But aberration is deterministic in the velocity, which
      is measured, so it is corrected, not feared — the same as for a natural-star tracker.

    **Link budget — isotropic is hopeless at this range, so beam, but the consumers are
    bunched.** This is the relative-OD budget rescaled from 300 km to ~0.05 AU: inverse-square
    is ~(7.5×10⁶ km / 300 km)² ≈ 6×10⁸ harsher, so an isotropic few-watt flash falls ~9 orders
    short and cannot close. The fix is to beam, and the geometry permits it: every consumer
    (spacecraft, co-flyers, coordinator nodes, PuffSats) is clustered within ~hundreds of km of
    the collision point, which subtends only arcseconds from a beacon 0.05 AU away, so *one*
    modest beam lights the whole cluster at once — beamed and seen-by-everyone are not in
    conflict here. A beam aimed to ~0.1° (the cluster position is known far better than that)
    buys ~10⁶× over isotropic, bringing a joules-to-kilojoules UV pulse — a xenon flashlamp's
    or pumped laser's natural regime, not milliwatts — into a strong photon-counted fix. The
    exact per-pulse energy, beam width, and pulse cadence need a proper budget (flagged as the
    open sizing question for this item).

- [ ] **Option D — deterministic-coast two-tier correction (defeats the v² floor)** · `[sizing]`

  Restate as the control architecture: a **gross early correction** (~tens of m/s of Δv
  to get roughly into the path) plus a **fine, late, high-precision correction**
  (~mm/s applied ~1 s before impact). Not last-moment terminal homing.

  At ~400 km/s head-on closing, classical homing is hopeless — its miss floor grows
  with closing speed squared. *In plain terms: you cannot "steer in" at the last second
  when you are closing this fast; instead you set up the shot early in a predictable
  environment and apply one tiny, precisely-timed nudge at the end.* The reason this
  works is that the corona environment is **predictable**, so the projectile is nulling
  a *known, already-measured* offset rather than fighting fresh sensor noise — which is
  what lets a millimetre-per-second nudge a second out translate to a millimetre miss.
  The chapter should frame the high closing speed as something the structure *defeats*,
  not something it fights.

- [ ] **Option E — solar-pressure common-mode cancellation, "track, don't predict"** · `[sizing]`

  Offer as the SRP argument: the enormous absolute solar radiation pressure near the
  Sun (~470× its 1 AU value) is **largely irrelevant to the collision**, because both
  converging projectiles share nearly the same sun-facing geometry and so feel nearly
  the same push — it is **common-mode and cancels in the difference**.

  This is the Part 1 block-miss idea reappearing in a new setting, and the chapter can
  lean on it. *In plain terms: a strong wind that pushes both racers equally does not
  change who reaches the line first — only the difference between them matters, and that
  difference is small.* The residual scales with the *mismatch* in area and
  reflectivity (a percent at matched manufacturing), the actual relative trajectory is
  **measured continuously** by the ranging arc rather than predicted, and only the brief
  final coast must be modelled. The one term that does *not* cancel — a velocity-
  dependent relativistic tilt that differs between the prograde and retrograde
  projectiles — is **deterministic** and can be baked into the trajectory, not a
  stochastic risk.

- [ ] **Option F — a sub-gram sun-sensor photodiode setting the effective area (attitude aid)** · `[sizing]`

  Offer as a light third layer: a tiny solar-intensity photodiode is most valuable not
  as a navigation sensor but as a **sun sensor for attitude**, because attitude sets the
  sun-facing area — the one solar-pressure term that does *not* auto-cancel.

  *In plain terms: the cheapest way to keep the un-cancelled part of sunlight pressure
  under control is to keep the projectile pointed consistently, and a pinhead-sized
  light sensor is enough to do that.* It is worth one line in the chapter as the
  low-cost closure on the residual SRP term, distinct from the ranging and camera
  options above.

---

## §Sorry, I Don't Need ISRU → `sec:periapsis_challenges` (near-Sun absorbing nozzle / chamber)

The near-Sun absorbing structure that catches each prograde/retrograde collision.
The paper already gestures at it in `sec:periapsis_challenges` ("the pulsed propulsion
chamber may ablate slightly on each pulse, and the projectiles must be miniaturized to
at most a few kilograms to contain the immense energy"). These items put numbers behind
that sentence and add the magnetic-nozzle option. Cross-links to
`sec:radiative_differences` (opacity only buys restitution, not size) and
`sec:lightweight_pusher_plates` (the magnetic-damper / Medusa hardware lineage).
Hand-derived order-of-magnitude sizing from a design grilling session (2026-06-22).
Worked scenario: 2.5 kg retrograde + 7.5 kg prograde, head-on at 4 solar radii,
~300 km/s each (600 km/s closing), per the appendix optimal 1:3 split.

- [ ] **The absorbing structure has a minimum size set by per-pulse energy; the near-Sun rocket is large** · `[sizing]`
  - [ ] State the energy per pulse: in the center-of-mass frame `E = ½ μ v_rel²` with reduced mass `μ = m_pro m_retro / (m_pro + m_retro) = 1.875 kg` and `v_rel = 600 km/s`, giving `E ≈ 340 GJ ≈ 81 tons TNT`, plasma ~4–5 MK. This is the number the structure must survive every pulse.
  - [ ] State the size floor and how it scales. For an ablative/contact chamber the wall is thermal-fluence-limited: `R ≈ √(f_wall E / (2π F_max))`, so `R ∝ √E ∝ √m` at fixed closing speed. Worst case (`f_wall = 1`, all energy into the wall) is ~73 m; with an open sail that reflects/expels most of the plasma the realistic floor is ~15–20 m.
  - [ ] Draw the consequence the paper should state: there is a hard minimum mass and size to the absorbing structure, and it shrinks only as `√(per-pulse mass)`. Cutting the radius 4× (≈20 m → 5 m) needs ~16× less mass per pulse (10 kg → ~0.6 kg) and ~16× more pulses for the same total impulse. So unless the projectiles are miniaturized to a very high degree, the rocket operating near the Sun is inherently large. This sharpens the existing "miniaturized to a few kilograms to contain the immense energy" line rather than contradicting it.
  - [ ] Tie to the radiative argument: opacity (the `sec:radiative_differences` win) only governs restitution / the radiative channel. It does not shrink the structure, because the bulk convective momentum load that sets the size is opacity-blind. Keep these separate so a reader does not think low radiative loss buys a small chamber.

  The thing the near-Sun chamber must survive every pulse is set by the closing energy.
  In the center-of-mass frame `E = ½ μ v_rel²`, with reduced mass
  `μ = m_pro m_retro / (m_pro + m_retro) = (2.5)(7.5)/10 = 1.875 kg` and `v_rel = 600 km/s`,
  so `E ≈ 3.4×10¹¹ J ≈ 340 GJ ≈ 81 tons of TNT`, releasing a plasma at roughly 4–5 MK.
  A contact wall is thermal-fluence-limited, `R ≈ √(f_wall E / (2π F_max))`, so the radius
  grows as `√E ∝ √m` at fixed closing speed. The worst case, the whole 340 GJ loading the
  wall, gives ~73 m; an open sail that reflects or expels most of the plasma pulls the
  realistic floor to ~15–20 m. Either way there is a hard minimum, and it shrinks only as
  the square root of per-pulse mass: a 4× smaller radius costs ~16× less mass per pulse and
  ~16× more pulses for the same total impulse. The honest takeaway for the paper is that
  unless the projectiles are miniaturized to a very high degree, the rocket near the Sun is
  inherently large. This is the same point `sec:periapsis_challenges` already makes ("a few
  kilograms to contain the immense energy"), now with the scaling attached. Note that the
  low radiative loss argued in `sec:radiative_differences` does not help here: opacity buys
  restitution and blocks the radiative channel, but the bulk convective load that sets the
  size is opacity-blind.

- [ ] **A magnetic nozzle avoids contact and ablation; the trade is roughly even at low energy but tips decisively to the nozzle as per-pulse energy climbs, so near the Sun it can overperform a contact wall** · `[sizing]`
  - [ ] State the appeal: a magnetic nozzle reflects the conductive collision plasma off a field with no material contact, so there is no ablation limit and no thermal-fluence size floor. The plasma is a near-perfect conductor here (magnetic Reynolds number `Rm = μ₀ σ L v ~ 10⁷` at 4–5 MK), so it excludes and compresses field lines (frozen-flux / diamagnetic exclusion) and bounces off.
  - [ ] **State the regime-dependence (why it overperforms near the Sun, not unconditionally).** The two options scale oppositely with per-pulse energy. A contact wall is thermal-fluence-limited and ablates, so it gets *worse* as `E` rises (`R ∝ √E`). The field coupling gets *better*: Spitzer conductivity `σ ∝ T^{3/2}`, so a hotter plasma has a higher `Rm`, reflects more cleanly off frozen-in flux, and leaks less resistive heat into the coil. The crossover tilts to the nozzle as `E` climbs. At the low end (LEO insertion, weakly ionized 3–16 km/s gas near `10⁴ K`) the gas barely conducts and a material plate wins; in the Parker regime the nozzle overperforms. The momentum floor is unchanged across this range (the coil still reacts the full impulse), so "overperform" is about ablation, feasibility, and per-pulse consumables, not about escaping the mass-from-impulse floor. *(added 2026-06-30 grill)*
  - [ ] State that the field can be self-powered by the expansion. The field acts as a conservative spring: a persistent superconducting current holds it with zero per-pulse energy, and the work of redirecting the plasma comes from the plasma's own thermal/kinetic energy. Flux compression lets a modest seed field be transiently amplified by the expanding plasma (Sakharov MK-generator physics), so you need not hold the full peak field statically. (A static 10 T field over a ~20 m bubble already stores ~1.3 TJ, far above one pulse, so flux compression matters.)
  - [ ] State the honest catch: the impulse does not go away. The full thrust still reacts as J×B force on the coil and its support, so the tensile/hoop-stress and minimum-size story carries straight over to the coil. The magnetic nozzle removes ablation and the thermal-fluence floor; it does not remove the momentum floor. Net thrust also needs an open, asymmetric nozzle geometry, not a symmetric mirror.
  - [ ] **Pulsed magnetic nozzle: possible, but complex whether it helps.** A pulsed / flux-compression nozzle buys a smaller seed field and lighter coil by letting the plasma amplify the field, at the cost of switching, arming-within-microseconds timing, and recovery efficiency. A persistent DC superconducting field is simpler and already near-zero per-pulse energy. State it as a real option with an unsettled trade, not a clear win.
  - [ ] **Sun shielding is probably lighter for a magnetic nozzle, but not guaranteed.** Being mostly open, a magnetic nozzle presents far less solid area to shield from the Sun than a closed chamber or solid plate. Caveat to keep: a REBCO coil is cryogenic (~20–77 K) and is harder to shield per unit area than a passive hot refractory wall, since near the Sun the environment is ~3.9 MW/m² at 4 R_sun (~2900 K blackbody equilibrium). The reduced area probably wins, but the cryo penalty can eat part of it.
  - [ ] **At Earth distance the magnetic-nozzle case is lighter on two counts.** First, the solar flux is ~2900× lower (1361 W/m² at 1 AU), so no Parker-class heat shield is needed (a REBCO coil still wants MLI + radiators for cryo, but not a heavy sunshade). Second, the Earth-crossing collision speeds are lower than near the Sun, so the per-pulse energy and the nozzle floor are both smaller. If magnetic nozzles are used for the Earth-distance collisions they can be markedly lighter than the near-Sun version.

  The lever that escapes the contact-wall size floor is a magnetic nozzle: reflect the
  conductive collision plasma off a magnetic field with no material touching it, so there
  is no ablation and no thermal-fluence radius. The plasma cooperates because it is a
  near-perfect conductor at 4–5 MK (magnetic Reynolds number `Rm = μ₀ σ L v ~ 10⁷`), so it
  excludes and compresses field lines and bounces. The field can largely power itself: a
  persistent superconducting current holds it for free, the field behaves as a conservative
  spring, and the work of turning the plasma comes from the plasma's own energy. Flux
  compression even lets a modest seed field be transiently amplified by the expansion
  (the Sakharov flux-compression-generator effect), which matters because a static 10 T
  field over a ~20 m bubble already stores ~1.3 TJ, far more than a single 340 GJ pulse.
  The catch to state plainly: the impulse does not vanish. The full thrust reacts as J×B
  force on the coil and its structure, so the minimum-mass and hoop-stress story carries
  over to the coil. The magnetic nozzle removes ablation and the thermal floor, not the
  momentum floor, and net thrust needs an open asymmetric geometry rather than a symmetric
  mirror.

  What makes this a likely *win* near the Sun, not just an even trade, is that the two options
  scale oppositely with per-pulse energy. A contact wall is thermal-fluence-limited and ablates,
  so it gets worse as the energy rises (`R ∝ √E`). The field coupling gets better: Spitzer
  conductivity rises as `T^{3/2}`, so a hotter plasma carries a higher magnetic Reynolds number,
  reflects more cleanly off frozen-in flux, and leaks less resistive heat into the coil. The
  crossover therefore tilts to the magnetic nozzle as the collision energy climbs. At the low end
  (LEO insertion, weakly ionized 3–16 km/s gas near `10⁴ K`) the gas barely conducts and a
  material plate is the simpler winner; in the Parker regime the nozzle overperforms. What does
  not change across this range is the momentum floor, since the coil still reacts the full impulse,
  so the advantage is in ablation, feasibility, and per-pulse consumables, not in escaping the
  mass-from-impulse minimum.

  Three takeaways follow that the paper should state as honest, not oversold. A *pulsed*
  magnetic nozzle is possible but it is genuinely unclear whether pulsing helps: flux
  compression buys a smaller seed field and lighter coil, but adds switching, microsecond
  arming, and energy-recovery complexity that a simpler persistent DC field avoids.
  Shielding is probably lighter for a magnetic nozzle because its open geometry presents
  little solid area to the Sun, though the caveat is real: a cryogenic REBCO coil
  (~20–77 K) is harder to shield per unit area than a passive hot wall, against the
  ~3.9 MW/m² flux at 4 solar radii. And at Earth distance the magnetic-nozzle case is
  lighter twice over: the solar flux is ~2900× weaker so no Parker-class sunshade is needed
  (only MLI and radiators for cryo), and the lower Earth-crossing collision speeds drop the
  per-pulse energy and the nozzle floor as well.

- [ ] **Stage the large near-Sun ship: peel off payload chunks so delivery is metered, not a single slug** · `[sizing]`
  - [ ] State the motivation: a large near-Sun ship (thousands of tons) amortizes the fixed ~100 t nozzle/shield over a big payload, but you do not want to fly the whole slug to the destination, and the destinations want metered delivery anyway.
  - [ ] State the mechanism: the nozzle doubles as a serial accelerator. Bring the stack up to speed, peel off ~50 t chunks, keep pushing the remainder. Shed chunks coast to the target independently. Each pulse adds `Δv = J / M_remaining`, so the lighter remnant accelerates faster as mass leaves.
  - [ ] State the Section 6 payoff (the strongest reason to stage): a metered stream turns the impactor concept from a single catastrophic event into a throttle. 50 t every 10 s is a power plant; 5000 t at once is a bomb. Cross-link `sec:world_set_free`.
  - [ ] State the Section 5 payoff: chunking sizes secondary-payload insertions into elliptical orbits sanely, instead of delivering one giant object. Cross-link the orbital-lift text in `sec:no_isru_rocket` / Section 5.
  - [ ] Quantify the metering (it is cheap): a ~1 AU coast at ~200 km/s is ~8.7 days, and arrival timing scales as `dt/t = dv/v`. So 10 s spacing between 50 t chunks needs only ~3 m/s of relative trim, and an hour-wide stream is a ~1 km/s spread on a ~200 km/s bulk velocity, under a percent.
  - [ ] Correct the efficiency framing (decouple two levers): arrival spread and mass efficiency are not the same lever. Accelerate the full stack together, then peel chunks with sub-percent trims, and the overhead stays at roughly the nozzle-to-total fraction. The "less efficient as you accelerate smaller chunks" penalty bites only for wide velocity spreads or when you keep flogging the nearly-empty tail.
  - [ ] State that staging does not shrink the nozzle: its size is set by per-pulse energy (projectile mass × collision v²), not ship mass. Staging changes the delivery pattern and the dead-mass fraction, not the nozzle. It stays a fixed ~100 t overhead.
  - [ ] State the nozzle-fate fork (the real open decision): expend it (Section 6) and it becomes the fastest, last impactor, so waste ≈ 0; reuse it (Section 5, or amortize over runs) and you no longer want it at v_final, but external pulses push the whole assembly forward, so recovery costs deceleration pulses or a return leg, ~100 t × v_final of momentum. "Only the nozzle mass is wasted" is the reusable case.
  - [ ] State the heat-shield-as-impactor handling: passive is free (the shield was already accelerated at periapsis, so leave it attached and let it hit the target, no extra pulses); active re-acceleration far from the Sun costs weak pulses (slower collisions, less Δv per pulse) and is only worth it if the shield must move faster than periapsis left it. The shield is load-bearing during the high-energy pulses near the Sun, so the conversion to impact mass is post-periapsis only.

  Because the near-Sun rocket is inherently large (previous item), it is worth amortizing the
  fixed ~100 t nozzle and shield over a large payload (thousands of tons) and then staging the
  delivery rather than flying the whole slug to the target. The nozzle doubles as a serial
  accelerator: bring the stack up to speed, peel off ~50 t chunks, and keep pushing the
  remainder, each pulse adding `Δv = J / M_remaining` so the lighter remnant accelerates
  faster. Shed chunks coast to the destination on their own. The payoff is metered delivery.
  For the impactor concept (`sec:world_set_free`) this is the difference between a power plant
  and a bomb: 50 t every 10 s is a throttle, 5000 t at once is a single catastrophic impact.
  For Section 5 it sizes secondary-payload orbital insertions sanely instead of delivering one
  giant object.

  The metering is cheap. A ~1 AU coast at ~200 km/s takes ~8.7 days, and arrival timing scales
  as `dt/t = dv/v`, so 10 s spacing between 50 t chunks needs only ~3 m/s of relative trim, and
  an hour-wide stream is a ~1 km/s spread on a ~200 km/s bulk velocity (under a percent). This
  decouples two levers that are easy to conflate: arrival spread and mass efficiency are not
  the same. Accelerate the full stack together, then peel chunks with sub-percent trims, and
  the overhead stays at roughly the nozzle-to-total fraction; the "less efficient as you
  accelerate smaller chunks" penalty bites only for wide velocity spreads or when you keep
  accelerating the nearly-empty tail.

  Two things to keep honest. Staging does not shrink the nozzle: its size is set by per-pulse
  energy (projectile mass times collision v²), not by ship mass, so it stays a fixed ~100 t
  overhead however the payload is chunked. And the nozzle's fate is the real open decision.
  Expended (the impactor case) it becomes the fastest, last shot in the stream, so nothing is
  wasted; reused (the orbital case, or to amortize over many runs) you no longer want it at
  final velocity, but external pulses push the whole assembly forward, so recovering it costs
  deceleration pulses or a return leg, of order 100 t × v_final in momentum. So "only the
  nozzle mass is wasted" is the reusable case; for impactors the waste is closer to zero. The
  heat shield follows the same logic: leave it attached and it rides to the target as free
  impact mass (already accelerated at periapsis), or re-accelerate it far from the Sun at the
  cost of weaker pulses. It cannot be shed near the Sun, where it is load-bearing during the
  high-energy pulses, so the conversion is post-periapsis only.

---

## §One Hiroshima Per Second, The World Set Free → new `\subsection` in `sec:world_set_free` (MHD extraction option)

A third energy-extraction pathway for the Straw Way, beside the steam chamber ("Power Plant
Chamber Details", currently *unlabeled* — give it a `\label{}` so the new text can cross-ref it)
and the direct chemical-synthesis loop (`sec:strawway_economics`). Presented as an *alternative*
architecture, not a replacement of the steam baseline. Shares the magnetic-nozzle primitive with
the near-Sun propulsion item (`sec:periapsis_challenges`; see `CONTEXT.md` "magnetic nozzle" for
the two opposite-energy-goal senses) and the metering/safety logic with the staging item ("50 t
every 10 s is a power plant; 5000 t at once is a bomb"). Resolved in a grilling session
(2026-06-30). Tag `[raw]`/qualitative: the rep-rate is a free parameter, so state scaling and
architecture, not committed numbers.

- [ ] **Standalone new subsection: extract straw power electromagnetically — vacuum bottom + magnetic nozzle + km-long MHD channel** · `[raw]` → new `\subsection` in `sec:world_set_free`, after "Power Plant Chamber Details", before `sec:vacuum_airlock`
  - [ ] **The win is killing the airlock, not MHD efficiency per se.** A vacuum bottom makes the projectile flight path and the energy-extraction stage one continuous vacuum, so the entire `sec:vacuum_airlock` machinery (a 300 m/s door sealing a 30 cm aperture in 1 ms, sacrificial polyethylene plugs, ice coatings) that exists only to keep steam from backflowing up the tube simply disappears. State this as the headline motivation.
  - [ ] **Geometry: a ~90° magnetic turn.** Plasma arrives heading straight down; a km-long channel can't be vertical. The magnetic nozzle *redirects* (not reflects) the downward plasma into a horizontal, km-long underground MHD channel, keeping the heavy MHD hardware off to the side of the vertical projectile path. Flag the 90° turn of a `~10⁵–10⁶ K` plasma slug as speculative, not free.
  - [ ] **Division of labor: nozzle redirects, MHD channel extracts.** Opposite energy goal from the propulsion nozzle (`sec:periapsis_challenges`), which reflects near-elastically to *conserve* momentum for thrust. Here you *brake* the plasma against the field and pull its kinetic energy out as current in an external load; reflecting it elastically would waste the energy and shove the structure. Same "steer conductive plasma with a big field, no contact" primitive.
  - [ ] **Manageable explosions is the rationale for many small pulses (the rate itself is arbitrary).** Per-pulse energy sets the structure (the `R ∝ √E` floor from the near-Sun item) and the worst-case failure. Two payoffs: (1) structure — a smaller pulse means a smaller nozzle/channel/load, and since the ~150 km/s impact speed is unchanged the plasma is just as hot and conductive, so shrinking the pulse does not hurt the MHD coupling; (2) safety — a malfunctioning or hijacked projectile is a small bang, not a Tunguska (cross-link the §War, Policy hacker/Tunguska scenario). Same metering principle as the near-Sun staging item: stream many small pulses and a catastrophic single event becomes a throttle.
  - [ ] **MHD as a *topping* stage over the existing bottoming cycles (decided: option b, not pure MHD).** MHD extracts only the high-grade fraction (~20–40% before the gas is too cool to conduct), so the cooled channel *exhaust* feeds the existing steam-turbine ("Power Plant Chamber Details") or cerium/iron chemical-looping (`sec:strawway_economics`) stages — now sitting a km downstream at the channel's far end, out of the projectile path. Recovers the bulk enthalpy MHD can't take and reuses the paper's existing extraction work rather than discarding it.
  - [ ] **Plasma removal is continuous-flow, not pump-down.** At any sane rate you never evacuate between pulses; the channel runs like an open-cycle MHD generator or an altitude-test facility. The plasma recombines to neutral gas as it cools, a supersonic diffuser recovers pressure, and a large condenser does the "pumping" (liquid is ~1000× denser than vapor); steam ejectors or cryopumps clear the non-condensable trickle; a magnetic divertor steers the spent flow onto the condenser (the tokamak-exhaust pattern). Two synergies: the **bottoming-cycle heat exchanger *is* the condenser** (so option b also solves plasma removal with the same hardware), and the **non-condensable fraction (CO / CO₂ / H₂) is the fuel feedstock** `sec:strawway_economics` already wants, not waste.
  - [ ] **No seeding needed (a genuine advantage over ground MHD).** Terrestrial MHD generators must seed the gas with cesium/potassium to conduct at combustion temperatures, with seed-recovery and corrosion headaches. This plasma is `~10⁵–10⁶ K`, intrinsically conductive, so no seeding. State as a real plus.
  - [ ] **Oxidizer caveat.** The steam chamber gets its combustion oxygen from decomposing steam; a vacuum bottom has no ambient steam, so the carbon → CO/CO₂ chemistry must run on oxygen the projectile carries (its water/oxidizer interior). One sentence; not a blocker.
  - [ ] **Open efficiency question to flag: radiative loss vs. extraction.** At `~10⁵–10⁶ K` the plasma radiates (bremsstrahlung + lines); for a power plant you want that energy in the load, not on the channel walls. Whether MHD extracts faster than the plasma radiates is the real net-efficiency unknown. State as speculative, the key open question.

  The Straw Way can extract power a third way, beside the steam chamber and the direct
  chemical-synthesis loop: electromagnetically, from the collision plasma itself. Keep the bottom
  of the straw under vacuum rather than filling it with steam. The strongest reason is not
  conversion efficiency, it is that the airlock disappears. Today an entire subsection of hardware
  exists only to keep the steam chamber's vapor from backflowing up the evacuated tube where the
  next projectile is falling: a door that seals a 30 cm aperture in a millisecond, sacrificial
  polyethylene plugs, ice coatings. If the bottom is also vacuum, the projectile path and the power
  stage are one continuous vacuum, and that whole problem is gone.

  The projectiles arrive heading straight down, so a long extraction channel cannot be vertical. A
  large magnetic nozzle at the base turns the downward plasma about ninety degrees into a
  horizontal, kilometer-long underground channel. The plasma is a good conductor at these
  temperatures, so as it flows along the channel through a transverse magnetic field it drives a
  current in external electrodes: an MHD generator with no moving parts and nothing touching the
  plasma. The same magnetic-nozzle idea used to redirect collision plasma for thrust near the Sun
  is used here for the opposite purpose. Instead of reflecting the plasma to conserve its momentum,
  the channel brakes it against the field and draws its kinetic energy out as electricity.

  Run the straw as a stream of many small pulses rather than a few enormous ones. The exact rate is
  a free parameter; the point is that the per-pulse energy is what sizes the structure and sets the
  worst case. A smaller pulse means a smaller nozzle and channel and a gentler load, and because the
  impact speed is unchanged the plasma is just as hot and conductive, so shrinking the explosion
  costs nothing in the MHD coupling. It also makes the plant safe: a malfunctioning or hijacked
  projectile is a small burst, not a multi-megaton event. This is the same metering logic that turns
  a single catastrophic impact into a throttle elsewhere in the paper.

  MHD takes only the high-grade fraction of the energy, perhaps a fifth to two fifths, before the
  gas cools too far to conduct. So the cooled channel exhaust feeds the steam-turbine or
  chemical-looping stage already described, now placed a kilometer downstream at the far end of the
  channel and out of the projectile path. That bottoming stage solves a second problem at the same
  time. The plasma never has to be pumped out of a chamber between pulses; the channel runs as a
  continuous flow, like an open-cycle MHD generator. The spent plasma recombines into neutral gas as
  it cools, a diffuser recovers its pressure, and the bottoming cycle's heat exchanger doubles as the
  condenser that holds the vacuum, since condensing the working fluid to liquid is how one pumps an
  enormous volume of gas cheaply. The gases that do not condense, the carbon monoxide, carbon dioxide,
  and hydrogen from the vaporized projectiles, are exactly the feedstock the synthesis loop wants, so
  clearing them and collecting them are the same step.

  Two honest caveats and one bonus. The bonus: ground MHD generators normally seed the gas with
  cesium or potassium to conduct at furnace temperatures, with all the seed-recovery and corrosion
  trouble that brings, but this plasma is hot enough to conduct on its own, so no seeding is needed.
  The caveats: the steam chamber drew its combustion oxygen from decomposing steam, so a vacuum
  bottom must rely on oxygen the projectile carries in its water or oxidizer interior; and at these
  temperatures the plasma radiates strongly, so whether the channel extracts energy faster than the
  plasma radiates it to the walls is the open question that decides the net efficiency.

---

## §When We Get Greedy, We'll Go to Phoebe → `sec:ceresly_good` (ISRU propellant)

Extends the Ceres "convert volatiles to fuel" loop with two propellant options that the
passive-shielding physics unlocks: cryogenic LH₂/LOX where it can be kept cold, and
on-demand water electrolysis everywhere else. Shares the cryo physics with the
`sec:lox_puffsat` sunshade item above. Cross-links `sec:greedy_phoebe` (same logic for
Phoebe/Saturn logistics and the He-3 miner under `sec:mining_helium_3`) and
`sec:fine_control_thrusters` (the "propellant on demand, no pressurized tank" principle).
Resolved in a grilling session (2026-06-30).

- [x] **LH₂/LOX as a cryo option beside methalox, plus on-demand electrolysis for closer-in needs** · `[sizing]` → `sec:ceresly_good` *(landed 2026-06-30: one paragraph after the fuel-loop para in `sec:ceresly_good`, "paragraph + electrolysis line" scope per Seth. Build clean, all cites resolve. Closes the LH₂ forward-ref left in the JWST sunshade item. New cite `nist_webbook_hydrogen` for the 33 K critical temp [NIST WebBook host firewalled, value confirmed via search ~33.19 K]. r^(−1/2) law written in plain words; Saturn/Phoebe ~13 K figure dropped for brevity; "H₂ is propellant not puff gas" caveat dropped as out-of-scope for this para.)*
  - [x] Passive-shielding temperature law: a shaded radiator sits at `T ∝ r^(−1/2)`. Anchored at JWST's ~40 K at 1 AU, that gives ~24 K at Ceres (2.77 AU) and ~13 K at Saturn/Phoebe (9.6 AU). Cites `jwst_sunshield`. *(kept ~24 K at Ceres; ~13 K Saturn figure trimmed)*
  - [x] Passive-LH₂ threshold ~1.5 AU: hydrogen's critical temperature is 33 K, so only beyond ~1.5 AU can a passive shield keep H₂ liquid. Inside it (Moon, Mercury) no shield works at any pressure; at Ceres LH₂ sits at a modest ~3–4 bar. This is the physics behind "Ceres and icy moons, not lunar." *("a few bar" in prose rather than the 3–4 bar range)*
  - [x] Burns are at the cold body: for an Earth-flyby trajectory from Ceres, the departure Δv (lowering perihelion) is applied at Ceres aphelion; the inner leg is ballistic or PuffSat-driven. So LH₂/LOX is made, stored, and burned cold, which dissolves the long-duration boiloff problem.
  - [x] Add LH₂/LOX as a higher-Isp **option alongside methalox** (the ISRU workhorse from Ceres carbon + water) for the local logistics rockets these scenarios already need: return trips, orbit maintenance, mining hold-down/retro, and the Saturn He-3 miner (`sec:mining_helium_3`). H₂ is propellant, **not** PuffSat puff gas (low molecular weight buys nothing for momentum transfer and a near-massless puff spills past the plate). *(Isp 450 s vs 360 s cited to `sutton_rocket_propulsion`; puff-gas caveat dropped — see parent note)*
  - [x] On-demand electrolysis for closer-in / electric / no-cryo cases: store water and electrolyse it with onboard solar at the point of use. Pure-chemical variant = Imperial **ICE-Cube** (`imperial_ice_cube`); Hall-effect electric variant = Imperial **WET-HET** (`schwertheim2022wet_het`). Cross-link `sec:fine_control_thrusters`. *(compressed to the two closing sentences)*

  A shaded radiator equilibrates with the attenuated sunlight, so its temperature falls as
  `r^(−1/2)` with heliocentric distance. Anchoring on the JWST sunshield's ~40 K at 1 AU,
  that is ~24 K at Ceres and ~13 K out at Saturn. Because hydrogen's critical temperature is
  33 K, passive shielding can hold hydrogen liquid only beyond about 1.5 AU: at the Moon or
  Mercury no shield keeps it liquid at any pressure, but at Ceres liquid hydrogen sits at a
  modest few bar. That threshold is exactly why this is a Ceres-and-beyond capability and not
  a lunar one. It also matches where the propulsion happens: for an Earth-flyby trajectory
  launched from Ceres, almost all of the chemical Δv is the departure burn at Ceres aphelion,
  with the inner leg flown ballistically or by PuffSat collision, so the hydrogen is made,
  stored, and burned at the cold body and never carried hot. Liquid hydrogen and oxygen then
  become a higher-performance option beside methalox (which Ceres can make from its carbon and
  water) for the local logistics rockets, the return trips, orbit maintenance, mining
  hold-down and retro thrusters, and the Saturn helium-3 miner. Closer to the Sun, where a
  cryogen cannot be passively stored, the same water serves through on-demand electrolysis
  driven by onboard solar power, feeding either a chemical thruster (the Imperial ICE-Cube
  design) or a Hall-effect thruster (the Imperial water electrolysis Hall thruster), the same
  "make propellant on demand, no pressurized tank" idea as the PuffSat fine-control thrusters.

---

## §War, Policy, And Pulsed Propulsion → `sec:overflight_politics`

- [ ] brief note about geopolitcal overflight risks of PuffSat suborbital travel · `[raw]`

- [x] **Ozone / stratosphere policy mention: avoidable reentry NOx, plus water worth monitoring at scale** · `[raw]` → **new subsection** in §War, Policy (`\label{sec:ozone_policy}`) *(landed 2026-06-30: final subsection of §War, Policy, after `sec:overflight_politics`. Build clean, all 8 cites resolve.)*
  - [x] add the new subsection (two short paragraphs, prose below) *(folded with style cleanup: NOx/bow-shock/photodissociation glossed on first use, SI-wrapped `\SIrange{50}{100}{\year}`, `\SI{200}{\kilo\meter}`, `\SIrange{15}{35}{\kilo\meter}`; reentry spelling matched to paper)*
  - [x] cross-ref `\autoref{sec:200_mile_high}` (where the retrograde reentry-PuffSat deceleration already lives) *(two refs, render as "Section 2.2")*
  - [x] add the 8 `references.bib` entries (block below); verify the `% TODO-CITE`-flagged fields at fold-in *(all author lists now fully resolved via Crossref after `api.crossref.org` was allow-listed: Ferreira [Ferreira, Huang, Nomura, Wang]; Hunga [Xin Zhou, Quanliang Chen, Feng, Heddell, Dhomse, Mann, Pumphrey, Millán, Santee, Chipperfield], vol 7(1) art 198; Barker full 13-author list, corrected to vol 14(5) art e2025EF007229. WMO/IPCC notes stripped since `%` is not a `.bib` comment char and would print. CFC "~50 to 100 yr" kept as hedge. Bibliography still renders "et al." per biblatex default, full lists stored in `.bib`.)*
  - [x] leave the §3 "less pollution for a given ΔV" line (`templateArxiv.tex` ~L244) untouched, per decision *(untouched)*

  **Framing settled in the 2026-06-30 grill** (all three of Seth's points, with the honesty caveats agreed):
  point 1 = reentry NOx is the dominant *avoidable* ozone term and we skip it by braking on PuffSats;
  point 2 = ascent water is the residual worth monitoring at airline-replacement scale, but it clears in
  years; point 3 = PuffSat water at 200 km photodissociates above the ozone layer. Keep the `[raw]`
  epistemic voice ("worth watching", "deserves monitoring"); the policy ask is *measure-and-gate, not
  pre-emptive caps*. NOTE: "hydrolyze" in the original idea was wrong; the upper-atmosphere mechanism is
  **photodissociation** (see `CONTEXT.md` flagged ambiguity). There is **no Starship-specific reentry-NOx
  study**; we apply the general reentry-NOx literature to a Starship-class E2E vehicle. Plain numbers/units
  below get `\SI{}{}`-wrapped at fold-in (style cleanup happens in the paper, per the standing instructions).

  Proposed prose:

  > \subsection{Don't Sweat the Stratosphere (But Do Watch It)}\label{sec:ozone_policy}\cite{carlson1997smallstuff}
  >
  > SpaceX's Earth-to-Earth Starship (see \autoref{sec:200_mile_high}) brakes by hitting the atmosphere at
  > orbital speed. The bow shock heats the surrounding air past several thousand kelvin and makes nitric
  > oxide out of ordinary nitrogen and oxygen. Re-entry NOx is one of the largest ozone-depletion terms for
  > present-day spaceflight, on par with the chlorine from solid rocket motors \cite{ryan2022rocket}. A
  > PuffSat suborbital plane has another route. It sheds orbital velocity against a retrograde formation of
  > reentry PuffSats (see \autoref{sec:200_mile_high}) and enters the air slowly, with a weaker shock and far
  > less NOx. Those PuffSats gasify to water, nitrogen, oxygen, and carbon dioxide, so they also avoid the
  > metal-oxide pathway flagged for re-entering satellites \cite{ferreira2024ozone, barker2026megaconstellation}.
  > The braking is not free. The reentry PuffSats are extra mass that had to be launched, and a slow entry
  > means much less NOx, not zero. Removing the dominant ozone term by design is still a real gain over
  > aerobraking.
  >
  > Water is the residual worth watching. Both the suborbital rocket burn and the Starship that lofts the
  > PuffSats inject water vapor into the stratosphere on the way up. At the scale of replacing airline travel,
  > that input deserves monitoring. Stratospheric water mildly depletes ozone \cite{ryan2022rocket} and adds a
  > modest greenhouse warming \cite{solomon2010stratospheric}, but it clears in a few years, up to about a
  > decade for the highest injections \cite{hunga2026residence}. That is far below the roughly 50 to 100 year
  > atmospheric lifetimes of the CFCs \cite{wmo2022ozone} and the centuries over which carbon dioxide persists
  > \cite{ipcc2021ar6}. The water the PuffSats themselves release sits near 200 km, well above the 15 to 35 km
  > ozone layer. There it photodissociates under solar ultraviolet into hydrogen and hydroxyl, and the light
  > hydrogen escapes to space, so most of it never reaches the ozone below, though some may. The short
  > residence time and the avoidable NOx point to one policy. Monitor the stratospheric water and NOx burden
  > as suborbital traffic grows, and gate expansion to the measured impact rather than capping flights in
  > advance.

  Proposed `references.bib` entries (paste at fold-in; resolve `% TODO-CITE` first):

  ```bibtex
  @article{ryan2022rocket,
    author  = {Ryan, Robert G. and Marais, Eloise A. and Balhatchet, Chloe J. and Eastham, Sebastian D.},
    title   = {Impact of Rocket Launch and Space Debris Air Pollutant Emissions on Stratospheric Ozone and Global Climate},
    journal = {Earth's Future},
    volume  = {10},
    number  = {6},
    pages   = {e2021EF002612},
    year    = {2022},
    doi     = {10.1029/2021EF002612},
  }

  @article{ferreira2024ozone,
    author  = {Ferreira, Jos\'e P. and others}, % TODO-CITE: confirm full author list
    title   = {Potential Ozone Depletion From Satellite Demise During Atmospheric Reentry in the Era of Mega-Constellations},
    journal = {Geophysical Research Letters},
    volume  = {51},
    number  = {11},
    pages   = {e2024GL109280},
    year    = {2024},
    doi     = {10.1029/2024GL109280},
  }

  @article{barker2026megaconstellation,
    author  = {Barker, Connor and others}, % TODO-CITE: confirm full author list
    title   = {Radiative Forcing and Ozone Depletion of a Decade of Satellite Megaconstellation Missions},
    journal = {Earth's Future},
    year    = {2026},
    doi     = {10.1029/2025EF007229},
  }

  @article{solomon2010stratospheric,
    author  = {Solomon, Susan and Rosenlof, Karen H. and Portmann, Robert W. and Daniel, John S. and Davis, Sean M. and Sanford, Todd J. and Plattner, Gian-Kasper},
    title   = {Contributions of Stratospheric Water Vapor to Decadal Changes in the Rate of Global Warming},
    journal = {Science},
    volume  = {327},
    number  = {5970},
    pages   = {1219--1223},
    year    = {2010},
    doi     = {10.1126/science.1182488},
  }

  @techreport{wmo2022ozone,
    author      = {{World Meteorological Organization}},
    title       = {Scientific Assessment of Ozone Depletion: 2022},
    institution = {World Meteorological Organization},
    type        = {GAW Report No. 278},
    address     = {Geneva, Switzerland},
    year        = {2022},
    note        = {Annex lists CFC-11 and CFC-12 atmospheric lifetimes (~50 and ~100 yr). % TODO-CITE: pin exact annex values; csl.noaa.gov PDF is sandbox-blocked, verify on an allowed host},
  }

  @book{ipcc2021ar6,
    author    = {{IPCC}},
    title     = {Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change},
    publisher = {Cambridge University Press},
    address   = {Cambridge, United Kingdom and New York, NY, USA},
    year      = {2021},
    doi       = {10.1017/9781009157896},
    note      = {CO2 has no single lifetime; a substantial fraction persists for centuries},
  }

  @article{hunga2026residence,
    author  = {others}, % TODO-CITE: confirm authors
    title   = {Residence Time of Hunga Stratospheric Water Vapour Perturbation Quantified at 9 Years},
    journal = {Communications Earth \& Environment},
    year    = {2026},
    doi     = {10.1038/s43247-026-03216-5},
  }

  @book{carlson1997smallstuff,
    author    = {Carlson, Richard},
    title     = {Don't Sweat the Small Stuff ... and It's All Small Stuff: Simple Ways to Keep the Little Things from Taking Over Your Life},
    publisher = {Hyperion},
    address   = {New York},
    year      = {1997},
    isbn      = {9780786881857},
    url       = {https://www.barnesandnoble.com/w/dont-sweat-the-small-stuff-and-its-all-small-stuff-richard-carlson/1101004106},
  }
  ```

  Citation verification status (from the 2026-06-30 grill): DOIs/IDs confirmed via search for Ryan, Solomon,
  Ferreira, Barker, Hunga; WMO 2022 and IPCC AR6 are real standard references; Carlson confirmed (Hyperion 1997,
  ISBN 0786881852, B&N page above). Outstanding `% TODO-CITE`: full author lists for Ferreira / Barker / Hunga,
  and the exact CFC-11/-12 annex lifetimes (write "~50 / ~100 yr" until pinned; NOAA/EPA/Wayback are all
  sandbox-blocked here).

---

## §Engineering Feasibility of the Near-Term PuffSat Architecture (`sec:engineering`)

The bulk of the near-term LEO architecture. **Part-1 numbers here are simulation
results** (closed-loop control sim, Rungs A–D, closed out 2026-06-15/16), not
sizing. A terminology primer recurs throughout these subsections and should be
glossed once where the section introduces the guidance concepts (likely
`sec:neural_navigation`):

> **Terminology primer (gloss once in the section).**
> - **Common-mode vs. per-unit error** *(the "block-miss" idea).* When a whole group
>   of projectiles share the same error — they all drift the same way — that is a
>   *common-mode* error: the **block** slides as one. When each projectile differs
>   from its neighbours, that is *per-unit* scatter: the block **spreads**. A
>   block-slide can be cancelled by moving the aim point, whereas spread cannot — so
>   the two need completely different fixes.
> - **Catch radius** *(how close is "close enough").* The largest miss the projectile
>   can still correct in the final seconds. It is set by **engine strength**, not by
>   how well the projectile can see — a thrust limit, not a knowledge limit.
> - **σ_θ · R** *(angular precision × range = position error).* If you measure a
>   direction to an angular precision σ_θ and the target is a distance R away, your
>   sideways position error is σ_θ · R. The same angle that is precise up close is
>   sloppy far away — which is why range R matters as much as the sensor.
> - **Feed-forward** *(plan it, don't chase it).* Computing a disturbance in advance
>   and cancelling it on a schedule, instead of reacting to it after it has pushed you
>   off course.

### → `sec:engineering` (new section-intro overview)

- [x] **"LEO at a glance": the near-term architecture and its confidence ladder, in one place** · `[SIM]` (Tier-1 spine; Tiers 2/3 are `[sizing]`/`[raw]`) *(landed 2026-06-30: three-paragraph section intro inserted at the top of `sec:engineering` [L641–645], before the first subsection. Para 1 = the closed-loop Monte Carlo result (5 m plate feasible, conditional, simulation-not-flight) + the GOCE-upgrade. Para 2 = the three off-board nav assets as a compact preview with `\autoref` to `sec:coordinator_node_dry_mass_disposal` (avoids duplicating that subsection). Para 3 = the three-tier confidence ladder (Tier 1 sim 5 m / Tier 2 argued 10 cm / Tier 3 near-Sun sketch). ADAPTATION: cited `Katz_aim_is_all_you_need_2025` (the bib'd companion repo) rather than naming the raw `puffsat_control_simulation` repo, which has no bib entry — keeps the cite consistent with the GOCE/coordinator folds. Register held at preliminary+conditional. Build clean.)*
  - [x] Open the section with a compact overview a reader grasps before the subsection detail
  - [x] State the GOCE-upgrade up front: navigation feasibility no longer rests on the GOCE analogy; a preliminary closed-loop Monte Carlo (companion repo `puffsat_control_simulation`) now models the full apogee-to-interception problem
  - [x] Name the three off-board nav assets (apogee nav constellation; target-side tracker array; co-flying tracker) and that no dedicated co-flying coordinator satellite is needed
  - [x] Carry the explicit three-tier confidence ladder (Tier 1 simulated 5 m; Tier 2 argued ~10 cm; Tier 3 near-Sun sketch)
  - [x] Hold the umbrella register at "preliminary + conditional"

  A preliminary closed-loop Monte Carlo simulation (companion repo
  `puffsat_control_simulation`) models the full path a PuffSat flies, from deployment near
  apogee (~150,000 km) down to interception near perigee (200 km), and finds that capturing
  a 5 m pusher plate is feasible under the modeled dispersions. The result is conditional on
  the sensor and thruster grades the simulation takes as inputs, uses a conservative
  cannonball drag shape, and is not yet cross-checked against an independent astrodynamics
  tool. It is a simulation result, not a flight result. What it buys the paper is concrete:
  the navigation problem is no longer argued only by analogy to GOCE.

  The near-term LEO implementation uses three off-board navigation assets, none of them a
  dedicated co-flying "coordinator" satellite. (1) A permanent **apogee nav constellation**:
  a small (~3-member) Ka-band network near apogee that broadcasts a one-way authenticated
  nav signal, which the passive PuffSat receives to fix its coast position. This is not GNSS;
  GPS reaches only ~20,200 km, well below apogee. (2) A **target-side tracker array**:
  several independently calibrated cameras on the target that image each PuffSat's optical
  beacon against the star field and drive its terminal homing. (3) A **co-flying tracker**:
  the reused launch rocket, a closer vantage that adds margin but is not required. The
  original paper's co-flying coordinator nodes, which were to track each PuffSat and uplink
  commands, are not needed for LEO. The target itself and the reused launch rocket carry that
  role.

  The feasibility claim runs in three tiers, kept separate on purpose. Tier 1, a 5 m plate
  capture, is the closed-loop simulation result above. Tier 2, shrinking the plate toward
  ~10 cm with surveyor-anchored centring, is argued and sized but not simulated. Tier 3,
  extending the same pattern to a near-Sun (Parker-class) trajectory, is an architectural
  sketch with two open sizing numbers. Only Tier 1 is a simulation result; Tiers 2 and 3 are
  labeled as extrapolations.

### → `sec:formation_challenges_current_missions`

- [x] **Success criterion = capturing the pusher plate, not centimetre centring** · `[SIM]`  (D4 resolved; landed 2026-06-30) *(reframed the committed lateral claim in `sec:formation_challenges_current_missions` [L650] and the related `sec:neural_navigation` claim [L712]: the binding requirement is landing on the 5 m plate, tolerance ~2 m, not centimetre centring. Centimetre centring retired as the committed requirement; ~10 cm stated as the argued achievable capability with LED beacon metrology, 5 cm only as a stretch, framed as margin. Capability-vs-requirement conflation called out per D4(b); RCS off-center-torque cost + plate rotational inertia stated per D4(a). DEFERRED — kept qualitative, no appendix to back them: the ≥99% capture-probability / per-unit σ≤1.65 m / 10 ms arrival-timing specifics [:1147]. The ~10 cm number rests on the gram-scale camera's distortion calibration (the load-bearing bench claim, not beacon brightness), per the 2026-06-30 discussion; that caveat lives in the unfolded Tier-2 item [:1187]. Build clean.)*
  - [ ] Add/replace: mission success = arriving within a ~5 m plate with ≥99% probability (per-unit σ ≤ ~1.65 m, arrival-timing ≤ 10 ms) — *deferred (qualitative for now)*
  - [x] Retire "few-centimetre terminal centring" as the *committed* requirement
  - [x] Keep the centimetre number only as an optional later tightening (Item 9-optional)

  Mission success = the projectile arriving within a **~5 m pusher plate** with
  **≥99 %** probability (per-unit arrival scatter held to σ ≤ ~1.65 m, arrival-timing
  error ≤ 10 ms). The earlier "few-centimetre terminal centring" framing is retired as
  the *committed* requirement.

  The momentum transfer the mission exists to perform (paper §2) happens whenever the
  projectile lands on the plate; it does not require hitting a point. Re-stating the
  requirement as *plate capture* rather than *centimetre centring* is not a softening —
  it is the correct statement of what physically has to happen, and it is what the
  closed-loop simulation actually demonstrates. *In plain terms: the goal is to hit a
  dinner-plate-to-table-sized target reliably, not to thread a needle.* The
  centimetre-class number returns only as an **optional** later tightening (Item
  9-optional), not as the bar the baseline must clear.

- [x] **Block-miss vs. spread: shared error cancelled by re-aiming, only per-unit scatter must fit the plate** · `[SIM]` *(landed 2026-06-30: two compact paragraphs in `sec:formation_challenges_current_missions` [L652–654], right after the D4 reframe and before the drag paragraph. Para A = treat the swarm as a block, common-mode (shared modeled-drag bias or inherited deployer offset) moves it together and is re-aimed away cheaply, plus the off-by-a-kilometer analogy. Para B = only the per-unit scatter must fall within the catch radius (the single most important lever), and the drag/atmosphere corollary (both act on the whole formation nearly identically, so mostly common-mode). ADAPTATIONS: "projectiles"→"PuffSats"; the ±2 km re-aim figure softened to "a few kilometers" (qualitative, no source for the exact number; the launch geometry's tens-of-km retarget authority easily covers it); introduced "catch radius" with a self-contained gloss ("the miss the terminal guidance can still null") and NO number, so it sets up the unfolded catch-radius item [:1361] (~475 m) without pre-empting or duplicating it; dropped the markdown bold and the italic "In plain terms" label (body register is plain prose); split the draft's colon-weld ("not the threat they first appear: they are mostly common-mode") per the colon rule. REFINED 2026-06-30 per Seth (first-use jargon clarity): "common-mode" now introduced bound to its definition ("the same for every PuffSat in the block"), "per-unit scatter" defined inline ("the way the PuffSats differ from one another"), and the catch-radius gloss reworded to "the largest miss the terminal guidance can still correct" (dropped "null"); the summary line reuses "common-mode and per-unit" rather than a third synonym. Build clean.)*
  - [x] Add: treat the train of projectiles as a **block**; common error moves it together and is removed by re-pointing the aim point ±2 km (essentially free)
  - [x] State that only per-unit scatter must fit inside the catch radius — the single most important conceptual lever
  - [x] Note the consequence: stochastic atmosphere + uncertain drag coefficient are mostly common-mode, so not the threat they first appear

  Treat the train of projectiles as a **block**. The part of the error that is
  **common to all of them** (shared coefficient bias, the same atmosphere, a deployer
  offset they all inherit) moves the whole block together and is removed by
  **re-pointing the aim point** by up to ±2 km — essentially free. Only the **per-unit
  scatter** — how the projectiles differ from *each other* — has to fit inside the catch
  radius. This split is the single most important conceptual lever in the architecture.

  *In plain terms: if every projectile is off by the same 1 km, you just aim the whole
  salvo 1 km the other way and they all land on target; you only have a real problem
  if they are scattered relative to one another.* Formally, the common-mode component
  is absorbed by a **centroid retarget** (shifting where the swarm is collectively
  told to go), so the binding requirement is not the absolute miss but the residual
  **per-unit dispersion** about that re-aimed centre. This is why a stochastic
  atmosphere and an uncertain drag coefficient — which hit all the projectiles
  nearly identically — turn out *not* to be the threat they first appear: they are
  mostly common-mode, and common-mode is cheap to cancel.

- [ ] **Optional stretch — surveyor-anchored centring shrinks the plate from 5 m toward ~10 cm** · `[SIM]` (option)  (framing depends on D4)
  - [ ] Add as an explicitly optional §2 tightening, without changing the baseline
  - [ ] (1) sacrificial "surveyor" projectile measured by an independent instrumented gate (laser/microwave hoop, not the optical tracker, not a real impact) pins the swarm's shared optical bias
  - [ ] (2) strobed known-pattern LED beacons on each projectile drive per-unit scatter to centimetres
  - [ ] Beacon power: ~1 W peak optical (tens of mW average at low strobe duty) is ample at formation range; the photon SNR runs in the hundreds, so the cm floor stays the camera's distortion bias, not brightness. The old "kilowatt" scale was the radiation-pressure laser, a different device.
  - [ ] State the honest committed claim: 10 cm (robust); 5 cm as a stretch contingent on a ≤1 cm gate and a well-calibrated camera; 2 cm not claimed

  The plate can be shrunk roughly **50×** (5 m → ~10 cm) by adding two metrology aids,
  *without* changing the baseline above. (1) A **sacrificial "surveyor" projectile**
  whose true crossing is measured by an **independent instrumented gate** (a "hoop"
  using laser or microwave ranging — deliberately *not* the optical tracker, which
  would be checking itself, and *not* a real impact, which would throw off-centre debris
  and glare) pins the swarm's shared optical bias to the plate. (2) **Strobed,
  known-pattern LED beacons** on each projectile let the units measure each other's
  relative positions like a rigid body, driving the per-unit scatter to centimetres.

  The beacons are cheap on power. A strobed near-infrared LED at roughly 1 W peak
  optical output, pulsed at a low enough duty that the average draw is tens of
  milliwatts, lands on the order of 10^5 to 10^6 photoelectrons per frame onto a
  centimetre-aperture camera at formation range (the ~144 m Proba-3 baseline, out to
  ~1 km). That is a photon signal-to-noise ratio in the hundreds, so brightness is
  never the binding term. The centimetre floor stays the camera's distortion
  calibration, the same bias named above, not how hard the beacon shines. Even
  ~1 mW peak would still clear detection, so the watt is margin, not a requirement.
  The "kilowatt" scale belongs to the radiation-pressure laser on a coordinator node
  (a device that *pushes* PuffSats), not to a beacon that only has to be seen. This is
  an order-of-magnitude link budget, not a simulation result.

  This is firmly a **knowledge/metrology** upgrade, not a control one — the centimetre
  trims it asks for sit deep inside the 475 m thrust funnel, so the engine is never the
  limit. *In plain terms: one projectile is sacrificed as a "test shot" measured by an
  independent gauge to fix the whole group's aim, and the projectiles wear blinking
  markers so they can see exactly where each sits relative to the others — shrinking
  the plate without needing a better tracker or a bigger engine.* The achievable plate
  size is then set by two bench numbers: the gate's ranging precision (≤1 cm → a 5 cm
  plate; ~3 cm → a 10 cm plate) and the camera's own calibrated distortion floor. The
  honest committed claim is **10 cm (robust); 5 cm as a stretch** contingent on a ≤1 cm
  gate and a well-calibrated camera; a 2 cm plate is *not* claimed.

- [x] **Precision tiers: near-term meter-class requirement (reframe the lateral claim)** · `[sizing]`  (D4 resolved; landed 2026-06-30) *(folded together with [:1146]. Lateral claim reframed from the 5 cm std-dev assumption to ~2 m required / ~10 cm achievable at L650 and L712; RCS torque cost from a 2 m miss stated. Capability stated as ~10 cm argued via LED beacon metrology, NOT bare "cm", per D4. DEFERRED: the ~100 m along-track / 10 ms timing tolerance [:1227] — the lateral cross-track was the load-bearing piece the 2026-06-30 discussion centered on; along-track can fold later. Build clean.)*
  - [ ] State near-term interception tolerances: ~100 m along-track (≈ 10 ms timing slop at ~10 km/s), ~2 m cross-track on the 5 m plate — *cross-track done; along-track/timing deferred*
  - [x] Reframe the `\SI{5}{\centi\meter}` std-dev centring claim to "~2 m required, cm achievable (VISORS-class)"
  - [x] Note the RCS must cancel the off-center torque from a 2 m miss (more torque = the cost of the relaxed nav)

  Required interception tolerances. These are requirement ceilings, not best-case
  capability:
  * Along-track (approach axis): about 100 m, equal to about 10 ms of timing slop at a
    roughly 10 km/s closing speed. In meters this scales with closing speed; at lower
    closing speeds the same 10 ms is fewer meters. This is cheap: detonation triggers on
    proximity (the ice-wire layer, `sec:icy_puffsat`), the plate is moving and the
    absorber reshapes to keep the pulse centered, and the rocket's RCS absorbs the 10 ms
    timing error. Along-track error mostly sets *when* the pulse lands, not *whether* it
    lands on the plate.
  * Cross-track (lateral, on the plate face): up to 2 m. This is the binding one,
    because the pulse must land on the plate. A 2 m miss on a 5 m-wide plate (2.5 m
    half-width) still lands with about 0.5 m of edge margin.

  Reframe the paper's current lateral claim. The near-term assumption stated as
  centimetre-scale (5 cm std dev) centring should be reframed: cm-scale is the
  achievable/nominal capability (VISORS-class), but the near-term *requirement* is only
  about 2 m lateral on the 5 m plate. Stating the loose requirement, not the tight
  capability, makes the near-term feasibility case far more honest. The cm capability
  becomes margin, not a load-bearing assumption. The RCS must still cancel the
  off-center torque from a 2 m miss; a larger miss means more torque, so that is the cost
  we pay for the relaxed nav: more RCS authority, paid against a heavier plate's
  stability.

- [ ] Big one. GOCE level accelerometer is kilogram scale technology and is not something that fits on a PuffSat. Probably why we can't get millimeter scale PuffSat working. · `[raw]`
- [ ] We only target Puffsat accuracy to 1 meter. Assumption is pusher plate can move, shock absorber can reshape to keep pulse centered. Rockets on main craft also help. · `[raw]`
- [ ] is it easier to do 1mx1mx50m uncertainty of 2m sphere uncertainty and which is relevant? · `[raw]`
- [ ] What if the part of the trajectory above 800 km just needs accuracy within 30 km in absolute terms of where interception is, but then the PuffSat formation (each PuffSats relative position is accurate to within 1 meter radius)? The rationale is the plane can fly to meet the formation. Once the pusher impacts start, then the structure of the PuffSats should be constant - so the bottom one can be shifted as long as shape of every remaining PuffSat is within 2 meters of relative target. · `[raw]`
- [ ] star maps may be enough for necessary angular resolution estimated at 10 micro-rad on the main plane · `[raw]`
- [ ] note the plane can adjust its starting point by 10s of kilometers, so if there is systemic drift in PuffSats is OK as long as PuffSat formation shape is good looking. · `[raw]`

- [x] **GOCE, re-divided: keep it for drag/thrust sizing and as a flown drag precedent; navigation feasibility graduates to the closed-loop sim** · `[SIM]`/`[sizing]` → `sec:engineering` *(landed 2026-06-30: edited the GOCE paragraphs in `sec:engineering` [L648–650]. The ion-unrealistic-for-PuffSats point was already in the paper at L648. Replaced the overclaiming "GOCE accelerometers enable precise corrective maneuvers" sentence with the "encouraging precedent rather than a proof" framing per Seth: GOCE held altitude with ion thrusters + a kg-class accelerometer, neither of which a PuffSat carries, so the precision case rests on the preliminary closed-loop control sim (cite `Katz_aim_is_all_you_need_2025`, the sanctioned [SIM] companion-repo cite), which feed-forward-cancels terminal drag from a ground prior and needs no onboard accelerometer. GOCE's two honest jobs kept (400 mN / <2% sizing; the 229 km drag-compensated-flight precedent). Build clean.)*
  - [x] Keep GOCE as the source of the ~400 mN peak-thrust and <2% cold-gas sizing (`sec:estimate_cold_gas`), now corroborated by the sim's catch-radius and propellant budget
  - [x] Keep one sentence that GOCE flew drag-compensated at 229 km, as a precedent that controlled low-altitude flight is real
  - [x] Move the navigation/guidance feasibility claim onto the closed-loop sim; stop leaning on GOCE as the navigation analogy
  - [x] Dissolve the kg-accelerometer worry (this file, the line-1133 raw note): the sim needs no onboard precision accelerometer, because terminal drag is feed-forward-solved from a ground prior and the bar is a 5 m plate, not millimetres
  - [x] Drop or soften the "GOCE accelerometers enable precise corrective maneuvers" sentence accordingly

  GOCE keeps two honest jobs and loses a third. It stays the source of the thrust and
  propellant sizing: the ~400 mN peak thrust is the GOCE-scaled peak drag at 200 km
  (`sec:estimate_cold_gas`), and the <2% cold-gas budget follows from it. The closed-loop
  simulation now corroborates both, since the 400 mN actuator sets the ~475 m catch radius
  and the full closed-loop propellant budget lands under 2%. GOCE also stays as a one-line
  precedent that drag-compensated flight at ~229 km has actually been flown.

  What GOCE no longer has to carry is the navigation argument. The earlier text leaned on
  GOCE's drag-free control as evidence that PuffSat guidance would work, but GOCE never
  demonstrated an interception. The closed-loop sim models that directly, so the
  navigation-feasibility claim moves there. This also retires a liability: GOCE measured drag
  with a kilogram-scale accelerometer that will not fit on a PuffSat. The sim shows no such
  instrument is needed. Terminal drag is computed ahead of time and cancelled on a schedule
  from a ground-measured coefficient prior, and the success bar is a 5 m plate, not a
  millimetre point. The sentence crediting GOCE accelerometers with "precise corrective
  maneuvers" should be dropped or softened to match.

### → `sec:fine_control_thrusters`

- [ ] propose 3m/s omnidirectional thrust capability of rocket, Gaussian distributed with .5 m/s standard deviation, align once per second. · `[raw]`
- [ ] torque correction is RCS + rocket engine - non,toxic fuel obviously · `[raw]`

### → `sec:coordinator_node_dry_mass_disposal`

- [x] **Rewrite the coordinator-node framing: no dedicated co-flying coordinator satellite for LEO; the role redistributes into three off-board nav assets** · `[SIM]` → `sec:coordinator_node_dry_mass_disposal` *(landed 2026-06-30: rewrote the first paragraph of `sec:coordinator_node_dry_mass_disposal` [L675]. ADAPTED from the backlog draft per Seth: KEPT the coordinator node as an OPTION rather than "retiring" it — the sim finds a dedicated coordinator is not required for LEO and the role can split across three off-board assets (apogee Ka-band ranging constellation, target-side tracker array, reused launch rocket hedge), but the coordinator "stays available where extra on-board computing or relay is wanted." Folded the GNSS-free coast item [:1319] in (no GNSS; Ka-band authenticated ranging near apogee ~150,000 km). Dry-mass-disposal content [L677+] left unchanged. Figure + subsection title KEPT (no rename, since the node stays an option). Cite `Katz_aim_is_all_you_need_2025`. Build clean. Minor follow-up: L677 still says "communication links to the coordinator nodes" — fine since the node remains an option, could be generalized later.)*
  - [x] Replace "a small number of coordinator satellites ... fly alongside the formation ... track the PuffSats' positions and relay adjustment commands" with the redistributed architecture
  - [x] (1) apogee nav constellation (one-way Ka-band broadcast, passive PuffSat) for the coast; (2) target-side tracker array for terminal homing; (3) reused launch rocket as co-flying tracker (a hedge, not required)
  - [x] Keep the dry-mass-disposal content unchanged (discard/aperture/pulverize strategies, the Whipple-like plate as last line of defense): that argument does not depend on who does the tracking
  - [x] Flag, do not silently rename: the subsection title and the `images/Coordinator Nodes.png` caption need revising when this lands
  - [x] Fold the "GNSS-free coast" item below in here as the coast half of the story

  The original section frames a small number of heavier coordinator satellites that fly
  alongside the formation, track each PuffSat, and uplink corrections. The closed-loop sim
  does not need them for LEO. The tracking-and-relay role splits across three assets, none of
  them a dedicated co-flying satellite built to shepherd the swarm.

  For the multi-day coast, a permanent **apogee nav constellation** pins position. It is a
  small Ka-band network near apogee broadcasting a one-way authenticated signal that the
  passive PuffSat receives. For terminal homing, a **target-side tracker array** (several
  independently calibrated cameras on the target) images each PuffSat's beacon against the
  stars and drives the final correction. The reused launch rocket adds a closer **co-flying
  tracker** as a hedge. The target and the launch rocket are already in the architecture, so
  the dedicated coordinator node is retired.

  The dry-mass disposal argument is unchanged, because it does not depend on who tracks the
  PuffSats. The PuffSat still carries little non-volatile solid, still sheds or routes it
  before impact, and the plate still backstops a failed disposal like Whipple shielding. Two
  housekeeping items: the subsection title and the "Coordinator Nodes" figure caption should
  be revised when this lands, and the GNSS-free coast item below folds in here as the coast
  half of the story.

- [x] **GNSS-free coast: a Ka-band, authenticated ranging constellation near apogee** · `[SIM]` → folded into `sec:coordinator_node_dry_mass_disposal` *(landed 2026-06-30 inside the coordinator-node rewrite [:1292]: no GNSS; coast position from a Ka-band authenticated ranging constellation near apogee (~150,000 km). NOT folded here: the dual-use / near-Sun cross-link [`sec:periapsis_challenges`] and the 3–4-member constellation-sizing detail — out of scope for this one paragraph; they remain available for the periapsis chapter or a fuller coast treatment.)*
  - [x] Add: no GNSS anywhere; coast position knowledge from a Ka-band authenticated ranging constellation near apogee (~150 000 km)
  - [ ] Terminal knowledge comes from the optical tracker array (see `sec:neural_navigation`); midcourse computed against the coast solution, endgame against the optical one
  - [ ] Size the constellation only to *match* the coast accuracy needed (a few hundred metres at hand-off); 3–4 members supply it with large margin
  - [ ] **Dual use:** the same Earth-apogee constellation also covers the near-Sun (Parker) scenario, because an Earth→Sun transfer has its departure apoapsis at Earth · `[raw]` (cross-link `sec:periapsis_challenges`)

  There is **no GNSS** anywhere in the chain. Position knowledge during the multi-day
  coast comes from a **Ka-band, authenticated ranging constellation** parked near apogee
  (~150 000 km), and terminal knowledge comes from the optical tracker array. The
  midcourse correction is computed against this coast solution; the endgame against the
  optical one.

  Relying on GNSS for a mission whose whole point is high-energy interception would be
  fragile and, near the Sun, impossible. *In plain terms: the projectiles navigate by
  ranging off a small fleet of "lighthouse" satellites high up during the cruise, then
  switch to looking directly at the target for the final approach — no reliance on the
  GPS network at all.* The constellation is sized only to **match** the accuracy the
  coast actually needs (a few hundred metres of position knowledge at the hand-off),
  which a minimum of **3–4 members** supplies with large margin; it does not need to be
  a precision instrument. This is a genuine architectural addition — the current paper
  does not specify how the coast state is known.

  The same constellation does double duty for the near-Sun chapter. An Earth→Sun
  transfer departs from Earth, so the orbit's apoapsis at departure — its slow, far
  point from the Sun, where the probe lingers longest — sits at Earth's orbital radius,
  right where this fleet is parked. The apogee ranging that fixes the coast state for
  the Earth-interception case therefore carries straight over to the heliocentric,
  Parker-style trajectory: the probe is still near Earth, and still slow, at that first
  apoapsis, exactly when the constellation can range it. It only stops being useful as
  the probe falls inward toward periapsis, which is the regime the near-Sun options in
  `sec:periapsis_challenges` (ranging nodes, optical endgame) exist to cover. *In plain
  terms: the lighthouse fleet built for Earth apogees also lights the start of the run
  to the Sun, because that run begins at Earth.*

- [ ] active transponder on PuffSat. Measures both distance and doppler velocity shifts · `[raw]`
- [ ] at least 4 coordinator nodes, with both perigee and apogee updated. Consider also using GNSS signal below geostationary orbit. · `[raw]`
- [ ] do we need GNSS if we have this precise measuring/broadcasting from the rocket coming up from the ground and any ground infrastructure, which seems like everything is much closer than GNSS to the key impact point · `[raw]`
- [ ] explain hardware encryption of repeated signal. Question need for coordinator nodes. Two telescopes on opposite side of rockets, 10 microradians, satellites may only be hundres of kilometers apart in orbit even though the distance grows much larger at perigee. At around 2500 km, bigger satellite changes orbits to raise perigee, come around one more time for its landing spot with another apogee burn. · `[raw]`
- [ ] space only GNSS. ka-band higher frequency helps doppler and range accuracy. Verifying no coordinator nodes needed. · `[raw]`

### → `sec:neural_navigation`

- [x] **The catch radius is a thrust-limited funnel (~475 m), set by the engine** · `[SIM]` *(landed 2026-06-30: two compact paragraphs at the end of `sec:neural_navigation` [L718–720], after the lateral-requirement paragraph and before `sec:handling_space_debris`. This starts the terminal-navigation trio; the knowledge-limit item [:1379] and tracker-array item [:1400] will follow here. Para 1 = the catch radius (~475 m recoverable miss) set by $\tfrac{1}{2}a t^2$ thrust×time, not by tracking quality; ties back to the block argument "above" (`sec:formation_challenges_current_missions`) and delivers the number that the block-miss gloss deliberately deferred; cited `Katz_aim_is_all_you_need_2025`. Para 2 = the funnel narrows as time-to-go shrinks (funnel defined inline), the rocket-not-eyesight analogy, the ~2× authority margin (kept qualitative as "a factor of two to spare"), and a pivot to "knowledge is the real limit" as a standalone insight that sets up [:1379] without a dangling cross-ref. ADAPTATIONS: "projectile"→"PuffSat"; dropped the italic "In plain terms" label; $\tfrac{1}{2}a t^2$ uses `\tfrac` (amsmath + `\tfrac` already in the paper); reworded the backlog's internal "the limit lives elsewhere, in the next item" pointer into a self-contained closing insight. Build clean.)*
  - [x] Add: terminal endgame corrects any miss up to ~475 m, fixed by ½·a·t² of constant acceleration, not by nav quality
  - [x] Explain the funnel: time-to-go shrinks, reachable sideways distance shrinks, region closes toward the plate
  - [x] State the separation of concerns: authority (engine) sets recoverable miss; entry error budgeted ~2× inside the funnel; the real limit is Item 4

  The terminal endgame can correct any miss up to a **catch radius of ~475 m**, and that
  number is fixed by how far the engine can pull the projectile sideways in the time
  remaining — the familiar ½·a·t² of constant acceleration — *not* by navigation quality.

  Because the projectile is descending fast, the time-to-go shrinks continuously, and
  with it the reachable sideways distance: the correctable region is a **funnel** that
  closes toward the plate. *In plain terms: the closer you get, the less room you have
  to swerve, and the size of the last possible swerve is decided by your rocket, not
  your eyesight.* The practical consequence for the paper is a clean separation of
  concerns — **authority** (engine strength) sets *how big* a miss is recoverable, and
  the projectile arrives with margin to spare on that axis (the budgeted entry error is
  ~2× inside the funnel). The limit lives elsewhere, in the next item.

- [ ] **The binding constraint is terminal cross-track *knowledge*, a calibration bias not random noise** · `[SIM]`
  - [ ] Add: the deciding quantity is how well the projectile knows its sideways position in the last seconds (σ_θ · R); requirement is an effective ~3 µrad
  - [ ] State it is limited by a fixed calibration bias in the optics, not random noise
  - [ ] State what does NOT help (more engine/later burns/bigger thrusters; longer integration/faster sensors/heavier filtering) and what does (sharper angle via calibration or star-differencing, or shorter R)

  The one quantity that actually decides success is **how accurately the projectile
  knows its sideways position relative to the target in the last seconds** — the
  cross-track error σ_θ · R. The simulation shows the requirement is an effective
  **~3 µrad** angular precision on the target tracker, and crucially that this is limited
  by a **fixed calibration bias** in the optics, *not* by random noise.

  This distinction reorders the engineering priorities and is worth stating plainly in
  the paper. *In plain terms: the problem is not a shaky picture you can steady by
  taking more exposures — it is a ruler with a slightly bent end. Averaging more
  measurements cannot fix a bent ruler; only re-calibrating or cross-referencing it
  can.* Two whole families of "obvious" fixes therefore do **nothing** here — more
  engine, later burns, bigger thrusters (the limit is knowledge, not control) and
  longer integration, faster sensors, heavier filtering (the limit is a bias, not
  noise). The levers that *do* work are spatial and geometric: sharpen the angle
  (better calibration, or differencing against known stars) or shorten the range R.

- [ ] **Terminal homing rides a *fused tracker array* (plus optional close co-flyer), not a single sensor** · `[SIM]`
  - [ ] Add: the ~3 µrad effective grade comes from fusing several cruder (~10 µrad) detectors on the target plate, optionally a co-flying rocket much closer to the action
  - [ ] Explain the two handles: array averages independent biases (∝ 1/√N; five 10 µrad → ~1.6 µrad); co-flyer shortens R
  - [ ] Present terminal nav as redundant/fused — more accurate and protects the result if one optic's calibration is worse than hoped

  The ~3 µrad effective grade is delivered not by one exquisite sensor but by **fusing
  several cruder (~10 µrad) detectors** on the target plate, optionally augmented by a
  **co-flying rocket** much closer to the action. The array beats a single sensor by
  averaging independent errors (∝ 1/√N), and the co-flyer wins by shortening the range R.

  Each detector does its own star-referenced measurement with its own separately
  calibrated optics, so their distortion biases are largely independent and partly
  average away — five 10 µrad detectors give ~1.6 µrad. *In plain terms: five ordinary
  cameras that each make their own small, different mistakes beat one expensive camera,
  because their mistakes partly cancel when you combine them.* The co-flyer contributes
  on the **other** handle in σ_θ · R: sitting closer to the converging projectiles, its
  modest angular precision still yields a small sideways error because R is small. The
  paper should present terminal navigation as this **redundant, fused** architecture —
  it is both more accurate and more robust than any single-sensor story, and the
  redundancy is what protects the result if the calibration of any one optic proves
  worse than hoped.

- [ ] **Atmospheric drag is feed-forward-cancelled, not fought in the loop** · `[SIM]`
  - [ ] Add: in terminal descent, drag is removed by computing it ahead of time and thrusting against it on a schedule (feed-forward), not a reactive loop
  - [ ] State the numbers: an entirely uncompensated drag pass displaces the crossing only ~8.5 cm; feed-forward reduces it to ~2 mm
  - [ ] Note the real coefficient risk sits upstream as a small, mostly common-mode coast bias (handled by the midcourse correction)

  During the terminal descent, drag is removed by **computing it ahead of time and
  thrusting against it on a schedule** (feed-forward), not by a reactive drag-rejection
  loop. Drag does **not** set the terminal miss. The place where an uncertain
  drag/solar-pressure coefficient *does* matter is far earlier — it slightly biases the
  long coast, and that is handled by the midcourse correction (next item), not the
  endgame.

  The simulation makes this concrete: an *entirely uncompensated* drag pass displaces
  the crossing by only ~8.5 cm (drag concentrates in the final seconds), and the
  feed-forward profile reduces even that to ~2 mm. *In plain terms: near the target the
  air is so thin that drag barely nudges you, and the small nudge it does give is
  predictable enough to cancel by planning, not by chasing.* The consequence for the
  paper is that the much-feared coefficient uncertainty is **not** a terminal-accuracy
  problem; it lives upstream as a small, mostly common-mode coast bias — which the
  block-miss item has already shown is cheap to absorb.

- [ ] **The midcourse burn acts on a *ground prior* — no on-board estimator runs before it** · `[SIM]`
  - [ ] Add: because deployment, apogee, and the first burn occur at nearly the same time/place, no in-flight nav filter can usefully run before the burn
  - [ ] State the midcourse correction is planned against the ground-determined prior, and the sim confirms it is more than good enough (tolerant across a coefficient band ~34× the prior's uncertainty)
  - [ ] State plainly: in-flight coefficient estimation is unnecessary for the midcourse — removes a whole speculative subsystem

  Because deployment, apogee, and the first correction burn all occur at nearly the same
  time and place, **no in-flight navigation filter can usefully run before the burn**.
  The midcourse correction is therefore planned against the **ground-determined prior**
  (the best pre-flight estimate of state and coefficients), and the simulation confirms
  this prior is more than good enough.

  This is a subtle but important honesty in the architecture. *In plain terms: the
  projectile does not get a chance to "figure out" its drag in flight before it must
  act — there isn't enough time or distance — so it uses the number measured on the
  ground, and that number turns out to have ample margin.* The measured tolerance is
  wide: the correction stays accurate across a coefficient error band ~34× larger than
  the ground prior's actual uncertainty. The paper can state plainly that **in-flight
  coefficient estimation is unnecessary for the midcourse**, which removes a whole
  speculative subsystem from the near-term story.

- [ ] PuffSat self-homing as a redundancy layer: besides the load-bearing target-side tracker array, each PuffSat can carry a few-gram camera to image a bright target beacon against stars and run its own terminal guidance, fusing both bearing directions. Strengthens the no-coordinator story and the autonomy of the final correction. Costs a little non-volatile dry mass that must be disposed before impact (within the 250 g budget). Not yet simulated: the sim modeled only the target-side path, which stays the baseline. We expect it to help, not replace. · `[raw]`

### → `sec:handling_space_debris`

- [ ] **Propellant stays under 2 %, and the low (~50 km) perigee is an intended disposal feature** · `[SIM]`
  - [ ] Add/reinforce: full closed-loop propellant budget (cruise corrections + terminal aim) lands under 2% of the 25 kg projectile mass even in the worst sampled case
  - [ ] State the deliberately low perigee (~50–65 km) is a designed outcome: de-orbits the spent projectile, burns up any miss (clean disposal)
  - [ ] Make explicit perigee is a diagnostic where lower is safer, not a target to hit (so a reader does not mistake "50 km perigee" for a nav error)

  The full closed-loop propellant budget — cruise corrections plus the terminal aim —
  lands **under 2 % of the 25 kg projectile mass** even in the worst sampled case.
  Separately, the deliberately **low perigee (~50–65 km)** is a *designed* outcome: it
  de-orbits the spent projectile and burns up any unit that misses, for clean debris
  disposal (paper §9). Low perigee is **good**, not a fault.

  The paper already claims <2 % propellant; the contribution here is that a *simulated
  closed loop* — corrector, terminal guidance, finite-thrust execution, dispersed
  environment — confirms it rather than asserting it. *In plain terms: the whole job
  costs less than one part in fifty of the projectile's mass in fuel, and a miss
  self-disposes by re-entry instead of becoming space junk.* It is worth making
  explicit in the text that perigee is a **diagnostic where lower is safer**, not a
  target to be hit — otherwise a reader sees "50 km perigee" and mistakes the disposal
  feature for a navigation error. (Propellant-budget reinforcement also touches the
  cold-gas appendix `sec:estimate_cold_gas`.)

### → `sec:leo_orbit_details`

- [ ] Van Allen radiation shielding is provided by Puffsat itself. Relatively easy for outer Van Allen belt - time through inner belt with high energy protons is short enough to accept risk. Triple mmjority redundance (used on SpaceX - need source) · `[raw]`
- [ ] slow down PuffSat can't be purely low Earth orbit because of atmospheric drag. · `[raw]`

### → `sec:lightweight_pusher_plates`

This subsection ("Lightweight Pusher Plate Design: Materials and Damping Innovations
Beyond Orion") is the destination for the Medusa-geometry and pusher-plate trades.
The body gets the conceptual claims (2–3 sentences each); the math goes to the new
appendix below.

- [x] **Body: our Medusa-style sail is behind the rocket (compression), unlike real Medusa (tension)** · `[sizing]` → `sec:lightweight_pusher_plates`  (D2 resolved; refined by the 2026-06-29 Medusa grill — now the authoritative Medusa-structural body item; Appendix Y killed) *(landed 2026-06-30: three paragraphs after the Medusa-sail intro paragraph in `sec:lightweight_pusher_plates`. Build clean, no undefined refs, no AI-smell violations. Para 1 = buffer-invariant tradeoff (long-stroke light sail vs short-stroke heavy plate) + concave-face cross-ref to `\autoref{sec:mass_fraction}`. Para 2 = compression/buckling (qualitative Euler L² point, NO formula or strut numbers) + sailboat-mast guy-wire / telescoping mitigation. Para 3 = rear-mount fail-safe + uncrewed-cargo front/tension fork + side-split (paired/annular, partially fail-safe, harder aiming). Adaptations: did NOT name the undefined "m·s law" — stated the stroke-vs-mass tradeoff self-containedly, since the rigid-plate body paragraph [:1562] isn't folded yet; did NOT claim the "direction half of f" split (unfolded), just "raises the effective f" matching the existing L260 collimation point; cited `solem_medusa` for the real-Medusa sail-ahead/tension geometry.)*

  > **STATUS 2026-06-29 (Medusa grill).** Appendix Y is killed; its content collapses into
  > this body item plus re-homing. Decisions: (1) keep the full rear-mount fail-safe
  > paragraph (compression + crew-shielding + cargo fork) — sub-bullets and prose below;
  > (2) rescue ONE buckling-mitigation clause into the body (guyed by tension stays like a
  > sailboat mast, telescoped so peak load hits at short length), drop all strut numbers
  > (10–12 t / 1.5–2 t / √E·ρ⁻¹); (3) keep ONE qualitative buffer-invariant unification
  > sentence (sail and rigid plate are the two ends of one `m·s` law); (4) add a
  > half-sentence cross-ref to §Mass Fraction for the concave-face momentum point, do NOT
  > re-derive it here; (5) the LEO-drag idea was considered and dropped (~3 N on a 200 m²
  > sail at 200 km, negligible vs thrust); (6) the off-center-torque note and the
  > zero-torque down-push placement are re-homed outside the Medusa section (see those
  > items); (7) fold the parked `:1168` "possibility at sides" raw note into the body
  > cargo-fork as ONE hedged sentence (side-split front/tension sail kept on-axis by a
  > paired or annular layout, only partially fail-safe, harder aiming).
  - [x] State the sail is mounted behind the rocket, so its struts carry compression, unlike real Medusa's tension cables, and compression members buckle (the L² penalty). Add the one-clause mitigation: the strut is braced by tension stays like a sailboat mast and telescoped so peak compression coincides with its shortest length. No numbers.
  - [x] State the rear mount is a deliberate fail-safe: the expendable sail shields the crew and overshoots fly off behind, whereas a front/tension sail would force every PuffSat past the crew cabin
  - [x] One sentence: the front/tension variant suits uncrewed cargo. Drop all buckling numbers entirely (Appendix Y killed — the qualitative L² point plus the mitigation clause carry the argument)
  - [x] Add ONE qualitative buffer-invariant unification sentence where the sail is introduced alongside the plate: the sail and the rigid plate are the two ends of one `m·s` law — the sail trades a long stroke for a light buffer, the plate a short stroke for a heavy one. No numbers. (Lands with the pending rigid-plate body paragraph; the only Appendix Y content that survives.)
  - [x] Add a half-sentence cross-ref to §Mass Fraction for the shape/momentum point: the sail's concave gas-facing face wraps the divergent puff and collimates the rebound forward, the same curvature lever that raises effective `f`. Fix the wording — it is the **concave** face (convex is the payload side), and it helps the **direction** half of `f`, not the restitution. Do not re-derive the opacity-vs-geometry split; point to the fudge-factor item (`:130–135`).
  - [x] Add ONE hedged sentence extending the cargo fork (folds in the parked `:1168` "possibility at sides" raw note): a front/tension sail split symmetrically to the sides (paired or annular, thrust on-axis) routes PuffSats up the flanks and can keep even a crewed cabin off the centerline, recovering the no-buckling tension advantage — but it is only partially fail-safe (a miss can clip the flank, not fly off behind) and costs harder off-axis aiming.

  *Resolved context (behind = compression).* The behind-mounted sail puts the struts in
  **compression** (tension is real Medusa, sail in front). Real Project Medusa: sail
  ahead, payload behind, bomb detonated in the gap; every connective member in tension,
  so cables can be very long and very light. Our design: PuffSats approach from the rear,
  so the sail is behind the rocket; to add forward momentum the gas must move forward
  faster than the craft and strike the rear face of the sail, so the members carry
  **compression**, and compression members buckle. Euler critical load
  P_cr = π² E I / (K L)² falls as 1/L², so a ~100 m compression strut is a far harder
  structural problem than a 100 m Medusa tether. That is the real, substantive
  difference between our concept and Medusa. The penalty is paid down, not eliminated. A
  compression boom braced by tension stays, on the sailboat-mast principle, and telescoped
  so its peak load falls at its shortest length, stays buildable, which is why the concept
  survives the L² cost.

  *Why keep the sail behind anyway (the rationale to state).* Forward acceleration with
  *external* reaction mass forces the source PuffSat to approach from behind and overtake
  the craft. A front-mounted (true-Medusa, tension) sail would require every PuffSat to
  thread past the crewed vehicle at km/s, making the crew cabin the first thing a
  mis-aimed hypervelocity solid meets. A rear sail is fail-safe by geometry: size the
  sail silhouette at least as large as the craft, and any PuffSat that misses the sail
  also clears the craft; overshoots and duds fly off into empty space behind. The
  expendable membrane always shields the crew. So the compression/buckling mass penalty
  is the price of keeping humans out of the firing line. Fork for uncrewed cargo:
  front/tension (light tethers, no buckling) becomes attractive when a rare strike is a
  lost vehicle, not lost lives. A side-split variant could narrow that gap. A front/tension
  sail divided symmetrically to the sides, paired or annular so the thrust stays on the
  axis, routes the PuffSats up the flanks and keeps even a crewed cabin off the centerline,
  recovering the no-buckling tension advantage. It is only partially fail-safe, because a
  mis-aimed solid can still clip the flank rather than flying off behind, and it costs
  harder off-axis aiming.

  *Buffer-invariant unification (one sentence, with the rigid-plate paragraph).* The sail
  and the rigid plate are the two ends of one `m·s` law: the sail trades a long stroke for
  a light buffer, the rigid plate a short stroke for a heavy one.

  *Shape and momentum (half-sentence cross-ref).* The sail's concave gas-facing face wraps
  the divergent puff and collimates the rebound forward, the same curvature lever the
  fudge-factor discussion uses to raise the effective `f` (see §Mass Fraction).

- [x] **Body: the plate has no Orion-style critical mass — two compact paragraphs, no appendix** · `[sizing]` → `sec:lightweight_pusher_plates`  (D1/D3 superseded 2026-06-29; replaces the killed Appendix X) *(landed 2026-06-30: two compact paragraphs after the shock-absorber paragraph in `sec:lightweight_pusher_plates`, before the down-push passage. Build clean, `iso2631` resolves, no AI-smell violations. Para 1 = no-critical-mass / Orion yield-floor contrast (cite `balcomb1970nuclear`) + the quadratic buffer trade as ONE dividend (lighter plate OR shorter stroke, not both) + D3 anchor triple (4 Hz, 4.6 m, 3.2 t ≈ 10% of 32 t) + survivability-floor honesty clause (10–50 kg/m², dynamics not survival bind). Para 2 = ripple driven into the 4–8 Hz ISO 2631 band (single-stage 0–6 g) + two-stage Orion-heritage absorber (cite `projorion`) + the one number (~0.7 Hz second stage, ~30× cut, 3 g ± 0.1 g). KEY ADAPTATION: the appendix formula `m_p·s ≈ Ma/(4f²)` uses `f`=pulse FREQUENCY and `m_p`=plate mass, both clashing with the paper's f (fudge factor) and m_p (PuffSat mass); the units confirm f=frequency. So I dropped the explicit formula and stated the 1/frequency² scaling in words ("drops as the inverse square of the pulse rate; doubling the rate quarters it"), avoiding the clash. Wording guard honored (the PRODUCT scales, not each factor). New cite `iso2631` (ISO 2631-1:1997) added to references.bib. Tables + full worked example (235 kN·s, 73 m/s, 60 g, 128 kg/m²) dropped as decided. REVISED 2026-06-30 per Seth (no appendix to back precise figures): softened the D3 anchor triple and the Para-2 numbers to order-of-magnitude. KEPT: ~tenth-of-craft on the established \SI{32}{\tonne} LEO vehicle, the cited 4–8 Hz ISO 2631 band, and the inverse-square scaling (hedged "roughly as its inverse square"). SOFTENED: 4 Hz→"a few hertz", 4.6 m→"a few meters", 3.2 t→"a few tonnes", 0–6 g→"several g", and 0.7 Hz / 30× / 3 g ± 0.1 g → "tuned well below the pulse rate / more than an order of magnitude / a nearly steady push", 10–50 kg/m²→"tens of kilograms per square meter". This overrides D3's "keep the precise anchor triple" call.)*
  - [x] Slot both paragraphs near the existing shock-absorber discussion (`sec:lightweight_pusher_plates`, the MR-fluid / magnetic-braking paragraph, line ~739 of `templateArxiv.tex`, which already hooks "deliberately reduce acceleration per pulse... relaxing shock absorber requirements")
  - [x] **Paragraph 1 — the minimization argument (the spine).** Lead with the Orion contrast: Orion's plate was forced huge by the kiloton *yield floor* (no arbitrarily small bomb), whereas PuffSat pulse energy scales down smoothly — no critical mass. Then the mechanism, stated **as a trade, not a double win**: the buffer product `m_p·s ≈ M a /(4 f²)` falls as 1/f², so smaller, more frequent pulses buy either a lighter plate at fixed stroke or a shorter stroke at fixed mass — one quadratic dividend to allocate, *not* both shrinking quadratically at once. Anchor with the D3 triple: *at 4 Hz a 4.6 m stroke holds the plate near 3.2 t, ~10% of a 32 t craft.* Close with the honesty clause: floors remain but are gentle — a survivability floor of ~10–50 kg/m² (far below Orion's regime) eventually binds, but in the worked case it is the `m·s` dynamics, not survival, that set the ~10% plate (several-× margin). Cite Orion for the yield-floor contrast.
  - [x] **Paragraph 2 — the ripple cost and its fix (the load-bearing half).** Higher f drives the ripple into the worst whole-body-vibration band: a plain absorber swings the craft 0–6 g at 4 Hz (4–8 Hz is the ISO 2631 worst band). A two-stage absorber (Orion heritage) fixes it: stiff short-stroke first stage catches the per-pulse blow, soft second stage with natural frequency well below the pulse rate isolates the crew. Carry **one** representative number inline instead of the transmissibility table, e.g. *a ~0.7 Hz second stage cuts the ripple ~30×, leaving 3 g ± 0.1 g.* Cite Orion + ISO 2631.
  - [x] **Dropped:** both mass-trade tables; the full worked example (235 kN·s, 73 m/s, 60 g, 128 kg/m²); the three-row transmissibility table. Net: ~80 appendix lines → ~12 body lines. Keep the paragraphs genuinely compact — do not let the tables creep back as prose.
  - [x] **Wording guard:** never write "plate mass *and* stroke both fall quadratically" — that is a factor-f² overclaim. It is the *product* `m_p·s` that scales as 1/f².
  - [x] This supersedes the worst-case "1/1 pusher plate" raw note — the plate reaches ~10% of craft, not 1/1.

- [x] **Down-push from descending-leg interception, cancelled by the plate's rebound geometry** · `[sizing]` `[SIM]` → `sec:lightweight_pusher_plates` *(landed 2026-06-30: three compact paragraphs appended to `sec:lightweight_pusher_plates`, after the shock-absorber paragraph, before the Conclusion. Build clean, all cites resolve. Premise cross-refs the existing `\autoref{sec:handling_space_debris}` (50 km perigee + 200 km descending-leg interception already in the paper at L158/L709). Sim cited with the f=0.8-style "preliminary single-code hydrodynamic analysis" caveat `\cite{Katz_puffsat_impact_sim_2026}`; `solem_medusa`/`projorion` cited as design heritage (concave wrap / momentum coupling), `balcomb1970nuclear` untouched. Shared-lever/two-payoffs point cross-refs `\autoref{sec:mass_fraction}` (added a `\label` to the existing "Mass Fraction Of Rocket To PuffSat Mass" subsection, which already states the curved-plate-collimates-and-raises-`f` point at L260 — so the ref is non-dangling; it does NOT depend on the unfolded "disentangle `f`" reframe). New colon rule applied: no colon welds in the added prose. γ now COMPUTED, not estimated: for a 50 km perigee + ~150,000 km (near-escape) apogee, the flight-path angle at the 200 km interception altitude is γ ≈ 8.5°, so sin γ ≈ 0.148 ≈ 15% (robust: γ stays 7.9–8.6° / sin γ 13.7–14.9% across apogees 30,000–300,000 km). The old "order 10–25%" was replaced by this concrete value. Note: 8.5 is the angle in *degrees*; the downward momentum *fraction* is sin γ ≈ 15%, not ~8–9%. Softened the "mostly free" framing per Seth: at f≈0.8 the bounce is partly inelastic, so the geometric pass-through is imperfect and leaves a residual down-force (worst near orbital speed, where the down-fraction is ~half), handled by the active trim / RCS at a small thrust cost — "cheap rather than free," not "only forward thrust." Also added "deliberately low" to the 50 km perigee mention to motivate it inline (the `\autoref{sec:handling_space_debris}` was already present and carries the one-pass-destruction rationale; raising perigee to ~120 km was considered and rejected — only shaves γ 8.5°→6.2° and forfeits single-pass disposal since a 120 km pass at ~10.8 km/s is ~42,000× gentler in dynamic pressure than 50 km). SPIN-OFF LANDED 2026-06-30 in `sec:handling_space_debris`: added an alternative disposal option — raise the PuffSat perigee to the 200 km interception altitude (catch at perigee, ZERO down-angle), then the dry mass does a tiny ~4 m/s burn at the next apogee to drop its perigee to ~50 km for reentry. Cheap because at a near-escape apogee the package crawls (~453 m/s) and perigee is hypersensitive (the same change costs ~1.4 km/s if burned at perigee; ~350× worse). Framed as paying off ONLY when f is low (when the plate-angling cancellation leaves too big a residual); `\autoref{sec:lightweight_pusher_plates}` back-ref; costs ~1 extra orbit (~1.3 days) of loiter and REQUIRES highly reliable hardware (a dud strands debris at 200 km). Within the microthrusters the dry mass already carries (sec:coordinator_node_dry_mass_disposal).)*
  - [x] State the premise (set up by the `sec:handling_space_debris` ~50 km disposal item): PuffSats are caught on the descending leg, falling toward the ~50 km disposal perigee, so their velocity relative to the craft carries a downward (radially-inward) component. Each pulse delivers forward thrust plus a downward kick of about `sin γ` of the impulse (γ = the PuffSat's flight-path angle below the craft's velocity), order ~10–25%. Pull γ from the trajectory design; do not invent it. Same sign every pulse, so it is cumulative and bends the trajectory Earthward if left uncorrected. *(γ now computed directly from the delivery orbit: 50 km perigee + near-escape apogee → γ ≈ 8.5° at the 200 km interception, sin γ ≈ 15%. Replaced the earlier "order 10–25%" estimate. The earlier 8–9% intuition was the angle in degrees, not the sin-γ fraction. Also added a sentence that the 15% is a FLOOR: the downward part holds ~1.6 km/s while the forward overtaking velocity shrinks as the craft accelerates, so the impulse's downward fraction climbs to ~49% by the time the craft reaches LEO speed (~7.8 km/s). Substantial growth, not "slight" — quantified rather than hedged.)*
  - [x] State the primary fix (orientation/shape, not active down-throwing): the net force on the craft is set by the plate's orientation relative to the **thrust axis**, not relative to the incoming-PuffSat line. A plate whose normal lies along the thrust axis reverses only the forward component of the gas and lets the downward component pass back out, so the rebound carries the PuffSat's downward momentum away and the craft feels pure forward thrust. A plate squared-on to the incoming PuffSat does the opposite and doubles the down-kick.
  - [x] State why the trim rides on the reflected momentum, not on spill: the plate is opaque (the same opacity result behind the high `f`), so little gas escapes sideways past it (now backed by our hydrocode — see the support bullet below), and we want to keep that spill small anyway to hold `f` high. If an active upward trim `F_up` is wanted beyond just neutralizing the kick, get it by tilting the plate slightly further off the thrust axis so the reflected gas is thrown a little downward, giving an upward reaction scaled by the full rebounded momentum rather than by a small spill fraction. (Drops the earlier biased-spill variant, which tried to harvest sideways-escaping gas; an opaque plate reflects rather than letting gas escape past the edge.) *(biased-spill "earlier variant" meta-note dropped from the paper; its substance — trim rides on reflected momentum, not spill — kept.)*
  - [x] Support (resolved 2026-06-29): the empirical "little gas spills sideways" claim now rests on our own hydrocode, not on a contested reading of Solem. A preliminary single-code hydrodynamic analysis (companion repo `puffsat_impact_simulation`, `Katz_puffsat_impact_sim_2026`) finds **sideways escape** is a subdominant loss channel across the LEO insertion band, below the condensation/conduction channels even at the cool 3.2 km/s water worst case. Cite it with the same "preliminary single-code, not yet validated" caveat the paper already uses for `f=0.8` (`templateArxiv.tex:253`). `[SIM]` fill in the actual sideways-escape fraction (and its velocity anchor) from the loss-decomposition output once it is in hand; until then state the claim qualitatively (subdominant), not with a number. *(landed qualitatively per instruction; the `[SIM]` sideways-escape number is still OPEN and remains the only follow-up for this item once the loss-decomposition output is in hand.)*
  - [x] Cite roles now that the sim is primary: `solem_medusa` (concave sail wrapping the divergent expansion) and `projorion` (pusher-plate momentum coupling) demote to **design heritage** — cited for *why* the plate is shaped to collimate the rebound, not as the load-bearing no-spill proof. That makes the old "verify Solem actually states the capture/no-spill *geometry*, not just the sail *shape*" worry a non-blocker: we now cite Solem only for the shape/lineage, which he plainly describes. `balcomb1970nuclear` is unchanged — opacity→restitution only, never the geometry. Note: the parallel fudge-factor item (§How PuffSats Work → Mass Fraction) still carries the original Solem caveat; it was left untouched in this pass and should be reconciled the same way later.
  - [x] State the zero-torque placement (the appendix math): a net upward trim `F_up` applied at the rear plate (distance `d` behind the CoM) would pitch the craft. Putting the impact point a height `h = d·(F_up/F_fwd)` below the centerline makes the forward thrust's couple cancel it, so the resultant points through the CoM and the trim costs nothing in attitude. This is the vertical, by-design cousin of the lateral off-center-torque note. **(Routing resolved 2026-06-29, Medusa grill: keep ONLY the one-line body statement of the placement in this down-push item's body prose; the full `h = d·(F_up/F_fwd)` derivation is dropped with the killed appendices. The off-center-torque note it referenced now folds into the D4 body clause.)** *(landed as the one-line placement statement, formula kept inline, no derivation.)*
  - [x] Note the shared lever with the fudge-factor item (§How PuffSats Work → Mass Fraction): a curved plate that wraps the divergent puff both raises `f` (collimates the rebound forward) and is what lets the rebound carry the down-momentum out. One plate-shape decision, two payoffs.

  Because PuffSats are caught while falling toward their ~50 km disposal perigee, the
  momentum each one delivers is not purely forward. It carries a downward component of
  about `sin γ` (γ is the flight-path angle below the craft's velocity, order 10–25% from
  the interception geometry). That component has the same sign every pulse, so it
  accumulates and pushes the craft Earthward unless the plate cancels it. The cancellation
  is mostly free and geometric. The net force on the craft is set by the plate's
  orientation relative to the thrust axis, not relative to the line back to the PuffSat: a
  plate normal to the thrust axis reverses the gas's forward component and lets its
  downward component pass straight back out, so the rebound carries the unwanted
  down-momentum away and the craft feels only forward thrust. (A plate aimed square at the
  incoming PuffSat would instead double the down-kick.) Because the plate is opaque, little
  of the gas escapes sideways past it. A preliminary single-code hydrodynamic analysis
  (`Katz_puffsat_impact_sim_2026`) backs this. Its loss decomposition puts sideways escape
  below the condensation and conduction channels across the LEO insertion band, including the
  cool 3.2 km/s worst case. The down-component therefore reflects cleanly rather than leaking
  past the edge. We want to keep that spill small anyway to hold `f` high, so the trim rides
  on the reflected momentum rather than on a biased loss.
  Neutralizing the kick this way is usually enough; if a steady upward trim `F_up` is
  wanted on top of it, tilt the plate slightly further off the thrust axis so the reflected
  gas is thrown a little downward and the craft feels an upward reaction set by the full
  rebounded momentum. Any such upward trim, applied at the rear plate a distance
  `d` behind the CoM, would pitch the craft; placing the impacts a height
  `h = d·(F_up/F_fwd)` below the centerline makes the forward thrust's couple cancel that
  pitch, so the resultant passes through the CoM. The curvature that does this is the same
  curvature the fudge-factor item wants for collimating the rebound, so the down-push fix
  and the high-`f` argument are one plate-shape decision. (This drops an earlier variant
  that tried to harvest sideways-spilling gas for the trim: with an opaque plate the gas
  reflects rather than escaping past the edge, so the trim must ride on the reflected
  momentum.)

- [ ] torque but if spacecraft is long, force may be small for reaction wheels - when there is an off center impact. · `[raw]`
- [ ] We should discuss that for 5 meter wide plate, its OK because plate needs some mass anyway to smooth acceleration without unreasonably long shock absorber. · `[raw]`
- [x] ~~Explain issues with Medussa large strechy parachute, but possibility to do at sides.~~ · `[raw]`  **RESOLVED 2026-06-29 (Medusa grill).** (a) The "large stretchy parachute" issues are already handled by the existing taut-net design (`templateArxiv.tex:723`: the Vectran net keeps the sail taut, not billowing, so it holds its concave collimating shape). (b) "Possibility at sides" = a front/tension sail split symmetrically to the sides so PuffSats route up the flanks and keep a crewed cabin off the centerline; folded into the body item's cargo fork as ONE hedged sentence (on-axis via a paired/annular layout; only partially fail-safe; harder aiming).
- [x] explain possibility of 1/1 pusher plate · `[raw]`  *(superseded by the body buffer paragraph, now LANDED 2026-06-30: plate reaches ~10 % of craft mass, not 1/1)*
- [ ] for shock physics, higher atmosphere - string of pearls shaping to elongate the design · `[raw]`

---

## Appendix

### → New appendices: "Rigid pusher plate" (X) and "Medusa sail and struts" (Y)  (D1/D3 SUPERSEDED 2026-06-29)

> **STATUS 2026-06-29 (grill).** The "two appendices" plan is overridden.
> **Appendix X (rigid plate) is killed and folded into the body** as two compact
> paragraphs — see the rewritten body item "Body: the plate has no Orion-style
> critical mass" above; that item is the authoritative spec. The numbers below are
> kept only as source material for writing those paragraphs (the invariant, the
> survivability floor, the one transmissibility figure); the trade tables and full
> worked example below are **dropped**, not transcribed.
> **Appendix Y (Medusa sail + struts) is KILLED 2026-06-29 (Medusa grill).** No appendix.
> Its content collapses into the body item "our Medusa-style sail is behind the rocket"
> above: the rear-mount fail-safe paragraph stays, ONE buckling-mitigation clause and ONE
> buffer-invariant unification sentence are rescued to the body, and all strut numbers are
> dropped. See that item's STATUS block for the full routing.

The original "two appendices" rationale (now historical): each appendix would restate
the buffer invariant `m·s ≈ M a T²/4` briefly, carrying the math so a skeptical reader
could check it without bogging down the narrative. The unifying thread — the sail
(long stroke, light) and the rigid plate (short stroke, heavy or fast) are the two
ends of one `m·s` invariant — moves to the **body**. Appendix X = Subsection 1 below;
Appendix Y = Subsection 2 below.

- [x] ~~**Subsection 1 — the rigid plate: buffer invariant, 1/f² scaling, ripple, two-stage transmissibility**~~ · `[sizing]`  **SUPERSEDED 2026-06-29 → folded into the body item above (no appendix).** Source numbers retained below; trade tables and full worked example dropped.
  - [x] Derive `m_p·s ≈ M a T²/4` and the 1/f² scaling — **kept**, stated in body Paragraph 1 as a trade
  - [ ] ~~Include the two trade tables (plate mass vs stroke; stroke vs frequency)~~ — **dropped**
  - [ ] ~~Include the 4 Hz / 4.6 m / 3.2 t worked example with derived quantities~~ — **dropped** except the D3 triple + the survivability-floor clause, which go in body Paragraph 1
  - [x] Ripple analysis + two-stage absorber — **kept**, in body Paragraph 2, with one representative transmissibility number replacing the table

  **The buffer invariant.** A rigid plate on a shock absorber is a momentum buffer. To
  give the craft acceleration a, the average force is F = M a, so each pulse carries
  impulse J = M a T, with T = pulse period = 1/f. A pulse kicks the plate velocity by
  delta-v_p = J / m_p. The absorber arrests that recoil over stroke s at force about
  M a. Result:

      m_p · s  is approximately  M a T² / 4  =  M a / (4 f²)

  The prefactor is 1/4 to 1/2 depending on the absorber's force-versus-stroke profile.
  At fixed stroke, m_p scales as T² = 1/f². So 1 Hz to 4 Hz is a 16× lighter plate. The
  product m_p · s is what is fixed; the plate is only "heavier than the craft" if you
  pair low frequency with a short stroke.

  **Two views of the same curve (32 t craft, 3 g).** Plate mass versus stroke at 1 Hz:

  | Stroke at 1 Hz | Plate mass | Percent of 32 t craft |
  |---|---|---|
  | 2 m  | ~118 t | 370% (absurd) |
  | 10 m | ~24 t  | 74% |
  | 30 m | ~7.8 t | 24% |
  | 73 m | ~3.2 t | 10% |

  Stroke needed to hold the plate at 3.2 t (10 percent of craft) versus frequency:

  | Pulse rate | Stroke for a 3.2 t plate |
  |---|---|
  | 1 Hz  | ~73 m |
  | 2 Hz  | ~18 m |
  | 4 Hz  | ~4.6 m |
  | 10 Hz | ~0.7 m |

  **Worked example (4 Hz, 4.6 m).** m_p about 3.2 t (10 percent of craft), stroke 4.6 m.
  Both buildable. Per-pulse impulse J = 235 kN·s. Plate recoil delta-v_p about 73 m/s.
  Plate's own deceleration about 60 g (fine, no humans on the plate). One pulse equals
  25 kg of gas at about 5 km/s closing, self-consistent with the PuffSat design. Areal
  density 3.2 t / 25 m² is about 128 kg/m². Survivability floor is probably 10 to
  50 kg/m², because PuffSat total impulse is orders of magnitude below Orion's, so about
  0.25 to 1.25 t. Dynamics set the 3.2 t here, not the floor, with 3 to 12× margin.
  Higher f could ride the plate down toward about 1 t before survivability stops it.

  **The ripple problem (the real work item at 4 Hz).** The plate pushes only during the
  compression half of each cycle, so a plain absorber gives the craft a force swinging
  roughly 0 to 6 g (twice the 3 g mean) at 4 Hz. 4 to 8 Hz vertical is the worst
  whole-body vibration band (ISO 2631). Plate mass does not fix this. A heavier plate
  just moves slower; ripple amplitude is set by duty cycle and absorber law, not by m_p.
  Smoothing comes from absorber design and frequency.

  **The two-stage absorber (Orion heritage, the smoothing answer).** Orion connected the
  pusher plate to the vehicle through a two-stage absorber tuned to two different
  frequencies. The first-stage embodiment varied across iterations (toroidal gas bags or
  peripheral pneumatic cylinders), with a long central pneumatic/mechanical column as
  the second stage. The two-stage, frequency-separated principle is the constant.
  Cascaded mechanical low-pass filter:
  - First stage (plate to intermediate structure): stiff, short stroke, high frequency.
    Catches the sharp millisecond blow; the plate does its 60 g, 73 m/s bounce here.
    This is the about 4.6 m budget.
  - Second stage (intermediate structure to crew module): soft, long stroke, low natural
    frequency f_n. With f_n well below the pulse rate, it filters the ripple.

  Isolation at 4 Hz, transmissibility T is approximately 1 / ((f/f_n)² - 1):

  | Second-stage f_n | Ripple attenuated by | Crew feels | Static deflection under 3 g |
  |---|---|---|---|
  | 1.0 Hz | ~15x | 3 g +/- ~0.2 g  | ~0.74 m |
  | 0.7 Hz | ~32x | 3 g +/- ~0.1 g  | ~1.5 m |
  | 0.5 Hz | ~63x | 3 g +/- ~0.05 g | ~3.0 m |

  A second stage at f_n about 0.5 to 1 Hz turns the 0 to 6 g swing into 3 g plus or minus
  a few tenths, with a second-stage static deflection of about 0.7 to 3 m under the mean
  3 g load (very buildable). Two stages, not one: a single soft absorber would let the
  plate wander meters on every blow and could not take the peak pressure; a single stiff
  one transmits the jolt. With a good two-stage absorber, the duty-cycle skew (long push,
  quick re-cock) and multi-plate phasing become optional refinements, not necessities.

- [x] ~~**Subsection 2 — the Medusa sail and struts: same invariant at long stroke, buckling-limited struts**~~ · `[sizing]`  **KILLED 2026-06-29 (Medusa grill) → no appendix.** What survives, all in the body item above: the fail-safe paragraph (kept), ONE buckling-mitigation clause (sailboat-mast bracing + telescoping, no numbers), ONE qualitative buffer-invariant unification sentence. **Dropped:** every strut number below (10–12 t / 1.5–2 t / √E·ρ⁻¹ / steel 4–5×), the ~100 kg sail-floor number, the net-assembly tonnage. Source numbers retained below for reference only; do not transcribe.
  - [ ] Same invariant at long stroke gives the ~100 kg sail (~4 kg/m² over 25 m², coinciding with the thermal floor)
  - [ ] Strut buckling numbers: monolithic CFRP ~10–12 t (too heavy); guyed/lattice CF boom ~1.5–2 t (viable); the √(E)/ρ figure of merit; steel's 4–5× penalty; titanium/steel only at joints
  - [ ] The telescoping-helps-buckling point (peak force at max compression / shortest length)
  - [ ] The front-vs-rear fail-safe argument with the overtaking kinematics (D2 decides whether a version also goes in the body)

  **Sail can be light relative to the craft.** Long stroke buys a light sail. The sail
  sits on the same buffer invariant as the rigid plate: m_sail · s is approximately
  M a T² / (2 to 4). For a 100 m stroke and a few-m/s per-pulse delta-v on a 32 t craft
  at 3 g, the sail floor is about 100 kg, roughly 4 kg/m² over 25 m², about 0.3 percent
  of the craft. That areal density is also what the layered Nextel-720 / felt /
  Vectran-net sail needs for the heat, so the structural floor and the thermal floor
  coincide.

  **Strut mass (compression, buckling-limited).** Peak strut load is set by the craft,
  F = M a, about 1 MN at 3 g (design about 2 MN at safety factor 2), independent of
  stroke.
  - Monolithic CFRP tube, pin-ended, 100 m: about 10 to 12 t. Too heavy; the L² penalty
    dominates.
  - Guyed or lattice CFRP boom (effective buckling length about 15 m via tension stays):
    about 1.5 to 2 t. Viable.
  - Steel is about 4 to 5 times heavier than CF for the same buckling load. Buckling
    depends on stiffness E, and every steel has the same E of about 200 GPa, so
    "compression-resilient" high-strength steel buys yield strength we do not need and
    zero extra buckling margin. The buckling figure of merit is sqrt(E)/rho, where
    high-modulus CF beats steel by about 5x.
  - The real "combination" that beats buckling is a compression member braced by tension
    guys (sailboat-mast principle): CF boom carries the compression, Vectran or thin
    steel stays carry tension and cut the effective buckling length. Reserve titanium or
    steel for joints, end fittings, and damper cylinders, where concentrated ~1 MN
    bearing loads, impact, and fatigue matter and CF is brittle and notch-sensitive.
  - Telescoping helps for free: peak force occurs at maximum compression (shortest
    length); full extension (100 m) coincides with near-zero force. So the
    buckling-critical length at peak load is well under 100 m, and a naive
    fixed-100m-column estimate overstates the mass.
  - Net pusher assembly: order 1.5 to 2 t of structure plus 0.1 to 0.3 t of sail, a few
    percent of a 32 t craft.

- [x] ~~**Subsection note — off-center torque and rotational inertia (the forgiving-plate consequence)**~~ · `[sizing]`  **RESOLVED 2026-06-29 (Medusa grill) → folds into the D4 body clause, not the Medusa section.** The 2 m-miss torque cost already goes to the body via D4 ("a 2 m miss buys more RCS authority + plate inertia"); add the half-idea that a longer absorber stroke buys time to recenter between pulses. Drop the appendix torque/rotational-inertia derivation below (kept only as source). Not Medusa content.
  - [ ] Add the off-center-torque and rotational-inertia argument: accepting up to a 2 m lateral miss applies a torque; a larger/heavier 5 m plate resists tip-over and a longer stroke buys time to recenter and let the RCS cancel the moment
  - [ ] Note heavier-plate-plus-longer-stroke sits above the m_p·s minimum, so it costs nothing in feasibility — we trade mass-optimality for forgiveness deliberately

  Accepting up to 2 m lateral miss means off-center impacts up to 2 m, which apply a
  torque. A larger, heavier 5 m plate has more rotational inertia and resists tip-over
  from off-center hits; a longer absorber stroke buys more time to recenter the plate and
  let the RCS cancel the moment between pulses. So the relaxed cross-track requirement
  *justifies* a heavier plate and a longer stroke than the mass-minimizing point. This
  sits comfortably above the m_p · s buffer minimum, so it costs nothing in feasibility.
  A heavier plate plus a longer stroke just means we operate with peak-g and smoothness
  margin rather than at the minimum. We trade mass-optimality for forgiveness,
  deliberately, in the near term. (The 5 m plate also doubles as a disaster shield: if
  PuffSat gasification is imperfect and a solid fragment escapes — the 250 g dry mass, or
  incompletely vaporized propellant — the oversized plate catches it instead of the
  craft.)

### → `sec:estimate_cold_gas` (cold-gas propellant appendix)

- [ ] Reinforce the <2 % propellant bound with the closed-loop simulation result (see the `sec:handling_space_debris` item above): the appendix asserts the bound from a GOCE-derived back-of-the-napkin estimate; the sim now *confirms* it with a full corrector + terminal-guidance + finite-thrust + dispersed-environment loop. · `[SIM]`

---

## Provenance / cross-reference

- **Part-1 (near-term LEO) numbers are simulation results** from the companion control
  sim repo (Rungs A–D, closed out 2026-06-15/16), traceable to its ADRs: criterion
  (0015/0016), catch-radius & terminal guidance (0014), multi-tracker fusion (0019),
  apogee nav constellation (0020), drag feed-forward (0021), coefficient prior (0013),
  Rung-D closeout (0018).
- **Part-2 (near-Sun) items are option-level sizing**, traceable to the
  differential-ranging derivation and the near-Sun inversions noted in the
  relative-ranging and optical-sensing design discussions.
- The **surveyor-anchored centring** scheme (the optional §2 tightening) is a paper-side
  option, deliberately not built in simulation.
- The Medusa/pusher-plate trades and the periapsis-nav sharpening are **hand-derived
  order-of-magnitude sizing** from design grilling sessions (2026-06-12 and 2026-06-15),
  not simulation results.
- The **near-Sun absorbing nozzle / chamber sizing** (size floor `R ∝ √m`, energy per
  pulse, magnetic-nozzle option, staged/metered delivery) is hand-derived
  order-of-magnitude sizing from a design grilling session (2026-06-22), not a simulation
  result.
