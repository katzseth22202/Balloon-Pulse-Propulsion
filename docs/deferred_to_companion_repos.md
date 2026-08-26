# Deferred back to the companion repos

Things found while applying `paper_corrections.md` that cannot be settled in
this repository. Each says what is owed, which repo owes it, and what the paper
does in the meantime.

Nothing here blocks the paper. Every item has a stated interim treatment.

---

## D1. `tab:two_leg_growth` has no tolled two-axis sweep

**Owed by:** `aim_is_all_you_need`
**Raised by:** A1, 2026-08-26

A1 asks for the swept axis of *both* growth tables to become
`eta_geom`. Only one of the two can be regenerated. `make two-wave` prints the
full 8x4 tolled grid behind `tab:space_mortgage_growth`, and that correction
lands. `make two-leg` does not print the matching 8x5 grid over `e_1` x `e_2`.
What it prints is a tolled *matched diagonal*, a single shared `eta_geom` on
both legs, with every row below 0.70 inadmissible, plus the **untolled** `e_1` x
`e_2` grids.

So `tab:two_leg_growth` cannot be re-tabulated cell by cell without a
two-axis tolled sweep that does not exist yet.

**Interim treatment:** `tab:space_mortgage_growth` is relabelled and regenerated
under A1. `tab:two_leg_growth` is left on its `e_1` / `e_2` axes and handled
under C1, which replaces that comparison with the matched diagonal the
companion does compute.

---

## D2. A1's `eta_chem` row is labelled with the wrong slug ratio

**Owed by:** `aim_is_all_you_need` (`docs/paper_corrections.md`)
**Raised by:** A1, 2026-08-26

A1 prints a row of `eta_chem` "at `k` = 8.5":

| `w` [km/s] | 45.58 | 56.53 | 61.83 | 65.13 | 75.00 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| document | **0.754** | 0.835 | 0.864 | 0.879 | 0.910 |
| `chemistry_efficiency` at `k` = 8.5 | **0.731** | 0.835 | 0.864 | 0.879 | 0.910 |

Four of the five reproduce exactly. The 45.58 entry is the `k` = 7.77 value
(0.755), which is the tolled optimum rather than the flown ratio. It is the
cold-leg number, and the cold leg is what binds the fleet, so the difference is
not decorative.

**Interim treatment:** the paper prints **0.731**, the `k` = 8.5 value, which is
what the flown design actually pays.

---

## D3. C1's plate column is at `f` = 0.818, not the target's default 0.80

**Owed by:** `aim_is_all_you_need`
**Raised by:** C1, 2026-08-26

C1 says it grants the plate "its full measured `f` = 0.818" and prints
1.46e6 / 4.24e5 / 7.49e4 at `eta_geom` = 1.0 / 0.9 / 0.8, for ratios of
47x / 22x / 10x. Running `make two-leg` as committed gives a plate column of
3.547e5 / 6.289e4 at 0.9 / 0.8 and ratios of **26.84x / 12.28x**, because its
incumbent runs at `f` = 0.80. The nozzle column reproduces exactly, so the gap
is entirely the plate's elasticity.

Both are defensible numbers; they are answers to different questions. The
target should take `f` as an argument, or the document should say which run it
quotes.

**Interim treatment:** decided when C1 is worked.

---

## D4. A3 zeroes the film everywhere, and section F does not say so

**Owed by:** `aim_is_all_you_need` (`docs/paper_corrections.md`)
**Raised by:** A3, 2026-08-26

A3 zeroes the bag film in `tab:bag_state` from cold storage. `eq:bag_film_mass`
sizes a pressure vessel, so with nothing boiling it returns zero *wherever* it
is evaluated, not only in that table. Section F says of `tab:axial_bag` that
"every one of its 20 cells reproduces exactly. Nothing is owed." That is true of
reproduction and false once A3 lands. Checked against `BagState` at the solved
leak, its whole film column goes to zero:

| row | paper | solved leak, cold storage |
| --- | ---: | ---: |
| 10.8 m sphere | 2.8 kg | **0.00 kg** |
| 23 m | 3.6 kg | **0.00 kg** |
| 50 m | 3.7 kg | **0.00 kg** |

Three further passages rest on the same 2.8 kg: the shape-factor paragraph
("1.7% of the slug"), the polyethylene-against-polyester material choice, and
the 4.9 kPa liner argument. A8 does warn that `x` moves and its column needs
regenerating; nothing says the same about the film.

**Interim treatment (Seth, 2026-08-26):** the bag is requoted at Earth's 278 K
storage throughout, which is the case that still boils and still needs a vessel.
Every film mass scales by the same factor 1.725, because the film goes as
`F x T` and only `x T` moves. Cold storage is then presented as the case that
removes the requirement outright. What is still owed is a **handling-sized
membrane model**: with no pressure to hold, the real bag is not 0 kg, and
neither repository sizes it.
