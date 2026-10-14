# Below blackbody closing speeds, a pinch is the pass-through geometry's only upstream X-ray source

Status: proposed (2026-10-14). Follows ADR 0029. Open for the Jupiter scenario's head-on
departure wave, which the author named as the case of interest. Terms in `CONTEXT.md` under
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

## Open

The author's departure-wave framing replaces the 150 km/s placeholder, and it is to be
discussed next:
- a ~1:3 impactor-to-anchor ratio, so 25% of the energy leaves astern;
- the anchor (compressor and case) knocked astern, which costs the ship no momentum;
- X-rays heating argon at a light pusher plate to temperatures the walled chamber cannot
  survive, since frozen flow and wall heat limit it.

The comparison device is the departure wave's flown chamber (ADR 0027 / 0028). The leg's
closing speed and Δv come from the paper.
