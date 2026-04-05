# COP4533 Programming Assignment 3 — HVLCS

## Students

| Name | UFID |
|------|------|
| Taebok Joseph Kim | 13744367 |
| Manas Adepu | 67807126 |

## Build / Compile

No compilation required. The project is written in pure Python 3.

**Dependencies:**
```
pip install matplotlib
```

## Running the Code

### Solve a single input file
```
python src/hvlcs.py <input_file>
```

**Example:**
```
python src/hvlcs.py data/example.in
```
Expected output:
```
9
cb
```

### Run all test cases and generate the runtime graph
```
python src/benchmark.py
```
This prints timing results for all files in `data/` and saves the runtime graph to `data/runtime_graph.png`.

### Example input files
- `data/example.in` / `data/example.out` — worked example from the assignment
- `data/test01.in` – `data/test10.in` — nontrivial test cases (strings of length ≥ 25)

## Assumptions

- Input files follow the format:
  ```
  k
  char1 value1
  char2 value2
  ...
  A
  B
  ```
  where `k` is the number of distinct characters, followed by `k` character-value pairs, then strings `A` and `B` on their own lines.
- Character values are positive integers.
- Only characters listed in the value table appear in strings `A` and `B`; any unlisted character has an implicit value of 0.
- Strings `A` and `B` contain only lowercase letters.

## Question 1: Empirical Comparison

![Runtime Graph](data/runtime_graph.png)
