# AI Engineering Learning Progress

## Record provenance

Reconstructed on 2026-10-27 from existing repository files, Git history,
and the learner's explicit confirmation of completed work. No onboarding or
placement quiz was run. Historical quiz scores are unknown, not zero.

Latest completed checkpoint: `c80b5ad` — Add Compose web service and networking practice.

## Mission

Understand AI engineering through personally written code, small experiments,
exercises, testing, and projects (from README.md).

## Phase status

| Phase | Status | Position |
| --- | --- | --- |
| 00 — Setup and Tooling | Do | Lessons 01–11 complete; next: 12 — Debugging & Profiling |

Later phases have not been assessed or marked complete.

## Progress log

Dates below are commit dates; completion is confirmed by the learner.
Lesson identifiers are relative to `phases/` in the upstream curriculum.

| Date | Lesson | Score | Existing evidence |
| --- | --- | --- | --- |
| 2026-10-23 | 00-setup-and-tooling/01-dev-environment | Not recorded | `8cc7ae2`, `40dfa6c`: Python and NumPy exercise in hello.py; requirements.txt |
| 2026-10-23 | 00-setup-and-tooling/02-git-and-collaboration | Not recorded | `2c42455`: git-notes.md; repository commit and merge history |
| 2026-10-25 | 00-setup-and-tooling/03-gpu-setup-and-cloud | Not recorded | `3103047`: phasse00_gpu_practice.ipynb, Colab CUDA checks and synchronized CPU/GPU benchmark |
| 2026-10-26 | 00-setup-and-tooling/04-apis-and-keys | Not recorded | `e6a4c3e`, `c92be5a`: environment variables, request/response practice, Gemini SDK and raw HTTP |
| 2026-10-26 | 00-setup-and-tooling/05-jupyter-notebooks | Not recorded | `8a42b32`: phase00-notebook-practice.ipynb, timing, CSV data and plotting |
| 2026-10-26 | 00-setup-and-tooling/06-python-environments | Not recorded | `b26bace`: pyproject.toml, uv.lock, dependencies and optional extras; uv practice confirmed by learner |
| 2026-10-26 | 00-setup-and-tooling/07-docker-for-ai | Not recorded | `80dacc6`, `c80b5ad`: Dockerfile, Compose, external named volume, web service, port mapping and networking practice |
| 2026-10-27 | 00-setup-and-tooling/08-editor-setup | 3/3 (100%) | Completed against official exercises; interpreter, Pylance hover, Black format-on-save, Jupyter installation, and settings confirmed. Correctly explained Remote SSH, notebook output scrolling, and basic type checking in quiz; minor diagnostic issue and kernel check deferred. |

| 2026-10-27 | 00-setup-and-tooling/09-data-management | 3/3 (100%) | data_practice.py: reproducible 70/15/15 splits, overlap checks, JSON/CSV/Parquet round trips, file-size comparison, Hub caching and streaming; Git ignore verified. Quiz correct on Parquet, streaming, and DVC; concrete examples helped distinguish training/test roles. |

| 2026-10-28 | 00-setup-and-tooling/10-terminal-and-shell | Completed | Practiced shell navigation, pipes and grep, stdout/stderr redirects, background jobs, nohup, tmux detach/reattach, process monitoring, SSH/rsync, aliases, and training-log filtering with awk. |
| 2026-10-28 | 00-setup-and-tooling/11-linux-for-ai | Completed | Practiced Linux filesystem navigation, file creation, permissions with chmod, disk/cache inspection with df and du, process inspection, tmux persistence, and local scp/rsync transfer behavior. |
| 2026-10-28 | 00-setup-and-tooling/12-debugging-and-profiling | Completed | Practiced tensor debugging and NaN detection, profiled a PyTorch training loop with cProfile, identified memory allocations with tracemalloc, used TensorBoard to recognize overfitting, inspected tensor shape, device, and gradients with breakpoint and Pdb, and ran the official debugging toolkit. |

## Next lesson

`00-setup-and-tooling/13-python-for-ai-engineering` — Python for AI Engineering.

Lesson 08 completed on 2026-10-27; all three post-lesson quiz answers correct
(3/3, 100%).
Confirmed by learner: Pylance installed; project interpreter
`/home/student/ai-engineering-journey/.venv/bin/python` selected; NumPy imports
resolve and hover documentation works; Black formats spacing and indentation
on save.

Minor editor diagnostic issue: Pylance did not show a type diagnostic for
`add(2, "3")` despite basic type checking being configured. Learner explicitly
chose to defer troubleshooting this non-blocking issue and continue.

Learner requested assessment against the official Lesson 08 exercises.
Confirmed: VS Code working, project interpreter selected, Pylance Python/NumPy
hover information working, Black format-on-save working, Jupyter installed,
and project settings configured. Official Lesson 08 quiz completed. Missing
Pylance argument-type diagnostic and notebook/kernel verification remain
unresolved/deferred, not completion blockers under the official exercises.
Problems panel currently shows notebook SyntaxErrors in cell2 and cell3;
these are not Pylance type diagnostics. Remote SSH practice is conditional
on access to a remote machine; no such access has been established.
The requirement to finish the quiz and record Lesson 08 complete before
resuming Lesson 09 is now satisfied.

Lesson 09 completed on 2026-10-27, quiz 3/3 (100%).
Learner confirmed reproducible fixed-seed shuffling
and successful execution of data_practice.py: 14 training, 3 validation,
3 test examples (20 total), with pairwise disjoint example IDs verified by
assertions. Initially edited editor_practice.py; resolved by moving the data
code into data_practice.py. JSON save/load equality verified for 14 training
examples. CSV save/load verified; learner converted id/label strings back
to integers and confirmed equality with original training data. Installed
datasets via uv add datasets successfully (reported version 5.1.0).
Confirmed local CSV loading with inferred integer/text types, Parquet
round-trip equality, and sizes (CSV 229 B, JSON 874 B, Parquet 1822 B).
Library split produced 14/3/3; repeated seed preserved training examples.
Hub demo dataset loaded 5 training rows; repeat load matched and cache path
was displayed. Streaming returned IterableDataset and read two examples.
Git ignore practice confirmed: git check-ignore listed train.csv, train.json,
and train.parquet after learner saved the rules. Core practical walkthrough
finished. Explanations covered splits, disjoint IDs, JSON/CSV loading, type
conversion/inference, Parquet size overhead, caching, streaming, and Git ignore.
Learner initially confused training/test roles, overlap checks, smallest-file
comparison, and streaming choice; answered correctly after concrete examples.
Confirmed that Git ignore keeps files on disk. DVC introduced as versioning
data for reproducible experiments across machines. All 3 official post-quiz
answers correct: Parquet columnar storage, on-demand streaming, and DVC use.
Next: Lesson 10. Continue teaching one step at a time and wait for results;
explain each code chunk's purpose before asking the learner to add it.

Curriculum order checked against:
https://github.com/rohitg00/ai-engineering-from-scratch#phase-0

Lesson source:
https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/08-editor-setup/docs/en.md
https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/09-data-management/docs/en.md

## Review queue

No review needs recorded. Historical quiz results are unavailable.
