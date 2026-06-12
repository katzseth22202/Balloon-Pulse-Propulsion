# This is stuff that needs reconciliation with paper

* active transponder on PuffSat.  Measures both distance and doppler velocity shifts
* at least 4 coordinator nodes, with both perigee and apogee updated.   Consider also using GNSS signal below geostationary orbit.
* Big one.  GOCE level accelerometer is kilogram scale technology and is not something that fits on a PuffSat.  Probably why we can't get millimeter scale PuffSat working.
* We only target Puffsat accuracy to 1 meter.  Assumption is pusher plate can move, shock absorber can reshape to keep pulse centered.  Rockets on main craft also help.
* Van Allen radiation shielding is provided by Puffsat itself.  Relatively easy for outer Van Allen belt - time through inner belt with high energy protons is short enough to accept risk.   Triple mmjority redundance (used on SpaceX - need source)
*torque but if spacecraft is long, force may be small for reaction wheels - when there is an off center impact.
* is it easier to do 1mx1mx50m uncertainty of 2m sphere uncertainty and which is relevant?
* propose 3m/s omnidirectional thrust capability of rocket, Gaussian distributed with .5 m/s standard deviation, align once per second. 
* do we need GNSS if we have this precise measuring/broadcasting from the rocket coming up from the ground and any ground infrastructure, which seems like everything is much closer than GNSS to the key impact point
* What if the part of the trajectory above 800 km just needs accuracy within 30 km in absolute terms of where interception is, but then the PuffSat formation (each PuffSats relative position is accurate to within 1 meter radius)?  The rationale is the plane can fly to meet the formation.  Once the pusher impacts start, then the structure of the PuffSats should be constant - so the bottom one can be shifted as long as shape of every remaining PuffSat is within 2 meters of relative target.
* We should discuss that for 5 meter wide plate, its OK because plate needs some mass anyway to smooth acceleration without unreasonably long shock absorber.
* star maps may be enough for necessary angular resolution estimated at 10 micro-rad on the main plane
* torque correction is RCS + rocket engine - non,toxic fuel obviously
* note the plane can adjust its starting point by 10s of kilometers, so if there is systemic drift in PuffSats is OK as long as PuffSat formation shape is good looking.
* Explain issues with Medussa large strechy parachute, but possibility to do at sides.   
* explain possibility of 1/1 pusher plate 