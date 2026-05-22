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

When drafting or editing prose in this paper, avoid the patterns that read as AI-generated:

- **No em-dashes (`---`).** Break the thought into separate sentences, or use a comma, colon, semicolon, or parentheses if a connector is genuinely needed. En-dashes (`--`) are fine for compound modifiers (e.g. `alumina--mullite`) and number ranges.
- **Avoid stock AI vocabulary.** Do not use *delve*, *delve into*, *navigate the landscape*, *tapestry*, *crucial*, *pivotal*, *furthermore*, *moreover*, *in conclusion*, *it is important to note*, *leverage* (as a verb), *robust*, *seamless*, *underscore*, *underpin*, *commendable*, *meticulous*, or *realm*. Reach for the plainer word.
- **Avoid the "not only X but also Y" and "X is more than just Y" constructions.** They are tells.
- **Keep sentences short.** If a sentence runs longer than ~30 words or stacks more than two subordinate clauses, split it. One idea per sentence is the default.
- **Drop interruptive asides.** Em-dash and parenthetical interjections that interrupt the main clause make sentences dense. Put the aside in its own sentence instead.
- **Prefer concrete, technical phrasing** over hedged, qualifier-heavy prose ("a wide range of", "various", "a number of", "potentially", "it should be noted that").

## License

All Rights Reserved — see LICENSE file. Do not distribute or reuse content without permission.
