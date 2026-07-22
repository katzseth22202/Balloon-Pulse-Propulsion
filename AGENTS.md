# Agent Instructions

- Read `CLAUDE.md` before making project changes. Follow its repository-specific rules for builds, bibliography sources, scratch files, and writing style.
- Before finishing changes that touch LaTeX, bibliography, figures, build scripts, or paper text, run `bash build.sh --clean --quiet`.
- After each build, check `git status --short` and make sure only intentional tracked files are modified. LaTeX build outputs should remain ignored.
- Required build tools are `bash`, `pdflatex`, and `biber`.

## Hedging in the Paper

- The paper is explicitly speculative, so do not repeat generic caveats merely because a proposal has not been demonstrated.
- Add hedging only when the uncertainty changes the point being made, bounds a quantitative claim, distinguishes evidence from extrapolation, or identifies a specific design risk.
- State each material caveat once at the closest relevant point. Do not append routine reminders that a concept needs modeling, testing, qualification, or further development.
