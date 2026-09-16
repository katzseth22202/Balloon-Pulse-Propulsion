# Guidance deliverables owed by `puffsat_control_simulation`

Raised 2026-09-16, grilling the data-center delivery legs against `sec:needle_through_fog`,
`sec:tethered_rod_packages` and `sec:jovian_plume_encounter`. **Written to be copied verbatim into
`katzseth22202/puffsat_control_simulation`**, so it repeats context the paper repo already has.

Numbered G1-G4 so they do not collide with the S-items (`docs/deferred_to_companion_repos.md`,
targeting `aim_is_all_you_need`) or the N-items (`docs/nozzle_asks_for_impact_sim.md`, targeting
`puffsat_impact_simulation`). Backing decisions: `docs/adr/0020-jupiter-return-pushes-fly-high.md`
and `docs/adr/0021-port-capture-by-gnss-steering-and-a-moving-door.md`. Paper-side probes:
`todos/data_center_interception_altitude.py` and `todos/vertical_lob_lift.py` (gitignored).

The paper states the requirements below and names each number as open. Nothing waits on these to
be drafted. Same ground rules as elsewhere: **neither document is the source of truth**; if a
number here looks wrong, say so rather than working around it.

---

## The case these asks are about

The Jupiter chain's **departure wave** meets the craft head-on. Each unit is a 10 kg polyethylene
rod, 1.10 m by 11.0 cm, arriving at 57 km/s in Earth's frame (up to 65 km/s in the 2S family) and
closing on the craft at about 68 km/s. It must pass a 15.0 cm entrance port, which is **2 cm of
radial clearance**, and strike a methane plug twice its width (**+/-5.5 cm**). This is
**port capture**. The plate leg (**plate capture**) only has to land within about 2 m.

The rod carries no electronics. Three 83 g packages ride on Kevlar lines 8 m out, spin the
assembly at 23 deg/s, and steer it with ~5 mN water resistojets. Across the line they supply a
steady **0.73 mm/s^2**; along it, 1.46 mm/s^2. **The lines are no longer cut**; the packages ride to
impact and pass outside 8 m. The departure periapsis is **600 km**, the cadence **2 Hz**.

The paper-side funnel, `2 (sigma_theta v)^2 / a` for a target-side tracker, puts the rod's floor at
**32-105 m** with the ship's own trackers at 330-600 mas, because the rod has so little authority
and closes so fast. A co-flyer at 100 km would give 2.9-32 cm at 30-330 mas, but it holds that
standoff only for rods near it along a stream up to 22,000 km long. **The paper chose GNSS instead**:
a dual-frequency receiver on each package, differenced against a base receiver on the ship, as the
rod's load-bearing position source. A **movable door** (the aperture insert, with the plug on its
line) pre-positions between pulses from the GNSS prediction and trims from the ship's own trackers
once they beat GNSS, locking 20 ms before arrival.

---

## G1. Size the rod's GNSS relative-navigation grade

The number that sets the door's stroke, and so the pressure load its backing carries (3 sigma of
2-5 cm is a 6-15 cm stroke, a 27-45 cm backing hole, 5.2-14 MN at 900 bar).

Wanted: the 1-sigma radial and cross-track error of the rod's predicted arrival point, from
dual-frequency carrier-phase differencing, at the moment the rod still has steering time
(9-16 s out, **600-1100 km** from the ship). Terms the paper has not sized:
- differential ephemeris over that baseline (broadcast orbits leave ~5 cm; real-time precise
  orbits a few mm, by `baseline / range x orbit error`);
- residual ionosphere after the dual-frequency combination, with both receivers near 600 km;
- **acquisition and a fix inside ~7-8 minutes**, the rod's time between the GNSS shell and
  periapsis at 57 km/s;
- receiver dynamics at up to about **+/-320 kHz** of L1 Doppler (the LEO PuffSat receiver
  already needs +/-60 kHz and custom firmware);
- **rod-to-package-circle registration**: GNSS measures the packages, and the rod sits at the
  circle's centre only if tensions and geometry are balanced. The LEO entry's carrier-phase circle
  fit recovers spin phase and centre; say how well at 23 deg/s and 8 m;
- ship antenna to entrance-port registration through a structure that takes 900 bar pulses.

## G2. Fly the rod's terminal loop on that knowledge

With G1's grade as constant knowledge, the floor is `sigma_G`, reached with `sqrt(2 sigma_G / a)`
of divert (7.4 s at 2 cm, 11.7 s at 5 cm). Fly the actual loop with 0.73 mm/s^2 across the line and
report the arrival scatter. Include unmodeled drag: at 600 km the paper-side estimate of
uncorrected cross-line drift over the last 9 s is under 0.2 mm even at 10x density, so this should
not bind; confirm it. The paper also has not simulated the bridled spin under thrust (the packages'
out-of-plane swing near the spin rate), which `sec:tethered_rod_packages` already flags.

## G3. The door's handover and final placement

The ship's trackers beat GNSS inside `sigma_G / 1.6 urad` (12.5 km, ~0.19 s, at 2 cm; 31 km, ~0.46 s,
at 5 cm), and reach 0.5 cm at 50 ms and 0.2 cm at 20 ms. Wanted: the door's final placement error
against the ~1 cm radial clearance, given a trim that starts at the handover and ends at a 20 ms
lock, while the next charge is filling (about 3 bar, which seats an inside-mounted door with ~25 kN
unless it stays unseated until the lock). Drive force is not the issue (0.23-0.67 kN for 10-29 cm at
2 Hz). Timing and knowledge are.

## G4. The growth ring at 57 km/s

Tier 1 was simulated at 11 km/s. The Jupiter growth wave closes at 46-57 km/s on the same 5 m
plate. If its ring steers with 400 mN on 50 kg, the paper-side funnel with target-side tracking
alone is **2.1-6.8 m** at 1.6-2.9 urad, at or past the ~2 m plate tolerance. The growth ring's
thrust is not specified. Wanted: whether plate capture holds at 57 km/s with the ship's trackers
alone, and if not, whether the same GNSS approach as G1 closes it.

---

| ask | what is wanted | status |
| --- | --- | --- |
| **G1** | Rod GNSS relative-nav grade over 600-1100 km, with fix time, Doppler and registration | **open** |
| **G2** | Rod terminal loop on G1's knowledge, 0.73 mm/s^2, bridled spin | **open** |
| **G3** | Door handover and final placement against ~1 cm, trim during refill | **open** |
| **G4** | Plate capture for the growth ring at 57 km/s | **open** |
