# Meeting the miss farther out: ask S54 (for puffsat_impact_simulation)

Raised 2026-10-22 in `Balloon-Pulse-Propulsion` (after `8fe3d35`). **Written to be copied into
`puffsat_impact_simulation`.** It follows your S52 answers (Result 21, ADR-0072, carried here as
`docs/shaped_plug_answers_from_impact_sim.md` at `2992448`). Nothing here is in the paper yet.
Register entry: S54 in `docs/deferred_to_companion_repos.md`. The companion ask S55 to
`aim_is_all_you_need` re-solves k on your Result 21 and will take this answer when it lands.

## Seth's read of Result 21 (2026-10-22)

"The main takeaway is just the miss needs to occur further from the plate." He thinks the
shaped plug with a gun backup is still doable.

The parent agrees at k = 8.5, where the backup holds once the bullet meets the bag 46 m out
instead of 31 m. At k = 4 your item 4 table goes the other way. The peak rose from 2.41 GPa at
31 m to 3.04 GPa at 46 m, which you put down to the plug sitting in the cloud's middle as a
dense obstacle that the cloud jets past. Two runs at one k do not say whether the peak keeps
rising or turns over farther out. This ask is that sweep.

It matters for the ledger. aim's S51 answer chose k = 4 because the plug's mass was the only
cost of k it saw. At k = 4 your catch radius is 4 cm, so the gun fires on most bags, and no
tested backup holds the plate. If some meeting distance does hold at k = 4-6, the low-k plug
stays open. If none does, k has a floor near 8.5 set by the backup, not by leverage.

We use **meeting distance** for how far up-track of the plug's front face the bullet meets the
bag (your item 5). **Catch radius** is the plug's radius less the bag's 0.18 m, the largest
lateral miss that still lands the whole bag on the plug.

## S54. Wanted

1. **The meeting sweep.** The 100 g bullet, the 2x lens at 2 F, the plug centred in the cloud
   (your worst case), production grid with a fine-grid check where a run is near the limit. Run
   k = 4, 6 and 8.5 at meeting distances of 46, 60, 80, 100 and 120 m. Report face peak,
   impulse, leverage and the liner's graphite per backup pulse. At each k, give the shortest
   meeting that holds 2.3 GPa with your 1.2x margin, or say that none in the range does. Say
   whether the peak is monotone in distance past 46 m.
2. **The smallest k whose backup holds.** From item 1, the lowest k at which some meeting
   distance holds with the margin. If it falls between the k values run, bracket it.
3. **The plug at 2.5 F on a backup.** Your item 1 height table shows 2.5 F halves the normal
   pulse's peak for 1-3% of leverage. Run the backup pulse with the plug at 2.5 F at k = 4 and
   8.5, at 31 m and 46 m, and at the item 1 distance that holds if there is one. If 2.5 F
   rescues the backup at low k, also give the normal pulse's leverage there and the regraded
   plate's mass.
4. **The trigger window** for any new meeting distance, as in your item 5 table, at 500 m/s,
   1 km/s and 2 km/s. Say whether the gun still fires after the plug's last ~100 ms of steering.
5. **The mechanism, briefly.** If the k = 4 peak keeps rising with distance, say what the jet
   past the plug looks like (where on the face it lands, and how its peak scales with the
   cloud's width against the plug's radius). That tells the parent whether any plug that small
   can survive a backup, or whether the floor on k is physical.

Items 1 and 2 first. They set the floor on k that S55 carries.

## What the ledger is carrying meanwhile

S55 asks aim to price two policies across the gap. Above k = 8.5 the backup holds per your
Result 21, so a backup costs a spent plug and gives 4.16x. Below it a backup is counted as a
lost plate until this answer moves the floor.

The 3-D off-centre strike (your "What we did not do") stays open. It is not asked here.

Paper edits that wait on this: the Saturn cycle's `tab:saturn_cycle`, through S55.
