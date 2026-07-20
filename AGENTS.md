# Agent Instructions

- Read `CLAUDE.md` before making project changes. Follow its repository-specific rules for builds, bibliography sources, scratch files, and writing style.
- Before finishing changes that touch LaTeX, bibliography, figures, build scripts, or paper text, run `bash build.sh --clean --quiet`.
- After each build, check `git status --short` and make sure only intentional tracked files are modified. LaTeX build outputs should remain ignored.
- Required build tools are `bash`, `pdflatex`, and `biber`.
