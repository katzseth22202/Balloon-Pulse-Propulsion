# The head-on leg gets a walled nozzle, and methane fills it

Status: **proposed**. Resolved in a grill session on 2026-09-08, amended
2026-09-09 when the flown fluid changed from ammonia to methane, and amended again
the same day when the companion returned N9 item 0 and all of N10. Terms are
recorded in `CONTEXT.md` under **Wall-cap energy density**, **The slug ladder** and
**Density is what saves every fluid on the ladder**.

**The companion has answered N9 item 0 and N10 items 1 to 5.** The answer document
is carried verbatim at `docs/walled_nozzle_answers_from_impact_sim.md`, from
`puffsat_impact_simulation` at `6d74d3f`, computed at its `4a448c0`. Every number
below that changed is marked with the finding that moved it, W1 through W9. The
paper text is still not written, because **N9 items 1 to 7 are the load case and
none of them has been run**. Those decide whether the wall survives the arrival
transient and whether the throat holds its area, and the section cannot state a
survivable wall without them.

**The largest single change is that the 2026-09-09 dissociation correction is
withdrawn.** It cost methane 40 seconds on a two-parameter fit that the companion's
nine-species equilibrium solve overturns. The chemical store is 95 to 99 per cent
charged at the flown 10,000 K, not 61 to 67, so methane's full-recombination figure returns to
\SIrange{1120}{1133}{\second} across the geometry range.

**A second change goes the other way and is larger.** Applying the return exposed that this
decision has been scoring the wall on a different convention from the magnet it is compared
against: every walled figure assumed full recombination where `eq:eta_chem` charges the magnet
for its own. Charged the chemistry the companion actually measures, **methane is
\SI{709}{\second} against the magnetic nozzle's \SI{1249}{\second}**, not \SI{1129}{\second}
against it, and that 1249 is a target where the 709 is solved. See "The two nozzles were never
on the same convention".

## Decision

Admit a walled de Laval chamber as a non-magnetic option on the head-on
Earth-to-Jupiter departure burn of `sec:jupiter_only_growth`, at the flown
\SI{75}{\kilo\meter\per\second} closing speed. Run the chamber at
\SI{10000}{\kelvin}, which is Rubbia's own radiative ceiling, and do not chase
higher.

Going hotter was considered and declined. The ideal law $v = \sqrt{2c_pT}$ still
holds, but our capacity is $A + BT$ where $A$ is the atomisation store, and only $BT$
moves. Methane's sensible fraction is \num{0.273}, which the companion confirms at
\numrange{0.277}{0.287}, so the exponent on temperature is far from \num{0.5} and
\SI{12000}{\kelvin} returns 3.5 to 4.9\%. That is still smaller than the uncertainty in
$\eta_{\mathrm{geom}}$, in the convective wall flux and in the recombination fraction,
so it spends certainty to buy noise. \SI{10000}{\kelvin} additionally has a citation,
closes the heat balance with 91\% of the wall load absorbed against 71\%, and keeps the
liner at \SI{3.2}{\micro\meter} per pulse.

**Charging the chemistry reverses this, and the reason to stay at
\SI{10000}{\kelvin} is now much stronger than "the gain is small."** Every figure above
comes from the withdrawn full-recombination convention, where a hotter chamber was worth a
free 3.5\% and the only argument against it was that 3.5\% is inside the noise. Charged
properly, **going hotter is negative.**

The mechanism is worth following, because it is the same one that cost the wall its impulse
in the first place, running backwards. A hotter chamber genuinely helps where this decision
said it did: at \SI{12000}{\kelvin} a kilogram of methane holds more, so the slug falls from
\SI{489}{\kilo\gram} to 444, energy per kilogram rises from 136.8 to
\SI{149.8}{\mega\joule\per\kilogram}, and the tear-apart bill falls from 74.2\% of the budget
to 67.6\%. Held there, that is worth **+11\%**, three times what this decision booked.

**But the exit temperature rides along with the chamber, and the exit is what decides how much
of the bill comes back.** At a fixed area ratio $T_e/T_c$ is fixed, so a
\SI{12000}{\kelvin} chamber leaves the same \SI{7}{\square\meter} throat at
\SI{6701}{\kelvin} rather than 5584. On the companion's own three exit points, roughly five
points of store per \SI{500}{\kelvin}, it therefore leaves holding about 80.6\% of its store
where the \SI{10000}{\kelvin} case holds 69.8\%, and it leaves hotter as well. **Break-even is
78.4\% held**, so the hotter chamber falls just the wrong side of it on chemistry alone and
clearly the wrong side once the extra leftover heat is counted.

| throat | \SI{10000}{\kelvin} | \SI{12000}{\kelvin} | |
| ---: | ---: | ---: | ---: |
| \SI{7}{\square\meter} | 709 s | 614 s | $-13\%$ |
| \SI{4}{\square\meter} | 780 s | 715 s | $-8\%$ |
| \SI{2}{\square\meter} | 858 s | 806 s | $-6\%$ |

**The \SI{12000}{\kelvin} column is an extrapolation of the companion's three solved exit
states, not a solve.** The expansion has only ever been run from a \SI{10000}{\kelvin}
chamber. That is N14, and it is cheap: the same `make walled-nozzle-freeze` at a different
chamber temperature.

**And \SI{15000}{\kelvin} is not the prize `CONTEXT.md` has been calling it.** The chamber
arithmetic keeps improving, $k$ falling to \num{16.36} and the bill to 62.5\%, but the
\SI{7}{\square\meter} exit lands near \SI{8400}{\kelvin}, where essentially nothing has
recombined. That is roughly \SI{435}{\second}, not a near-tie with the magnetic nozzle.

**What is binding is how cold the gas gets before it leaves, not how hot it started**, and the
throat sets that at no cost in wall temperature. Narrow the throat, do not raise the chamber.

**And going cooler is better, which is the same finding read the other way. The claim that it
is worse does not survive either.** Written here yesterday: "\SI{8000}{\kelvin} costs 6 to 12\%
and does not get the exit-temperature refund, because a cooler chamber has less energy to begin
with." The second half is wrong. The exit temperature is a fixed **fraction** of the chamber
temperature, so a cooler chamber gets the refund in exactly the same proportion a hotter one
pays the penalty.

At \SI{8000}{\kelvin} the slug grows from \SI{489}{\kilo\gram} to 608 and $u$ falls from 136.8
to \SI{111}{\mega\joule\per\kilogram}. **But the tear-apart bill's share barely moves**, 74.2\%
to 74.6\%, because the charged store and $u$ fall together. Meanwhile the
\SI{7}{\square\meter} exit falls from \SI{5501}{\kelvin} to 4401, where the store held drops
from 69.0\% to 58.4\%. Net: **\SI{817}{\second} against \SI{722}{\second}, a gain of 13\%**,
where the withdrawn convention booked an 8\% penalty.

| chamber | $k$ | slug | exit $T$ | store held | effective Isp | wall load |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \SI{8000}{\kelvin} | 24.33 | \SI{608}{\kilo\gram} | 4401 K | 58.4\% | **817 s** | **0.41$\times$** |
| \SI{9000}{\kelvin} | 21.65 | \SI{541}{\kilo\gram} | 4951 K | 63.7\% | 778 s | 0.66$\times$ |
| \SI{10000}{\kelvin} | 19.56 | \SI{489}{\kilo\gram} | 5501 K | 69.0\% | 722 s | 1.00$\times$ |
| \SI{12000}{\kelvin} | 17.77 | \SI{444}{\kilo\gram} | 6601 K | 79.6\% | 579 s | 2.07$\times$ |

**A cooler chamber is the only lever in this decision that pays on the exhaust and the wall at
the same time.** Escaping flux goes as $T^4$, so \SI{8000}{\kelvin} hands the wall 41\% of the
load \SI{10000}{\kelvin} does, and the liner loses \SI{1.3}{\micro\meter} per pulse rather than
3.2. Every other lever here trades one against the other. **That is what makes the narrow
throat of N15 affordable**, because the throat's problem is wall and throat heat flux and a
cooler chamber is what pays for it.

**Two ways to reach the same exit temperature, and they cost different currencies.** Cooling to
\SI{8000}{\kelvin} at the \SI{7}{\square\meter} throat and staying at \SI{10000}{\kelvin} with a
\SI{2.3}{\square\meter} throat both land the exit near \SI{4450}{\kelvin}. The first costs
\SI{119}{\kilo\gram} more slug per pulse. The second costs three times the pulse length and
three times the throat flux. **They compose**, and the combination is what N14 and N15 should be
run together to price.

**Where the floor is has not been established.** The companion's chamber solve stops at
\SI{8000}{\kelvin}, and W1 flags that row as its softest, with the \ce{C3} exposure at 3.4 to
9.9\% against 0.1 to 1.2\% at \SI{10000}{\kelvin}, erring toward understating the charge. So
\SI{8000}{\kelvin} is probably better than the table says, and nothing here shows where cooling
stops helping. That is the first half of N14, and it is now the interesting half.
Present it as a family of working fluids ordered by one number, and name **methane**
as the fluid we would fly.

The precedent is Rubbia's thin-film \ce{^{242m}Am} fission-fragment-heated rocket,
Project 242, which heats hydrogen to the same temperature continuously
\cite{augelli2013project242}.

## The number that orders the family

A walled nozzle's exhaust speed is $w/\sqrt{1+k}$, and the slug ratio $k$ is set by
how much energy a kilogram of working fluid can hold at the temperature the wall
survives. Call that the **wall-cap energy density**. At \SI{10000}{\kelvin} the
companion's solve runs hydrogen \SI{320.8}{\mega\joule\per\kilogram}, methane 136.8,
ammonia 95.2 and water 69.4, against the 338, 143, 98 and 72 estimated here. Helium is
31 and unsolved. Everything else follows from it.

| slug | $k$ | slug/pulse | conversion | $\eta_{\mathrm{jet}}$ | effective Isp | GN\,s per load | vessel | storage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| **methane** | 19.56 | \SI{489}{\kilo\gram} | 0.406 | 0.621 | **709 s** | **0.696** | \SI{8.7}{\tonne} | \SI{422}{\kilogram\per\cubic\meter} at \SI{111}{\kelvin} |
| water alone | 39.55 | \SI{989}{\kilo\gram} | 0.415 | 0.628 | 579 s | 0.568 | \SI{9.2}{\tonne} | ambient |
| ammonia | 28.54 | \SI{714}{\kilo\gram} | *0.410* | *0.624* | *640 s* | *0.628* | \SI{9.5}{\tonne} | \SI{240}{\kelvin}, \SI{10}{\bar} |
| liquid hydrogen | 7.77 | \SI{194}{\kilo\gram} | 0.532 | 0.711 | 1087 s | 0.604 | \SI{11.6}{\tonne} | \SI{20}{\kelvin} |
| (water on the magnetic nozzle) | 8.52 | \SI{213}{\kilo\gram} | -- | *0.775* | 1249 s | 1.225 | \SIrange{17.3}{37.6}{\tonne} | ambient |

$\eta_{\mathrm{jet}}$ is the square root of the conversion fraction the companion solves,
times a walled $\eta_{\mathrm{geom}}$ of \num{0.974}. **The magnetic nozzle's \num{0.775} is
italicised because it is a target rather than a solve**, and that matters when reading the last
two columns against each other.

Scored at a \SI{25}{\kilo\gram} impactor, a \SI{200}{\cubic\meter} chamber,
\SI{10000}{\kelvin} and the ask's own \SI{7}{\square\meter} throat. **Every slug ratio is
the companion's, solved on a nine-species equilibrium equation of state with NIST-JANAF
thermochemistry** (W1, W8). They are outputs rather than inputs, and where this decision had
already stated one they come back close: \num{7.77} against a stated \num{7.99} for hydrogen
and \num{39.55} against \num{37.70} for water, both inside 5\%. **Every
$\eta_{\mathrm{chem}}$ is the companion's too**, being the square root of the energy
conversion fraction it solves per fluid. Effective Isp and the launch ledger are then this
repository's own, from `todos/matched_convention_ladder.py`.

## The two nozzles were never on the same convention, and it flattered the wall

This is the largest correction in the whole return and it was found on the paper side while
applying N12. **Every walled figure this decision has ever printed assumed full
recombination.** `CONTEXT.md`'s assumptions line said so out loud, and the ladder was scored at
$\eta_{\mathrm{geom}} = 0.852$ with nothing else, which is $\eta_{\mathrm{chem}} = 1$.

**The magnetic nozzle row in the same table is not scored that way.** `sec:jet_efficiency`
factors the paper's jet efficiency as
$\eta_{\mathrm{jet}} = \eta_{\mathrm{chem}}\eta_{\mathrm{geom}}$, and the
\SI{1249}{\second} row uses $0.775 = 0.910 \times 0.852$, where \num{0.910} is
`eq:eta_chem` charging water its bond energy at \SI{75}{\kilo\meter\per\second}. So the
paper charges the magnet for its chemistry and this decision charged the wall for none of its
own, and then set the two side by side.

**The companion has now measured what the wall actually returns**, and it is not 1. Through the
flown \SI{7}{\square\meter} throat the methane nozzle converts \num{0.406} of the chamber's
internal energy into directed kinetic energy, so the exhaust runs at $\sqrt{0.406} = 0.637$ of
the loss-free speed this decision was quoting.

**Where the missing 59\% goes, and it is two different things.** At the exit plane the gas
still holds 69.8\% of its atomisation store, and bonds are 74.2\% of the wall's energy budget,
so unrecovered chemistry alone costs $0.742 \times 0.698 = 51.8$ points of $u$. The rest, about
8 points, leaves as heat: the exhaust is still at \SI{5584}{\kelvin} and that never became
directed motion.

**Those two losses live in different factors of the paper's split**, which is the part that is
easy to get wrong. `sec:jet_efficiency` puts unrecovered chemistry in $\eta_{\mathrm{chem}}$ and
**exhaust-speed spread in $\eta_{\mathrm{geom}}$**, alongside divergence, radiative escape and
mass the field fails to grip. The companion's conversion fraction already covers **both**,
because its $u_e$ is the bulk axial speed at a plane where the gas is still hot. Multiplying it
by the magnet's \num{0.852} therefore charges the exhaust heat twice, and a first pass at this
correction did exactly that and reported \SI{571}{\second}.

**What is actually left for a walled $\eta_{\mathrm{geom}}$** is divergence, near \num{0.98} for
a bell, and radiative escape, near \num{0.994} on this decision's own 1.2\%. There is no field
to fail to grip. That gives \num{0.974}, so

$$\eta_{\mathrm{jet}} = \sqrt{0.406} \times 0.974 = \num{0.621},
\qquad \mathrm{Isp}_{\mathrm{eff}} = \SI{709}{\second}.$$

**The wall recombines better than the plume it is compared against and loses anyway**, which is
the result worth carrying out of this. It hands back 30.2\% of its store where
`sec:watering_it_down`'s water plume freezes with 90 to 100\% still held. It loses because
capping the temperature forces $k$ from \num{8.52} to \num{19.56}, and a bigger slug spreads the
same collision energy thinner, \SI{136.8}{\mega\joule\per\kilogram} against 295. That turns
bonds from 18.4\% of the budget into **74.2\%** of it. **The wall wins the argument it was
adopted to win, and the slug it needs in order to win it is what costs the burn.**

**What this does to the decision's headline.** This section has been claiming
\SI{1129}{\second} against the magnetic nozzle's \SI{1249}{\second}, a 10\% gap, described as
the price of a device that exists. **Matched, it is \SI{709}{\second} against 1249, a 43\%
gap**, and the launch ledger is \num{0.696} against \num{1.225}.

**One thing cuts the other way and it is not small.** The \num{0.775} the wall is measured
against is not a solved result. `sec:jet_efficiency` calls it a literature-based performance
target at 147\% of the reflection baseline, and the one three-dimensional pulsed nozzle
simulated under the same definition, Schilling's, returns \num{0.34}. **The wall's \num{0.621}
is computed and the magnet's \num{0.775} is hoped for.** It also sits inside the
\numrange{0.6}{0.7} band Inatomi's solenoid scaling actually returns. The fair sentence is that
the wall delivers about four fifths of what the magnet is *targeting*, on a number that is
solved rather than aimed at. That is a different sentence from the one this decision used to
make and from the one the raw gap suggests, and it is the one the section should carry.

**Ammonia recovers the lead over water that the withdrawn correction took from it**,
because the correction discharged nitrogen's store hardest and the store is not in
fact discharged. Its rung is an estimate rather than a solve, and it is the one row
here that could still move by more than a few percent: there is no `eos_ammonia`, so
its $k$ is assembled from this decision's own \SI{68.9}{\mega\joule\per\kilogram} of
atomisation plus an exact translational term, and its conversion fraction is borrowed
from methane (W7, W8).

Vessel masses are the full-atomisation column restored. Vessel mass runs on $nRT$,
which is set by the sensible energy alone, and with the store charged the particle
count returns to what full atomisation gave. They are approximate to a few percent
and nothing in this decision turns on them.

**Volume is worth 1.2\%, not the 3.4\% the withdrawn correction booked.** Across
\SIrange{200}{673}{\cubic\meter} the solved $k$ moves only from \num{19.56} to \num{18.92},
and the companion's own exit speeds land within 0.3\% of each other at fixed throat, because a
larger chamber charges more of the store and is thinner and returns less of it by the exit
plane. The two effects cancel. N9's geometry choice should therefore be made on thermal and
structural grounds, which is where W3 and W6 land it from two other directions.

## Why methane rather than the hydrogen the precedent points at

Hydrogen wins the exhaust speed and loses the launch. It delivers
\SI{14700}{\newton\second} per kilogram of launched slug against the magnetic
nozzle's 12248, a 20\% gain on the paper's mass-based ledger. Against that, liquid
hydrogen is the first payload in this paper where **volume** binds first. A standard
bay holds about \SI{57}{\tonne} of it where it holds \SI{100}{\tonne} of a dense
fluid, and the Isp advantage only repays that above a burn of about
\SI{22}{\kilo\meter\per\second}. This leg is a few.

**N12 asked whether per-fluid conversion overturns this, and it does not. It widens the
margin.** The ladder used to charge every fluid the same conversion fraction, and the
companion's three solved rungs disprove that: hydrogen converts \num{0.532} of its store where
methane converts \num{0.406}, because hydrogen's banks straight into \ce{H2} and methane's
parks in \ce{C3} at the exit plane (W9). Carried properly, that raises hydrogen's specific
impulse to \SI{1087}{\second} against methane's \SI{709}{\second}, a lead of 53\%. **But the
launch ledger goes the other way**: \num{0.604} against methane's \num{0.696}, so methane wins
by 15\% where the full-recombination ladder had it winning by 32\%.

**Why charging the chemistry helps methane rather than hurting it.** The drift term subtracts a
fixed \SI{75}{\kilo\meter\per\second} of arriving momentum, and per kilogram of slug that is
$w/k$: \SI{9653}{\meter\per\second} against hydrogen's small slug and only
\SI{3834}{\meter\per\second} against methane's large one. Lowering everyone's exhaust speed
makes that fixed penalty a larger share of what is left, and hydrogen carries two and a half
times as much of it. **Hydrogen's advantage is real and its ledger is worse**, which is the same
verdict this section reached on volume, now reached on chemistry as well.

Methane leads ammonia on specific impulse by 16\%, on the launch ledger by 16\%, on
vessel mass by 8\% and on slug mass per pulse by 33\%. That lead was 31\% under the
withdrawn dissociation correction, which discharged ammonia's nitrogen hardest and
therefore flattered methane. Restoring the store restores ammonia to second place,
ahead of water rather than tied with it. Methane is also not toxic, and Starship
already flies it, so its tankage and boil-off management are flown hardware rather
than a new subsystem. Ammonia keeps only the easier storage temperature, and
\SI{111}{\kelvin} against \SI{240}{\kelvin} is not the gap that \SI{20}{\kelvin}
was.

**Ammonia could still close that 16\%, and nothing here rules it out.** Its rung is
assembled rather than solved and it is handed methane's conversion fraction, which W8
argues is the assumption least likely to hold: ammonia's store returns as \ce{N2} and
\ce{H2}, two simple diatomics with no \ce{C3} trap in the way. It draws level with
methane at a conversion of \num{0.601} against methane's solved \num{0.406}, which is
a large ask but not an absurd one, since hydrogen reaches \num{0.532} through the same
geometry. Settling it needs an `eos_ammonia` the companion does not have.

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
for ammonia against \SI{4.15}{} for methane. Both are a few percent. Methane's figure
was \SI{4.66}{} here and the companion returns 4.15, with atomisation
\SI{102.35}{\mega\joule\per\kilogram} against the 103.7 this decision carried. The
gap is the reference state rather than a disagreement: this side used 298 K heats of
formation and the companion uses 0 K, matching its partition functions. State whichever,
but state which. Ammonia's 2.70 has not been rechecked at 0 K.

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
the plume thin. **This is now solved rather than estimated, and it comes back on the
side the decision needs** (W5). Running Bray's criterion station by station down the
expansion on literature $\ce{H} + \ce{H} + M$ coefficients, the Damkoehler number never
falls into the freezing band anywhere in the bore. The flown case, \SI{200}{\cubic\meter}
through a \SI{7}{\square\meter} throat, clears it by **2.16 decades**, against a stated
rate uncertainty of 0.5 decades. So the composition tracks equilibrium all the way out and
**the frozen branch does not apply**. `sec:watering_it_down` finds the water plume freezing
at \SI{0.02}{\kilogram\per\cubic\meter} only because a magnetic nozzle free-expands it.
Bray's sudden-freezing criterion is the mechanism \cite{bray1959recombination}.

The hand estimates this decision carried were both wrong and both erred safe. The
$\times 3400$ for $\ce{H} + \ce{H} + M$ is 3.5 decades, more generous than the best case
the solve finds; the $\times 403$ for $\ce{N} + \ce{N} + M$ is the wrong reaction for a
methane chamber entirely. Two further findings sharpen the same conclusion. **The rate is
extrapolated at the hot end in the conservative direction**: Hurle et al. measured
$\ce{H} + \ce{H} + M$ directly over \SIrange{2500}{7000}{\kelvin} and found it
temperature-independent, roughly $3\times$ faster than the cold evaluations extrapolate,
so every margin quoted is a floor. And **atomic hydrogen is the third body here**, since
W1 puts the charge at 93 to 98\% dissociated, and three independent shock tubes agree
atomic hydrogen stabilises the collision 7 to 67 times better than argon.

**Nitrogen's eight-times-slower is not a settled ratio and should not be carried as
one** (W7). Byron's 1966 shock tube makes nitrogen *faster* than hydrogen at 6000 K;
a 2025 ab initio master equation makes it 12.7 times slower. The two disagree by 1.3
decades, the claimed $8\times$ sits inside that band only near the ab initio end, and
ammonia's whole rung depends on it.

There is a real ceiling, and it is not a freeze. Pushed past the bore as a diagnostic,
the 400 and \SI{673}{\cubic\meter} cases do eventually freeze, at area ratios of 95 to
188 and \SIrange{3300}{3500}{\kelvin}, with about half the store still held. No nozzle
recovers all of it.

The vessel is a filament-wound composite case behind a refractory liner, not steel.
Mass runs as $1.5\,nRT\rho/\sigma$ and does not depend on pressure. The same
\SI{16.9}{\giga\joule} of $nRT$ gives \SI{991}{\tonne} in steel, \SI{125}{\tonne} in
titanium and about \SI{8.7}{\tonne} in carbon overwrap for the methane charge.

## The throat is the largest lever in the section, and N9 has to price it

This decision treated throat area as a chemistry knob, holding density up so
recombination could keep up. **That is the right knob for the wrong reason and it
points the other way** (W6). The chemistry is not what is in short supply: the worst
case anywhere has 0.4 decades of margin and the flown one has 2.16. What limits the
return is that the nozzle does not expand far enough. At an area ratio of 4.04 the gas
leaves at \SIrange{5300}{5600}{\kelvin} still holding 70 to 76\% of its store, not
because it froze but because at \SI{5500}{\kelvin} equilibrium itself still holds the
bonds broken.

The bore is fixed at \SI{28.3}{\square\meter}, so the throat is the only
expansion-ratio knob there is. Narrowing it, scored on this repository's own ledger with
the companion's conversion fractions (`todos/ladder_companion_k.py`):

| throat | $A/A_*$ | conversion | $\eta_{\mathrm{jet}}$ | effective Isp | GN\,s per load | turnovers | sets $k$? | blowdown |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- | ---: |
| \SI{7}{\square\meter} | 4.04 | 0.406 | 0.621 | 709 s | 0.696 | 6.8 | **no** | \SI{8.0}{\milli\second} |
| \SI{4}{\square\meter} | 7.07 | 0.460 | 0.661 | **780 s** | **0.765** | 11.9 | yes | \SI{14.0}{\milli\second} |
| \SI{2}{\square\meter} | 14.14 | 0.523 | 0.704 | **858 s** | **0.841** | 23.8 | yes | \SI{28.0}{\milli\second} |

The magnetic nozzle's target is 1249 s and \num{1.225} for comparison. **Narrowing the throat to
\SI{2}{\square\meter} is worth 21\% and closes about a third of the gap**, from 43\% to 31\%. It
does not pass the magnet, which an earlier reading of this table on the full-recombination
ladder had it doing. What it does do is take the wall to $\eta_{\mathrm{jet}} = \num{0.704}$,
at the top of the \numrange{0.6}{0.7} band Inatomi's solenoid scaling returns.

**Three independent arguments converge on the same recommendation**, which is what makes
it worth acting on. The Isp gain above; W3's turnover count, which fails at
\SI{7}{\square\meter} and passes at 4; and the freeze margin, comfortable at 4 in every
chamber. **Narrow the throat on the small chamber rather than the large one.** At
\SI{2}{\square\meter} the \SI{673}{\cubic\meter} chamber's margin falls to 0.41
decades, below the rate coefficient's own uncertainty, where \SI{200}{\cubic\meter}
still holds 1.33.

**The cost is blowdown time and it is not priced.** Choked mass flow goes as the throat
area, so the pulse stretches from \SI{8}{\milli\second} to 28 as the throat goes 7 to
2. That is $3.5\times$ longer for the wall to absorb the same pulse, while the throat
itself passes the same power through a third of the area. Both are N9 items 1 to 7 and
neither has been run, so **every number in that table is an upper bound on what is
actually collectable**. The \SI{2}{\square\meter} row also exits at
\SIrange{4349}{4561}{\kelvin}, walking into the range where the companion's equation of
state omits condensed carbon and stops being a physical answer.

## Four hotter-chamber options priced and declined, and what they point at

Raised 2026-09-09. All four are declined, and the disproof is the same in every case, which
is why they are recorded together: **what pays is how cold the gas gets before it leaves, and
raising the chamber temperature raises the exit temperature in the same proportion.**

The exit temperature is a fixed fraction of the chamber temperature at fixed area ratio. Fitting
the companion's own four points, including its deep-expansion diagnostic, gives
$T_e/T_c = 0.667\,(A/A_*)^{-0.138}$. It falls very slowly, and blowdown time runs as the area
ratio at a fixed bore. Those two facts settle all four options.

**\SI{25000}{\kelvin}, on the nuclear light bulb precedent, with a sacrificial hydrocarbon film.**
The wall side is closer to workable than expected. Escaping flux goes as $T^4$, so
\SI{87}{\mega\watt\per\square\meter} becomes about 3400, and an \SI{8}{\milli\second} pulse
delivers \SI{27}{\mega\joule\per\square\meter}, which ablates \SI{184}{\micro\meter} of graphite
per pulse against GA-5009's flown \SI{150}{\micro\meter} on a 0.8 to \SI{1.5}{\second} recycle.
That is \SI{54}{\kilo\gram} per pulse, against about \SI{19}{\kilo\gram} for a 10\% mass
allowance, so the proposal is short by a factor of three rather than by an order of magnitude,
and the vaporisation locks up 5.2\% of the pulse. **The nozzle is what fails.** A
\SI{25000}{\kelvin} chamber leaves the \SI{7}{\square\meter} throat near
\SI{14000}{\kelvin}. Reaching a \SI{3500}{\kelvin} exit from there needs
$A/A_* \approx \num{84000}$, a \SI{3}{\square\centi\meter} throat and a
\SI{167}{\second} blowdown. **A brief flash and a hot chamber are mutually exclusive in a fixed
bore**, because the hotter the chamber the longer the gas must be held in the nozzle to give the
energy back.

**And the light bulb is not the precedent it looks like.** Its wall is transparent fused silica
and runs near \SI{2000}{\kelvin}; the radiation passes *through* it, which is the design's whole
premise. This chamber is optically thick at $\tau = 7$ to 45 and the wall absorbs what reaches
it. The two designs are opposite in the one property that decides the wall load. `CONTEXT.md`
already prefers Rubbia's transpiration-cooled porous carbon--carbon for the film, and this is
why.

**Water at \SI{15000}{\kelvin}, on the hope that it recombines and returns everything.** Its
bond share does fall, from 74.5\% of the budget to 59.7\%, and $k$ from 39.55 to 31.35. But
\ce{H2O} only re-forms below about \SI{4000}{\kelvin}, and a \SI{15000}{\kelvin} chamber leaves
the \SI{7}{\square\meter} throat near \SI{8300}{\kelvin}, where the molecule cannot exist at
all. Nothing recombines, and it returns about \SI{369}{\second}. **A hot chamber forbids exactly
the recombination the proposal assumes.** Water is the fluid that needs a cold exit most, not
least.

**A \SI{10}{\kilo\gram} impactor with a steel vessel.** Vessel mass runs as $nRT\rho/\sigma$, so
the impactor scales $nRT$ and the material ratio is untouched: carbon overwrap goes
\SIrange{8.7}{3.5}{\tonne} and steel goes \SIrange{991}{396}{\tonne}, against a
\SI{100}{\tonne} craft. **Steel is out by two orders of magnitude at any impactor size.** The
chamber itself becomes tidy, \SI{80}{\cubic\meter} at \SI{2.21}{\meter} radius over
\SI{5.23}{\meter} with \SI{103}{\square\meter} of wall, and the film costs
\SI{0.73}{\kilo\gram} per pulse or \SI{181}{\kilo\gram} over a 250-pulse burn. That is cheap and
it is not what was ever binding.

**And \SI{100}{\micro\meter} of graphite is the wrong thickness for a different reason than
ablation.** Against ablation at \SI{10000}{\kelvin} it is ample, 31 pulses' worth at
\SI{3.2}{\micro\meter} each. But heat soaks \SI{146}{\micro\meter} into pyrolytic graphite in
\SI{8}{\milli\second} and \SI{1033}{\micro\meter} in 400, so a film thin enough to spray does
not keep the substrate cold for the length of the pulse. **Film thickness is set by the pulse
length, not by the ablation rate**, and it wants roughly three soak depths.

## The slug does not have to be one fluid, and a water--hydrogen mix beats both ends

Raised 2026-09-10. **The ladder has been treating the working fluid as a choice between
pure substances, and it is a continuous dial.** A water slug carrying a hydrogen fraction was
scored once, at 10\%, and recorded in `CONTEXT.md` at `6faf171` as \SI{987}{\second}. That line
was lost when the ladder was rewritten. It should not have been, because the dial is the most
useful thing in this section.

**Why a small hydrogen fraction moves so much.** Hydrogen is light enough that 10\% of the mass
is half the atoms. Ten percent liquid hydrogen in water gives **\num{3.99} hydrogen atoms per
oxygen against water's 2**, exactly doubling the hydrogen, and drops the mean atomic mass from
\SI{6.005}{amu} to \num{4.015}. Wall-cap energy density rises from 72 to
\SI{98}{\mega\joule\per\kilogram}, so $k$ falls from \num{38.24} to \num{27.61} and the slug from
956 to \SI{690}{\kilo\gram}.

| \ce{H2} by mass | H per O | $\bar{m}$ | $u$ | $k$ | slug | storage | Isp | GN\,s per load |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0\% (water) | 2.00 | 6.005 | 72 | 38.24 | 956 kg | \SI{1000}{\kilogram\per\cubic\meter} | 601 s | 0.589 |
| 10\% | 3.99 | 4.015 | 98 | 27.61 | 690 kg | 432 | 698 s | 0.684 |
| 20\% | 6.47 | 3.015 | 125 | 21.51 | 538 kg | 276 | 776 s | 0.761 |
| 35\% | 11.62 | 2.196 | 165 | 16.06 | 401 kg | 179 | 870 s | 0.853 |
| **55\%** | 23.84 | 1.611 | 218 | 11.89 | 297 kg | **122** | **971 s** | **0.927** |
| 70\% | 43.70 | 1.343 | 258 | 9.90 | 247 kg | 98 | 1034 s | 0.796 |
| (methane) | -- | 3.21 | 137 | 19.56 | 489 kg | 422 | 722 s | 0.696 |
| (pure hydrogen) | -- | 1.008 | 321 | 7.77 | 194 kg | 70.8 | 1087 s | 0.604 |

**The launch ledger has an interior optimum and neither pure fluid is near it.** A
\SI{100}{\tonne} bay is filled by mass above about
\SI{125}{\kilogram\per\cubic\meter} and by volume below it, so the best mix is the lightest one
that still fills the bay by mass. That is near 55\% hydrogen, at \num{0.927} against methane's
\num{0.696} and pure hydrogen's \num{0.604}. **Pure hydrogen loses the ledger to volume and
water loses it to specific impulse, and a mix escapes both.**

**And it is a dial rather than a choice**, which is worth more than the number. The mission can
trade specific impulse against propellant cost leg by leg without changing the hardware, using
whatever hydrogen fraction the logistics of that leg can carry. Nothing else in this decision
has that property.

**The proposal's own physics argument is half right and it matters which half.** Doubling the
hydrogen doubles $\ce{H} + \ce{OH} + M$ and roughly doubles $\ce{OH}$ as well, so the initial
rate goes as about $4\times$. **That is correct and it does not cash**, because W5 established
the walled nozzle is not rate-limited: it carries 2.16 decades of Damkoehler margin and tracks
equilibrium everywhere in the bore. A reaction already at equilibrium does not care that it
could go faster.

**What actually pays is that hydrogen's store comes back through the one channel that works.**
At the flown \SI{7}{\square\meter} exit the gas is near \SI{5500}{\kelvin}, and \ce{H2O} does not
form in quantity above about \SI{4000}{\kelvin}. So **essentially no water re-forms at the flown
exit whatever the hydrogen fraction**, and the mix does not win by combusting better. It wins by
**substituting an easy store for a hard one**: hydrogen's returns through $\ce{H}+\ce{H}+M$,
which W5 has established with margin to spare, where water's needs a temperature this nozzle
does not reach.

**Le Chatelier is the part that has not been priced, and it belongs with N15.** At equilibrium
$[\ce{H2O}]/([\ce{H}]^2[\ce{O}])$ is fixed at a given temperature, so doubling the free hydrogen
does raise the oxygen's conversion to water. That effect is real, it is in none of the numbers
above, and it is worth nothing at a \SI{5500}{\kelvin} exit and a great deal at the
\SI{3200}{\kelvin} exit N15 asks for. **The mix and the deep expansion are complementary**, and
they should be run together.

**One correction to the proposal's premise.** Ten percent of the mass is **61\% of the volume**,
so the cryostat is not small in the sense that matters for boil-off, which scales with surface
area. What is true is that the hydrogen volume per pulse falls from \SI{2.74}{\cubic\meter} to
\SI{0.97}{\cubic\meter} against a pure-hydrogen slug, a genuine factor of \num{2.8}.

## Winning the freeze race, and why it forces a cooler chamber

Raised 2026-09-10. Reaching the temperature where the store actually comes back is a race
against the density that makes coming back possible. Expanding cools the gas, which is what
recombination needs, and thins it, which is what recombination cannot survive. Three-body rates
go as $n^2$, so the second effect wins eventually and Bray's criterion says where.

Calibrated on the companion's two solved \SI{200}{\cubic\meter} points, $Da$ falls as
$\rho_{\mathrm{exit}}^{1.38}$ and the freezing threshold sits at $Da = 10$, which reproduces its
2.16-decade margin at the flown throat.

**Every chamber freezes at about the same area ratio, near 125 to 170, because that is where
the density runs out.** What a cooler chamber buys is being **colder when it gets there**:

| chamber | coldest exit before freezing | $A/A_*$ | throat | blowdown | what has re-formed |
| ---: | ---: | ---: | ---: | ---: | :--- |
| \SI{12000}{\kelvin} | **4112 K** | 125 | \SI{0.23}{\square\meter} | \SI{247}{\milli\second} | nothing; \ce{H2O} has not started |
| \SI{10000}{\kelvin} | 3384 K | 137 | \SI{0.21}{\square\meter} | \SI{270}{\milli\second} | \ce{H2O} forming, partial |
| \SI{9000}{\kelvin} | 3005 K | 151 | \SI{0.19}{\square\meter} | \SI{298}{\milli\second} | \ce{H2O} essentially complete |
| \SI{8000}{\kelvin} | **2630 K** | 168 | \SI{0.17}{\square\meter} | \SI{333}{\milli\second} | past complete |

**That is a threshold, not a trend.** \ce{H2O} does not form above about \SI{4000}{\kelvin} and
completes near 3000. A \SI{12000}{\kelvin} chamber freezes at 4112, before the window opens, so
no nozzle recovers its water at all. A chamber at \SI{9000}{\kelvin} or below reaches the window
with room. **The chamber temperature does not merely trade against the exit temperature. It
decides whether the exit can reach the chemistry at all.**

**Cooling wins the race three separate ways at once**, which is why it is decisive rather than
incremental. A cooler chamber starts denser, because it needs a bigger slug to absorb the same
pulse, \SIrange{2.57}{3.17}{\kilogram\per\cubic\meter} from 10,000 to \SI{8000}{\kelvin}. It
reaches any given exit temperature at a far smaller area ratio, because the exit is a fixed
fraction of the chamber, so it thins out much less on the way, $A/A_*$ of 21 against 107 for a
\SI{3500}{\kelvin} exit. And the shorter expansion is a shorter pulse. At a
\SI{3500}{\kelvin} exit that is $Da = 175$ from \SI{8000}{\kelvin} against 14 from
\SI{10000}{\kelvin}, a factor of twelve.

**Two further levers, both already evidenced, and one of them is free.** $Da$ is linear in
nozzle length (the companion's weakness 5), so a bell twice as long doubles it. And W5's
third-body find says atomic hydrogen stabilises the collision 7 to 67 times better than argon.
**A water--hydrogen slug supplies that third body by construction**, so the mix bought for the
launch ledger helps the race as well, for a reason that has nothing to do with the fuel value of
the hydrogen. Taking a conservative $3\times$ on the third body and a nozzle twice as long turns
the marginal \SI{10000}{\kelvin} case from $Da = 14$ into 84.

**Every row above fits inside the pulse period.** The \SI{8}{\milli\second} pulse at 2\% duty
gives \SI{400}{\milli\second}, and the slowest of these is 333.

**What it is worth, and this is an estimate rather than a result.** Methane at
\SI{8000}{\kelvin} expanded to a \SI{2630}{\kelvin} exit would hold about 11\% of its store, for
roughly \SI{1150}{\second} and \num{1.13} on the launch ledger, against the magnetic nozzle's
target of 1249 and \num{1.225}. **That would be a near-tie, and it is the first configuration in
this decision that reaches one.**

**Three things make it an estimate.** The $Da$ fit is calibrated on two points and extrapolated
thirty-fold in area ratio. The companion's equation of state omits condensed carbon below about
\SI{4000}{\kelvin}, and every row in the table above is under it. And that omission bites
**methane specifically**, because the cold end is exactly where its carbon wants to condense.
**Water has no condensed phase to worry about at \SI{2630}{\kelvin}**, so the fluid choice may
reverse at the cold end, which is one more reason to run N14, N15 and the mix together rather
than separately.

## No, a longer nozzle does not let water catch methane, and the reason is the useful part

Asked 2026-09-10. **It does not, and the lever is the wrong one twice over.**

Water's store splits by stoichiometry alone, no rates needed. \ce{H2O} costs
\SI{917}{\kilo\joule\per\mole} to atomise; forming \ce{H2} from the two hydrogens returns
47.1\% of that, forming $\tfrac{1}{2}\ce{O2}$ from the oxygen returns 27.2\%, and
$\ce{H2} + \tfrac{1}{2}\ce{O2} \rightarrow \ce{H2O}$ returns the last 26.0\%. **Reaching only
the diatomics returns 74\%**, which is water's analogue of W9's acetylene split, and the last
quarter is ordinary gas-phase combustion rather than anything exotic.

**Water starts with a free head start on the freeze race and it is not enough.** Because it
needs twice the slug, its chamber is twice as dense, \SIrange{2.57}{5.07}{\kilogram\per\cubic\meter},
and $Da$ goes as density$^{1.38}$, so water carries $2.6\times$ methane's margin for nothing.
It can therefore expand to $A/A_* = 269$ where methane freezes at 137, reaching a
\SI{3082}{\kelvin} exit against methane's 3384.

**And that is exactly why the longer nozzle is wasted on it.** Water is essentially fully
recombined by about \SI{3100}{\kelvin}, and its freeze limit is 3082. **The two coincide**, so
lengthening the nozzle moves the freeze limit down into a temperature range where there is no
store left to collect. Methane freezes at \SI{3384}{\kelvin} still holding about 13\%, so the
extra length is worth something to methane and nothing to water. **The lever helps the fluid
that looks like it needs it least.**

| at its own freeze limit | exit | store held | effective Isp |
| :--- | ---: | ---: | ---: |
| methane | 3384 K | 13\% | **1250 s** |
| water, diatomics only | 3082 K | 26\% | 884 s |
| water, combustion complete | 3082 K | 10\% | **961 s** |

**What water is short of is energy density, and no nozzle touches it.** A kilogram of water
holds 51\% of what a kilogram of methane holds at \SI{10000}{\kelvin}, so it needs
$2.0\times$ the slug, 989 against \SI{489}{\kilo\gram}. Effective Isp is charged per kilogram of
slug the vehicle carried, so that ratio **is** the gap. Recombination was never what water was
short of, and fixing recombination perfectly still leaves 23\%.

**The fix is the hydrogen dial rather than the nozzle.** Adding hydrogen attacks the energy
density directly, which is the actual shortfall, and it supplies atomic hydrogen as the best
available third body at the same time.

**One caveat cuts against every water row above and it has not been modelled.** The deep
expansion that makes the gas cold also makes it thin, and low density favours dissociation at
equilibrium. Water at \SI{3000}{\kelvin} is about 5\% dissociated at \SI{1}{\bar} and
considerably more at the millibar exit pressures these area ratios imply. **The "combustion
complete" row may not be reachable at any nozzle length**, for a reason that is equilibrium
rather than kinetics, and that is the first thing a real solve has to answer.

## Correction: the cold-end numbers were read off a table computed at the wrong density

Found 2026-09-10 while pricing a higher-pressure chamber. **Every cold-exit figure produced
here before this section used W9's equilibrium speciation, which the companion computed at
\SI{1}{\kilogram\per\cubic\meter}.** The exhaust at a deep expansion is two orders of magnitude
thinner than that, and **low density favours dissociation at equilibrium**, so those figures
were optimistic.

Calibrating against the companion's three solved exit states instead gives

$$\mathrm{held}(T, \rho) = \mathrm{held}_{\mathrm{W9}}(T)\,\rho^{-0.21}$$

which reproduces all three to within 4\%. Applied to the \SI{200}{\cubic\meter} chamber:

| $A/A_*$ | exit $T$ | exit $\rho$ | held, as read | held, corrected | Isp as printed | **Isp corrected** |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4.04 | 5501 K | 0.191 | 49.8\% | 70.5\% | 899 s | **707 s** |
| 14.1 | 4628 K | 0.055 | 32.6\% | 60.0\% | 1077 s | **853 s** |
| 50 | 3887 K | 0.015 | 19.2\% | 46.1\% | 1205 s | **1005 s** |
| 200 | 3211 K | 0.0039 | 12.9\% | 41.4\% | 1251 s | **1046 s** |

**N15's headline of \SI{1156}{\second} becomes about \SI{1074}{\second}.** The corrected model
also reproduces the companion's own flown case at \SI{707}{\second} against the
\SI{709}{\second} already carried, which is the check that it is calibrated rather than fitted.
The cold end is still the best configuration in this decision. It is not as free as it looked.

## Raising the chamber pressure is the fix, and it is free on vessel mass

**The correction above and this section are the same physics.** What re-dissociates the exhaust
is its density, so the answer is to arrive at the cold end denser.

**Chamber density is set by volume, and volume is free.** Vessel mass runs as $nRT\rho/\sigma$
and $nRT$ is fixed by the pulse, so trading volume for pressure does not change it. A
\SI{100}{\cubic\meter} chamber at \SI{1284}{\bar} weighs what a \SI{200}{\cubic\meter} one at
642 does. **That is the whole reason this lever exists**, and it is already in this decision's
own vessel paragraph without having been used.

**At a fixed exit temperature, halving the volume doubles the exit density.** At the
\SI{3211}{\kelvin} exit of $A/A_* = 200$, going from 200 to \SI{50}{\cubic\meter} takes the store
held from 41.4\% to 31.0\% and the impulse from 1046 to \SI{1124}{\second}. **And it cuts the
blowdown from \SI{396}{\milli\second} to 99**, which matters more, because blowdown against the
\SI{400}{\milli\second} pulse period is what caps the area ratio in the first place.

**Pushed to each volume's own freeze limit**, the exit density is pinned at
\SI{0.0056}{\kilogram\per\cubic\meter} by definition, so what a smaller chamber buys there is a
*colder* exit at the same density rather than a denser one:

| volume | length | $p_c$ | $A/A_*$ | throat | exit $T$ | held | effective Isp |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 400 m³ | 14.1 m | 321 bar | 68 | \SI{0.42}{\square\meter} | 3724 K | 50.9\% | 971 s |
| 200 m³ | 7.1 m | 642 bar | 137 | \SI{0.21}{\square\meter} | 3384 K | 40.9\% | 1050 s |
| **100 m³** | **3.5 m** | **1284 bar** | 273 | \SI{0.10}{\square\meter} | 3076 K | 36.2\% | **1086 s** |
| 50 m³ | 1.8 m | 2568 bar | 546 | \SI{0.05}{\square\meter} | 2795 K | 34.3\% | 1100 s |
| 25 m³ | 0.9 m | 5136 bar | 1092 | \SI{0.03}{\square\meter} | 2540 K | 33.4\% | 1107 s |

**It works and it saturates.** The density exponent is $-0.21$, which is weak, so a
sixteen-fold pressure rise is worth 14\% and most of that comes in the first halving. Take
\SI{100}{\cubic\meter} and stop; \SI{1086}{\second} against the magnetic nozzle's target of
1249, on a vessel that weighs the same and a chamber a third the length.

**Two things fall out that are worth more than the impulse.** The blowdown at
\SI{100}{\cubic\meter} is half what it was, so the deep expansion fits inside the pulse period
with room. And the column becomes \SI{3.5}{\meter} long, where this decision has the spreading
cone reaching a \SI{3}{\meter} wall only after \SI{6}{\meter} of column. **Below about
\SI{170}{\cubic\meter} the front leaves before it touches the wall at all**, which would retire
N9 items 1 to 3 rather than answer them. That is the single largest open item in this decision
and a short chamber may simply delete it.

**What it costs, and N9 has to price all of it.** The wall area falls with the column, so the
same pulse lands on less of it. The throat becomes \SI{0.10}{\square\meter}, which is N9 item 5's
problem raised by another factor of two. And \SI{1284}{\bar} is a real containment pressure even
if the vessel mass does not feel it, with a liner that has to survive it. **The volume dial
should be swept alongside the throat rather than fixed at 200 to 673 as this decision has it.**

## At the cold end water is within 10\% of methane, and at a large chamber it wins

Asked 2026-09-10, and it changes what the fluid choice is about.

**Each fluid has a ceiling that no chemistry, pressure or nozzle can beat**, because it is fixed
by the slug ratio and the slug ratio is fixed by energy density in the chamber. Perfect
recombination with nothing left hot gives **methane \SI{1336}{\second} and water
\SI{1006}{\second}**.

**Water essentially reaches its ceiling at any cold exit. Methane does not.** Water's remaining
store is $\ce{H2} + \tfrac{1}{2}\ce{O2} \rightarrow \ce{H2O}$, ordinary gas-phase combustion
that finishes by about \SI{3100}{\kelvin}. Methane's is stuck behind the \ce{C3} to acetylene
path and then soot. So as the chamber shrinks and the exit gets colder, **methane keeps climbing
and water is already done**:

| volume | $p_c$ | methane exit | methane Isp | water exit | water Isp | gap |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 400 m³ | 321 bar | 3724 K | 971 s | 3528 K | **984 s** | **water wins, +1.3\%** |
| 200 m³ | 642 bar | 3384 K | 1050 s | 3206 K | 990 s | $-5.7\%$ |
| 100 m³ | 1284 bar | 3076 K | 1086 s | 2914 K | 995 s | $-8.4\%$ |
| 50 m³ | 2568 bar | 2795 K | 1100 s | 2648 K | 999 s | $-9.2\%$ |

Both store above \SI{125}{\kilogram\per\cubic\meter}, so both fill a \SI{100}{\tonne} bay by
mass and the launch ledger tracks these one for one.

**This decision picked methane on a 31\% lead that no longer exists.** At the cold end the gap is
5 to 9\%, and it reverses at \SI{400}{\cubic\meter}. **The fluid choice is now a liner argument
rather than an impulse argument**, and that is a different question from the one this decision
answered.

**What water gains beyond the number.** Ambient storage against methane's \SI{111}{\kelvin}, so
no cryogenics at all. A chamber twice as dense at the same volume, worth $2.6\times$ the freeze
margin for nothing. **No condensed-carbon problem**, which matters more than it sounds: ADR-0050's
equation of state cannot speak below \SI{4000}{\kelvin} and every row in the table above is under
it, but that limitation is *methane's*. And no throat carbon deposition, which is N9 item 5
entire.

**What water loses, and it is the reason this decision chose methane in the first place.** The
liner. Methane's exhaust carries \SI{376}{\kilo\gram} of carbon past a liner losing 1.26 to
\SI{13.9}{\kilo\gram}, so 0.34 to 3.7\% redeposition makes it self-healing, and a water exhaust
carries nothing that could rebuild it. Worse, `sec:watering_it_down` already picks pyrolytic
graphite for a water plume **and then hedges it against oxygen**. A water chamber has to solve
liner chemistry that a methane chamber solves for free.

**So the recommendation is not to reopen the fluid choice yet, but to stop resting it on
specific impulse.** N16 should report both fluids on the same grid, and the decision should then
be made on the liner, on storage, and on which equation of state can actually speak at the
temperatures the design wants to run at.

**One caveat on water's column.** Its recombination model here is a paper-side construction, 5\%
dissociated at \SI{1}{\bar} and \SI{3000}{\kelvin} scaled as $p^{-1/3}$, not a solve. Pushing the
store held from 3\% to 15\% would cost water \SI{53}{\second}, which does not change the
conclusion but does change the margin.

## Carbon in the bulk slug does not rebuild the liner, and a fuel-rich wall film does

Asked 2026-09-10: can a water slug carry a little methane so its carbon rebuilds the liner?
**No, and the reason is stoichiometry rather than kinetics.**

**The oxygen outnumbers the carbon eight to one.** A 90/10 water/methane slug has
$\mathrm{C/O} = 0.12$. Soot needs $\mathrm{C/O}$ comfortably above 1, and reaching even 1 takes
**47\% methane by mass**, at which point it is a methane slug with water in it.

**And carbon prefers oxygen even without the surplus.** $\ce{C + O -> CO}$ releases
\SI{1077}{\kilo\joule\per\mole} against \SI{966}{} for $\ce{C + O -> C(s)} + \tfrac{1}{2}\ce{O2}$,
so CO wins by 111 even at $\mathrm{C/O} = 1$. **Every carbon atom leaves as CO and the liner gets
nothing.**

**But CO is a gain, which inverts the proposal.** The CO bond is among the strongest in
chemistry, \SI{1077}{\kilo\joule\per\mole} against \ce{H2}'s 432, so it re-forms early and stays
formed where \ce{H2O} needs the exhaust below \SI{4000}{\kelvin} and soot needs nucleation nobody
can model. `tab:seed_carrier` already says as much about \ce{CO2} in the paper. So adding methane
to water hands the carbon an easy high-temperature bond:

| methane in a water slug | $u$ | $k$ | slug | ceiling Isp | at a cold exit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0\% | 69.4 | 39.55 | 989 kg | 1006 s | 990 s |
| 10\% | 78.6 | 34.77 | 869 kg | 1061 s | **~1035 s** |
| 20\% | 85.6 | 31.86 | 797 kg | 1100 s | -- |

**So a little methane in water is a small impulse improvement wearing a liner argument's
clothes.** It is worth about $+4.5\%$ over pure water and it does nothing whatever for the wall.

**The liner fix is a fuel-rich wall film, and that is ordinary engine practice.** Oxidiser-rich
staged-combustion engines keep the boundary layer fuel-rich precisely so the wall survives a bulk
flow that would eat it. This decision already retains film injection as a shield for the shocked
front and as a convective coolant; making it a hydrocarbon and keeping it locally fuel-rich makes
it the carbon source as well. The budget is already there: the stated film of 0.02 to
\SI{0.2}{\kilogram\per\square\meter} over \SI{134}{\square\meter} is 2.7 to
\SI{27}{\kilo\gram} per pulse, against a liner losing 1.26 to \SI{13.9}{\kilo\gram}.

**And the film is doing something more important than resupply.** `sec:watering_it_down` picks
pyrolytic graphite for a water plume **and then hedges it against oxygen**, so an oxygen-bearing
chamber does not merely fail to rebuild a carbon liner, it actively attacks one. Tungsten is no
escape, since its oxides are volatile. **A fuel-rich boundary layer is the answer to both**, and
it is the same answer real engines already use.

## Does that put water on top? It removes the reason methane was on top

**The liner was methane's argument, and the film retires it for both fluids.** If the wall needs
a sprayed hydrocarbon film either way, then methane's exhaust carbon stops being a free service
and becomes a duplicate of something the design is already doing.

What is left of the comparison, at the cold end this decision is now heading toward:

| | pure water | water + 10\% methane | pure methane |
| --- | ---: | ---: | ---: |
| 400 m³ | 984 s | **~1030 s** | 971 s |
| 200 m³ | 990 s | ~1035 s | **1050 s** |
| 100 m³ | 995 s | ~1040 s | **1086 s** |
| storage | ambient | ambient plus a small \SI{111}{\kelvin} tank | \SI{111}{\kelvin} |
| throat carbon (N9 item 5) | none | small | **the whole item** |
| EOS below \SI{4000}{\kelvin} | fine | mostly fine | **cannot speak** |
| liner | needs a fuel-rich film | needs a fuel-rich film | needs a fuel-rich film |

**Methane's remaining lead is 4 to 6\% of impulse at the small chambers, and it reverses at
400 m³.** Against that, water is stored at ambient, has no throat-carbon item, and can actually
be modelled at the temperatures the design wants to run at, which methane cannot.

**This decision should therefore stop naming methane as the flown fluid and name the question
instead.** It is now: is 4 to 6\% of impulse worth a cryogenic tank, a throat-deposition item and
an equation of state that goes blind exactly where the design is heading? **That is a reasonable
question with a defensible answer either way, and it is not the question this decision answered
when it picked methane on a 31\% lead.** N16 should settle it by running both fluids on the same
grid.

## Reference: both Isp conventions, and the slug ratio behind every number

**Every Isp in this decision is EFFECTIVE**, meaning impulse per kilogram of *launched slug*.
The impactor arrives from outside at \SI{75}{\kilo\meter\per\second} and the vehicle never
lifted it, so it is not charged:

$$\mathrm{Isp}_{\mathrm{eff}} = \frac{(1+k)\,u_e - w}{k\,g_0},
\qquad \mathrm{Isp}_{\mathrm{true}} = \frac{u_e}{g_0}.$$

The companion reports **true**. Setting one beside the other is the error W5 records and it is
easy to make, so the table carries both.

| | $k$ | slug | conv | $\eta_{\mathrm{jet}}$ | $u_e$ | true Isp | **effective Isp** | drift charge |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **flown \SI{7}{\square\meter} throat, companion-solved** ||||||||
| methane | 19.56 | 489 kg | 40.6\% | 0.621 | 10265 | 1047 s | **709 s** | 391 s |
| water | 39.55 | 989 kg | 41.5\% | 0.627 | 7390 | 754 s | **579 s** | 193 s |
| hydrogen | 7.77 | 194 kg | 53.2\% | 0.710 | 17992 | 1835 s | **1086 s** | 984 s |
| **cold end, \SI{200}{\cubic\meter} at its freeze limit, estimated** ||||||||
| methane | 19.56 | 489 kg | 69.7\% | 0.813 | 13445 | 1371 s | **1050 s** | 391 s |
| water | 39.55 | 989 kg | 97.4\% | 0.961 | 11321 | 1154 s | **990 s** | 193 s |
| water + 10\% \ce{CH4} | 35.95 | 899 kg | 98.1\% | 0.965 | 11905 | 1214 s | **1035 s** | 213 s |
| **ceilings, perfect recombination** ||||||||
| methane | 19.56 | 489 kg | 100\% | 0.974 | 16110 | 1643 s | **1336 s** | 391 s |
| water | 39.55 | 989 kg | 100\% | 0.974 | 11472 | 1170 s | **1006 s** | 193 s |
| water + 10\% \ce{CH4} | 35.95 | 899 kg | 100\% | 0.974 | 12017 | 1225 s | **1047 s** | 213 s |
| **for comparison** ||||||||
| water, magnetic nozzle | 8.52 | 213 kg | -- | *0.775* | 18838 | 1921 s | **1249 s** | 898 s |

**The drift column is the part worth reading.** It is $w/(k g_0)$, the arriving momentum that has
to be cancelled, charged per kilogram of slug. It is \SI{391}{\second} against methane and only
\SI{193}{\second} against water, because water carries twice the slug to spread it over. **That
is why water's true and effective columns sit closer together than methane's**, and why a fluid
that wins on true Isp can lose on effective, which is what happens to hydrogen.

$(1+k)/k$ is the free-impactor bonus and it is already inside every effective number: $+5.1\%$
for methane, $+2.5\%$ for water. It is a decomposition, not an addition.

**One inconsistency this table exposes and settles.** Water's ceiling was quoted at
\SI{1020}{\second} in one place and \SI{1006}{\second} in another. The first uses the paper-side
full-atomisation $k = 38.24$ and the second the companion's solved $k = 39.55$. **The solved one
is right**, and every water row in the cold-end tables already used it.

## Layering the pre-charge to break up the arrival shock: same physics either way, and second-order

Raised 2026-09-10, with the question of whether a mix of gases would do it or whether density
layers of one gas would serve. **Density layers of one gas serve, and the two are the same
mechanism.**

What a shock feels crossing an interface is acoustic impedance $Z = \rho c$. Different gases at
the same pressure and temperature give $\rho \propto M$ and $c \propto 1/\sqrt{M}$, so
$Z \propto \sqrt{M}$. The same gas at different densities and the same pressure gives
$c \propto \sqrt{T} \propto \sqrt{1/\rho}$, so $Z \propto \sqrt{\rho}$. **Identical scaling.** A
second fluid buys nothing a density gradient does not, and costs a tank, a feed system and an
entry on the propellant ladder.

**But the mechanism is weaker than it looks for this shock.** Impedance mismatch reflects
strongly for a *sound* wave. A strong shock's jump conditions are set by its pressure ratio,
which here is enormous, so a modest density step mostly transmits. What layering actually
produces is Richtmyer--Meshkov instability: the interface goes unstable, deposits vorticity, and
**broadens** the front rather than reflecting it.

**Broadening is still the right goal**, because ablation depth follows the fluence a surface
takes while it is above its sublimation point, so spreading the same energy over a longer arrival
lowers the peak. The energy is not destroyed, only rescheduled.

**It costs impulse, and that part is computable.** Thrust goes as $\sum m_i \sqrt{u_i}$ at fixed
$\sum m_i u_i$, and the square root is concave, so any non-uniformity in specific energy loses:
0.5\% at a 1.5:1 density ratio, **1.4\% at 2:1**, 5\% at 4:1. Cheap, but a real cost against a
benefit nobody has computed.

**And it fights W3, which is what the walled chamber rests on.** The sealed-vessel result is that
the chamber turns over enough times during blowdown that $k$ is set by what was loaded rather
than by what the cone swept. Deliberate stratification is the opposite of that, and the outcome
is a timescale question: if the layers survive to the throat the exhaust is non-uniform and the
cost above is real, and if they do not survive they are gone before the shock reaches the wall
either.

**One version of the idea is not second-order, and the sign is what separates them.** Uniform
layering is about breaking coherence. A gradient that is **dense at the wall and thin on the
axis** is a different mechanism: it puts mass between the shock and the liner, absorbing arrival
energy in its own heat capacity. That is the injected film extended from a surface coating into
the gas, and this decision already keeps the film "as a shield for the shocked front and as a
convective coolant." **That is where the effort belongs if the wall strike survives N9.**

**And it may not survive N9 at all.** ADR-0016 has the spreading cone reaching a
\SI{3}{\meter} wall after \SI{6}{\meter} of column. A \SI{100}{\cubic\meter} chamber is
\SI{3.5}{\meter} long. **Below about \SI{170}{\cubic\meter} the front leaves before it touches
the wall**, so there is no strike to mitigate. Shortening the column deletes the problem where
layering only softens it, and the short column is already recommended for three other reasons.

**Parked rather than pursued**, and noted on N9 items 1 to 3 so the companion prices the strike
before anyone designs a mitigation for it.

## Hydrogen as a dial on any base slug, priced at 5\% and 10\%

Asked 2026-09-10. Effective Isp throughout, at the flown \SI{7}{\square\meter} throat with the
companion's own conversion fractions, plus the perfect-recombination ceiling, which needs no
chemistry model at all.

| base slug | \ce{H2} | $k$ | slug | $u$ | storage | **flown** | ceiling | GN\,s | gain |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **pure methane** | 0\% | 19.57 | 489 kg | 136.7 | 422 | **709 s** | 1335 s | 0.695 | -- |
| | 5\% | 18.23 | 456 kg | 146.2 | 338 | 738 s | 1372 s | 0.724 | $+4.0\%$ |
| | 10\% | 17.06 | 426 kg | 155.7 | 282 | **765 s** | 1407 s | **0.750** | $+7.8\%$ |
| **pure water** | 0\% | 39.54 | 989 kg | 69.4 | 1000 | **579 s** | 1006 s | 0.568 | -- |
| | 5\% | 33.19 | 830 kg | 82.3 | 604 | 630 s | 1082 s | 0.617 | $+8.7\%$ |
| | 10\% | 28.56 | 714 kg | 95.2 | 432 | **674 s** | 1150 s | 0.661 | $+16.4\%$ |
| **90\% water / 10\% methane** | 0\% | 35.95 | 899 kg | 76.1 | 880 | **597 s** | 1047 s | 0.585 | -- |
| | 5\% | 30.72 | 768 kg | 88.7 | 560 | 644 s | 1117 s | 0.631 | $+7.9\%$ |
| | 10\% | 26.79 | 670 kg | 101.2 | 411 | **686 s** | 1180 s | 0.672 | $+14.9\%$ |

**Hydrogen is not the stronger lever.** Switching water to methane is worth $+22.4\%$ against
10\% hydrogen's $+16.4\%$ on the same base. **What hydrogen has that the fluid switch does not is
that it works on every base**, so it stacks rather than competes.

**Its leverage runs inversely to the base fluid's energy density**, which is the rule worth
carrying: $+16.4\%$ on water at \SI{69}{\mega\joule\per\kilogram} and only $+7.8\%$ on methane
at 137. Hydrogen is a bigger relative addition to a weaker store. **So the two levers are
substitutes rather than complements, and hydrogen is most valuable exactly where the base fluid
is worst.**

**It is close to linear over this range**, 4.0\% then 7.8\% on methane, 8.7\% then 16.4\% on
water, so there is no knee to find between 0 and 10\% and the dial behaves as a dial.

**Best on the table is methane with 10\% hydrogen**, \SI{765}{\second} and \num{0.750} on the
launch ledger. Water with 10\% hydrogen reaches \num{0.661}, which is 95\% of plain methane's
ledger while storing at \SI{432}{\kilogram\per\cubic\meter}, the same density as methane, and
without a methane tank.

**The cryogenic bill is the thing to weigh it against.** Ten percent hydrogen is 43 to
\SI{71}{\kilo\gram} per pulse depending on the base, or 0.6 to \SI{1.0}{\cubic\meter} of liquid
hydrogen, against a pure-hydrogen slug's 194 kg and \SI{2.74}{\cubic\meter}. **Five percent is
half the cryogenics for a little over half the gain**, which is the trade a mission would
actually tune.

## The configuration this decision should now propose, and what N16 has to confirm

Assembled 2026-09-10 from everything above. **A \SI{100}{\cubic\meter} chamber at
\SI{1284}{\bar}, expanded to its own freeze limit near a \SI{3100}{\kelvin} exit, with a
fuel-rich methane wall film for the liner** (2.7 to \SI{27}{\kilo\gram} per pulse, off the
propellant ladder). Scored on that geometry, effective Isp:

| bulk slug | $k$ | slug | storage | held | effective Isp | GN\,s | bay fills by |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| water | 39.54 | 989 kg | 1000 | 2.5\% | 995 s | 0.976 | mass |
| water + 5\% \ce{H2} | 33.19 | 830 kg | 604 | 2.5\% | 1070 s | 1.049 | mass |
| **water + 10\% \ce{H2}** | 28.56 | 714 kg | 432 | 2.5\% | **1138 s** | **1.116** | mass |
| methane | 19.57 | 489 kg | 422 | 36.2\% | 1085 s | 1.064 | mass |
| **methane + 10\% \ce{H2}** | 17.06 | 426 kg | 282 | 32.8\% | **1174 s** | **1.151** | mass |
| pure hydrogen | 7.60 | 190 kg | 71 | 2.0\% | 1851 s | 1.028 | **volume** |
| *(magnetic nozzle target)* | 8.52 | 213 kg | -- | -- | *1249 s* | *1.225* | mass |

**The cold end compresses the fluid differences, which is the finding that matters.** Everything
recombines by \SI{3100}{\kelvin} except methane's carbon, which is stuck at 36\% held because
$\ce{C3} \rightarrow \ce{C2H2}$ is unfinished and soot needs nucleation. **Water goes from 40\%
behind methane at the flown throat to 8\% behind it here**, and with 10\% hydrogen it passes
plain methane outright.

**So the recommended configuration is: \SI{100}{\cubic\meter}, a \SI{0.1}{\square\meter} throat,
90\% water with 10\% liquid hydrogen in the bulk, and a methane wall film.** \SI{1138}{\second}
and \num{1.116}, against methane-plus-hydrogen's 1174 and \num{1.151}. **The remaining 3\% is
smaller than every unresolved item in this decision**, and it buys ambient bulk storage, no
throat-carbon item, and an equation of state that can speak below \SI{4000}{\kelvin} where
methane's cannot.

**Pure hydrogen wins specific impulse by 56\% and still loses the launch ledger**, because a
\SI{100}{\tonne} bay holds only \SI{57}{\tonne} of it. That is this decision's original finding
and the cold end does not change it. **Hydrogen is worth paying for only if the mission is
delta-v limited rather than launch-mass limited**, which is the same \SI{22}{\kilo\meter\per\second}
threshold argument above and this leg is a few.

**Nothing here passes the magnetic nozzle's \num{1.225}**, but that number is a performance
target rather than a solve, and the only three-dimensional simulation under the same definition
returns \num{0.34}. On solved-against-solved the walled option is ahead.

**What N16 has to confirm before any of this is written into the paper.** Three paper-side fits
are stacked under every row: `held(T, rho)`, `T_e/T_c` against area ratio, and `Da` against exit
density. The 10\% hydrogen rows additionally run 2\% high on `u`. And the whole table sits below
\SI{4000}{\kelvin}, where ADR-0050's equation of state does not claim to work. **The
configuration is a proposal to be priced, not a result.**

## The cold end is where the unclaimed impulse is

The same fit that kills all four options above points hard the other way, and this is the
largest number found anywhere in this decision.

The companion's deep-expansion diagnostic says the \SI{200}{\cubic\meter} chamber **does not
freeze out to $A/A_* = 400$**, being the densest. W9's equilibrium speciation says a methane
exhaust that reaches \SIrange{3000}{3500}{\kelvin} holds only 12 to 14\% of its store, against
the 69.8\% it holds at the flown \SI{7}{\square\meter} exit. So the acetylene energy W9 says is
sitting on the table is reachable by expanding further, at no cost in wall temperature:

| $A/A_*$ | throat | exit $T$ | store held | effective Isp | blowdown |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4.04 | \SI{7.0}{\square\meter} | 5501 K | 70\% | 590 s | \SI{8}{\milli\second} |
| 14.1 | \SI{2.0}{\square\meter} | 4628 K | 60\% | 726 s | \SI{28}{\milli\second} |
| 50 | \SI{0.57}{\square\meter} | 3887 K | 35\% | 971 s | \SI{99}{\milli\second} |
| 100 | \SI{0.28}{\square\meter} | 3533 K | 20\% | 1097 s | \SI{198}{\milli\second} |
| **200** | **\SI{0.14}{\square\meter}** | **3211 K** | **13\%** | **1156 s** | **\SI{396}{\milli\second}** |
| 400 | \SI{0.07}{\square\meter} | 2918 K | 12\% | 1171 s | \SI{792}{\milli\second} |

**The \SI{8}{\milli\second} pulse at 2\% duty gives a \SI{400}{\milli\second} period, and that
caps the area ratio near 200.** At that cap the walled nozzle returns about
\SI{1156}{\second} against the magnetic nozzle's \SI{1249}{\second} target, which is the first
version of this decision in which the two are close.

**Three things stand between this and a result, and all three are N9's.** The throat is
\SI{0.14}{\square\meter}, passing the same power through 50 times less area than the
\SI{7}{\square\meter} baseline, which makes throat carbon and throat heat the whole problem
rather than a footnote. The film has to hold heat off the substrate for \SI{400}{\milli\second}
rather than 8, which wants millimetres rather than microns. And the companion's equation of
state omits condensed carbon below about \SI{4000}{\kelvin}, so every row under
\SI{3900}{\kelvin} is outside what it can currently answer. **The Isp column is what the
chemistry allows, not what the hardware permits**, and it is recorded here as a target for N15
rather than as a number this decision carries.

## What this deliberately does not do

The section is self-contained. One sentence goes into `sec:minimum_nozzle` pointing
at a non-magnetic option on the head-on leg, and nothing existing is re-scored.

Two re-scorings were considered and declined. The methane vessel's
\SI{8.7}{\tonne} against the magnet's \SIrange{17.3}{37.6}{\tonne} of structure plus
conductor would move `sec:minimum_nozzle`'s finding that the nozzle is 8 to 38\% of a
\SI{100}{\tonne} craft. Rerunning the growth chain at \SI{709}{\second} would say
whether the thermal nozzle passes the chain's binding launch-and-return budget. Both are
companion-repo work, and the second one is now the one that decides whether this section exists.

**The wall clears `tab:mass_interest_growth`'s growth threshold, but not by much.** Its
$\eta_{\mathrm{jet}}$ is \num{0.621} at the flown throat and \num{0.704} at
\SI{2}{\square\meter}. Forward thrust needs only $1/\sqrt{1+k} = \num{0.220}$ here, which it
clears easily. Net growth is the harder test: that table loses mass at
$\eta_{\mathrm{geom}} = 0.50$, where the flown chemistry puts $\eta_{\mathrm{jet}}$ near
\num{0.46}, and grows at \num{0.60}, where it is near \num{0.55}. **The wall sits above that
crossing at both throats**, which is the first version of this decision in which that can be
said from solved numbers rather than assumed ones. It still cannot be read off the table
directly, because the table is scored at $k = 8.52$ on water with a pusher plate on the growth
push, and the impulse law depends on $k$. Rerunning the chain at \SI{709}{\second} and
$k = 19.56$ is what turns "above the threshold" into a growth multiple, and it belongs to
`aim_is_all_you_need` rather than to the impact simulation.

## Chamber and film

The chamber keeps the paper's \SI{3}{\meter} bore and shortens the column. Methane
carries \SI{489}{\kilo\gram} per pulse at \SI{200}{\cubic\meter} and 478 at 400,
against ammonia's 714, so the charge is \SI{514}{\kilo\gram}. At
\SI{200}{\cubic\meter} over \SI{7.1}{\meter} the optical depth is 45, the wall
takes \SI{0.42}{\mega\joule\per\square\meter} per pulse, and the sprayed carbon
film stays at \SI{3.2}{\micro\meter}. The full \SI{23.8}{\meter} column gives 7.3,
\SI{2.29}{\mega\joule\per\square\meter} and \SI{17.5}{\micro\meter}.

**Pressure is confirmed and the pre-charge was quoted without its volume.** The
companion returns \SI{642}{\bar} at \SI{200}{\cubic\meter} against the 636 here and
\SI{190}{\bar} at 673 against the 206 the ask carried, neither of which the vessel mass
feels. The \SI{1.4}{\bar} pre-charge belongs to the \SI{200}{\cubic\meter} chamber
alone: the same methane mass sits at \SI{0.70}{\bar} in 400 and \SI{0.41}{\bar} in 673
at \SI{111}{\kelvin}. At all three the bag, the membrane and the atomiser disappear.

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
chamber unswept propellant is still in the chamber and equilibrates during the
blowdown. **N9 item 0 has come back and it dissolves the geometry question rather
than answering it** (W3). The number of column turnovers is $V / (L A_* f)$ and
$V = \pi r^2 L$ at a fixed bore, so the length divides out exactly and the count is
$A_{\mathrm{bore}} / (f A_*)$. It is a **throat** question, not a length question, and
the short column is admissible on exactly the same terms as the long one.

**Two of this decision's inputs were wrong and the verdict is conditional.** The
\SI{11}{\kilo\meter\per\second} sound speed is atomic hydrogen's; dissociated methane
at \SI{10000}{\kelvin} averages 3.33 amu per particle, so the real figure is
\SIrange{6.0}{6.3}{\kilo\meter\per\second} (W4). The count is linear in it, and
"some fifty times" is in fact 23.8 turnovers at a \SI{2}{\square\meter} throat, 11.9 at
4 and **6.8 at 7, which fails the tenfold criterion**. So the sealed vessel sets $k$ only
for throats of about \SI{4}{\square\meter} or narrower. At \SI{7}{\square\meter} the
chamber empties before it has equilibrated and $k$ goes back to being set by what the cone
sweeps, which is the coupling problem the walled chamber was adopted to escape.

**And the sealed vessel does not soften the arrival transient**, which is the part N9
items 1 to 3 turn on. The impactor crosses the column at \SI{75}{\kilo\meter\per\second}
against a \SI{6}{\kilo\meter\per\second} sound speed, so it completes 0.08 of one
acoustic crossing while it is inside. Equilibration happens over the blowdown, long
afterwards. Those items stand exactly as posed.

Film injection is retained as a shield for the shocked front and as a convective
coolant. It is **not** a radiation shield, and the section must not claim it is. The
chamber's own optical depth already does that work, and a film thin enough to inject
sits near an optical depth of 0.03. With methane the between-pulse spray may be
unnecessary, since the exhaust carries \SI{376}{\kilo\gram} of carbon past a liner
that loses \SIrange{1.26}{13.9}{\kilo\gram}.

## What stays open

Two questions arrive with methane and neither existed for ammonia.

**Does carbon condensation complete?** This was booked as the section's largest single
chemical exposure, worth 43\% of methane's atomisation, on the grounds that soot forms
by nucleation and so gets none of the density help the rest of this decision rests on.
**W9 shrinks it by a factor of six and changes what it is a question about.** The
stoichiometry needs no rate constant: $\ce{2 CH4 -> C2H2 + 3 H2}$ returns **89.0\%** of
full atomisation, against 52.6\% for the \ce{H2} channel alone and 95.9\% for \ce{H2}
plus fully condensed carbon. So 84\% of the carbon store comes back in the **gas phase**
before any particle forms, and only 16\% of it, **7 points of atomisation or 5.2\% of
the energy budget**, is genuinely hostage to nucleation. The two-phase lag exposure
shrinks with it, because carbon leaving as \ce{C2H2} is gas and stays momentum-coupled.
**The \SI{880}{\second} floor was therefore far too pessimistic** and should not be
quoted; what replaces it has not been computed.

**But the flown geometry collects almost none of that acetylene energy.** At the exit
plane the expansion parks 66 to 82\% of the carbon in \ce{C3}, which is better than free
atoms and a long way from done. From there to acetylene equilibrium is **59 points of
atomisation**; from acetylene to fully condensed carbon is **7**. The dominant missing
energy is unfinished gas-phase recombination, and it is unfinished because the nozzle
stopped 1000 to \SI{1500}{\kelvin} too hot. **This is W6's throat argument arriving from
the carbon side**, and it is the second of the three converging reasons to narrow the
throat.

What is left open is the kinetics rather than the thermodynamics. The companion's
Damkoehler work prices $\ce{H} + \ce{H} + M$ only, so nothing yet shows the
$\ce{C -> C3 -> C2H2}$ path keeps up during the expansion. That is ordinary combustion
kinetics rather than nucleation theory, and it is worth 59 points against soot's 7, so
it is now the top priority on this rung. Two warnings travel with it. \ce{C3} is the
companion's least trustworthy species, treated as a harmonic rotor-oscillator when its
bend is quasilinear, and it is the one now carrying most of the carbon through the range
that decides the answer. And the evaluated literature holds one measurement of
$\ce{C} + \ce{C} + M$ and nothing at all for $\ce{C} + \ce{H} + M$, so the remaining 7
points cannot be settled by a rate coefficient the way the \ce{H2} channel just was.

**And does carbon deposit in the throat?** A drifting throat area is the one dimension a
nozzle cannot tolerate. The throat is the hottest and fastest station so it should
clean itself, but nothing here shows that. It stays with N9, and W6 raises its priority,
because the recommendation that follows from every other result is to make the throat
smaller.

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
arithmetic says otherwise. **That tension is now settled rather than argued** (W2). The
companion solved equilibrium hydrogen at \SI{10000}{\kelvin} on the same frame and both
its columns are ceilings on a perfect nozzle, everything converted and nothing left in
the exhaust, which is what makes the comparison decisive in one direction:

| $p$ | Isp equilibrium | **Isp frozen** | store return \SI{2700}{\second} needs |
| ---: | ---: | ---: | ---: |
| \SI{1}{\bar} | 3070 s | **2229 s** | 0.52 |
| \SI{10}{\bar} | 2992 s | **2122 s** | 0.63 |
| \SI{100}{\bar} | 2959 s | **2085 s** | 0.67 |

**\SI{2700}{\second} is 24 to 29\% above the frozen ceiling at every pressure in "a few
bar".** No nozzle reaches it without recombination, and it sits comfortably inside the
equilibrium ceiling near \SI{3000}{\second}, so the number is not absurd either. It
requires 52 to 63\% of the held dissociation store to return, which brackets the
\SI{67}{\percent} this decision estimated. The supporting figures here are right in
shape and 5 to 10\% low: \SI{206}{\mega\joule\per\kilogram} for sensible-only
hydrogen against a solved 217 to 239, and 421 for full recovery against 421 to 453. The
\SI{351}{\mega\joule\per\kilogram} that \SI{2700}{\second} demands is exact. Their
thrust and jet power close exactly, so the number is the one they flew.

**This matters more than a validation.** This decision rests its whole case on running
139 times Rubbia's number density. That argument needs Rubbia's own case to have
recombination in it, otherwise the density scaling starts from zero. It does.

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

## The companion's return, item by item

Answered at `puffsat_impact_simulation` `6d74d3f`, numbers computed at `4a448c0`, both
2026-09-09. The full document is `docs/walled_nozzle_answers_from_impact_sim.md`.

| item | verdict | what moved here |
| --- | --- | --- |
| **N10.4b**, chamber dissociation | **Reverses the premise.** Hydrogen is 93 to 98\% dissociated at \SI{10000}{\kelvin}, not 49 to 76. The store is 95 to 99\% charged | the 2026-09-09 correction is withdrawn; \SIrange{1120}{1133}{\second} before the convention fix below |
| **N10**, Project 242 | **Settles the tension.** \SI{2700}{\second} is 24 to 29\% above the frozen ceiling of \SIrange{2085}{2229}{\second} | the arithmetic-over-prose reading is now a result |
| **N9.0**, sealed vessel | **The geometry question dissolves.** Column length cancels; the verdict is a bore-to-throat area ratio, and it fails at \SI{7}{\square\meter} | the fifty turnovers and the \SI{11}{\kilo\meter\per\second} sound speed are both gone |
| **N10.1-3**, freeze stations | **The fork closes on the good side.** Damkoehler stays above threshold everywhere, 2.16 decades of margin at the flown point | the frozen \SI{793}{\second} branch does not apply |
| **N10.3**, the ladder | **Answered for water and hydrogen, ammonia unplaced.** The stated $k$ come back as outputs within 5\% | ladder re-scored on solved $k$; ammonia back above water |
| **N10.5**, carbon | **Reframed and six times smaller.** 84\% of the carbon store returns as gas-phase acetylene | the \SI{880}{\second} floor is withdrawn |
| **N9.1-7**, the load case | **Not started**, and W6 raises their priority | the section still cannot be written |
| **N11**, radiative escape | **Not started** | nothing |

**N12 is answered on the paper side rather than sent.** Per-fluid conversion does not overturn
the fluid choice: it widens methane's launch-ledger lead over hydrogen from 32\% to 15--22\%,
because the head-on drift term subtracts a fixed $w/k$ that bites hardest on the smallest slug.
What it did expose is the convention mismatch above, which is much larger than N12 itself was.

**One correction was found while applying it, and it resolves an inconsistency the
companion flagged.** W1 scaled specific impulse by $\sqrt{1+k}/k$ and got two answers
that disagreed by 3\%, depending on which of this decision's rows it anchored on, and
said so. The reason is that the effective-Isp column is not proportional to
$\sqrt{1+k}/k$: it is $w(\eta\sqrt{1+k} - 1)/k$, and the $-1$ is the drift term of
`eq:reflection_baseline`, which subtracts a velocity rather than scaling one. Applying
the formula itself to the companion's solved $k$ gives \SI{1120}{\second} at
\SI{200}{\cubic\meter}, 1129 at 400 and 1133 at 673, between the two anchored rows.
Those are the numbers this decision now carries. `todos/ladder_companion_k.py`
reproduces them and reproduces both of W1's rows alongside, so the three can be told
apart.

**What the answer does not license.** A charge is not a return. The store being 95 to
99\% charged is a ceiling on what recombination could hand back, and W5 puts the actual
return at 22.6 to 26.2\% through the flown \SI{7}{\square\meter} throat. The two numbers
answer different questions and the section must not use one for the other.

## What is still owed before the section can be drafted

**N9 items 1 to 7 are the whole of it.** They are the load case, and the companion's
return makes them more binding rather than less: W4 confirms the sealed vessel does not
soften the arrival transient, and W6's recommendation to narrow the throat stretches the
pulse from \SI{8}{\milli\second} to 28 and passes the same power through a third of the
throat area. Until they return, the section would have to state a chamber whose wall
loading is unpriced at the geometry every other result recommends.

Three items go back with them.

- **N13, the walled nozzle's own $\eta_{\mathrm{geom}}$.** Now a small item rather than a large
  one, because the companion's conversion fraction turned out to carry the exhaust-speed spread
  already. What is left is divergence and radiative escape, taken here as \num{0.98} and
  \num{0.994} from a bell nozzle and this decision's own 1.2\%. Worth about 30 seconds if both
  are wrong by a realistic amount, so it can wait behind N9. **What should be asked instead is
  the exit-plane velocity distribution**, since a quasi-1D solve cannot produce a divergence
  factor at all.
- **The acetylene kinetics.** Worth 59 points of atomisation against soot's 7, and it is
  ordinary combustion kinetics rather than nucleation theory.
- **An `eos_ammonia`.** Ammonia is the only rung that is assembled rather than solved,
  and it is second on the ladder rather than fourth.
