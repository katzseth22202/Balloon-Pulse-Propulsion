# Nothing may pass inside the node, so the plunger placement is inadmissible

Status: accepted (2026-09-02 grill, applying companion `docs/paper_changes_owed.md` P1 and
companion ADRs 0024/0025). The decision bars an option this paper has been offering as a
cheap alternative since `sec:no_isru_rocket`, so it needs recording or a later pass will
read the plunge's own numbers, see that they are good, and put it back.

We adopt **node-depth admissibility**: every trajectory in the architecture, the payload,
the opposing stream, and any projectile stream feeding any node, must have a perihelion no
lower than the dive node's depth. Nothing in the system may pass inside the node. It is
stated in the paper as `sec:node_depth_admissibility`.

## Why it is a rule and not a preference

The **plunger**, a projectile dropped at the Sun on a near-zero-angular-momentum orbit, has
a perihelion of zero by definition. It does not skim the Sun, it enters it, and it crosses
the node radius on the way down. Three consequences follow and each one is disqualifying on
its own.

1. **The unconsumed share hits the Sun.** No stream is perfectly consumed; `sec:lost_puffsat`
   exists because of that, and the depth dial's rendezvous timing tolerance is an along-track
   miss budget rather than a guarantee. A plunger architecture continuously puts projectiles
   on a Sun-impacting trajectory.
2. **It contradicts the reason for the depth.** A shallow dive is *chosen* to escape the
   thermal load. Backing the payload out to 23 R☉ while aiming the ammunition at `r = 0` has
   moved the exposure onto the half of the collision nobody was scoring.
3. **The depth stops meaning one thing.** Under the rule, "the dive is at 23 R☉" describes the
   closest approach of everything in the system. Without it, it describes one of two arrivals.

**The tell, and why it is worth teaching.** `tab:opposing_stream_depth` prices the radial
placement **flat at 29.78 km/s at every depth**. A depth-independent price is the giveaway
that the trajectory is not aiming at a depth at all. The payload column, 24.09 falling to
14.62 km/s, is what a column that *is* aiming at a depth looks like.

**The trap that closes the argument.** Forcing the plunger to bottom out at the node instead
of passing through means carrying the tangential speed a perihelion there requires, 15.16
km/s at 32 R☉. That is the payload's own prograde injection. The repaired plunger arrives
*alongside* the payload rather than across it, and there is no collision left. Zero angular
momentum is the plunger's defining property, so "plunger" and "bottoms out at the target
depth" are mutually exclusive.

## Considered and rejected

**Rejecting the plunger on its 135-degree geometry alone.** True at `k` = 30, where it keeps
0.757 of the head-on effective exhaust speed, but it is inadmissible *before* it is
inefficient, and an efficiency argument is one a better `k` could overturn. The geometry
analysis stays on the record in `sec:arrival_angle` as why it would have lost anyway, not as
why it is rejected.

**Treating the Sun crossing as survivable because the collision happens on the way in.** That
is true of the approach and wrong about the architecture, for reason 1 above. Companion ADR
0024's "considered and rejected" section should be read with this ADR.

## Consequences

**Retrograde placement becomes the only admissible head-on arrival**, which promotes the
bi-elliptic co-placement from convenient to load-bearing. Injected at one far node, payload
and opposing stream fly the same ellipse in opposite senses, so they arrive together at 180
degrees with no tuning knob and neither leg ever goes closer to the Sun than the node. The
rule is satisfied there by construction.

**No published number moves.** No result in the paper ever *selected* the plunger, so this is
a constraint on the option set rather than a correction. What changes is that four paragraphs
of plunge trade in `sec:opposing_stream_depth` compress to one, and the arithmetic moves to
`sec:arrival_angle`.

**It opens one unpriced object.** Under the rule, a coplanar admissible arrival is co-moving
or head-on with nothing in between, because anything bottoming out at the node carries the
local near-parabolic speed tangentially. An intermediate arrival angle now has to be bought
with an **inclined placement**, and a plane change on a placement leg is priced nowhere in
this paper. `sec:split_dive_open` lists it.
