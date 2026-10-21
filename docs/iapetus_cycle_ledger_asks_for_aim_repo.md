# The Iapetus water cycle: ledger and true cost, ask S51 (for aim_is_all_you_need)

Raised 2026-10-20 in `Balloon-Pulse-Propulsion` (after `5d63e81`). **Written to be copied into
`aim_is_all_you_need`; self-contained.** Nothing here is in the paper yet. Seth wants the cycle
priced as a ledger, including the nuclear engines as a cost line (Seth, 2026-10-20: "Need to be
part of the ledger"). The leverage and plate mass come from the impact sim's S50
(`docs/iapetus_bag_plate_asks_for_impact_sim.md` in the parent). Until S50 lands, run both the
placeholder rows below.

## Why NASA's interest frames this

NASA has renewed interest in surface fission and nuclear thermal propulsion. This cycle is the
parent's candidate nuclear use case. The ledger should therefore price it honestly against the
paper's non-nuclear routes, not assume it wins.

## The cycle (one round, 9.5 years)

1. **Out.** Seed hardware is pushed by returning PuffSats into the eccentric Earth orbit
   (10.916 km/s at 200 km). At perigee a stage burns for Saturn on a fast 3.0-year transfer. The
   first round starts from LEO instead, since there are no PuffSats yet.
2. **Saturn capture and dog-leg.** Brake at a 150,000 km periapsis (outside the main rings) onto
   an ellipse with apoapsis 20 million km. At apoapsis, raise periapsis to Iapetus's orbit, match
   Iapetus, land the mining kit. The dog-leg takes 1.17 years each way, which is why the cycle is
   9.5 years and not 7.5 (Seth: the dog-leg is necessary).
3. **Load.** Ice is thrown mechanically into low Iapetus orbit, as the parent's
   `sec:greedy_phoebe` proposes for Phoebe. The stage loads in orbit. It cannot lift off loaded,
   because its thrust is sized for Saturn periapsis and not for Iapetus gravity.
4. **Return.** Escape Iapetus, coast to the 20 million km apoapsis, drop periapsis to
   150,000 km, then burn there onto a retrograde-leaning transfer that reaches Earth in 3.7 years
   at **51.1 km/s** (closing speed at 200 km).
5. **Disposal.** The PuffSats separate at burn cutoff. The empty stage brakes back to a bound
   orbit and, at apoapsis, falls into Saturn. Single use. **Two redundant reactors** guard the
   brake (Seth dropped a trajectory-based safety feature in favour of redundancy).
6. **Earth push.** The PuffSats overtake the next round's Earth-launched ship and push it to the
   eccentric orbit, with a carried charge of `k` kg per kg of PuffSat.

Two rounds fit a 20-year horizon (years 0-9.5 and 9.5-19).

## Delta-v (parent scratch model: circular coplanar planets, about 10-20% uncertainty)

| Leg | Delta-v (km/s) | Notes |
|---|---|---|
| Earth departure from eccentric-orbit perigee | 4.90 | 3.0-yr transfer; from LEO add about 3.1 (8.0 total) |
| Saturn capture at 150,000 km into 20e6 km apoapsis | ~2.5 | Arrival v_inf ~12 km/s |
| Raise periapsis at apoapsis / match Iapetus / land | 0.59 / 0.99 / 0.65 | Saturn side total 4.76 incl. 2% on capture |
| Iapetus escape from low orbit after loading | 1.00 | 0.74 impulsive plus a low-thrust penalty |
| Drop periapsis at 20e6 km apoapsis | 0.59 | |
| Saturn periapsis departure burn | 2.37 impulsive, **2.49 finite** | Start acceleration 0.093 m/s^2 for at most 5% finite-burn loss; burn 4.2 h. Departure v_inf 10.4 km/s |
| Disposal brake (empty stage) | 2.89 | Brake to bound at cutoff plus 0.2 at apoapsis to fall into Saturn |

The parent's sizing of the finite burn is a 2-D integration on Saturn's point mass, thrust along
the velocity, burn start optimised. Rerun it on your own propagator if you have one.

## The return stage

**Fuel (Seth, 2026-10-20):** uranium oxide in a tungsten cermet, with a silicon carbide barrier
that forms an eroding silicon dioxide layer in steam. Graphite fuel (NERVA's) is out, because hot
steam gasifies carbon. Propellant is water from Iapetus ice. Below 20% enrichment (the parent's
`sec:ntr_departure` rule).

**The barrier sets the exhaust temperature: 1300 K at about 1 MPa.** Steam carries the silica
skin away as Si(OH)4, so SiC recedes linearly and life is coat thickness divided by recession
rate. NASA's burner-rig fit (Smialek, Robinson, Opila, Fox and Jacobson, NASA/TP-1999-208696;
1473-1723 K, 4-15 atm, 18-25 m/s, fuel-lean gas of about 10% steam) is
`k [mg/cm^2/h] = 2.04 exp(-108 kJ/mol / RT) P^1.5 v^0.5`. Its boundary-layer basis scales as
P_H2O^2 P^-0.5, so pure steam recedes about 100x faster than the rig gas at the same total
pressure. Terrani et al. 2014 (ORNL, pure steam to 2 MPa and 1700 C) find a total-pressure
exponent of about 1.78, consistent with that. The parent's extrapolation:

| Hot wall | Steam pressure | Recession (30-100 m/s) | Coat for 32.5 h |
|---|---|---|---|
| ~1950 K (1800 K exhaust) | 50 atm | 1.6-2.9 mm/h | 5-9 cm |
| ~1950 K | 10 atm | 0.14-0.26 mm/h | 4.6-8.4 mm |
| ~1700 K | 20 atm | 0.15-0.27 mm/h | 4.9-8.9 mm |
| **~1400 K (1300 K exhaust)** | **10 atm** | **10-19 um/h** | **0.33-0.62 mm** |

The extrapolation runs 3-8x past the tested pressure, 10x in steam fraction, and above the tested
wall temperature; channel saturation with Si(OH)4 could cap the loss but is not sourced. Please
check it against the full Terrani data or Opila's Si(OH)4 equilibrium if you can reach them. 1800 K
stays as a row labelled **needs a barrier not yet demonstrated** (rare-earth silicate
environmental barrier coatings protect SiC in turbines, but no pure high-pressure steam data).

| Exhaust | Isp (water) | Heat per kg from 100 K ice | Thrust per 560 MW reactor |
|---|---|---|---|
| **1300 K (base, ~1 MPa)** | **200 s** | **5.35 MJ** | **205 kN, 1.85x NERVA** |
| 1800 K (needs undemonstrated barrier) | 235 s | 6.55 MJ | 197 kN, 1.78x NERVA |

Thrust at fixed reactor power scales as exhaust speed over heat per kilogram, which is why water
gives about 1.8x NERVA's thrust at a quarter of its Isp. The 1800 K Isp is scaled as sqrt(T) and
the heat per kg is about 3.0 MJ through boiling plus steam at 2.3-2.6 kJ/kg/K; both are parent
estimates. The low chamber pressure costs a larger throat and nozzle, not thrust.

| Input | Base | Optimistic | Pessimistic |
|---|---|---|---|
| Engine mass per 560 MW reactor | 3.23 t | 2.68 t | 4.5 t |
| Tankage (walls holding the water), share of propellant | 0.2% | 0.1% | 1% |
| PuffSat skins and electronics, share of PuffSat | 5% | 3% | 10% |
| Mining and launch kit, kg per tonne of ice mined | 0.3 | 0.1 | 1.0 |

**Tankage is light, but keep it as its own line** (Seth, 2026-10-20: the walls should be very
light at these thrusts and Iapetus gravity). On the 12-hour policy the stack never exceeds about
0.15 m/s^2, under 0.02 g, and Iapetus's surface gravity is 0.22 m/s^2. The propellant can ride as
ice at Saturn's 100 K, held by a net or film rather than a pressure wall, with the reactor's heat
melting it into a small feed tank (the 5.35 MJ/kg already includes warming from 100 K). The 0.2%
base and 0.1% optimistic are parent guesses on that basis; 1%, the old base, is now the
pessimistic row. It stays separate from the skins-and-electronics budget because it scales with
propellant, and propellant per kg of PuffSat rises from 10 kg on the 3-hour policy to 16 kg on the
12-hour one. Folded into a per-PuffSat budget it would hide the long burn's cost. At 1% the 12-hour
stage carries about 123 t of tank, 15% of its PuffSat; at 0.2%, about 25 t.

**PuffSat resistojet water comes from Iapetus too** (Seth). It is part of the loaded water, not an
Earth-sourced line; only the resistojets and their power sit in the skins-and-electronics share.

The base engine is NASA's Mars engine as the parent prices it (`sec:ntr_departure`: 111 kN,
3.23 t, about 560 MW thermal). The optimistic mass is NASA GRC's 25 klbf GE-711 cermet engine
(2,675 kg; Fittje, Schnitzler and Borowski, NTRS 20150007681), a 93%-enriched design. The
pessimistic 4.5 t is a parent guess for a heavier low-enriched core, not a sourced figure; please
replace it.

**Burn policy: 12-hour periapsis burn, 32.5 h of engine run (Seth, 2026-10-20).** The parent's
integration chains a finite Iapetus escape (thrust along velocity from a circular orbit at
800 km, to the 986 m/s v_inf the old 0.74 km/s impulsive figure implies), the 0.59 km/s apoapsis
burn, and a finite periapsis burn (2-D, Saturn point mass, thrust along velocity, start
optimised). Engine life is not a constraint; the run it implies is the coat requirement above.
Per 560 MW engine at 1300 K:

| Periapsis burn | Oberth loss | Iapetus escape | Ice loaded | PuffSat | Engine run | PuffSat per Earth kg* | Engine $/kg at $40M |
|---|---|---|---|---|---|---|---|
| 2 h | 1.3% | 0.82 km/s | 2,186 t | 214 t | 5.2 h | 6.2 | $187 |
| 3 h (growth optimum) | 2.8% | 0.85 | 3,308 t | 314 t | 7.9 h | **6.3** | $127 |
| 6 h | 8.5% | 0.91 | 6,653 t | 554 t | 16.0 h | 5.9 | $72 |
| **12 h (base)** | **20.3%** | **0.99** | **13,185 t** | **826 t** | **32.5 h** | **4.8** | **$48** |
| 16 h | 27.2% | 1.02 | 17,456 t | 919 t | 43.5 h | 4.2 | $44 |

*At Iapetus: engine, tanks, mining kit and skins; outbound stages not counted.

Iapetus escape is not thrust-limited. The stack starts there at 0.016 m/s^2 on the 12-hour
policy, and the spiral costs 0.99 km/s against 0.74 impulsive and a 1.37 km/s very-low-thrust
limit. The two policies differ: growth compounds PuffSat per Earth kg, which peaks near 3 h;
steady-state delivery minimises $/kg, which favours long burns because the engine is the scarce,
expensive item and ice is cheap. Please carry the 3-hour growth policy and the 12-hour cost policy
as separate rows, solve the cost optimum with real prices, and check that 12-hour arcs (which
start hours before periapsis) clear the rings on your propagator. Every mass in the chain scales
with thrust, so PuffSat per engine scales with reactor power.

**Redundancy.** Price two rows. (a) A second full engine set. (b) A brake-only reactor sized for
the empty stage, which needs only a small share of the main thrust.

## The comparison: nuclear rocket vs nuclear reactor plus chemical rockets (Seth, 2026-10-21)

**The question for aim (Seth, 2026-10-21).** Compare two ways to spend uranium at Saturn. (a) The
nuclear rocket: one single-use water NTR engine per stage, its reactor dumped into Saturn after
one 32.5-hour run. (b) A nuclear reactor plus chemical rockets: one reactor, launched once, stays
at Saturn for years. It fuels many single-use methalox stages, so its cost is spread over every
stage it fuels. The rest of this section describes (b).

**Framing.** The water cycle stays the paper's base case. Its case is simplicity
and certainty: the cycle has few steps, and the water is known to be there. Methalox is a priced
comparison and a later upgrade, not a replacement. It is examined because on a dollar basis it may
be much cheaper. The uranium in a single-use engine is the expensive line. This alternative keeps
the reactor at Saturn and throws away only a chemical engine and tanks. A methalox engine also
lifts more for the same delta-v and burn time. A Raptor Vacuum-class engine gives roughly 2.5 MN
from about 1.6 t, against 205 kN from the 3.23 t water engine, so about 12x the thrust. At the same
12-hour burn it could push roughly 10x the stack. Price it beside the water stage, at both
Iapetus and Phoebe.

Parent pairing check: an 8,000 t PuffSat stage needs about 17,000 t of methalox and about 230 TJ
from the ceria plant. A 10 MWt ceria plant (1 MW of fuel at 10%) makes that in about 7 years, so
one large stage per round. An electric plant at about 20% does it in about 3.6 years.

**The plant.** A heat-only fission reactor drives a two-step ceria cycle. Ceria (CeO2) is reduced
at about 1773 K in vacuum, releasing oxygen. It is then reoxidised at about 1073 K by water vapour
and CO2, releasing H2 and CO. A methanation step (CO + 3H2 -> CH4 + H2O) turns the gas into
methane, and the oxygen from reduction is captured as LOX. The reactor never touches steam, so the
SiC recession limit above does not apply and the core can be reused for years (Seth). Heat reaches
the ceria by radiation (Seth's base) or through a molten-tin loop (Seth's alternative). Ice Fresnel
lenses (`sec:greedy_phoebe`) are a labelled backup only. At Saturn's 15 W/m^2 they need about
75,000x concentration and an optical error under about 3.7 mrad to hold 1773 K, over about 2 km^2
for 25 MWt.

Parent sizing notes, to check and replace:
- **Radiative coupling.** At an effective emissivity of 0.8, a 1900 K reactor face delivers about
  143 kW/m^2 to 1773 K ceria (about 175 m^2 for 25 MWt, 700 m^2 for 100 MWt). A 2000 K face
  delivers about 278 kW/m^2.
- **Oxygen near the core.** Reduction releases O2 right where the reactor radiates. Tungsten
  oxide volatilises and graphite burns at these temperatures, so the core needs a sealed ceramic
  wall between it and the ceria. Price that wall.
- **Molten tin.** The demonstrated pumping record is about 1673 K (Amy et al., Nature 2017,
  ceramic pump). That is about 100 K short of the 1773 K reduction temperature, so label the tin
  row as needing a modest extension.
- **Core life.** Fuel swelling and fission-gas release at about 2000 K over years set the life.
  The closest flown analogue is the Soviet TOPAZ thermionic reactor, whose emitters ran near
  1800 K for about a year (Cosmos 1867). Find a sourced life for a heat-only core at this
  temperature.
- **Burnup.** 25 MWt for 9.5 years fissions about 91 kg of U-235; 100 MWt fissions about 366 kg.
  Size the inventory for the burnup, not only for criticality.
- **Ceria efficiency.** Heat into the ceria converted to chemical energy: 10% base, 5%
  pessimistic. The parent's energy balance gives 9-18% with no recovery of the solid's sensible
  heat and 15-27% with 50% recovery, at a vacuum reduction extent of 0.02-0.05. Demonstrated
  solar-to-fuel is about 4-5% (ETH Zurich's reactors), but that figure includes concentrator and
  receiver losses a reactor does not have. Cool the ceria only to the oxidation temperature, with
  the incoming cold vapour as both oxidant and coolant, and use low-grade waste heat to sublimate
  the next feed. Quenching against ice wastes the sensible heat and slows oxidation below about
  773 K.
- **Ceria inventory.** About 15-25 t at 100 MWt for minute-scale cycles, 150-250 t for 10-minute
  cycles; scale with power.

**Propellant per stage (parent scratch, impulsive, Isp 370 s base and 380 s optimistic (Raptor
Vacuum class), dry mass 8-12% of propellant, 826 t of PuffSat to match the water stage's 12-hour
base).** Chemical thrust is high, so the 20.3% Oberth loss of the long nuclear burn goes away.
The Iapetus escape is taken at the doc's 0.74 km/s impulsive figure.

| Site | Delta-v from the moon to the departure (km/s) | Methalox | CO2 needed (or carbon equivalent) | Ceria output |
|---|---|---|---|---|
| Iapetus | 0.74 + 0.59 + 2.37 = 3.70 | 1,620-1,860 t | 970-1,110 t | 22-25 TJ |
| Phoebe | about 0.10 + 1.45 + 2.42 = 3.97 | 1,850-2,160 t | 1,110-1,290 t | 25-30 TJ |

The Phoebe 1.45 km/s cancels most of Phoebe's 1.71 km/s retrograde orbital speed to drop
periapsis to 150,000 km straight from Phoebe's 12.95 million km orbit. Per kg of methalox at O/F
3.6, the plant makes 13.7 MJ of chemical energy and consumes 0.60 kg of CO2 (0.163 kg of carbon)
and 0.49 kg of net water.

**Power policy: target 5-10 MWt (Seth, 2026-10-21).** Methane boils at 112 K and LOX at 90 K,
close to the moons' 90-130 K surfaces. Shaded storage can therefore hold the propellant for years
without a deep cryocooler. The plant can run all round and stockpile. At 10%, one stage per round
needs about 1 MWt running for nine years, or about 20 MWt if it runs only during a 0.4-year stay.
5-10 MWt running all round fuels about 5-10 stages per round (about 4,000-8,000 t of PuffSat), so
stage count is no longer set by engine price. 100 MWt (about 100 stages) stays as a sensitivity
row only. Please solve the number of stages per round against reactor power, Earth-sourced
chemical engines and the Earth plates' push capacity, and report $/kg against power.

**Electric route at the same power (Seth asked whether it wins at 5-10 MW).** Price a second plant:
the same reactor class run at about 1150 K into a Brayton converter (about 25% thermal to
electric), with solid-oxide co-electrolysis of H2O and CO2 (about 80% electric to chemical; MOXIE
on Mars is the flown small-scale analogue) feeding the same methanation step. That chain turns
about 20% of the heat into fuel, against the ceria plant's 10% base. Parent ballpark, per MW of
chemical output:

| | Ceria plant | Electric plant |
|---|---|---|
| Heat per MW of fuel | 10 MWt | about 5 MWt |
| Reactor | heat-only core at about 2000 K, years of life not demonstrated | about 1150 K, the Kilopower/KRUSTY and SP-100 class |
| Big items | ceria, ceramic wall, high-temperature heat rejection | converter, about 900 m^2 of radiator per MWe at 450 K (about 5 t), electrolyser stacks (2-5 kg/kWe) |
| Total, t per MW of fuel | about 10-20 (parent guess) | about 15-30, at 10-20 kg/kWe for MW-class space fission power (NASA NEP study targets) |

The two are close on mass. The electric plant is more mature, and its power also runs mining, the
cryogenic radiators and PuffSat charging. Both plants can dump waste heat into mined ice instead of
radiators if they sit on the surface; price that option for both. Fuel cost does not separate them
at this power: 5 MWt for 9.5 years fissions about 18 kg of U-235, well below a HALEU core's
criticality inventory, so the inventory is set by criticality either way. Report $/kg for both
plants across 1-20 MWt and say where, if anywhere, ceria wins.

**Carbon is the open gate.** Neither moon has a measured bulk carbon content (see the parent's
note below the table in item 2, tankage). CO2 ice and organics are detected only in the top
surface layer. A stage needs about 1,000 t of CO2 or its carbon equivalent. At 1% CO2 in mined
dark material that is about 100,000 t of regolith per stage; at 0.1%, about a million. Print
rows at 0.1%, 1% and 10% CO2 (or carbon) in the mined material for each moon. No hydrolox row:
liquid hydrogen needs a cryocooler of a few hundred kWe per stage and years of storage below 20 K,
which Seth ruled out (2026-10-21). If carbon fails, the water stage is the fallback.

**Carbon processing kit (Seth, 2026-10-21).** Charge the equipment that turns surface material
into feedstock as its own Earth-sourced line, priced by the tonnes of regolith it must handle.
Do not assume it is light. The methanation reactor is small, but the dig scales with carbon
grade: at 10% carbon about 10,000 t of regolith per stage, at 1% about 100,000 t, at 0.1% about a
million. Include excavation, heating the regolith to release CO2 or pyrolyse organics, and gas
cleanup. Use the mining kit's kg per tonne figures as the starting rows, and report the grade at
which the kit stops paying.

**Site rows.** Iapetus: ice about 75-80% by mass (parent estimate from its 1.09 g/cm^3 density),
surface gravity 0.22 m/s^2, a 79-day synchronous rotation. Phoebe: about 50% ice
(`castillo_rogez2012_phoebe` in the paper), about 0.05 m/s^2 and 100 m/s escape, a 9.3-hour day,
anchoring by hold-down thrusters (`sec:greedy_phoebe`). Compute the outbound Saturn-side
delta-v to match Phoebe's retrograde orbit on your propagator; the parent has not.

**The stage.** Single use, with engines from Earth and tanks made at Saturn or shipped (the
tankage row). It needs no disposal brake, because it carries no reactor. After separation, the
empty stage is still on the PuffSats' Earth-bound arc. It needs a small divert burn to miss Earth
and the plate; price a reserve (50 m/s, parent guess). Price a reuse row as well: brake back to a
bound orbit (the 2.89 km/s above) to recover the engines.

## Parent results to reproduce (bare plate unless noted)

These came from the earlier 200 s, 3-4 h life sizing (flat 1.00 km/s Iapetus escape, engines sized
by life) and predate the 12-hour burn policy. Reproduce them at that point as a check, then rerun
at the new base.

| Quantity | Value |
|---|---|
| PuffSat per Earth-sourced kg at Iapetus | 5.4:1 (5.0:1 with a second full engine set) |
| Ice mined per kg of PuffSat | 12.4 kg |
| Outbound cost, kg in eccentric orbit (LEO) per kg landed at Iapetus | 8.2 (13.9). Hydrogen NTP for Earth departure, methalox at Saturn, tanks priced |
| Earth push per kg of returned PuffSat | 6.7x bare plate; **10.3x** at k = 8.5, eta_jet = 0.775 |
| Growth per round, round 1 / round 2 | 2.6x / 4.4x bare; 3.7x / 6.3x with k = 8.5 and redundancy |
| 19 years | about 10x bare; **about 23x** with the charge; about 120x optimistic |

**New-base estimates to reproduce** (12-hour policy, 826 t of PuffSat per 560 MW engine, Seth
rounding the push to about 8,000 t):

| Line | Parent estimate |
|---|---|
| Mass pushed to the eccentric orbit per engine | 826 t x 10.3 = about 8,500 t with the charge (includes the plate; Seth carries 8,000 t); 5,500 t on a bare plate |
| Reactor, $/kg pushed | **about $5** ($40M / 8,000 t); $7.5 at $60M, $12.5 at $100M, $7 on a bare plate; 2x with a second full engine set |
| Reactor with cost of capital (9.5 years from purchase to delivery) | x1.45 at 4%, x5.6 at 20% |
| Earth charge, $/kg pushed | **about $25**: 8.5 x 826 = 7,000 t lofted at $26.6/kg (lob) plus $2/kg (polyethylene), about $200M |

The charge, not the reactor, is the larger Earth-side line. Both await S50's leverage.

Leverage law used for the charge, from the parent's overtake impulse
`I/(m w) = eta_jet sqrt(1+k) + 1`: `M_f/m = k / ((w/(w - v_f))^(k/B) - 1)`, with
`B = 1 + eta_jet sqrt(1+k)`. Replace with S50's numbers when they land.

## S51. Wanted

1. **The mass ledger.** Build the cycle as a parameterised module, for example
   `src/iapetus_cycle.py`, with every row above as an input. Reproduce the parent's base, then
   report growth per round and over 19 years for the three cases. Size engines by
   `max(window, life)`.
2. **The cost ledger.** Price each line on its own evidence, and carry the worst cases as a
   labelled row rather than stacking them (the parent's rule). Seth also wants two whole ledgers
   printed side by side (2026-10-20):

   | | Ledger A: reuse at scale | Ledger B: no reuse |
   |---|---|---|
   | Earth pusher plate, per flight | **$200K** (reused; see below) | **$5M** (expended each flight) |
   | PuffSat electronics | **$1/kg of delivered payload** (at scale) | the ledger's existing prices |
   | Burn policy off Iapetus | 12 h: 826 t of PuffSat per engine | 6 h: 554 t (a less ambitious payload) |
   | Engine, tankage, charge | per-line base rows | per-line base rows |

   Plate reuse is credible because Saturn departures can spread across a broad window, perhaps
   half the year, each onto a fast Earth-crossing orbit. Returns then arrive as a steady stream
   rather than one pulse, so an Earth plate can fly many pushes. $200K per flight on a $5M plate
   is about 25 flights. Report how many pushes the arrival stream supports per plate, and the
   plate count each ledger needs.
   - **Engines.** Price fuel per kilogram of U-235, not of uranium: HALEU at $20-25k per kgU is
     about $100-125k per kg of U-235 (anchors: a December 2023 model at about $23,700-25,700 per
     kgU, and a press range of $25,000-35,000 per kgU). Reactor-grade 4.5% LEU is about the same
     per kg of U-235, so lower enrichment saves nothing. Inventory is the lever. NASA GRC's
     93%-enriched 25 klbf engines carry 36.8 kg of U-235 in graphite composite and 258.6 kg in the
     GE-711 cermet (NTRS 20150007681); this stage must use the cermet, so it starts near
     $28M of U-235 before the larger low-enriched inventory. Find a sourced U-235 inventory for a
     low-enriched cermet engine of this class, then build up fuel fabrication, any tungsten-184
     enrichment, and non-fuel hardware. Price rows: **$40M optimistic, $60M estimate, $100M
     pessimistic (labelled)** per engine at scale; these are working figures from the parent's
     discussion, not cited, for a 560 MW engine. Above criticality, power is cheap in U-235: in
     NASA GRC's cermet pair, 266 MW took 238.5 kg and 564 MW took 258.6 kg (2.1x the power for 8%
     more U-235, 1.5x the engine mass). So model the engine as a fixed part (the U-235 a
     criticality-limited HALEU cermet core needs) plus a per-MW part (fuel elements, tungsten,
     turbopump, structure), find the most power that core reaches at the 1400 K wall, and let the
     ledger pick the cheapest power per engine. Report the engine line's share of $/kg. Each stage dumps nearly all
     its uranium into Saturn, since one run fissions only about 0.2 kg per engine.
   - **Outbound stages,** using the ledger's existing hydrogen NTP and methalox prices.
   - **PuffSat skins and electronics,** at the ledger's existing prices (Ledger B) or $1/kg of
     delivered payload (Ledger A).
   - **Earth pusher plates,** per the two ledgers above.
   - **Tankage and the mining kit.** Price a second tankage row: **walls made at Saturn** from
     local carbon and water (Seth, 2026-10-20). Iapetus's dark leading hemisphere carries organics
     and CO2 ice, and Phoebe's surface shows CO2 ice. Neither moon's bulk carbon is measured: the
     dark, flat spectra also fit metallic iron and iron oxides (Clark et al., Icarus 2012, for
     Iapetus), and reflectance sees only the top millimetres. Polyethylene from CO2 and water
     takes electrolysis plus synthesis, roughly 50-100 MJ of electricity per kg (parent estimate;
     polyethylene's heat of combustion is about 46 MJ/kg). The propulsion reactor has no power
     conversion, and running steam through it to idle erodes its barrier, so the row uses a
     separate surface fission unit of NASA's Fission Surface Power class (40 kWe target). At
     40 kWe and 75 MJ/kg it makes about 17 t a year, enough for the 12-hour stage's 25 t of tank
     (0.2%) in about 1.5 years of the round, or a fiber net for frozen-ice tanks. Charge the unit's
     Earth-sourced mass and price, amortised over the rounds and stages it serves, and report the
     break-even against shipping the tank from Earth. Chemical propellant from the same plant is
     out: 13,000 t per stage at about 60 MJ/kg would take a 40 kWe unit about 600 years.
   - **The Earth charge,** `k` kg per kg of returned PuffSat, at the ledger's lob price.
   - **Round 1's launch to LEO,** at the ledger's Starship price book.
3. **Valuation: two models, each on both ledgers** (Seth, 2026-10-20), so four cells:
   - **Gated rNPV**, the paper's drug-development convention (CONTEXT.md "Gated rNPV"; companion
     ADR 0072): time at 10% a year, each cash flow weighted by the odds of every gate before it,
     growth then held level and the surplus sold, break-even as PV of dollars over PV of kilograms.
   - **Government loan**: the same gates and break-even, with time at 4% a year (Seth: a
     risk-free government loan instead of startup capital). The gates stay on, because a cheap
     loan lowers the price of waiting, not the chance the cycle fails. If you also print a
     no-gates row, label it as assuming every gate passes.

   **Gates (Seth confirmed 2026-10-20).** Seth's argument: the Saturn side is
   well-understood technology that can largely be tested on Earth. A 1300 K exhaust with a
   ~1400 K wall is milder than the 2,550 K Rover/NERVA ground-tested in 22 reactors. The Earth-side
   PuffSat and plate gates carry the paper's risk. Odds:

   | Gate | Odds | Why |
   |---|---|---|
   | Outbound stack captures at Saturn and lands the kit on Iapetus | 95% | Hydrogen NTP and methalox, flight-analog manoeuvres |
   | Water stage qualified (ground test) and its first Saturn departure works, ice mined and loaded | 90% | Earth-testable reactor; first ice throw and long periapsis burn are new |
   | PuffSats coast 3.7 years and home onto the Earth plate at 51 km/s | 85% | The paper's homing gate at a new closing speed |
   | First Earth push with the carried charge | 90% | The paper's first-push gate |

   Together about 65%, against the solar-dive cycle's 55%. Growth: two rounds (19 years, the
   paper's drug-timeline analogue) reinvested, then held level and the surplus sold. Report the
   break-even $/kg to the eccentric orbit in all four cells, plus the per-line worst-case rows.
4. **The comparison.** Price mass delivered to the same eccentric orbit by this cycle, in dollars
   per kg, against the paper's current recommended route to that orbit. Use whatever the
   ledger now prints for that route, not a convenient reference.
5. **The core comparison: nuclear rocket vs reactor plus chemical rockets (Seth, 2026-10-21).**
   One reactor launch fuels many chemical stages, so amortise the plant over every stage it fuels
   across its life (rounds served, stages per round). Report how many chemical stages one reactor
   fuels, and the reactor's $/kg pushed in each option. Price the methalox option at
   Iapetus and at Phoebe, on both ledgers and both valuation models, beside the water stage.
   Lines: the reactor-heated ceria plant (reactor, ceramic wall or tin loop, ceria, methanation,
   LOX capture), amortised over its life and the stages it fuels; the electric plant as a second
   row; the carbon processing kit; chemical engines at the ledger's methalox prices; tanks; the
   divert reserve; and the carbon-abundance rows. Replace the water-stage gate with "ceria plant runs at Saturn and fuels the
   first stage". Use the water stage's 90% as a labelled placeholder until Seth sets the odds.
   Report $/kg to the eccentric orbit for water NTR, methalox at Iapetus and methalox at Phoebe
   side by side. Size the methalox stage by burn time as well as by plant output, since its
   engine is not the scarce item.

   **Target: about $1-2 per kg for data-center launch** (Seth's hope, 2026-10-21, with reusable
   Earth plates (Ledger A) and low capital cost). Report whether any cell reaches it. If none
   does, report which lines must fall, and how far, to get there. The parent's own estimate
   points at the Earth charge first: about $25/kg pushed at k = 8.5 lofted at $26.6/kg, against
   about $5/kg for the reactor. Cheaper Saturn-side propulsion cannot reach $1-2 while that
   line stands at that price. The $1-2 target assumes the Earth charge itself rides reusable
   plates on an optimised trajectory (Seth, 2026-10-21); the parent's $26.6/kg lob price does not
   assume that. Price the charge on that basis, say what lob price it implies, and print it next
   to the $26.6/kg base, a bare-plate row (6.7x, no Earth charge) and any cheaper charge source.
6. **Sensitivities worth printing.** Arrival speed (51 vs 68-70 km/s; the faster arrival raises
   push leverage but costs more at Saturn), engine price, reactor power per engine, exhaust
   temperature (1300 K base; 1800 K labelled), chamber pressure, burn policy (3 h growth, 12 h
   base, 16 h), and `k`.

Paper edits that wait on this: the whole cycle. The parent will not print the Iapetus option
until S50 and S51 land.
