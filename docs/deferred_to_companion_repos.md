# Items deferred to the companion repos

Raised 2026-09-01 while applying companion ADR 0023 to `sec:split_dive`. All three are
prices the paper needs before it can state a conclusion the companion ADR already states.
See `docs/adr/0007-the-split-dive-ships-at-held-strength.md` for why each is held.

Target repo for all three: `katzseth22202/aim_is_all_you_need`, module
`src/bielliptic_dive_split.py` unless noted.

---

## S1. Price a dedicated impactor delivery to a 1.96 AU node

**Why.** `split_dive_ledger()` charges the impactors consumed at both nodes and nothing for
getting them to the far one. The **partial split** (`q` = 0.4918 AU) does not satisfy
outer-node co-location, so the returning beam does not reach its far node at 1.9649 AU.
Without this price, "better on both axes the ledger scores" cannot become "dominating."

**What is wanted.** The Earth-departure impulse, and the launched slug per kilogram
delivered, for placing an impactor wave at 1.9649 AU on the partial split's schedule. The
natural comparison is the two-impulse phasing loop's second node at 1 AU, which the paper
already treats as a network-maturity cost rather than an impulse cost.

**What would settle it.** Whether the partial split still beats the single-impulse dive's
2.365 kg/kg once the far node's delivery is added to its 1.536.

**Lifts.** `sec:split_dive_growth`'s held sentence, and `CONTEXT.md`'s **Partial split**
`_Avoid_` line.

---

## S2. Price a larger perihelion burn at the solar node

**Why.** The 19.80 solar-radii conduction crossing moves ~1.9 R☉ per km/s of perihelion
burn (5.58 at 20 km/s, 19.80 at the paper's 35.98 tuning, 35.91 at 45). **38.15 km/s holds
the direct departure conducting out to 23 R☉**, the depth `sec:depth_cost` recommends
starting at, for 6% more burn. So the crossing does not show that the split is *required* to
fly shallow; it shows that the direct route cannot fly shallow *at this burn tuning*.

**What is wanted.** What a perihelion burn of 38.15 km/s rather than 35.98 costs the direct
single-impulse dive at the node, charged the way `jovian_solar_dive_cycle` charges a node, so
the cycle can be scored end to end at both tunings. `paper_resonant_dive_ledger()` is not
sufficient: it takes the stream speed and the Earth burn, charges the node nothing for the
larger boost, and therefore reports the extra burn as a free improvement.

**What would settle it.** Whether there is a depth at which no affordable perihelion burn
keeps the direct departure conducting, and whether the split clears the committed fifteenth
of liftoff at that depth. Related and also unrun: the split dive's own pad-charged launch
ledger across the depth dial, in ADR 0021's `0.25 * chain * survival` form.

**Lifts.** `sec:self_cooling_departure`'s held paragraph, and the depth-window claim that
`sec:split_dive` no longer makes.

---

## S3. Trace whether any ledger already absorbs the opposing stream's placement

**Why.** Placing the opposing stream costs 35.48 km/s of heliocentric impulse at 4 solar
radii and 44.94 at 32, against the payload's own 24.09 falling to 14.62. That is the same
order as the payload's whole injection, and it moves the opposite way under the depth dial,
so it becomes the dominant Earth-side cost past about 8 solar radii. `sec:jovian_dive_open`
sets the opposing side aside twice, once at 1.34--2.15% of the vehicle consumed at the node
and once as "one-way and expendable." Both are about the projectiles once they are in place.
Neither is about the impulse that puts them there, and every impulse in this architecture is
a PuffSat collision charged to a pad.

**What is wanted.** For the direct dive, the Jovian dive cycle and the Jupiter-only chain in
turn: does the growth ledger, the pad ledger, or the impactor bill already carry the cost of
placing the opposing stream, and if not, how much does adding it move the doubling times.

**What would settle it.** One of two sentences. Either the placement is absorbed and the new
subsection says where, or it is not and the paper states the size of the omission.

**Blocks.** The restructure of `sec:split_dive` around the two-arrival asymmetry, agreed in
the 2026-09-01 grill as the subsection's spine. Until S3 lands the subsection keeps its
present order and leads with the Delta-v family.

---

## What landed

Nothing yet. This section is the record once the three come back, in the format
`docs/paper_corrections_checklist.md` used for D1--D9.
