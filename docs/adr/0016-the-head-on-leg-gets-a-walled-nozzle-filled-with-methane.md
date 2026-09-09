# The head-on leg gets a walled nozzle, and methane fills it

Status: **proposed**. Resolved in a grill session on 2026-09-08 and amended
2026-09-09, when the flown fluid changed from ammonia to methane. The paper text
is not yet written and no companion calculation has been rerun. Terms are recorded in
`CONTEXT.md` under **Wall-cap energy density**, **The slug ladder** and
**Density is what saves every fluid on the ladder**.

## Decision

Admit a walled de Laval chamber as a non-magnetic option on the head-on
Earth-to-Jupiter departure burn of `sec:jupiter_only_growth`, at the flown
\SI{75}{\kilo\meter\per\second} closing speed. Run the chamber at
\SI{10000}{\kelvin}, which is Rubbia's own radiative ceiling, and do not chase
higher.

Going hotter was considered and declined. The ideal law $v = \sqrt{2c_pT}$ still
holds, but our capacity is $A + BT$ where $A$ is the atomisation store, and only $BT$
moves. Methane's sensible fraction is \num{0.273}, so its exponent on temperature is
\num{0.136} rather than \num{0.5}, and \SI{12000}{\kelvin} returns 2.5\%. That is
smaller than the uncertainty in $\eta_{\mathrm{geom}}$, in the convective wall flux
and in the recombination fraction, so it spends certainty to buy noise.
\SI{10000}{\kelvin} additionally has a citation, closes the heat balance with 91\% of
the wall load absorbed against 71\%, and keeps the liner at
\SI{3.2}{\micro\meter} per pulse.
Present it as a family of working fluids ordered by one number, and name **methane**
as the fluid we would fly.

The precedent is Rubbia's thin-film \ce{^{242m}Am} fission-fragment-heated rocket,
Project 242, which heats hydrogen to the same temperature continuously
\cite{augelli2013project242}.

## The number that orders the family

A walled nozzle's exhaust speed is $w/\sqrt{1+k}$, and the slug ratio $k$ is set by
how much energy a kilogram of working fluid can hold at the temperature the wall
survives. Call that the **wall-cap energy density**. At \SI{10000}{\kelvin} it runs
hydrogen \SI{338}{\mega\joule\per\kilogram}, methane 143, ammonia 98, water 72,
helium 31. Everything else follows from it.

| slug | $k$ | slug/pulse | effective Isp | GN\,s per load | vessel | storage |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| **methane** | 21.59 | \SI{540}{\kilo\gram} | **1080 s** | **1.059** | \SI{8.6}{\tonne} | \SI{422}{\kilogram\per\cubic\meter} at \SI{111}{\kelvin} |
| water alone | 42.51 | \SI{1063}{\kilo\gram} | 831 s | 0.815 | \SI{9.2}{\tonne} | ambient |
| ammonia | 43.58 | \SI{1089}{\kilo\gram} | 823 s | 0.807 | \SI{11.2}{\tonne} | \SI{240}{\kelvin}, \SI{10}{\bar} |
| liquid hydrogen | 11.02 | \SI{275}{\kilo\gram} | 1356 s | 0.753 | \SI{12.4}{\tonne} | \SI{20}{\kelvin} |
| (water on the magnetic nozzle) | 8.52 | \SI{213}{\kilo\gram} | 1249 s | 1.225 | \SIrange{17.3}{37.6}{\tonne} | ambient |

Scored at a \SI{25}{\kilo\gram} impactor, $\eta_{\mathrm{geom}} = 0.852$ from the
flown water case, a \SI{400}{\cubic\meter} chamber and \SI{10000}{\kelvin}, **with
the dissociation equilibrium solved rather than assumed**. Hydrogen runs 55 to 76\%
dissociated across these cases, not fully, so the chemical store is only partly
charged and it responds to pressure as well as to temperature. Earlier drafts of this
decision assumed full atomisation and read \SIrange{15}{30}{\percent} high. Methane
spans \SIrange{1059}{1095}{\second} across the \SIrange{200}{673}{\cubic\meter}
geometry range that N9 has yet to close. The solve omits OH, CH, \ce{C2} and
ionisation, so it is a paper-side estimate pending N10.

## Why methane rather than the hydrogen the precedent points at

Hydrogen wins the exhaust speed and loses the launch. It delivers
\SI{14590}{\newton\second} per kilogram of launched slug against water's 12247, a
19\% gain on the paper's mass-based ledger. Against that, liquid hydrogen is the
first payload in this paper where **volume** binds first. A standard bay holds about
\SI{57}{\tonne} of it where it holds \SI{100}{\tonne} of a dense fluid, and the Isp
advantage only repays that above a burn of about \SI{22}{\kilo\meter\per\second}.
This leg is a few.

Methane leads ammonia on specific impulse by 31\%, on the launch ledger by 31\%, on
vessel mass by 23\% and on slug mass per pulse by 50\%. The gap widened when the
dissociation equilibrium was solved, because ammonia's nitrogen re-forms \ce{N2} and
discharges its store further than methane's carbon does. Ammonia and water are now
within 1\% of each other rather than ammonia leading. It is
also not toxic, and Starship already flies methane, so its tankage and boil-off
management are flown hardware rather than a new subsystem. Ammonia keeps only the
easier storage temperature, and \SI{111}{\kelvin} against \SI{240}{\kelvin} is not
the gap that \SI{20}{\kelvin} was.

## The two objections to methane that failed

This decision first named ammonia, on 2026-09-08, and reversed a day later. Both
objections were wrong and both are worth recording so they are not raised again.

**The soot two-phase objection was calibrated on the wrong particle.** Solid rockets
pay 5 to 8\% of specific impulse because alumina is about \SI{5}{\micro\meter} of
dense liquid. Soot primaries are \SI{30}{\nano\meter}. Velocity relaxation against a
\SI{1}{\milli\second} residence gives a margin of \num{1e6} at
\SI{30}{\nano\meter} and still \num{900} for a \SI{1}{\micro\meter} agglomerate,
against 36 for the alumina. Even agglomerated soot follows the flow.

**The high-$Z$ radiation objection reverses in an optically thick chamber.** Carbon
gives 1.84 times the free electrons and 3.4 times the volumetric emission at
\SI{10000}{\kelvin}. But escape goes as $\sigma T^4(1-e^{-\tau})/(1+\tfrac{3}{4}\tau)$
and the same electrons raise $\tau$. Above $\tau \sim 1$ more absorbers means less
escapes. Rubbia's chamber is $\tau \approx 0.003$ and ours is 7 to 45, so his
transparency argument is a low-density argument in the same way his recombination
finding is, and neither transfers.

The endothermic cost separates nothing. What never returns is the formation enthalpy
rather than the atomisation energy, and that is \SI{2.70}{\mega\joule\per\kilogram}
for ammonia against \SI{4.66}{} for methane. Both are a few percent.

What decides it in methane's favour beyond the ledger is that **the carbon is the
sacrificial layer this design already wants**. The liner loses \SIrange{1.26}{13.9}{\kilo\gram}
per pulse against \SI{376}{\kilo\gram} of carbon in the exhaust, so
\SIrange{0.34}{3.7}{\percent} redeposition makes it self-healing. A water or ammonia
exhaust carries nothing that could rebuild a liner and has to be sprayed between
pulses. Methane's exhaust is the spray.

## What the wall survives on

Two mechanisms, and both are density.

The chamber is optically thick, $\tau \approx 7$ to 37 across the bore, so it leaks
radiation through a gradient rather than emitting $\sigma T^4$. That is the same
treatment `eq:cooling_race` already gives the lead fireball. The escaping flux is
about \SI{87}{\mega\watt\per\square\meter} instantaneous, and at a 2\% duty cycle the
time-averaged load is \SI{1.7}{\mega\watt\per\square\meter} against Rubbia's
\SI{1.6}{\mega\watt\per\square\meter} continuous.

Three-body recombination goes as $n^2$, and a wall holds $n$ up where a field lets
the plume thin. Margins against a \SI{1}{\milli\second} transit at chamber density
are 3400 for $\ce{H} + \ce{H} + M$ and 403 for $\ce{N} + \ce{N} + M$. Carbon is the
exception and it is the one that now matters, because soot forms by nucleation
rather than by a three-body collision and so gets none of this help. Nitrogen is
about eight times slower, which is why it freezes in arcjets at
\SIrange{0.1}{1}{\bar} and does not freeze here. `sec:watering_it_down` finds the
water plume freezing at \SI{0.02}{\kilogram\per\cubic\meter} only because a magnetic
nozzle free-expands it. Bray's sudden-freezing criterion is the mechanism
\cite{bray1959recombination}.

The vessel is a filament-wound composite case behind a refractory liner, not steel.
Mass runs as $1.5\,nRT\rho/\sigma$ and does not depend on pressure. The same
\SI{16.9}{\giga\joule} of $nRT$ gives \SI{991}{\tonne} in steel, \SI{125}{\tonne} in
titanium and about \SI{8.7}{\tonne} in carbon overwrap for the methane charge.

## What this deliberately does not do

The section is self-contained. One sentence goes into `sec:minimum_nozzle` pointing
at a non-magnetic option on the head-on leg, and nothing existing is re-scored.

Two re-scorings were considered and declined. The methane vessel's
\SI{8.7}{\tonne} against the magnet's \SIrange{17.3}{37.6}{\tonne} of structure plus
conductor would move `sec:minimum_nozzle`'s finding that the nozzle is 8 to 38\% of a
\SI{100}{\tonne} craft. Rerunning the growth chain at 1080 seconds would say whether
the thermal nozzle passes the chain's binding launch-and-return budget. Both are
companion-repo work.

## Chamber and film

The chamber keeps the paper's \SI{3}{\meter} bore and shortens the column. Methane
carries \SI{474}{\kilo\gram} per pulse against ammonia's 688, so the charge is
\SI{499}{\kilo\gram} at \SI{12.73}{\giga\joule} of $nRT$. At
\SI{200}{\cubic\meter} over \SI{7.1}{\meter} the optical depth is 45, the wall
takes \SI{0.42}{\mega\joule\per\square\meter} per pulse, and the sprayed carbon
film stays at \SI{3.2}{\micro\meter}. The full \SI{23.8}{\meter} column gives 7.3,
\SI{2.29}{\mega\joule\per\square\meter} and \SI{17.5}{\micro\meter}. Pressure
rises to \SI{636}{\bar}, which the vessel mass does not feel, and the pre-charge is
\SI{1.4}{\bar} of methane vapour at \SI{111}{\kelvin}, so the bag, the membrane and
the atomiser all disappear.

One thing got worse in the flip to methane. Its latent heat is
\SI{511}{\kilo\joule\per\kilogram} against ammonia's 1371 and it carries 31\% less
mass per pulse, so the regenerative sink absorbs 73\% of the wall load at
\SI{200}{\cubic\meter} where ammonia absorbed all of it. The remainder is about
\SI{38}{\giga\joule} over a \SI{100}{\second} burn, or \SI{380}{\mega\watt} of
radiator. Superheating the methane past about \SI{400}{\kelvin} before injection
closes the gap, and the classical limit on that is coking in the cooling channels.
Here the same carbon is the liner, so whether coking is a fault is itself open.

A short column is admissible only if a sealed vessel escapes the
`sec:needle_through_fog` coupling problem. That section worries because a magnetic
nozzle's bag is a free-standing cloud, so unswept mass is left behind. In a closed
chamber unswept propellant is still in the chamber, and at an
\SI{11}{\kilo\meter\per\second} sound speed a \SI{7}{\meter} column equilibrates
some fifty times during the blowdown. That is the first thing N9 has to check. Until
it returns, \SI{400}{\cubic\meter} over \SI{14}{\meter} is the conservative middle.

Film injection is retained as a shield for the shocked front and as a convective
coolant. It is **not** a radiation shield, and the section must not claim it is. The
chamber's own optical depth already does that work, and a film thin enough to inject
sits near an optical depth of 0.03. With methane the between-pulse spray may be
unnecessary, since the exhaust carries \SI{376}{\kilo\gram} of carbon past a liner
that loses \SIrange{1.26}{13.9}{\kilo\gram}.

## What stays open

Two questions arrive with methane and neither existed for ammonia. **Does carbon
condensation complete?** Soot forms by nucleation rather than by a three-body
collision, so it gets none of the density help the rest of this decision rests on. If
it does not nucleate, 43\% of methane's atomisation stays as \ce{C}, \ce{C2} and
\ce{C3} vapour. That is the largest single chemical exposure in the section, and it is
bounded rather than fatal: the floor is \SI{880}{\second}, against helium's chemically
risk-free \SI{667}{\second} and methalox's 380. The only propellants that cannot
freeze are monatomic and they are far worse, so this risk cannot be bought off. **And
does carbon deposit in the throat?** A drifting throat area is the one dimension a
nozzle cannot tolerate. The throat is the hottest and fastest station so it should
clean itself, but nothing here shows that. Both belong with N9 and N10.

The wall's load case during the crossing is not the \SI{10000}{\kelvin} equilibrium
this decision clears it for. `sec:needle_through_fog` puts the freshly shocked layer
at the nose of a \SI{45.58}{\kilo\meter\per\second} arrival near
\SI{94600}{\kelvin}, and has the spreading cone reaching a \SI{3}{\meter} wall after
\SI{6}{\meter} of a \SI{23.8}{\meter} column. At \SI{75}{\kilo\meter\per\second} the
specific energy is 2.7 times higher. This belongs with the impact simulation, and
until it returns the section carries it as a stated condition rather than as a
settled result.

Project 242 has now been read, and it supports this decision more directly than the
secondary summaries did. Their prose says molecular recombination "is not" fast. Their
arithmetic says otherwise. The carried baseline of \SI{2700}{\second} at
\SI{3200}{\newton} needs \SI{351}{\mega\joule\per\kilogram} of stagnation enthalpy,
where sensible-only hydrogen at \SI{10000}{\kelvin} supplies 206 and full dissociation
recovery supplies 421. Their figure therefore implies \SI{67}{\percent} of the
dissociation energy returns, and a frozen-molecular \SI{2700}{\second} would need a
\SI{17000}{\kelvin} chamber against their own \SI{9500}{\kelvin} radiative ceiling.
Their thrust and jet power close exactly, so the number is the one they flew.

They still cannot run dense, and the reason is their heat source rather than their
nozzle. A fission fragment stops in about \SI{0.5}{\milli\gram\per\square\centi\meter}
of gas, which is \SI{12.5}{\milli\meter} in their cold wall gas and
\SI{1.4}{\milli\meter} at our \SI{200}{\cubic\meter} chamber density. At our density
the fragments would deposit inside the wall's own boundary layer. A \SI{25}{\kilo\gram}
impactor at \SI{75}{\kilo\meter\per\second} has no range to match, and density only
helps it couple. We run 139 times their number density, so roughly \num{1.9e4} on the
three-body rate before the longer residence is counted. Project 242 is the anchor for
the confinement argument, not a counterexample to it.

Their measured efficiency is \SI{18.7}{\percent}, being \SI{43}{\mega\watt} of jet
power from \SI{230}{\mega\watt} thermal with \SI{190}{\mega\watt} rejected through a
\SI{3}{\tonne} radiator. Their walls are transpiration-cooled through porous
carbon--carbon, which is the precedent for the film this decision retains.

The liner material is unchosen. `sec:watering_it_down` picks pyrolytic graphite for
a water plume and then hedges it against oxygen. Methane removes the oxidation
problem and keeps graphite as the default, which is convenient because the exhaust
may rebuild it. The tungsten option and the question of atomic nitrogen attacking
carbon to form CN belong to the ammonia variant rather than to this one.
