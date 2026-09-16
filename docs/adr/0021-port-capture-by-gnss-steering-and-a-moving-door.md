# Port capture is closed by GNSS steering and a moving door, with the lines left uncut

Status: accepted (2026-09-16 grill). Recorded because the head-on nozzle asks for an aim about a
hundred times tighter than the plate, and the architecture that meets it is not the one the plate
uses.

**Plate capture** needs a unit anywhere on a 5 m plate, about 2 m of tolerance. **Port capture**
needs the departure rod (11.0 cm) through a 15.0 cm entrance, 2 cm of radial clearance, and into a
methane plug twice its width. The rod steers by three 83 g resistojet packages with only
0.73 mm/s^2 across the line at a 68 km/s closing speed. By the funnel `2 (sigma_theta v)^2 / a`,
the ship's own star trackers leave it 32-105 m off, because their error grows with range while
the rod still needs knowledge 600-1100 km out. The paper's earlier sentence, "a centimeter or two
of error left after release", was not supported by its own tracking grades.

We decided: a dual-frequency **GNSS receiver on each package**, differenced against the ship, is
the rod's load-bearing position source until the ship's trackers beat it in the last fraction of
a second. A **movable door** (the aperture insert, with the plug on its line) is a requirement. It
pre-positions between pulses and trims from the ship's trackers, locking 20 ms out, with a stroke
of 3 sigma of the GNSS floor. The package **lines are not cut**; they ride to impact on three known
radial strips behind a thin standoff bumper. The cadence stays **2 Hz**.

## Considered options

- **Cut the lines about a second out.** Retired: steering in that last second is worth 0.37 mm.
- **An oil film where the lines strike.** Too light: a 0.1-0.2 mm strand carries 144-288 g/m^2
  across its width against 5-10 g/m^2 of oil. A standoff foil in the 20 g/m^2 class vaporizes it.
- **A co-flyer as the rod's tracker.** 2.9 cm radial at a 30 mas grade and 9.7 cm at 100 mas
  (Jena-Optronik ASTRO XP class), but it holds a ~100 km standoff only for rods near it along a
  stream up to 22,000 km long. Kept as an optional cross-check.
- **Resize port, insert and plug to a decimeter.** Leakage and plug mass grow; rejected before the
  aim number is known.
- **1 Hz cadence to give the door time.** The door needs only 0.23-0.67 kN at 2 Hz. Its late trim
  window is set by when the ship's trackers beat GNSS, not by the period. 1 Hz would double the
  burn and the fixed-direction steering loss (+27 m/s at 320 s, +101 m/s at 640 s), and a given
  shock isolator passes four times the ripple.

## Consequences

- The door is the least mature element and only its drive force is sized. It carries the pulse
  through its backing: 5.2-14 MN at 900 bar for a 6-15 cm stroke, the class of a 155 mm howitzer
  breech (6.6-7.5 MN), but it must seat at a new place every shot, in hot sooty gas.
- The GNSS grade, the terminal loop, the door handover, and plate capture for the 57 km/s growth
  ring are owed by `puffsat_control_simulation` as **G1-G4** (`docs/asks_for_control_sim.md`).
- The LEO cycle keeps GNSS as a cross-check only; the departure rod is the one place it is primary.
