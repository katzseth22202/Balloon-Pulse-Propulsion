# Milestones: answers for the child (`puffsats_for_datacenters`)

Answers 2026-10-29 to `docs/milestone_asks_for_parent.md` at child `480194d`, copied into this repo
as `docs/milestone_asks_from_child.md`. Parent `fdd1d32`, aim `c559cc7`. **Written to be copied
into the child's `docs/`.**

Most of what the child asked is already priced in the parent, under another name. The parent's
Jupiter-only growth ledger (`sec:growth_ledger`) has always flown a methalox departure as its
"incumbent", and `tab:seed_return` and `tab:delivery_ledger` price it. What the parent has not
done is fly that methalox departure behind **today's** push: Kapton sheets on the 63.4 t spring
plate. The printed methalox rows sit behind the older spray-cup push plate. That run is now asked
of aim as **S63** (`docs/milestone_one_asks_for_aim_repo.md`).

| Item | Status |
|---|---|
| 1. Milestone 1's growth | **Answered on the previous push plate; asked of aim (S63) on today's.** It grows. The premise that it shrinks is wrong. |
| 2. Its best departure | **Answered in part.** Three-synodic windows only. A slow, Hohmann-like departure does not fit the clock and returns too slow a stream. aim asked to confirm. |
| 3. Is it the right first step? | **Answered. Yes.** The two alternatives either don't exist without the Sun or are already inside milestone 1. |
| 4. "Makes the venture pay" | **Answered. Reword.** The parent supports a narrower claim, and the growth is 3.24, not 3.23. |
| 5. The smaller seed | **Not answered. Open with aim since S29.** The parent's own seed figure also needs reconciling (S63 item 4). |

## 1. Milestone 1 grows, on the plate the parent has priced

The parent flies the Jupiter-only chain with a methalox departure in `sec:growth_ledger`
(`tab:growth_ledger_doubling`, `tab:growth_ledger_ten_year`). That is milestone 1 with an older
push. The setup there:

- Same 1500 t launch unit, pushed at 400 km by the returning wave.
- No departure wave, so the whole returning batch pushes and nothing is split.
- Departure on Raptor 3 engines at **380 s (3.73 km/s exhaust)**, steered along the velocity,
  with **0.018 kg of tank per kg of propellant**, engine count optimized (280 tf for 1525 kg each).
  Engines and tanks are expended every cycle.
- Methalox also pays the apoapsis turn and both waves' course corrections, as every design does.
- **Three-synodic windows only** (nine cycles over the same span), because methalox cannot fly the
  two-synodic burn.

| Push plate | Doubling (yr) | Growth per 3.276 yr | Annual | 10 yr | Payload sent on (t per unit) |
|---|---|---|---|---|---|
| Spray cup, jet efficiency 0.60, 20-day orbit | 7.92 | 1.33 | 9% | 2.3x | 142 |
| Spray cup, 0.60, 10-day orbit | 9.66 | 1.27 | | | |
| Plug, 0.70 | 5.54 | 1.51 | 13% | 3.3x | |
| Earlier plate, 0.84 (reference only) | 4.08 | 1.75 | 19% | 5.1x | |

Growth per 3.276 yr is 2^(3.276 / doubling), converted here from the printed doubling times. The
10-day orbit row matters most, because today's loop parks on the 10-day orbit. The paper explains
why that orbit hurts methalox (22% slower): its cheaper early-arrival burn (179 m/s) does not make
up for its dearer apoapsis reversal (373 m/s).

**Prices, same chain** (spray cup, gated valuation at 10%/yr, 15 synodic periods of growth; aim
`make solar-dive ARGS="--child"`): steady cost **$353 per kg at L1**, break-even **$2323 cheap /
over $5000 dear**. The bowl chain (milestone 2) at 0.5 g is $1474 steady and $761 / $1881. The dive
(milestone 3) is $96 and $130 / $156.

**Why the child's estimate expects shrinkage and the ledger does not.** The mass-ratio arithmetic is
right: 5.5-7.6 km/s at 3.73 km/s exhaust leaves only a fifth to an eighth of the stack. But growth is
not counted on the stack. It is the PuffSat mass a unit sends on to Jupiter, divided by the PuffSat
mass that arrived to push it. Most of the 1500 t unit is charge, plate and payload that the booster
lofts from Earth and that is paid in dollars. The wave that pushes a unit is only about 102-130 t
(`sec:mass_interest`). So a unit can burn most of itself in methalox and still send 142 t onward,
more than the wave that pushed it.

**"Needs launches from Earth every cycle"** is true of every milestone, not just milestone 1. Every
cycle of every loop lofts fresh launch units from Earth. What grows is the returning wave, which
pushes more lofted mass each cycle. The child should not print the Earth launches as milestone 1's
special cost.

**What does not transfer.** The printed rows sit behind the spray cup: a 150 t plate, a sprayed
argon charge, ice PuffSats, jet efficiency 0.60 at about 57 km/s. Milestone 1 as the child defines
it pushes Kapton sheets at k about 5 onto the 63.4 t spring plate at 54-65 km/s. The lighter plate
helps and the slower-stream push law hurts, so the sign (it grows) is safe and the size is not.
The child can print:

> On the paper's earlier push plate, the Jupiter-only loop with a methalox departure grows about 1.3
> times per 3.28 years, against 1.65 times with the departure bowl. On the sheets and spring plate it
> has not yet been computed.

The S63 answer will replace both numbers with today's plate.

## 2. Its best departure: three-synodic only

**The windows.** The parent's ledger already found that methalox cannot fly the two-synodic burn
(14.0-14.6 km/s of excess), so milestone 1 flies only the three-synodic windows, 11.9-13.2 km/s.
The paper prints the bowl chain on those windows alone too (`tab:no_sun_loop`): 1.46 times at 0.5 g
against 1.65 on the mixed chain. So milestone 1 loses the two-synodic windows that make milestone 2's
best row. One consequence for the child's text: the "54 to 65 km/s" push stream includes the
two-synodic returns. Milestone 1's stream is the three-synodic part of that range. aim is asked for
the exact band (S63 item 1).

**The slow departure.** A Hohmann-like departure does not help, for two reasons. This is the parent's
reasoning; no ledger run backs it yet:

- *It does not fit the clock.* Earth to Jupiter and back on Hohmann legs takes about 2 x 2.73 =
  5.5 yr, about five synodic periods, not two or three.
- *It returns too slow a stream.* On this loop the departing ship comes home as the next push wave.
  A slow departure meets Jupiter slowly, and the flyby cannot send it home fast. It returns near its
  own departure excess, about 14 km/s at 400 km, against 54-65 km/s. A plate's exhaust speed grows
  with the speed of the stream that strikes it, so the next push would be weak.

The paper already states the general rule for this loop: at each window's fixed dates, Jupiter's
geometry pins the return speed (`sec:why_sun_dive`). Saving methalox at departure is paid back on
the next push. aim is asked to sweep the departure excess and confirm (S63 item 2).

## 3. Milestone 1 is the right first step

The parent agrees with Seth's order, and it matches the risk gates the parent already prices
(`sec:mass_interest`):

| Gate (parent's odds) | Retired by |
|---|---|
| Sheets unfurl and arrive face-on (85%) | Milestone 1 |
| First push (part of 90%) | Milestone 1 |
| Bowl departure (rest of 90%) | Milestone 2 |
| Carrier splits the disks off at Jupiter (part of 95%) | Milestone 3 |
| First Sun boost (75%, the one with no flight analog) | Milestone 3 |

The lowest-odds gate comes last. Milestone 1 also has a precedent the child can cite: the parent's
own ledger has always flown methalox as the incumbent that each plate design is measured against.

The two alternatives the child named:

- **The dive's 130 deg departure, flown without the Sun.** This does not exist. The 130 deg comes
  from the Sun dive itself, which sets where the departure stream arrives from. A loop without the
  dive returns from Jupiter and meets the bowl at 161-180 deg (`sec:why_sun_dive`).
- **A push-only demonstration that does not close a loop.** That is already inside milestone 1. Its
  first event is a push, and every later piece rides on it. A push that does not send the unit on
  to Jupiter tests the same plate and sheets but cannot show growth. Milestone 1 shows both.

## 4. "Makes the venture pay": narrower wording

The parent stands behind the comparison, not the phrase.

- **The number.** The parent's headline is **3.24** times, not 3.23 (parent `fdd1d32`, after S62:
  the 1 kg disk on a charge 1.2 times its radius, aimed to 1.36 cm with the track hold). aim's own
  `make solar-dive` still prints 3.23, because it flies the matched charge. Print 3.24 to match the
  parent.
- **What the parent can support.** The dive breaks even at $130 cheap / $156 dear per kg at L1. That
  is under both published bars for orbital computing, Suncatcher's $200 and Johnston's $500
  (`tab:l1_comparison`). The best Jupiter-only row breaks even at $761 / $1881, over both.
- **What it cannot.** Every break-even leaves out research and development, on purpose
  (`sec:mass_interest`). "Makes the venture pay" reads as a claim about the whole venture.

Suggested wording:

> The third adds the Sun dive, where graphite disks strike a second bowl head-on at perihelion. It
> tests the Sun hardware and raises growth to 3.24 times. That is the growth at which the loop breaks
> even under both published launch-cost bars for orbital computing, before research and development.

The abstract's "the Sun dive that makes the growth pay" needs the same narrowing. "The Sun dive that
brings the price under the published bars" works.

## 5. The smaller seed: still open

The parent asked aim this as **S29** and has no answer. The parent prints the same sentence the child
does: "Whether a smaller seed would start the loop has not been computed." S29 asks whether anything
in the loop is indivisible below one 1500 t launch unit, and for both headlines on a 1-ship and a
2-ship seed. S63 item 3 re-raises it.

The one-unit seed itself needs reconciling first. The parent prints **622 t** at Parker's depth (4.0
to 4.6 stripped Starships, `tab:seed_amortization`) and 725 t at 4 solar radii. The parent's answer
of 2026-10-25 gave the child 567 t. A fresh run of aim's `headline_report` today gives **567 t**
(3.7-4.2 ships) and 674 t. The parent cannot yet say which is right at its adopted headline, so it is
S63 item 4. Until aim answers, the child should keep "about four stripped Starships", which holds on
both figures.

## Parent-side corrections this raised

- `tab:seed_amortization` and `sec:mass_interest` print 622 t / 725 t; aim's headline gives 567 t /
  674 t. Held for S63 item 4.
- `sec:why_sun_dive` still says "The heavier spring plates cost it most". The 2026-10-25 answers
  (`docs/no_sun_loop_answers_for_child.md`, item 2) said the parent would reword it; it has not.
