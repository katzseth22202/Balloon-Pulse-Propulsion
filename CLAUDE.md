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

Compile `templateArxiv.tex` (the main paper):

```bash
pdflatex templateArxiv.tex
biber templateArxiv
pdflatex templateArxiv.tex
pdflatex templateArxiv.tex
```

Compile `templatePRIME.tex` (uses natbib, not biblatex):

```bash
pdflatex templatePRIME.tex
bibtex templatePRIME
pdflatex templatePRIME.tex
pdflatex templatePRIME.tex
```

## License

All Rights Reserved — see LICENSE file. Do not distribute or reuse content without permission.
