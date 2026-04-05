# Commit Plan — HVLCS Project

## Commit 1: Core DP algorithm — table computation and input parsing
- Create `src/hvlcs.py` with input parsing and DP table computation
- Builds the value table for the highest-value common subsequence

## Commit 2: Subsequence reconstruction and full end-to-end solver
- Add backtracking to reconstruct the optimal subsequence
- Program reads from file, outputs max value and subsequence

## Commit 3: Test data — 10+ nontrivial input/output files
- Create `data/` with 12 input files (strings length >= 25) and expected outputs
- Include the worked example from the assignment

## Commit 4 (Partner): Benchmarking script — time solver on all inputs
- Create `src/benchmark.py` to run and time the solver on each input file
- Print timing results

## Commit 5 (Partner): Runtime graph generation (Question 1)
- Extend benchmarking to produce a runtime graph (`data/runtime_graph.png`)
- Covers the empirical comparison deliverable

## Commit 6 (Partner): README.md with documentation and written answers
- Student names and UFIDs
- Build/run instructions with example commands
- Question 2: Recurrence equation, base cases, correctness explanation
- Question 3: Pseudocode and Big-O runtime analysis
- Pointers to example input/output files
