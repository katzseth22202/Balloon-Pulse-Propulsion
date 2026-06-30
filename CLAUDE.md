# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a LaTeX paper repository for **"Aim Is All You Need: A Speculative White Paper on PuffSat Pulsed Propulsion"** by Seth Katz, exported from Overleaf. The paper proposes externally pulsed propulsion (balloon-pulse / PuffSat) as a mechanism for space travel and clean energy.

The companion calculations repo is `katzseth22202/aim_is_all_you_need` on GitHub.

## Files

- `templateArxiv.tex` — The actual paper (arXiv submission). Uses `biblatex`/`biber` for references.
- `templatePRIME.tex` — Placeholder PRIME AI style template (not the paper content).
- `PRIMEarxiv.sty` — Shared LaTeX style file used by both templates.
- `references.bib` — Bibliography database.
- `images/` — All figures referenced in `templateArxiv.tex` via `\graphicspath{{images/}}`.

## Building the Paper

Always build/test the main paper via `./build.sh` rather than invoking `pdflatex`/`biber` directly. It handles the full pdflatex → biber → pdflatex → pdflatex sequence with `-halt-on-error`.

```bash
./build.sh            # build the paper
./build.sh --clean    # remove aux files first, then build
./build.sh --quiet    # suppress pdflatex chatter (errors still surface)
./build.sh --open     # open the PDF in the default viewer when done
```

Compile `templatePRIME.tex` (uses natbib, not biblatex) manually if needed:

```bash
pdflatex templatePRIME.tex
bibtex templatePRIME
pdflatex templatePRIME.tex
pdflatex templatePRIME.tex
```

## Bibliography Rules

- **No Wikipedia articles as scholarly or pop-culture citations.** Do not add `references.bib` entries that point to `*.wikipedia.org`, and do not link to Wikipedia from inline prose in `templateArxiv.tex`. When a claim needs a citation, find the primary literature, a peer-reviewed paper, a textbook, a government/agency report, a news article of record, or a directly attributable industry/institutional publication. Even pop-culture or framing cites should point to the actual work itself (e.g. IMDb for a film, the publisher/Goodreads for a novel, the studio page for a video game), never to a Wikipedia summary.
- **Wikimedia Commons is fine for public-domain image attribution.** Entries that credit `commons.wikimedia.org` for a figure's source image (e.g. NASA-derived Earth or Moon imagery rehosted there under public-domain license) are acceptable, because they're crediting the file, not citing Wikipedia as a source of facts.
- When in doubt, ask before adding a cite that points at any Wikimedia property.

## Scratch Files and Working Documents

When writing ephemeral working documents (todo lists, audit summaries, restart-handoff snapshots, draft analysis notes, anything that isn't part of the paper deliverable or persistent project configuration), put them in `todos/` rather than the repo root. The `todos/` directory is gitignored, so anything inside is safe from accidental commit.

Examples:
- `todos/citation_audit_2026-05-22.md` instead of `CITATION_AUDIT.md` at root
- `todos/restart_handoff.md` instead of `HANDOFF.md` at root
- `todos/todo.md` for in-progress task lists

Create the `todos/` directory on demand if it does not exist. Never write working documents to the repo root. If a working document needs to be committed (rare), the user will explicitly ask you to move it out of `todos/` and track it.

## Writing Style

When drafting or editing prose in this paper, avoid the patterns that read as AI-generated. The list below is the enforceable blocklist; the principle above it is so you can extrapolate to novel tells not yet enumerated. When in doubt, prefer the plainer word and the shorter sentence.

- **No em-dashes (`---`).** Break the thought into separate sentences, or use a comma, colon, semicolon, or parentheses if a connector is genuinely needed. En-dashes (`--`) are fine for compound modifiers (e.g. `alumina--mullite`) and number ranges.
- **Don't use a colon to weld two sentences.** When a colon joins two independent clauses that could each stand alone (e.g. "The result is clear: the plate holds."), it reads as an AI tell. Make them two sentences, or use a period/semicolon. Colons stay fine when they genuinely introduce something that follows: a block quote, a list, a table, an equation, or a long run-on stretch of explanation. The test is whether what comes after the colon is a *delivered item* (keep it) or just *a second sentence wearing a colon* (split it).
- **Avoid stock AI vocabulary.** Do not use *delve*, *delve into*, *navigate the landscape*, *tapestry*, *crucial*, *pivotal*, *furthermore*, *moreover*, *in conclusion*, *it is important to note*, *it is worth noting*, *it should be emphasized*, *keep in mind*, *leverage* (as a verb), *robust*, *seamless*, *underscore*, *underpin*, *commendable*, *meticulous*, *realm*, *in the realm of*, *in light of*, *given the fact that*, *a myriad of*, *a host of*, *a wealth of*, *a testament to*, *stands as*, *serves as*, *at the heart of*, *at its core*, *in essence*, *essentially*, *transformative*, *groundbreaking*, *revolutionary*, *game-changer*, *showcase*, *highlight* (as a verb where "show" works), *aim to*, *seek to*, *strive to*. Reach for the plainer word.
- **Avoid padding adverbs.** *remarkably*, *incredibly*, *profoundly*, *vastly*, *fundamentally*, *ultimately*, *arguably*. Cut them; if the claim needs support, give a number or a citation.
- **Avoid sentence-initial throat-clearing.** *Indeed*, *Notably*, *Interestingly*, *Importantly*, *Additionally*, *Subsequently*, *Consequently* at the start of a sentence. If the connection matters, make it with a real clause; otherwise just state the next thing.
- **Avoid the "not only X but also Y", "X is more than just Y", and "This isn't just X --- it's Y" constructions.** They are tells, all from the same family.
- **Avoid rule-of-three lists.** AI reaches reflexively for tricolons (three adjectives, three parallel phrases). Use two, or four, or whatever the content actually calls for. If you find yourself writing "efficient, scalable, and robust", cut at least one.
- **Avoid hollow openers.** "In the modern era of...", "As X continues to evolve...", "In today's landscape of..." Cut to the actual claim.
- **Avoid recap closers.** Do not end sections by restating what was just said ("By doing X, we have shown Y..."). Stop when the argument stops.
- **Avoid "from X to Y" range-gesturing** without specifics ("from theory to practice", "from concept to reality"). Either name the actual range with endpoints, or drop the construction.
- **Avoid passive throat-clearing.** "It can be observed that...", "It is the case that...", "It has been shown that..." State the observation directly, or attribute it.
- **Quantify, don't hedge.** "Significant improvement", "substantial gains", "a wide range of", "various", "a number of", "potentially" are placeholders for missing numbers. In a physics/engineering paper, this is especially bad. Give the value, the order of magnitude, or the citation.
- **Keep sentences short.** If a sentence runs longer than ~30 words or stacks more than two subordinate clauses, split it. One idea per sentence is the default.
- **Drop interruptive asides.** Em-dash and parenthetical interjections that interrupt the main clause make sentences dense. Put the aside in its own sentence instead.

**Direct quotations are off-limits to this stylebook.** If a passage is in quotation marks and attributed to a person (interview, talk, email, published source, transcript, social-media post), do not "fix" it for AI-style tells. Quote the speaker as they spoke, even if the prose contains em-dashes, *delve*, *crucial*, tricolons, or anything else banned above. The style rules apply to my authorial prose, not to material reproduced verbatim from a source. The same applies inside `\textquote{}`, blockquotes, and figure-caption quotations.

## License

All Rights Reserved — see LICENSE file. Do not distribute or reuse content without permission.
