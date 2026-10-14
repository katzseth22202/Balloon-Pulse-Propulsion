# Below blackbody closing speeds, a pinch is the pass-through geometry's only upstream X-ray source

Status: accepted (2026-10-14). Follows ADR 0029. **Rejected for the Jupiter scenario's
head-on departure wave** (author's decision, same day), the case the author named as the one
of interest. No leg currently adopts it. Terms in `CONTEXT.md` under
**The pinch at sub-blackbody closing speeds**. Scratch calc: `todos/pinch_150.py`.

## Context

In the head-on pass-through geometry the merged projectile and target recede astern at
v/(1+k). Gas therefore cannot carry their heat upstream to a plate on the ship's side. The
companion's ray count caps the forward share at 31.2% even at k = 7.06, and less comes forward
at k = 2. Light is the only carrier that crosses that gap, which is the same reason Orion used
X-rays. A direct gas-push pulse unit is **not** a valid low-speed baseline here. That was
proposed during the session and withdrawn on the author's correction.

Below ~600 km/s the fireball is too cool to be the light source. At 150 km/s and k = 2 it gets
~470 eV per carbon atom, kT is ~40-50 eV, and T^4 output is ~5e4 times weaker. A magnetic
pinch's radiating temperature is set by energy per unit of load mass, not by closing speed, so
the pinch still works. Its fields also fall to 600-1,200 T, which is inside demonstrated
flux-compressor range. At 618 km/s they would be 2,500-5,000 T.

## Decision (proposed)

Treat the coax-compressor pinch of ADR 0029 as the candidate X-ray source for pass-through
pushing below blackbody speeds. Adopt it only for a leg where the cheaper devices are ruled
out, namely where a catch aboard, the momentum charge, or a cold magnet is unacceptable. On
specific impulse alone it lands in a band the paper already covers. At 150 km/s with
eta 0.1-0.45 it gives 530-1,120 s (0.25 kg case, no sleeve) and 400-840 s with a 1.7 kg sleeve.
For comparison: the walled methane chamber gives 762-777 s, hydrogen on copper 1112 s, and the
companion's tamper bowl 984 s at 75 km/s.

Two bounds go with any version:
- At most k/(1+k) of the impactor's energy ever reaches the field. At k = 2 and eta 0.45 that
  is 30% of the impactor's energy reaching the propellant.
- The chain probably runs at the low end of eta at slow closing. The last 10 cm takes ~670 ns,
  four times longer than at 618 km/s, which leaves more time for flux diffusion and gives a
  slower pinch rise.

## The departure wave (rejected)

The author's departure-wave design: a pass-through pinch with impactor:anchor 1:3, so 25% of
the energy leaves astern and the anchor's momentum never reaches the ship. Its X-rays leave
through a **window** in the case and cross the standoff onto **argon gas sprayed against the
pusher plate**. A bowl centered on the source evens the illumination, and a light plate
replaces the walled chamber. This is the **X-ray-driven spray plate** in `CONTEXT.md`. Because
the argon pushes off the plate, it avoids the pulse split that would throw half a
free-floating slab astern.

It was priced at the departure wave's 75 km/s head-on reference (`todos/departure_xray_spray.py`).
Inputs: 2.11 GJ field-available per kg impactor at 1:3, X-ray path efficiency 0.15-0.40
(window escape x bowl share, 1.0 as the no-loss bound), eta_jet 0.60, and a spent mass of
anchor plus argon.

- **Isp is set by the anchor, not by the argon.** For a given anchor, Isp peaks when the argon
  mass equals the anchor mass. The author's 1:3:4 example gives 440-720 s, and 1,135 s with no
  losses. The walled methane chamber gives ~770 s.
- **Beating 770 s needs an anchor of about 1 kg per kg of impactor or less** (path 0.40).
  That leaves ~20 kN s per kg impactor, about a third of the chamber's ~53-64 kN s per kg rod
  (inferred from Isp x g0 x k at k 7-8.52), so roughly 3x the departure PuffSats.
- **Ceiling.** As the anchor shrinks to nothing, Isp approaches 1,150 / 1,450 / 2,300 s
  (path 0.25 / 0.40 / 1.0), and impulse per impactor goes to zero.
- **Near a 1:3 anchor** it ties or beats the chamber on projectiles (48-110 kN s at 10-20 kg of
  argon) at 300-600 s.

Rejected because Isp can only be bought with departure PuffSats. The growth ledger already
values PuffSats over carried mass: it prefers a departure charge of k ~7-8.5. Not priced, and
left as the only route back: a plate against the 48.2 t chamber stack on hardware mass. Plate
survivability looked plausible (~3 kJ per N s at 10-12 km/s exhaust, and ~3 mg/cm^2 of argon
stopping soft X-rays), so survivability was not the reason for rejecting it.
