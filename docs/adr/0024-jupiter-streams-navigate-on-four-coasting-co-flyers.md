# Jupiter-return streams navigate on four coasting co-flyers, with GNSS from twice-MEO

Status: accepted (2026-09-30 grill; paper `sec:jupiter_coflyers`, `sec:tethered_rod_packages`).
Recorded because the low-orbit navigation (apogee constellation, co-flying launch rocket, target
trackers) cannot reach a stream that coasts 16 days in from 0.53 AU at 57 km/s, and the rod's
funnel floor leaves ship-side tracking 32-105 m off.

Both Jupiter-return waves get the same design, four co-flyers each: the growth wave (inbound,
400 km, ring and plate) and the departure wave (outbound, 600 km, rod and port). The departure
wave's release point is not in the paper; it is assumed to match the growth wave's 1.3 AU and
~16 days, and the text says so.

## Decision

- **Phases.** Coast (release to ~40,000 km, twice the GNSS orbital radius): delta-DOR on the
  co-flyers for absolute position, the co-flyer ranging broadcast for relative position, PuffSat
  thrusters for trims. GNSS (last ~11 min): GNSS, differenced against the co-flyers; the target
  shifts up to 300 m (~2 m/s) to absorb common-mode error. Terminal (last ~0.1 s): ship trackers,
  then the door (rod) or plate (ring).
- **Requirement.** Tight formation, and a centroid within 20 m of the orbit to the target
  (far-field). Common-mode error goes to the target, per-PuffSat error to the PuffSat.
- **Co-flyer layout.** ~50 kg, coasting, never diverting. Three on a 500 km ring (outward, two out
  of plane, none Earth-ward), a spare outward at the trailing quarter point. ~0.7 m/s each.
- **Radio, one-way.** Co-flyers broadcast; PuffSats receive only and solve their own fix by time
  differences. No atomic clocks: PuffSat clock cancels; co-flyer quartz USOs held in step by dual
  one-way ranging among themselves.
- **Compute split.** Co-flyers do orbit determination, formation planning, aiding (slots,
  ephemerides, predicted Doppler) and wake scheduling; PuffSats keep a thin inner loop. Reasons:
  one solver for the formation, upgrades on four craft. Not power.
- **Beacons.** 1-3 GNSS-and-transmitter units lead each wave from ~40,000 km and pass unused.
- **Rod.** Propane cold gas at the package tips (resistojet fallback), thrusting to arrival with no
  quiet coast; swing dead-reckoned from carrier phase; cancelling burns (posicast, half a swing
  period) and balanced nulling bursts; viscoelastic links at the line attachments as the passive
  backup. The assembly is a major-axis spinner (16.0 vs 9.0 kg m^2), so passive loss is safe.
- **Ring.** Aim at the centre of mass, which swing cannot move; swing is a footprint-shape
  requirement. Sphere water damps it, with ullage or baffles.

## Numbers checked in-session (2026-09-30)

- Fix at the stream's end (L = 6,750 km, R = 500 km) with the chosen layout: 16.6 sigma_range
  radial, 9.6 out of plane, ~290 along track (`todos/coflyer_geometry.py`). 20 m radial needs
  ~1.2 m ranging. The grill's `L/(R sqrt 1.5)` is the symmetric layout and understates radial.
- Delta-DOR at the DSN handbook's 1.9 nrad per fix (not the "approaching 1 nrad" headline):
  151 m at release, 37 m at 4 d, 9 m at 1 d; 20 m from ~2.2 d out on single fixes.
- Propane at ~45 s: 1% of the assembly buys ~3.4 m/s across the line, against <1 m/s needed.

## Considered options

- **Angles-only from the co-flyers.** Rejected as primary; bearings stay a cross-check. (The
  grill's reason, star-tracker attitude knowledge, was not written into the paper because the
  parent's own co-flyer sizing assumes a 30 mas tracker is possible; ranging wins on simplicity.)
- **Optical co-flyer links.** The PuffSats span nearly half the sky from mid-stream; a laser would
  scan thousands of targets.
- **Two-way ranging to each PuffSat.** Needs a transmitter on every PuffSat.
- **Chip-scale atomic clocks.** Their strength is long-term stability at low power, which continuous
  co-flyer syncing makes unnecessary; over 1 s they are far less stable than a USO.
- **A symmetric co-flyer triangle.** Puts a vertex 250 km Earth-ward.
- **A quiet coast and cutoff before the port.** Authority fades by itself (3 cm in the last 9 s,
  0.37 mm in the last 1 s); the handover is a change of dominance.
- **1 cm/s^2 of PuffSat authority.** About 14x the line tension; 0.73 mm/s^2 already reaches ~80 m
  in the last 11 min against 20 m needed.
- **Beacon-rebroadcast fallback for a lost co-flyer.** Dropped for the fourth co-flyer.
- **Separate tethers for thrusters and electronics.** Needed power across the rod and a longer
  tether model.
- **Polymer on the rod and sensor boxes as the swing damper.** Damps their own ringing, not the
  swing, which works the lines.
- **Water resistojet as primary.** ~35 W, ~270 g of array; propane saves ~170 g net.

## Consequences

- ADR-0021's "GNSS carries the rod" stands; GNSS now starts at ~40,000 km with co-flyer aiding,
  and the co-flyer layout gap in CONTEXT **Port capture** is closed.
- CONTEXT's avoid-note on "GNSS at apogee" concerns the LEO apogee and does not conflict.
- Nothing is simulated. First calculation wanted: co-flyer fix covariance over the 16-day coast.
- Open: beacon share of each wave; line-model accuracy and the resonance check (swing modes near
  the 0.06 Hz spin rate); plume backflow profile setting the electronics-to-thruster spacing;
  whether a spinning array reaches ~1 kg/m^2 assembled; departure-wave release point.
