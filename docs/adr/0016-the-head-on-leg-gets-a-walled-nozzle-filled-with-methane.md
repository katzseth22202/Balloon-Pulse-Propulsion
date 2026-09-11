# The head-on leg gets a walled nozzle, and methane fills it

Status: **proposed**. Resolved in a grill session on 2026-09-08, amended
2026-09-09 when the flown fluid changed from ammonia to methane, amended again
the same day when the companion returned N9 item 0 and all of N10, and amended
2026-09-10 when it returned N9 items 1 to 7 and the whole of N16. Terms are
recorded in `CONTEXT.md` under **Wall-cap energy density**, **The slug ladder** and
**Density is what saves every fluid on the ladder**.

**The companion has now answered everything this decision asked except N11 and
N13.** Two answer documents are carried verbatim, both from
`puffsat_impact_simulation` at `1ffd367`:
`docs/walled_nozzle_answers_from_impact_sim.md` for W1 to W9 and
`docs/walled_nozzle_grid_answers_from_impact_sim.md` for W10 to W24. Every number
below that changed is marked with the finding that moved it.

**The section can now be drafted.** N9 items 1 to 7 were the load case and were
the stated gate, and they have come back. What remains open is the Stanton
number, which decides \SI{100}{\cubic\meter} against \SI{150}{\cubic\meter} and
nothing else, so the section can carry both rather than wait.

**Five of this decision's positions reversed on the second return, and they are
recorded in place rather than edited out.** The chamber runs hotter rather than
cooler (W17). Water loses to methane in all 128 grid cells rather than tying at
the cold end (W21). The water-plus-hydrogen configuration loses to plain methane
(W22). The \SI{2000}{\kelvin} exit is the wrong target rather than an expensive
one (W20). And the throat plates nothing back, so it is a consumable rather than
self-healing (W15). **The two largest reversals share one cause**, which is that
both priced what the exhaust returns without pricing what the chamber charged.

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
\SI{12000}{\kelvin} in \SIrange{100}{150}{\cubic\meter} through a
\SI{2}{\square\meter} throat, and book the throat as a consumable with a stated
replacement interval.

**That reverses the chamber temperature this decision has carried since it was
written, and the reversal is the largest correction the companion has sent.**
Every earlier version ran at \SI{10000}{\kelvin} or argued for cooling below it.
The companion's solved grid (W17) says the dial runs the other way, by 56 to
59\%, at every throat. The superseded argument is kept below, because where it
fails is the part worth having.

### What was argued here, and the one term it omitted

The argument ran in two steps and the first step is correct. Exit temperature is
a near-fixed fraction of chamber temperature, which the companion confirms
directly (W20). So a hotter chamber does leave a hotter exhaust, and hotter
exhaust has handed back less of its chemistry. Read on its own that says cool
the chamber, and this decision read it that way, booking \SI{817}{\second} at
\SI{8000}{\kelvin} against \SI{722}{\second} at \SI{10000}{\kelvin}.

**The omitted term is how much store the chamber charges in the first place.**
`todos/cooler_chamber.py` derives the tear-apart bill from an $A + BT$ capacity
and concludes it "barely moves, 74 to 75\% everywhere, because $u$ and the
charged store fall together". That holds only if the methane atomises fully at
every chamber temperature, and it does not. On the companion's own equilibrium
solve at \SI{100}{\cubic\meter}:

| chamber | \SI{6000}{\kelvin} | \SI{8000}{\kelvin} | \SI{10000}{\kelvin} | \SI{12000}{\kelvin} |
| --- | ---: | ---: | ---: | ---: |
| store charged | 0.336 | 0.657 | 0.887 | 0.961 |
| slug ratio $k$ | 45.71 | 27.01 | 20.48 | 18.11 |
| chamber pressure | \SI{1008}{\bar} | \SI{1127}{\bar} | \SI{1284}{\bar} | \SI{1448}{\bar} |

A \SI{6000}{\kelvin} chamber parks two thirds of the store in \ce{C3} and
\ce{C2H2}. That is already the recombined state, so there is nothing left down
there to hand back. A kilogram holds less, more kilograms are needed to absorb
the same \SI{70.3}{\giga\joule}, $k$ rises by two and a half times, and the
exhaust speed $w/\sqrt{1+k}$ falls with it. **The cold chamber is cheap on the
wall and expensive on the ledger, and the ledger term is much the larger.**

The second stale input compounds it. `k_from_ratio` inverts $\sqrt{1+k}/k$
against the companion's W1 ratio table, which was the credit-only column. Both
repositories now charge the head-on momentum debit, so the identity is
$(\sqrt{1+k}-1)/k$, and the inverted $k$ moves with it. The solved
\SI{8000}{\kelvin} slug ratio is \num{27.01} where this decision back-solved
\num{24.33}.

### What the solved grid says

Effective specific impulse, methane at \SI{100}{\cubic\meter}, on the
companion's conventions and carrying none of this paper's launch-ledger
normalisations:

| throat | \SI{6000}{\kelvin} | \SI{8000}{\kelvin} | \SI{10000}{\kelvin} | \SI{12000}{\kelvin} |
| ---: | ---: | ---: | ---: | ---: |
| \SI{7.00}{\square\meter} | 509 s | 637 s | 738 s | 808 s |
| \SI{2.00}{\square\meter} | 625 s | 780 s | 899 s | 976 s |
| \SI{0.50}{\square\meter} | 702 s | 884 s | 1012 s | **1093 s** |
| \SI{0.20}{\square\meter} | 716 s | 903 s | 1040 s | 1124 s |
| \SI{0.10}{\square\meter} | 725 s | 909 s | 1045 s | 1129 s |

**Hotter wins at every throat.** The reversal is not an artefact of the
momentum debit either. On the credit-only convention the same rows read 677 to
1231 and 892 to 1552, so the debit narrows the margin from \num{1.74} to
\num{1.56} and leaves the ranking untouched. The \SI{817}{\second} and
\SI{722}{\second} figures are withdrawn, along with the \SI{579}{\second} at
\SI{12000}{\kelvin} and the whole cooler-chamber table.

### The ceiling is a wall argument, and it should be stated as one

What survives from the old reasoning is the cost. Going hotter does load the
wall, and the companion now prices it (W14). Liner flux rises from
\SIrange{93}{174}{\mega\watt\per\square\meter} at \SI{10}{\kilo\kelvin} to
\SIrange{198}{351}{\mega\watt\per\square\meter} at \SI{15}{\kilo\kelvin}. So the
temperature ceiling is real and it is set by what the liner takes, not by the
gain being too small to chase. **The gain is not small.** This decision
previously declined \SI{12000}{\kelvin} on the grounds that 3.5 to 4.9\% sits
inside the noise in $\eta_{\mathrm{geom}}$. The solved figure is \SI{+8.9}{\percent}
at the ask's throat and \SI{+40.2}{\percent} once the throat moves with it.

\SI{15000}{\kelvin} is still not taken, and now for a stated reason rather than
an assumed one. The companion's grid stops at \SI{12000}{\kelvin}, so a
\SI{15000}{\kelvin} row would be an extrapolation, and W14 puts its liner flux
at roughly twice the \SI{12000}{\kelvin} load. The band worth running next is
\SIrange{12000}{15000}{\kelvin} against the liner, not against the ledger.

### Chamber volume is not free either

This decision has treated volume as costless, on the correct observation that
vessel mass runs as $nRT\rho/\sigma$ with $nRT$ fixed by the pulse. The mass
argument stands. The performance is not flat (W18). Effective Isp for methane
at a \SI{0.5}{\square\meter} throat:

| chamber | \SI{6000}{\kelvin} | \SI{8000}{\kelvin} | \SI{10000}{\kelvin} | \SI{12000}{\kelvin} |
| ---: | ---: | ---: | ---: | ---: |
| \SI{50}{\cubic\meter} | 692 s | 856 s | 995 s | 1091 s |
| \SI{100}{\cubic\meter} | 702 s | 884 s | **1012 s** | **1093 s** |
| \SI{200}{\cubic\meter} | **707 s** | **893 s** | 1008 s | 1081 s |
| \SI{400}{\cubic\meter} | 706 s | 879 s | 971 s | 1039 s |

Two effects cross. A bigger chamber is thinner, so it dissociates more and $k$
falls, which is the same physics as the temperature dial. A thinner chamber also
freezes sooner, because a three-body rate goes as density squared. The optimum
is interior and it moves with temperature, sitting at \SI{200}{\cubic\meter}
cold and \SI{100}{\cubic\meter} hot. At \SI{12000}{\kelvin} the whole column is
flat to within 1\%, so **the \SI{100}{\cubic\meter} recommendation is right, and
right for a reason this decision did not give.** It is only right in company
with a hotter chamber.

**The floor is about \SI{150}{\cubic\meter} and it is set by the contraction**
(W23). Below the \SI{178}{\cubic\meter} gate the front leaves the column without
reaching the side wall, which is what N9 items 1 to 4 turned on, but it does not
leave the hardware. Against a \SIrange{0.05}{1}{\square\meter} throat the
convergent section is 96 to 99\% of the bore area, so a short chamber trades a
grazing side-wall strike for a normal-incidence strike on the contraction. That
load runs the wrong way with shrinking volume. At \SI{50}{\cubic\meter} the
front still carries 42\% of the pulse energy at \SI{31.4}{\kilo\meter\per\second}
onto \SI{4.4}{\square\meter}, giving \SIrange{6.7}{66.7}{\mega\joule\per\square\meter}
against the \SI{1.6}{\mega\joule\per\square\meter} the section clears the wall
against. At \SI{150}{\cubic\meter} it is \SIrange{0.41}{4.14}{\mega\joule\per\square\meter},
a factor of 16 better, and the impulse is flat to \SI{12}{\second} out of 1093
across \SIrange{100}{200}{\cubic\meter}.

**So carry both \SI{100}{\cubic\meter} and \SI{150}{\cubic\meter} and pick on
the wall**, which is the only axis where they differ. \SI{100}{\cubic\meter}
exits at \SI{4061}{\kelvin}, above the condensed-carbon floor, and has
\num{0.36} decades of freeze margin. \SI{150}{\cubic\meter} is \num{2.9} times
softer on the contraction and exits \SI{2}{\kelvin} below that floor, so its
number is a bound rather than a solve.

Present it as a family of working fluids ordered by one number, and name **methane**
as the fluid we would fly.

The precedent is Rubbia's thin-film \ce{^{242m}Am} fission-fragment-heated rocket,
Project 242, which heats hydrogen continuously to \SI{10000}{\kelvin}
\cite{augelli2013project242}. That is now a floor on this chamber rather than the
ceiling this decision took it for, and W2 settles what it does and does not license.
Its \SI{2700}{\second} sits 24 to 29\% above the frozen ceiling of
\SIrange{2085}{2229}{\second}, so the figure requires the recombination its own prose
denies. Read the other way, \SI{2700}{\second} already implies converting 97.5\% of a
\SI{12000}{\kelvin} hydrogen chamber's store, which is this architecture's
full-conversion limit. It is not a target to scale upward from.

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

What decided it in methane's favour beyond the ledger was that **the carbon looked
like the sacrificial layer this design already wants**. The liner loses
\SIrange{1.26}{13.9}{\kilo\gram} per pulse against \SI{376}{\kilo\gram} of carbon in
the exhaust, so \SIrange{0.34}{3.7}{\percent} redeposition would make it self-healing.

**Withdraw that.** N9 item 5 came back and there is nothing to redeposit (W15). The
exhaust is **undersaturated** in carbon at every wall temperature graphite survives,
because the carbon is parked in acetylene rather than travelling as free atoms. The
state that decides whether carbon sticks is the free stream's pressure at the wall's
temperature, and at \SI{623}{\bar} the saturation ratio runs \num{1.00} at
\SI{1912}{\kelvin}, \num{0.21} at \SI{2500}{\kelvin} and \num{0.032} at graphite's
own \SI{3900}{\kelvin} working ceiling. A ratio below one means the gas can dissolve
more carbon than it is carrying. **At the surface temperature this design runs, the
exhaust takes graphite off the wall rather than putting it on**, with thirty-two times
spare capacity.

**The redeposition was not rate-limited. It is thermodynamically absent**, so no amount
of residence time or surface preparation recovers it. The band where nothing plates runs
from \SI{1912}{\kelvin} upward with no upper edge out to \SI{8000}{\kelvin}, and
holding a surface under \SI{1900}{\kelvin} while it takes
\SIrange{400}{2400}{\mega\watt\per\square\meter} means removing almost all of that
load actively. **A self-healing carbon throat and a passively cooled one are mutually
exclusive.**

This turns on the boundary layer being in chemical equilibrium, and it is, with five
decades to spare against a gas-kinetic collision frequency. If the layer were frozen at
the free stream's composition the saturation ratio would be \num{41} instead of
\num{0.032}, so the fork is six orders wide and the margin decides it cleanly.

**What this costs methane is the free-service argument, not the fluid choice.** A water
or ammonia exhaust carries nothing that could rebuild a liner, and it now turns out
neither does methane's. Methane's exhaust is not the spray. The liner and the throat
both need the sprayed film on their own account, and methane keeps its place on the
ledger instead (W21).

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

## The load case came back, and N9 items 1 to 7 close

Answered 2026-09-10 (W10 to W15, W23). These were the whole of what this
decision said was still owed before the section could be drafted. **The premise
they were posed against does not survive, and it fails in the design's favour.**

**The front never reaches the side wall below \SI{178}{\cubic\meter}** (W10).
The gate this decision guessed at \SI{170}{\cubic\meter} is real and the guess
was right to 5\%. On the 1.0, 1.6 and 1.9 times sound-speed spreading bracket
that `sec:needle_through_fog` already uses, the gate runs 178, 109 and
\SI{92}{\cubic\meter}. So the honest statement is that the side wall is safe at
\SI{50}{\cubic\meter}, and safe at \SI{100}{\cubic\meter} unless the front
spreads faster than its own sound speed.

**Where the front does reach the wall it is nowhere near \SI{200000}{\kelvin}**
(W11). That figure is right for the entering front and wrong for the arriving
one. At \SI{75}{\kilo\meter\per\second} into methane the freshly shocked layer
really is at \SIrange{166000}{205000}{\kelvin}. It then decelerates hard,
because the chamber is \SIrange{0.7}{11}{\kilogram\per\cubic\meter} rather than
the magnetic bag's \num{0.32}:

| chamber | contact station | arrival speed | swept | **layer $T$ at contact** |
| ---: | ---: | ---: | ---: | ---: |
| \SI{50}{\cubic\meter} | never, leaves at $r = \SI{1.19}{\meter}$ | | | |
| \SI{100}{\cubic\meter} | never, leaves at $r = \SI{2.02}{\meter}$ | | | |
| \SI{200}{\cubic\meter} | \SI{6.15}{\meter} | \SI{9.2}{\kilo\meter\per\second} | \SI{178}{\kilo\gram} | **\SI{4867}{\kelvin}** |
| \SI{400}{\cubic\meter} | \SI{5.64}{\meter} | \SI{19.2}{\kilo\meter\per\second} | \SI{72.5}{\kilo\gram} | **\SI{17186}{\kelvin}** |
| \SI{673}{\cubic\meter} | \SI{5.57}{\meter} | \SI{28.2}{\kilo\meter\per\second} | \SI{41.5}{\kilo\gram} | **\SI{30726}{\kelvin}** |

In the \SI{200}{\cubic\meter} chamber the front sweeps seven times its own mass
before it touches, so the layer at contact is 37 times cooler than the layer at
entry. **A wall argument made against \SI{200000}{\kelvin} is being made against
a state that never sees the wall.**

**Two corrections inside that.** The spreading cone is \SIrange{28.7}{30.3}{\degree},
not the \SI{24.9}{\degree} this decision carries. The \SI{24.9}{\degree} figure
belongs to water at \SI{45.58}{\kilo\meter\per\second}, and methane at
\SI{75}{\kilo\meter\per\second} opens wider. And the contact station is nearly
independent of chamber volume at \SIrange{5.6}{6.2}{\meter}, because a denser
pre-charge decelerates the front exactly as fast as it shortens the column. This
decision's "6 m of the column" is right, for a reason it did not state.

**The strike is convective, not radiative, and this decision had the wrong
channel worried** (W12). Radiative delivery is
\SIrange{0.001}{0.009}{\mega\joule\per\square\meter} against the
\SI{1.6}{\mega\joule\per\square\meter} the section already clears the wall
against. Convective delivery is \SIrange{0.11}{1.09}{\mega\joule\per\square\meter}
at \SI{200}{\cubic\meter} and \SIrange{8.79}{87.9}{} at \SI{673}{\cubic\meter}.
**The verdict does not depend on the opacity model**, because at the thin end
the blackbody cap settles it and at the thick end more opacity means less
delivery.

**And the convective channel gets worse with a bigger chamber**, since delivery
scales as shocked density times radial speed times specific energy times
duration and every one of those grows as the chamber thins. So the wall argument
and the ledger argument now point the same way, which is the first time in this
decision they have. **Make the chamber small**, subject to the contraction floor
in the Decision above.

**The Bartz estimate is a good liner number and should be labelled one** (W14).
This decision's \SIrange{123}{281}{\mega\watt\per\square\meter} between 10,000
and \SI{18000}{\kelvin} overlaps the solved liner column across 10 to
\SI{15}{\kilo\kelvin}, matching well at \SI{200}{\cubic\meter} and running high
at \SI{673}{\cubic\meter}. So the conclusion that convection is 80 to 90\% of
the wall load, and that it rather than radiation sets the temperature ceiling,
survives.

**What is new is the throat, and it is the binding component.** At the flown
\SI{7}{\square\meter} throat the flux is about three and a half times the
liner's on both heat-capacity edges, \SIrange{328}{610}{\mega\watt\per\square\meter}
against the liner's \SIrange{93}{174}{}, and the surface temperature at
radiative balance is \SIrange{7400}{12100}{\kelvin} against graphite's
\SI{3900}{\kelvin} working ceiling.

The throat ablates at \SI{0.23}{\milli\meter} per pulse at \SI{2}{\square\meter}
and \SI{1.07}{\milli\meter} at \SI{0.5}{\square\meter}. **Those two figures are
at \SI{100}{\cubic\meter} and \SI{8000}{\kelvin}**, at the equilibrium
heat-capacity edge with no transpiration credit, so read them as the pessimistic
end of a factor-of-two band and not as the flown chamber's numbers. That is what
the throat-life table in the throat section above is counting, and W15 says there
is no credit side to set against it.

**Read the size and not the digits.** Bartz was fitted on chemical rockets at
tens of bar and a few thousand kelvin, and is extrapolated here to a thousand
bar and a partly ionised boundary layer. Its frozen and equilibrium heat-capacity
edges differ by a factor of 1.9 to 2.2, which is the honest width of the answer.

**The one number that binds and is not solved is the Stanton number.** The
convective figures above are the stagnation enthalpy the layer brings to the
wall times a Stanton number bracketed over \numrange{0.001}{0.01}, which is the
Reynolds analogy on a turbulent boundary layer. That factor of ten is the
largest single uncertainty in the load case. It decides the
\SI{100}{\cubic\meter} against \SI{150}{\cubic\meter} choice in the Decision,
and closing it needs a boundary-layer solve on the contact geometry.

## The throat is the largest lever in the section, and it is priced in throat life

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

**The cost is dwell, and the companion has now priced it** (W24). This decision
expected the cost to be blowdown time and the throat flux, and only the first
half was right. Bartz gives the throat flux as $D_*^{-0.2}$, so halving the
throat area raises it by about 7\%, which is \SI{610}{\mega\watt\per\square\meter}
at \SI{7}{\square\meter} against 932 at \SI{0.1}{\square\meter}, a factor of
\num{1.5} across a factor of 70 in area. What moves is the blowdown, because the
same chamber empties through a smaller hole. It runs \SI{8}{\milli\second} at
\SI{7}{\square\meter}, \SI{56}{\milli\second} at 1 and \SI{560}{\milli\second}
at \SI{0.1}{\square\meter}, a factor of 70 that matches the area exactly.
Fluence is flux times time, so the dwell carries almost all of the cost.

> **A narrower throat does not heat the throat harder. It heats it for twice as
> long.**

**That converts into a pulse count, because the throat is a consumable** (W15,
below). Recession is radial, so an eroding throat opens, drifting back up the
trade curve it was narrowed to climb:

| throat | $A/A_*$ | conversion | effective Isp | vs \SI{7}{\square\meter} | recession per pulse | pulses to $+10\%$ area |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \SI{7.00}{\square\meter} | 4.0 | 0.406 | 738 s | | \SI{0.04}{\milli\meter} | 1947 |
| \SI{4.00}{\square\meter} | 7.1 | 0.468 | 822 s | $+11.3\%$ | \SI{0.07}{\milli\meter} | 795 |
| **\SI{2.00}{\square\meter}** | 14.1 | 0.532 | **902 s** | $+22.1\%$ | \SI{0.15}{\milli\meter} | **262** |
| **\SI{1.00}{\square\meter}** | 28.3 | 0.585 | **965 s** | $+30.7\%$ | \SI{0.32}{\milli\meter} | **87** |
| \SI{0.50}{\square\meter} | 56.5 | 0.623 | 1008 s | $+36.5\%$ | \SI{0.68}{\milli\meter} | 29 |
| \SI{0.20}{\square\meter} | 141.4 | 0.629 | 1015 s | $+37.5\%$ | \SI{1.87}{\milli\meter} | 7 |
| \SI{0.10}{\square\meter} | 282.7 | 0.633 | 1020 s | $+38.1\%$ | \SI{4.01}{\milli\meter} | 2 |

Methane at \SI{200}{\cubic\meter} and \SI{10000}{\kelvin}, the ask's own point,
so the rows are comparable with the table above. Hydrogen runs the same curve
slightly steeper, 1143 s at \SI{7}{\square\meter} and 1544 at 1.

**The exponent is derived rather than fitted, which is the part to trust.** Flux
goes as $A_*^{-0.1}$ and blowdown as $A_*^{-1}$, so recession goes as
$A_*^{-1.1}$. A fixed fractional area growth needs recession proportional to
$r_* \sim A_*^{0.5}$, so life goes as $A_*^{1.6}$, a factor of \num{3.03} per
halving. The solved columns reproduce that to 2\% across the ladder.

> **The exchange rate: each halving of throat area buys 4 to 10\% effective Isp
> and costs a factor of three in throat life.** The rate worsens as it goes. The
> step from 7 to \SI{2}{\square\meter} pays seven times the life for
> \SI{+22}{\percent}; the step from 1 to \SI{0.5}{\square\meter} pays three times
> for \SI{+4.4}{\percent}.

**Why the curve flattens is in the chemistry, not the geometry** (W19). Raw
conversion climbs all the way to \num{0.748}, but freeze-capped conversion
saturates at \num{0.633}. Past the freeze station the equilibrium branch keeps
releasing chemistry the real flow no longer has time to release. So below about
\SI{0.5}{\square\meter} the extra nozzle delivers nothing, and the chemical wall
sits between 1 and \SI{0.5}{\square\meter} rather than at $A/A_* = 140$ where an
earlier reading put it.

**Take \SI{2}{\square\meter}.** It is worth \SI{+22}{\percent} on methane and
\SI{+25}{\percent} on hydrogen, lasts 262 pulses to $+10\%$ area, stays on the
equilibrium branch, and exits above the condensed-carbon floor.
\SI{1}{\square\meter} buys a third more impulse for three times the erosion, and
is the right answer only if the throat is a scheduled consumable rather than
hard to service. Below \SI{0.5}{\square\meter} the gain is under 1\% per halving.

**This decision's stated cost of narrowing corresponds to \SI{2}{\square\meter}
and no deeper.** The 8 to \SI{28}{\milli\second} pulse stretch quoted above is
exactly the 7 to \SI{2}{\square\meter} step. Nothing in the section has ever
priced a throat narrower than that, and the deep-throat rows elsewhere in this
decision should be read against the 87-pulse and 29-pulse intervals rather than
as free choices.

**So the section must state a throat-replacement interval alongside its throat
area, and at present it states neither.** If the throat cannot be serviced at
all the calculus inverts, because total impulse per throat goes as pulses times
Isp and that falls fifty-fold from 7 to \SI{1}{\square\meter}. That makes the
throat choice an economics one, and the table above is the exchange rate to
price it with.

**Two caveats travel with the millimetres.** Bartz is far outside its
calibration here, having been fitted on chemical rockets at tens of bar and a
few thousand kelvin rather than a thousand bar at ten thousand kelvin with a
partly ionised boundary layer, so read the exponent and not the digits. And the
ablation depth takes no transpiration credit, while a blowing boundary layer
typically halves the net flux at these rates, so every pulse count above is the
pessimistic edge of a factor-of-two band.

The \SI{2}{\square\meter} row's exit at \SIrange{4349}{4561}{\kelvin} still sits
near the range where the companion's equation of state omits condensed carbon.
That has not moved.

## Four hotter-chamber options priced and declined, and what they point at

Raised 2026-09-09. All four are declined, and the disproof is the same in every case, which
is why they are recorded together: **what pays is how cold the gas gets before it leaves, and
raising the chamber temperature raises the exit temperature in the same proportion.**

**The four options stay declined and the disproof no longer generalises** (W17, W20).
The premise above is half right. Exit temperature genuinely is a near-fixed fraction of
chamber temperature, which N16 confirms directly, so the blowdown arithmetic that kills
these four extreme chambers stands untouched. What the premise does not license is the
general rule that a hotter chamber is worse, because it prices only the exhaust and not
the charge. **Between 6,000 and \SI{12000}{\kelvin} hotter wins at every throat**, and
the Decision above now runs at 12,000. What kills \SI{25000}{\kelvin} is that the
nozzle needed to cool it back down does not fit in the pulse period, which is a
different argument and a sound one.

The $T_e/T_c = 0.667\,(A/A_*)^{-0.138}$ fit below is also superseded (W20). The real
slope is not constant, running $-0.189$ near the throat and $-0.080$ far downstream, so
$-0.138$ is a fair average over $A/A_* = 4$ to 140 and a bad local slope at either end.
That does not rescue any of the four, because all four need extrapolation far past 140
where the flow has frozen anyway.

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

### N16 swept the dial, and the mix still loses to plain methane

Answered 2026-09-10 (W22). **The dial is real and it is not enough.** Swept at the
best methane cell, \SI{12000}{\kelvin} and \SI{100}{\cubic\meter} through a
\SI{0.5}{\square\meter} throat:

| \ce{H2} by mass | $k$ | $u$ | effective Isp, upper | min $Da$ |
| ---: | ---: | ---: | ---: | ---: |
| 0\%, pure water | 36.81 | \SI{74.4}{\mega\joule\per\kilogram} | 846 s | 2.89 |
| 5\% | 30.44 | \SI{89.5}{} | 933 s | 1.68 |
| **10\%** | 26.05 | \SI{104.0}{} | **1009 s** | 1.04 |
| 20\% | 20.25 | \SI{132.4}{} | 1140 s | 0.445 |
| 30\% | 16.55 | \SI{160.3}{} | 1251 s | 0.206 |
| *plain methane, same cell* | *18.11* | *\SI{147.2}{}* | *1093 s* | *23* |

**Hydrogen buys energy density and sells freeze margin.** Energy per kilogram
more than doubles across the sweep, which is the whole benefit and is genuine.
But diluting the water slows water's own three-body return, which goes as the
square of water density, so the Damkoehler number falls the whole way.
**Matching methane needs about 15\% hydrogen and passing it about 20\%**, and by
then the bracket is \SI{313}{\second} wide against methane's single hard number
with 23 decades of margin.

**Le Chatelier was the unpriced term and it runs the wrong way for the mix.**
This section flagged it as possibly worth a great deal at a cold exit. It is
still unpriced, because there is no joint hydrogen-oxygen equilibrium equation of
state, and the companion composes the mixture as two independent subsystems at a
common temperature. That is exact for the thermal terms and wrong in one
direction: the free hydrogen does not shift water's own dissociation equilibrium
in the model, and Le Chatelier puts the real mixture's held store **above** the
modelled one. **Every mixture figure is therefore an optimistic edge**, and the
mixture loses anyway, so the verdict is safe in the direction it matters.

**The volume correction above stands and is worth keeping**, since the cryostat
argument is unaffected by any of this.

## Winning the freeze race, and why it does not force a cooler chamber after all

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

### N16 answered it: the race is real, the wall is where this said, and the conclusion still reverses

Answered 2026-09-10 (W18, W19). **The mechanism in this section survives and the
recommendation drawn from it does not.** That combination is worth stating
plainly, because it is the same failure as the temperature dial and it has the
same cause.

**What survives.** There is a chemical wall and it sits near $A/A_* \approx 140$,
which is inside this section's own 125-to-170 estimate. Freeze margin in decades
against the threshold, methane at \SI{8000}{\kelvin}, negative meaning frozen:

| chamber \\ throat | \SI{7.00}{\square\meter} | \SI{2.00}{\square\meter} | \SI{1.00}{\square\meter} | \SI{0.50}{\square\meter} | \SI{0.20}{\square\meter} | \SI{0.10}{\square\meter} |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \SI{50}{\cubic\meter} | 3.48 | 2.10 | 1.37 | 0.64 | $-0.32$ | $-1.05$ |
| \SI{100}{\cubic\meter} | 3.00 | 1.65 | 0.93 | 0.20 | $-0.74$ | $-1.46$ |
| \SI{200}{\cubic\meter} | 2.48 | 1.16 | 0.45 | $-0.27$ | $-1.19$ | $-1.90$ |
| \SI{400}{\cubic\meter} | 0.76 | 0.49 | $-0.05$ | $-0.77$ | $-1.68$ | $-2.37$ |

A thinner chamber does freeze sooner, exactly as this section argued, because a
three-body rate goes as density squared. That is why the \SI{400}{\cubic\meter}
row is a decade worse than the \SI{50}{\cubic\meter} one at every throat.

**What reverses.** This section priced only the exit side of the ledger. It
asked how cold the gas can get before it freezes, found that a cooler chamber
gets colder, and stopped. What it did not price is how much store the chamber
charged before any of that. A \SI{8000}{\kelvin} methane chamber charges
\num{0.657} of full atomisation against \num{0.961} at \SI{12000}{\kelvin}, so
the cooler chamber is running a deeper expansion on a much smaller store. The
solved grid puts \SI{100}{\cubic\meter} at \SI{8000}{\kelvin} through a
\SI{0.5}{\square\meter} throat at \SI{884}{\second}, against
\SI{1093}{\second} at \SI{12000}{\kelvin}.

**So the \SI{1150}{\second} near-tie is withdrawn**, along with the
\SI{2630}{\kelvin} exit it was scored at and the claim that cooling wins the
race three ways at once. Cooling does win the race. It wins a race whose prize
shrank faster than the odds improved.

**The two free levers this section named both stand.** The Damkoehler number is
linear in nozzle length, and atomic hydrogen is a far better third body than
argon. Neither is enough to move the verdict, because the binding term is the
charge rather than the return.

**One thing this section got right and should keep credit for.** It identified
that the chamber temperature decides whether the exit can reach the chemistry at
all, rather than merely trading against it. That is a threshold argument and it
is correct. It points at methane rather than water, because methane's return
channel is $\ce{H} + \ce{H} + \ce{M}$ with both partners the same species, while
the water fluids need a scarce \ce{OH} and freeze four times sooner in area
ratio (W22).

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

**The fit is retired, and it over-corrected at the end that mattered** (W16). N16 computed
`held` directly over a nine-by-eight grid in density and temperature rather than fitting it, and
the exponent turns out not to be a constant and not able to be one. It runs from 0 to $-0.25$
for methane and 0 to $-0.42$ for water, vanishing at both ends, because a fully atomised gas has
nothing left to shift and a fully recombined one has nothing left to break. That is mass action
rather than a fitting artefact, and no single power law reproduces it.

Against the solved surface the $\rho^{-0.21}$ fit is exact at its own anchor and good to
$\pm 10\%$ between 3,500 and \SI{5000}{\kelvin}. **At \SI{3000}{\kelvin} it overstates
`held` by 32 to 44\%**, and that is exactly where the deep expansions this decision was chasing
actually exit. Overstating `held` understates recovery, **so the corrected cold-end numbers are
pessimistic rather than optimistic**, which is the opposite of the direction this correction was
made to guard against. The correction was right to make and it overshot at the cold end.

**Use the solved surface.** It is 72 rows per fluid, carried in this repository at
`docs/walled_nozzle_grid_answers_from_impact_sim.md` and committed in the companion as
`data/results/walled_nozzle/held_surface.csv` with the local exponent alongside. Every figure in
this section and the next is superseded by the grid tables in the Decision above.

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

**The gate is confirmed at \SI{178}{\cubic\meter} and the deletion is real** (W10), so this
paragraph's guess was right to 5\%. **The rest of this section is superseded.** Its throat
column runs to \SI{0.03}{\square\meter}, and the chemistry freezes between 1 and
\SI{0.5}{\square\meter} (W19) while the throat itself lasts two pulses at
\SI{0.1}{\square\meter} (W24). The impulse figures it reads off the retired fit are
superseded by the solved grid. What survives is the lever itself, which is genuine: chamber
volume trades against pressure at constant vessel mass, and a shorter column is what puts the
front outside the wall. It is the deep throats that are gone, not the short chamber.

**What it costs, and N9 has to price all of it.** The wall area falls with the column, so the
same pulse lands on less of it. The throat becomes \SI{0.10}{\square\meter}, which is N9 item 5's
problem raised by another factor of two. And \SI{1284}{\bar} is a real containment pressure even
if the vessel mass does not feel it, with a liner that has to survive it. **The volume dial
should be swept alongside the throat rather than fixed at 200 to 673 as this decision has it.**

## Withdrawn: water is not within 10\% of methane, and it never wins

Asked 2026-09-10 and answered by N16 on 2026-09-10 (W21). **The answer is that
water loses in all 128 cells of the grid**, so the near-tie this section was
built on is withdrawn along with the table that carried it.

Water's effective impulse as a fraction of methane's, both fluids run through
identical machinery at a \SI{2}{\square\meter} throat:

| chamber | \SI{50}{\cubic\meter} | \SI{100}{\cubic\meter} | \SI{200}{\cubic\meter} | \SI{400}{\cubic\meter} |
| ---: | ---: | ---: | ---: | ---: |
| \SI{6000}{\kelvin} | 0.772 | 0.780 | 0.790 | **0.800** |
| \SI{8000}{\kelvin} | 0.798 | 0.800 | 0.797 | 0.763 |
| \SI{10000}{\kelvin} | 0.792 | 0.787 | 0.786 | 0.570 |
| \SI{12000}{\kelvin} | 0.786 | 0.787 | 0.606 | 0.615 |

**The best water ever manages is \num{0.800}**, at \SI{6000}{\kelvin} and
\SI{400}{\cubic\meter}, which is also the worst corner of the grid in absolute
terms. The low cells at large volume are where water freezes and methane has
not. The claim that water reverses the ordering at \SI{400}{\cubic\meter} was an
artefact of the cold-end table below, and that reversal does not appear anywhere
in the solved grid.

**A ratio is quoted deliberately.** Both fluids carry identical conventions, so
every normalisation this paper applies cancels out of the column. The ratio
survives the conventions where an absolute number would not.

**Why water loses, and it is one variable.** Water's mean atomised particle mass
is \SI{6.0}{amu} against methane's \num{3.2}, so a kilogram of water holds fewer
particles and less energy at the same temperature. It needs $k$ of 40 to 50
where methane needs 20 to 27. Both the exhaust speed $w/\sqrt{1+k}$ and the
carried-mass credit $(1+k)/k$ punish that. The head-on momentum debit narrows
the gap by about six points, because water's larger $k$ means a smaller
per-kilogram debit, but it never closes it.

**What this decision got wrong, and where.** The withdrawn table read methane's
cold-end Isp off a paper-side recombination model rather than a solve, and read
water's off a construction that was 5\% dissociated at \SI{1}{\bar} and
\SI{3000}{\kelvin} scaled as $p^{-1/3}$. The construction was flagged as a
caveat at the time. The larger error is the one that was not flagged: the
`held` fit underneath both columns is wrong by 32 to 44\% at \SI{3000}{\kelvin},
which is exactly where those deep expansions exit (W16, below). The ceilings
quoted above, \SI{1336}{\second} for methane and \SI{1006}{\second} for water,
were computed on that fit and are withdrawn with it.

**What survives, and it is the part worth keeping.** Water's argument was never
really impulse, and this section said so in its last paragraph. It stores at
ambient against methane's \SI{111}{\kelvin}. It makes a chamber twice as dense
at the same volume. It has no condensed-carbon problem, which matters because
ADR-0050's equation of state cannot speak below \SI{4000}{\kelvin} and that
limitation is methane's alone. And it puts no carbon through the throat, which
is N9 item 5 entire.

**So the fluid choice is a liner choice, and it should be argued as one rather
than sold as a near-tie on impulse.** The price of choosing water is now known
and it is 26 to 30\% of the impulse, not 5 to 9\%. If the liner or the throat
turns out to decide the design, that may still be the right trade. It is a much
larger bill than this section booked.

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

## Does that put water on top? N16 answered it, and the answer is no

**The liner was methane's argument, and the film retires it for both fluids.** If the wall needs
a sprayed hydrocarbon film either way, then methane's exhaust carbon stops being a free service
and becomes a duplicate of something the design is already doing. **That part stands.** What
does not stand is the impulse table this section used to carry, which had methane's lead at 4 to
6\% and reversing at \SI{400}{\cubic\meter}. It was built on the withdrawn cold-end columns.

**On the solved grid the lead is 20 to 21\% at every chamber the design would fly** (W21), and
the reversal at \SI{400}{\cubic\meter} does not exist. So the question this section posed, and
which it framed as reasonable either way, has an answer:

| | pure water | pure methane |
| --- | ---: | ---: |
| effective Isp, \SI{100}{\cubic\meter} at \SI{12000}{\kelvin} | 0.787 of methane | **1093 s** |
| effective Isp, \SI{200}{\cubic\meter} at \SI{10000}{\kelvin} | 0.786 of methane | 1008 s |
| storage | ambient | \SI{111}{\kelvin} |
| throat carbon (N9 item 5) | none | eroded, not plated (W15) |
| EOS below \SI{4000}{\kelvin} | fine | **cannot speak** |
| liner | needs a fuel-rich film | needs a fuel-rich film |

**Methane stays the named fluid, and now on a solved margin rather than an assumed one.** The
bill for switching to water is 26 to 30\% of the impulse. That is a real question if the liner
turns out to decide the design, and it is no longer the near-tie that made the switch look
close to free.

**One column in that table did move in water's favour, and it is worth stating plainly.** The
condensed-carbon blindness is methane's alone, and most of the grid's interesting rows exit
below \SI{4000}{\kelvin}. The one cell that escapes it is \SI{100}{\cubic\meter} at
\SI{12000}{\kelvin} through a \SI{0.5}{\square\meter} throat, which exits at
\SI{4061}{\kelvin}. That the recommended cell is also the one cell free of the equation of
state's worst weakness is convenient, and it is worth not leaning on.

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

**The companion now charges the same debit, and the two repositories agree.** This
was the one place where the walled-nozzle answers and this decision were on
different conventions, and it was worth 3\% of disagreement between W1's two
anchor rows. The companion's ladder now reports
$w(\eta_{\mathrm{jet}}\sqrt{1+k} - 1)/(k g_0)$, which is the identity above, so
its effective column and this one can finally be set side by side. Its own
head-on expression carried the $-1$ all along. The anchor rows that used to
disagree by \SI{32}{\second} now agree to \SI{11}{\second}, which is inside
their rounding.

**One consequence is worth stating, because it reverses a claim this decision
made about hydrogen.** On the credit-only column hydrogen led methane by
\num{1.88} times. With the debit charged the lead is \num{1.55} times. Hydrogen
collects the largest carried-mass credit and pays the largest momentum debit,
and the debit is the bigger of the two by exactly $w/u_e$. It still wins the
ladder decisively on chemistry. Its margin is smaller than the credit-only
column showed.

**The solved ladder, at the ask's own \SI{7}{\square\meter} throat and
\SI{200}{\cubic\meter}** (W8), with the credit-only column kept alongside so the
two conventions cannot be confused again:

| fluid | $k$ | conv | $u_e$ | true Isp | **effective Isp** | *credit only* |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hydrogen | 7.77 | 0.532 | 18482 | 1885 s | **1143 s** | *2127 s* |
| methane | 19.56 | 0.406 | 10536 | 1074 s | **738 s** | *1129 s* |
| ammonia (estimated) | 28.54 | *0.41* | ~8800 | *~901 s* | *~665 s* | *~933 s* |
| water | 39.55 | 0.415 | 7588 | 774 s | **600 s** | *793 s* |

**The molecular-weight law belongs to the credit-only convention, and it does not
survive the correction.** Credit-only Isp tracks $1/\sqrt{\bar{m}}$ to within
10\% across a factor of six in particle mass. The corrected column is compressed
toward methane, running 1.55, 1.00 and 0.81 for hydrogen, methane and water
against the law's 1.78, 1.00 and 0.73. The reason is that the debit also scales
as $1/k$ and so also falls hardest on the light fluids. **The ordering is
untouched, and only the margins shrink**, which is what the fluid verdict rests
on.

**Two rows below are withdrawn.** The cold-end block and the ceilings block both
rest on the $\rho^{-0.21}$ fit for `held`, which the companion has retired
(W16). The \SI{1336}{\second} methane ceiling and the \SI{1006}{\second} water
ceiling go with it. The flown-throat block is unaffected, because it is the
companion's own solve.

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

## The configuration this decision proposes, after N16 priced the one it proposed first

Assembled 2026-09-10 and **replaced the same day, because N16 ran it and plain
methane beat it** (W22). The withdrawn proposal was \SI{100}{\cubic\meter} at
\SI{1284}{\bar}, a \SI{0.1}{\square\meter} throat, and a bulk slug of 90\% water
with 10\% liquid hydrogen, scored at \SI{1138}{\second}. Three of its four
choices do not survive.

**Priced at its own point**, \SI{100}{\cubic\meter} and \SI{8000}{\kelvin}
through a \SI{0.1}{\square\meter} throat:

| bulk slug | $k$ | $p_c$ | exit $T$ | conversion raw / capped | freezes at $A/A_*$ | effective Isp |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **90\% water + 10\% \ce{H2}** | 34.42 | \SI{1289}{\bar} | \SI{3108}{\kelvin} | 0.763 / 0.610 | 11.2 | **811 to 933 s** |
| water | 50.26 | \SI{1163}{\bar} | \SI{3228}{\kelvin} | 0.703 / 0.596 | 21.3 | 689 to 761 s |
| **plain methane** | 27.01 | \SI{1127}{\bar} | \SI{3109}{\kelvin} | 0.697 / 0.633 | 47.6 | **909 to 968 s** |

All three freeze at this throat, so each is a bracket rather than a number, with
capped conversion at the low end and equilibrium at the high end.

**Three readings, and only the first was this decision's.** The hydrogen
dilution is worth 18 to 23\% over plain water, which is real and is what the
proposal rested on. Plain methane still beats the mixture by 4 to 12\% at both
ends of the bracket. And methane's lead is partly that it freezes latest,
$A/A_*$ of \num{47.6} against \num{11.2}, because its return channel is
$\ce{H} + \ce{H} + \ce{M}$ with both partners the same species while the water
fluids need a scarce \ce{OH}.

**Hydrogen is a bigger dial than 10\%, and it is not enough.** Swept at the best
methane cell, \SI{12000}{\kelvin} and \SI{100}{\cubic\meter} through a
\SI{0.5}{\square\meter} throat, energy density runs from \SI{74.4}{\mega\joule\per\kilogram}
at pure water to \SI{160.3}{\mega\joule\per\kilogram} at 30\% hydrogen. That is
the whole benefit and it is real. But diluting the water slows its own
three-body return, which goes as the square of water density, so the Damkoehler
number falls the whole way. Matching methane on the upper bound needs about 15\%
hydrogen and passing it needs about 20\%, and by then the bracket is
\SI{313}{\second} wide against methane's single hard number.

**The mixture is an estimate and has to be labelled one wherever it is quoted.**
There is no joint hydrogen-oxygen equilibrium equation of state, so it is
composed of `eos_water` and a hydrogen equation of state as two independent
subsystems at a common temperature. That is exact for the thermal terms and
wrong about one thing, in that the free hydrogen does not shift water's own
dissociation equilibrium. Le Chatelier puts the real mixture's held store above
this, so every mixture number is an optimistic edge. The mixture already loses,
so the conclusion is safe in the direction it matters.

**The \SI{0.1}{\square\meter} throat is retired too**, and on three independent
counts. Its blowdown is \SI{560}{\milli\second} against the
\SI{400}{\milli\second} pulse period, so methane does not empty in time. Its
freeze-capped conversion is flat against \SI{0.5}{\square\meter}, so the extra
nozzle delivers under 1\% (W19). And it lasts two pulses to $+10\%$ area (W24).

**The throat is the one choice in this configuration that is not settled, and the
two candidates fail on different axes.** The chemistry optimum is
\SI{0.5}{\square\meter}, which returns \SI{1093}{\second}, keeps \num{0.36}
decades of freeze margin and exits at \SI{4061}{\kelvin}, just above the
condensed-carbon floor. It is the only cell in the grid that is both near-optimal
and free of the equation of state's worst weakness. Against that, W24's
throat-life ladder puts \SI{0.5}{\square\meter} at 29 pulses where
\SI{2}{\square\meter} gets 262, and that ladder was run at
\SI{200}{\cubic\meter}. **This decision takes \SI{2}{\square\meter} because an
unsolved throat life is not a reason to spend one**, and it names running the
ladder at the flown chamber as the way to reopen the question.

**So the configuration this decision now proposes is \SI{100}{\cubic\meter} at
\SI{12000}{\kelvin}, a \SI{2}{\square\meter} throat, plain methane in the bulk,
and a fuel-rich methane wall film.** It returns \SI{976}{\second} effective,
exits at \SI{4892}{\kelvin} with \num{1.73} decades of freeze margin, and
empties in \SI{12.5}{\milli\second}. Taking the throat to
\SI{1}{\square\meter} buys \SI{1040}{\second} and to \SI{0.5}{\square\meter}
\SI{1093}{\second}, the latter still on the equilibrium branch and still above
the condensed-carbon floor at \SI{4061}{\kelvin}.

**The throat-replacement interval at this chamber is not solved, and the section
must not imply otherwise.** The companion's throat ladder was run at
\SI{200}{\cubic\meter} and \SI{10000}{\kelvin}, which is where the 262-pulse
and 87-pulse figures above come from. Two terms move in opposite directions at
\SI{100}{\cubic\meter}, since the chamber empties in half the time, which halves
the fluence, while the pressure doubles, which raises the Bartz flux. **Quote the
\SI{200}{\cubic\meter} intervals as the available anchor and state the chamber
they were measured at**, or run the ladder at the flown chamber. The exchange
rate itself, a factor of three in throat life per halving of throat area, is
derived from the flux and blowdown exponents rather than fitted, so it transfers
where the absolute pulse counts do not.

**What changed under the proposal, in one line each.** The fluid went back to
methane because water loses in all 128 grid cells (W21). The chamber went hotter
because the temperature dial reverses (W17). The throat went from
\SI{0.1}{\square\meter} to \SI{2}{\square\meter} because the chemistry freezes
and the throat erodes (W19, W24). The chamber volume stayed at
\SI{100}{\cubic\meter}, which is the one choice that survived, though for a
reason this decision did not give (W18) and with a floor at
\SI{150}{\cubic\meter} if the contraction load lands at the pessimistic edge of
its Stanton bracket (W23).

**The three paper-side fits stacked under the withdrawn table are all now
retired or replaced.** `held(T, rho)` is replaced by the solved surface (W16),
$T_e/T_c$ against area ratio by the solved curve (W20), and the whole cold-exit
target by W20's finding that the proxy inverts once the flow freezes.

## Withdrawn: a \SI{2000}{\kelvin} exit is the wrong target, not just an expensive one

Asked 2026-09-10, from the flown \SI{10000}{\kelvin} chamber. **It fails both walls and the
prize is half a percent.**

**The chemistry is nearly done, but Carnot is not, and a first pass here missed that.**
The \SI{0.5}{\percent} figure this section first carried zeroed the exhaust's own sensible
enthalpy below \SI{5000}{\kelvin}. The exhaust still carries heat at \SI{2900}{\kelvin} and
cooling further recovers some of it. That is the Carnot term and it is the larger half:

| fluid | exit | store held | heat still in the exhaust | conversion | effective Isp |
| --- | ---: | ---: | ---: | ---: | ---: |
| water | 2914 K | 2.5\% | 7.8\% | 90.4\% | 947 s |
| water | 2000 K | 1.6\% | 5.3\% | 93.5\% | 967 s ($+2.1\%$) |
| hydrogen | 2914 K | 2.0\% | 13.1\% | 85.6\% | 1644 s |
| hydrogen | 2000 K | 1.0\% | 9.0\% | 90.4\% | **1715 s ($+4.4\%$)** |
| methane | 2914 K | 36.2\% | 4.4\% | 68.7\% | 1041 s |
| methane | 2000 K | 34.0\% | 3.0\% | 71.7\% | 1072 s ($+3.0\%$) |

**Why it is still small, and why hydrogen gains most.** Carnot acts on the **sensible** share
only. Water carries 27\% of its budget as heat and 73\% as chemistry; hydrogen 37\% and 63\%.
The chemical store does not care what temperature the expansion stops at, only whether the atoms
have paired up, and they have by \SI{3000}{\kelvin}. **Hydrogen gains twice what water does
precisely because more of its budget is heat**, which is the Carnot intuition arriving exactly
where it should.

**And on how dissociated the water is: quite, and it barely matters in energy.** At the
\SI{2914}{\kelvin} exit and \SI{0.10}{\bar}, **9.5\% of the \ce{H2O} is split**. But that split
only fails the *last* 26\% of the store: \ce{H2} and \ce{O2} are already complete at that
temperature, $D/kT$ being 18 and 21, and they are 74\% of it. So 9.5\% dissociated by mole is
2.5\% of the energy held. **A molar dissociation figure and an energy loss are different
numbers here, and the first is about four times the second.**

**This section first said \SI{2000}{\kelvin} was unreachable and that was wrong.** The claim
rested on $T_e/T_c = 0.667\,(A/A_*)^{-0.138}$, fitted to four companion points spanning
$A/A_* = 4$ to 140 and then extrapolated **forty-four-fold** to 6,200. That exponent is
$2.6\times$ shallower than the ideal-gas value of $-0.364$, and the reason is physical: **a
recombining nozzle cools slowly because the chemistry is pumping heat back in.** Once
recombination is finished that reason is gone and the curve has to steepen back toward ideal.
Steepening from the last solid point puts a \SI{2000}{\kelvin} exit at
**$A/A_* \approx 600$, not 6,200** — a factor of ten, and a \SI{24.5}{\centi\meter} throat
rather than a 7.6.

**On that reading it clears both walls, at a smaller chamber:**

| volume | $p_c$ | $A/A_*$ | throat | $Da$ | blowdown | |
| ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| 200 m³ | 642 bar | 602 | \SI{0.047}{\square\meter} | 3.3 | 1193 ms | freezes, too slow |
| 100 m³ | 1284 bar | 602 | \SI{0.047}{\square\meter} | 8.6 | 596 ms | marginal, too slow |
| **50 m³** | **2568 bar** | 602 | \SI{0.047}{\square\meter} | **22.3** | **298 ms** | **passes both** |
| 25 m³ | 5136 bar | 602 | \SI{0.047}{\square\meter} | 58.3 | 149 ms | passes with room |

**Rubbia is the argument that found this, and it is a good one.** Project 242 recombines hydrogen
from a \SI{10000}{\kelvin} chamber and reaches 91\% of the equilibrium ceiling W2 computes, so a
chamber at this temperature demonstrably can be expanded to where recombination substantially
completes. Two things make that easier for him and one harder. **Easier:** he runs continuously,
so there is no chamber to empty, no blowdown limit and no \SI{400}{\milli\second} period, and any
area ratio is free to him. **Easier:** hydrogen only, and $\ce{H}+\ce{H}+M$ is the channel W5
established with margin to spare. **Harder:** his chamber is a few bar against our 642 to 1284,
so at the same *pressure* ratio his exit is two orders of magnitude thinner than ours.

**That last one runs our way and is the point.** If Rubbia recombines at his exit density we
recombine at ours with room. **Density was never the binding constraint here. The
\SI{400}{\milli\second} pulse period is, and it is the one thing he does not have.**

**Hydrogen remains the worst of the three on freezing, which is the irony worth keeping.** It
gains most from a cold exit and reaches one least well, because the small slug that gives it its
specific impulse also makes the thinnest chamber, \SI{2.19}{\kilogram\per\cubic\meter} against
water's 10.13.

**Which extrapolation is right is exactly what N16 settles**, and it is worth naming as the
single most valuable thing in that grid: **where does $T_e$ against $A/A_*$ steepen?** Everything
past $A/A_* = 140$ in this decision is one or other guess about that curve.

**The reachable limit is already the right place to stop.** At \SI{100}{\cubic\meter} the
blowdown caps the area ratio at 404, which lands the exit at \SI{2914}{\kelvin}. **That is
"clearly into water recombination" already** — the phrase describes \SI{2900}{\kelvin} as well
as it describes 2000, because the combustion step is done by about \SI{3000}{\kelvin}.

**Methane is the fluid with most to collect down there**, being 36\% held at
\SI{3100}{\kelvin}, but it also freezes soonest of the three, having the thinnest chamber. And
below \SI{4000}{\kelvin} ADR-0050's equation of state omits condensed carbon, which is the very
chemistry the cold end would be reaching for. **Water is the fluid that can actually be modelled
where the design wants to run.**

**One rule falls out of this and it corrects an earlier reading.** Cooling the chamber was found
to help at the flown \SI{7}{\square\meter} throat and it does, but only because that exit is far
too hot to recombine. Once the expansion is deep enough to finish the chemistry there is nothing
left for a cooler chamber to buy, and only its bigger slug remains: water loses 18\% going from
10,000 to \SI{6000}{\kelvin} at a deep expansion. **Run the chamber hot and the nozzle long, not
the other way round.** The cool-chamber half of N14 should be read that way inside N16.

### N16 answered it, and the target should be retired rather than chased

Answered 2026-09-10 (W20), and the result splits this section's two claims
apart. **The geometry estimate is close to right. The prize is not there.**

**The equilibrium curve never steepens. It keeps flattening.** Methane at
\SI{100}{\cubic\meter} from a \SI{10000}{\kelvin} chamber:

| $A/A_*$ | exit $T$ | $T_e/T_c$ | local slope |
| ---: | ---: | ---: | ---: |
| 3.9 | \SI{5737}{\kelvin} | 0.574 | $-0.189$ |
| 30.6 | \SI{4204}{\kelvin} | 0.420 | $-0.124$ |
| 100.9 | \SI{3671}{\kelvin} | 0.367 | $-0.104$ |
| 297.5 | \SI{3305}{\kelvin} | 0.331 | $-0.091$ |
| 943.7 | \SI{2994}{\kelvin} | 0.299 | $-0.080$ |

The fitted $-0.138$ is a fair average across $A/A_* = 4$ to 140 and a bad local
slope at either end. Extrapolating the far-field slope puts a
\SI{2000}{\kelvin} exit at $A/A_* \approx \num{1.4e5}$, a \SI{0.8}{\centi\meter}
throat radius. Not 600 and not 6200.

**But the equilibrium branch is not valid out there**, because the chemistry
froze at $A/A_* \approx 140$ (W19). A genuinely frozen gas does steepen toward
the ideal $-0.364$, and on that slope a \SI{2000}{\kelvin} exit arrives near
$A/A_* \approx 700$. **So this section's estimate of 600 was close, and its
reasoning was sound as far as it went.** The answer to "where does it steepen"
is: at the freeze station, and the equilibrium curve is structurally incapable
of showing it.

**The trouble is what the gas is doing when it gets there.** Cold because
frozen is not the same as cold because finished. The gas is cold at
$A/A_* = 700$ precisely because it stopped handing energy back.
**Exit temperature was only ever a proxy for "the chemistry finished", and once
the flow freezes the proxy inverts.**

**The variable to optimise is the store returned, and it peaks at
$A/A_* \approx 56$ while the exhaust is still at \SI{3615}{\kelvin}** (W19).
Past that the equilibrium column keeps climbing while the capped column goes
flat, which is the equilibrium branch crediting chemistry the real flow no
longer has time to release. The \SI{2000}{\kelvin} target is withdrawn, and so
is the \SI{50}{\cubic\meter} chamber that was sized to reach it. The table of
gains above, +2.1\% for water and +4.4\% for hydrogen, priced a state the flow
does not arrive in.

**What survives is the closing rule, and N16 strengthened it.** "Run the chamber
hot and the nozzle long, not the other way round" is right on the first half and
needs one qualifier on the second. Run it hot, which W17 makes much stronger
than this section could. Run the nozzle long up to $A/A_* \approx 56$, and no
longer, because past that the chemistry freezes and the throat erodes.

## Aqueous ammonia: declined 2026-09-10 on handling and supply, not on performance

**Decision: ammonia stays off the ladder.** Raised as an ambient way to get hydrogen into a water
slug without cryogenics, and declined the same day because it is neither as safe nor as cheap as
methane. That is the same argument this decision already makes for methane over ammonia in "Why
methane rather than the hydrogen the precedent points at": not toxic, and Starship already flies
it, so its tankage and boil-off management are flown hardware rather than a new subsystem.
**The numbers below are kept so the case does not have to be re-derived if the supply picture
ever changes**, and because the last row of the table is a genuine result that was buried by a
correction rather than by an argument.

At household strength it is not worth the handling, and the reason why is what makes the
question worth recording.

**Ammonia is a poor hydrogen carrier by mass.** It supplies \SI{176}{\mole} of hydrogen per
kilogram against water's 111 and liquid hydrogen's 992. **To carry as much hydrogen as 10\%
liquid \ce{H2} takes 56\% ammonia**, past concentrated aqueous ammonia at about 30\%, let alone
household 5 to 10\%.

| slug | $k$ | $u$ | storage | effective Isp | GN\,s | vs water |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| pure water | 39.54 | 69.4 | 1000 | 845 s | 0.828 | -- |
| water + 5\% ammonia | 38.80 | 70.7 | 994 | 851 s | 0.834 | $+0.7\%$ |
| water + 10\% ammonia (household) | 38.09 | 71.9 | 989 | 857 s | 0.840 | $+1.4\%$ |
| water + 30\% ammonia (concentrated) | 35.49 | 77.1 | 968 | 880 s | 0.863 | $+4.2\%$ |
| water + 10\% liquid \ce{H2} | 28.56 | 95.2 | **432** | 943 s | 0.924 | $+11.6\%$ |
| **pure ammonia** | 28.59 | 95.0 | **900** | **954 s** | **0.935** | $+12.9\%$ |

**The useful finding is the last row.** Ammonia is not really a hydrogen carrier, it is a
propellant in its own right at \SI{68.9}{\mega\joule\per\kilogram} of atomisation against water's
50.9. **Pure ammonia beats a water slug carrying 10\% liquid hydrogen**, 954 s against 943, and
stores at \SI{900}{\kilogram\per\cubic\meter} at \SI{240}{\kelvin} and \SI{10}{\bar} instead of
needing a cubic metre of \SI{20}{\kelvin} tankage per pulse. **It is first among the
non-cryogenic options at the cold end.**

**This decision had ammonia on the ladder as the storable alternative and then lost it**, ranked
fourth by the withdrawn dissociation correction, which discharged nitrogen's store hardest and
was wrong. On the corrected numbers it is second overall.

**Two things would have stood in the way had it been pursued, and the second did not exist
before today.**

**Nitrogen's rate.** \ce{N2} is \SI{941}{\kilo\joule\per\mole}, among the strongest bonds there
are, so at a \SI{2914}{\kelvin} exit its formation is thermodynamically overwhelming, $D/kT$
being 39. Whether it *keeps up* is open: W7 found $\ce{N}+\ce{N}+M$ uncertain by 1.3 decades,
with Byron's shock tube making nitrogen **faster** than hydrogen and a 2025 ab initio result
making it 12.7 times slower. Ammonia's whole rung rests on that one number.

**CN attack on the wall film.** This decision already flags atomic nitrogen attacking carbon to
form CN and files it under "the ammonia variant." But the liner answer reached above is a
**fuel-rich methane wall film**, so ammonia in the bulk and carbon at the wall now meet by design
rather than by accident, and **a carbon film is exactly what atomic nitrogen would eat.** That
interaction has to be priced before ammonia and the film are recommended together.

## The cold end is where the unclaimed impulse is

The same fit that kills all four options above points hard the other way, and this is the
largest number found anywhere in this decision.

**Superseded 2026-09-10, and the direction was right while the destination was not**
(W19, W24). The impulse in this section's table is read off the $\rho^{-0.21}$ fit that
W16 retires and off an equilibrium branch that W19 shows has frozen. Its recommended
\SI{0.14}{\square\meter} throat sits past the chemical wall, and on the solved grid
freeze-capped conversion is flat below about \SI{0.5}{\square\meter}. **The
\SI{1156}{\second} headline is withdrawn.** The throat-life table in the throat section
adds the cost this section could not see: at \SI{0.2}{\square\meter} the throat lasts
seven pulses to $+10\%$ area, and at \SI{0.1}{\square\meter} it lasts two.

**What survives is that expanding further is the lever**, which was this section's real
finding and it is correct. It runs out at $A/A_* \approx 56$, a
\SI{0.5}{\square\meter} throat, rather than at the 200 the blowdown cap suggested. The
three N9 items this section named as standing between it and a result have all come back,
and the throat is indeed the whole problem rather than a footnote.

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
afterwards. Those items stood exactly as posed, and they have now come back answered.

Film injection is retained as a shield for the shocked front and as a convective
coolant. It is **not** a radiation shield, and the section must not claim it is. The
chamber's own optical depth already does that work, and a film thin enough to inject
sits near an optical depth of 0.03. **The between-pulse spray is required rather than
optional**, and the suggestion that methane's own exhaust might make it unnecessary is
withdrawn with the redeposition argument above (W15).

**The film is sized generously, which is the good news in the load case** (W13). A cold
methane film absorbs \SI{140.5}{\mega\joule\per\kilogram} at chamber conditions, being
atomisation plus sensible heat, so \SI{0.02}{\kilo\gram\per\square\meter} carries
\SI{2.8}{\mega\joule\per\square\meter} and \SI{0.2}{\kilo\gram\per\square\meter} carries
\SI{28.1}{}. Against the radiative transient that is three hundred times oversized.
Against the convective transient it is sized correctly at \SI{200}{\cubic\meter} and
undersized at \SI{673}{\cubic\meter} on the pessimistic edge.

**And `sec:watering_it_down`'s rejection of a sprayed film does not carry over to this
liner.** That rejection is about a liner facing a plume at
\SI{45.58}{\kilo\meter\per\second}. This liner is grazed by a layer arriving radially at
\SIrange{2.6}{12.2}{\kilo\meter\per\second} whose radiative load is negligible. The
film's problem in the walled case is mechanical scouring, and nothing prices scouring
yet.

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

**And does carbon deposit in the throat? No, and the question was the wrong way round**
(W15). A drifting throat area is the one dimension a nozzle cannot tolerate, and this
decision assumed the throat would clean itself because it is the hottest and fastest
station. It does not deposit carbon at any wall temperature graphite survives, so there
is nothing to clean off. It is being chemically eroded instead, and the throat drifts
**open** rather than closed. That is still a drifting throat area, and the throat-life
table above is what prices it.

The wall's load case during the crossing has returned, and it closes (W10 to W14, W23).
This decision carried it as a stated condition on the grounds that
`sec:needle_through_fog` puts the freshly shocked layer at the nose of a
\SI{45.58}{\kilo\meter\per\second} arrival near \SI{94600}{\kelvin}, with the
spreading cone reaching a \SI{3}{\meter} wall after \SI{6}{\meter} of a
\SI{23.8}{\meter} column. The contact station survives that reasoning and the
temperature does not. See the load-case section above. **What remains open is the
Stanton number**, bracketed over a factor of ten on the only channel that delivers
meaningful energy to the wall, and that is now the single largest uncertainty in this
decision.

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
problem and keeps graphite as the default. **The convenience that the exhaust might
rebuild it is withdrawn** (W15), so graphite is the default on oxidation grounds alone
and both the liner and the throat are consumables. The tungsten option and the question
of atomic nitrogen attacking carbon to form CN belong to the ammonia variant rather than
to this one. One point for a non-carbon refractory is now on the table, since a
refractory that is not carbon has no deposition question at all, and against that it
would run hotter and put the speciation back inside the equation of state's weak spot
above \SI{4700}{\kelvin}.

## The companion's return, item by item

Answered at `puffsat_impact_simulation` `6d74d3f`, numbers computed at `4a448c0`, both
2026-09-09. The full document is `docs/walled_nozzle_answers_from_impact_sim.md`.

| item | verdict | what moved here |
| --- | --- | --- |
| **N10.4b**, chamber dissociation | **Reverses the premise.** Hydrogen is 93 to 98\% dissociated at \SI{10000}{\kelvin}, not 49 to 76. The store is 95 to 99\% charged | the 2026-09-09 correction is withdrawn; \SIrange{1120}{1133}{\second} before the convention fix below |
| **N10**, Project 242 | **Settles the tension.** \SI{2700}{\second} is 24 to 29\% above the frozen ceiling of \SIrange{2085}{2229}{\second} | the arithmetic-over-prose reading is now a result |
| **N9.0**, sealed vessel | **The geometry question dissolves.** Column length cancels; the verdict is a bore-to-throat area ratio, and it fails at \SI{7}{\square\meter} | the fifty turnovers and the \SI{11}{\kilo\meter\per\second} sound speed are both gone |
| **N10.1-3**, freeze stations | **The fork closes on the good side.** Damkoehler stays above threshold everywhere, 2.16 decades of margin at the flown point | the frozen \SI{793}{\second} branch does not apply |
| **N10.3**, the ladder | **Answered for water and hydrogen, ammonia unplaced.** The stated $k$ come back as outputs within 5\% | ladder re-scored on solved $k$; the ammonia-versus-water ordering is conversion-dependent and neither is printed |
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

**The companion adopted this correction on 2026-09-10 and the two repositories now
agree.** Its ladder reports the same $w(\eta\sqrt{1+k} - 1)/(k g_0)$, its own head-on
expression having carried the $-1$ all along, and the two anchor rows that disagreed by
\SI{32}{\second} now agree to 11. So this was a convention mismatch rather than a
physics disagreement, and it is closed from both sides.

**What the answer does not license.** A charge is not a return. The store being 95 to
99\% charged is a ceiling on what recombination could hand back, and W5 puts the actual
return at 22.6 to 26.2\% through the flown \SI{7}{\square\meter} throat. The two numbers
answer different questions and the section must not use one for the other.

## The companion's second return, item by item

Answered at `puffsat_impact_simulation` `1ffd367`, 2026-09-10. The full document
is `docs/walled_nozzle_grid_answers_from_impact_sim.md`. It answers N9 items 1
to 7 and the whole of N16, and it carries fifteen items, W10 to W24. Every table
quoted in this decision was re-checked against the companion's committed CSVs
under `data/results/walled_nozzle/` rather than taken from its prose.

| item | verdict | what moved here |
| --- | --- | --- |
| **N9 items 1--2**, contact station | **The temperature premise does not survive.** The front reaches the wall at \SIrange{5.6}{6.2}{\meter}, but by then it has swept 41 to \SI{178}{\kilo\gram} and slowed to \SIrange{9}{28}{\kilo\meter\per\second}, so the layer is at \SIrange{4900}{30700}{\kelvin} | the \SI{200000}{\kelvin} load case is withdrawn; the \SI{24.9}{\degree} cone becomes \SIrange{28.7}{30.3}{\degree} |
| **the gate**, N9's own precondition | **The paper side's guess is right to 5\%.** The front never reaches the wall below \SI{178}{\cubic\meter} | items 1 to 4 close for the 50 and \SI{100}{\cubic\meter} chambers |
| **the contraction**, raised there not asked | **Priced, and it does not shrink with the chamber.** The bulk load is volume-independent and the arrival load worsens as the chamber shortens | a floor at \SI{150}{\cubic\meter} enters the Decision |
| **N9 item 3**, fluence | **It reverses which channel matters.** Radiative delivery is \SIrange{0.001}{0.009}{\mega\joule\per\square\meter}; the load is convective and grows with chamber volume | the wall argument now points the same way as the ledger |
| **N9 items 4 and 6**, the film | **Answered generously.** Even \SI{0.02}{\kilo\gram\per\square\meter} carries \SI{2.8}{\mega\joule\per\square\meter} | `sec:watering_it_down`'s rejection does not carry over to this liner |
| **N9 item 7**, convective flux | **Answered.** The Bartz-like \SIrange{123}{281}{\mega\watt\per\square\meter} is a good liner number and 2 to 3 times low at the throat | the estimate is relabelled rather than replaced |
| **N9 item 5**, throat carbon | **No self-healing, and no plating at all.** The exhaust is undersaturated in carbon at every wall temperature graphite survives | the \SIrange{0.34}{3.7}{\percent} redeposition line is deleted; the throat is a consumable |
| **N16**, `held(T, rho)` | **The fit is retired.** The exponent is not \num{-0.21} and not constant, running 0 to $-0.25$ for methane | every cold-end figure built on the fit is superseded |
| **N16**, the temperature dial | **It reverses.** \SI{6000}{\kelvin} returns 497 to \SI{743}{\second} where \SI{12000}{\kelvin} returns 800 to 1156 | the cooler chamber is withdrawn; the Decision runs at \SI{12000}{\kelvin} |
| **N16**, the volume dial | **"Free" is wrong.** Volume buys slug ratio and costs freeze margin, and the optimum is interior | \SI{100}{\cubic\meter} survives, for a different reason |
| **N16**, the throat dial | **There is a chemical wall.** The store returned peaks near $A/A_* = 56$ and then falls | the \SI{0.1}{\square\meter} and \SI{0.05}{\square\meter} throats are retired |
| **the throat's price**, raised there not asked | **Priced.** Narrowing buys $+22\%$ at \SI{2}{\square\meter} and costs a factor of three in throat life per halving | the decision now states a replacement interval |
| **N16**, water on the grid | **It loses everywhere.** Water returns 52 to 83\% of methane's effective impulse in all 128 cells | the cold-end near-tie is withdrawn; methane keeps the fluid choice |
| **N16**, the named configuration | **Plain methane beats it by 4 to 12\%** | the water-plus-hydrogen proposal is withdrawn |
| **N13**, exit-plane velocity distribution | **Not started, and confirmed unreachable from there.** It needs a 2-D solve | stays open, still worth about \SI{30}{\second} |
| **N11**, radiative escape | **Not started** | nothing |

**Eight of this decision's stated premises did not survive**, and five of them
were positions rather than inputs. The temperature dial, water's near-tie, the
water-plus-hydrogen configuration, the \SI{2000}{\kelvin} exit target and the
self-healing throat all reverse. Each is recorded in place above rather than
edited out, because where an argument failed is the part worth keeping.

**The common cause of the two largest reversals is the same omission.** Both the
temperature dial and the freeze-race conclusion priced only what the exhaust
gives back and not what the chamber charged in the first place. A cold chamber
parks its store in \ce{C3} and acetylene, which is already the recombined state,
so a deeper expansion recovers a larger share of a much smaller store. **Any
future argument on this rung has to carry the charge term and the return term
together.**

## What is still owed before the section can be drafted

**N9 items 1 to 7 are answered and no longer gate the section.** That was the
whole of what this decision previously said was owed. What replaces it is
shorter and softer.

- **The Stanton number.** The convective strike and the contraction load are
  both an energy-budget ceiling times a Stanton number bracketed over a factor
  of ten, and it is the only channel delivering meaningful energy to the wall.
  It decides \SI{100}{\cubic\meter} against \SI{150}{\cubic\meter} and nothing
  else in the Decision. **The section can be drafted carrying both**, which is
  what the Decision now does.
- **The throat-life ladder at the flown chamber.** It has only been run at
  \SI{200}{\cubic\meter} and \SI{10000}{\kelvin}. Running it at
  \SI{100}{\cubic\meter} and \SI{12000}{\kelvin} would settle
  \SI{2}{\square\meter} against \SI{0.5}{\square\meter}, which is worth
  \SI{117}{\second}. Cheap, being the same machinery at a different cell.
- **A genuinely frozen methane expansion.** `eos_water` has a frozen branch and
  `eos_methane` does not, so the freeze-capped conversion behind every deep
  throat is a lower bound rather than an answer. The gap to the equilibrium
  column is 0.03 to 0.09 in conversion, which bounds the error.
- **The acetylene kinetics**, unchanged from the first return. Worth 59 points
  of atomisation against soot's 7, and ordinary combustion kinetics rather than
  nucleation theory.
- **The chemical erosion rate.** That the exhaust erodes graphite is settled;
  how fast is not, so the ablation column is a floor rather than a total.
- **N13**, the exit-plane velocity distribution, confirmed to need the 2-D
  axisymmetric kernel. Worth about \SI{30}{\second} out of 1500, so it gates
  nothing.
- **N11**, radiative escape, untouched.
- **An `eos_ammonia`**, unchanged. Ammonia is the only rung that is assembled
  rather than solved.

**Nothing on that list blocks drafting.** The section should be written at
\SI{100}{\cubic\meter}, \SI{12000}{\kelvin}, a \SI{2}{\square\meter} throat and
plain methane, quoting \SI{976}{\second} effective and stating two open items
rather than waiting on them. Those are the Stanton bracket, and the throat
interval, which is solved at \SI{200}{\cubic\meter} and not at the flown
chamber.
