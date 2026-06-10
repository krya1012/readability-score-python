# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This is a JetBrains Academy / Hyperskill project ("Readability Score (Python)"). The goal is to build a
command-line program that reads a text file and reports various readability scores. The project is split
into 5 sequential stages (see `Readability Score (Python)/lesson-info.yaml`):

1. **Simple estimation** — classify a text as `EASY`/`HARD` based on character count and sentence count.
2. **Words and sentences** — classify based on average words per sentence (read text from a file given as
   a CLI argument).
3. **What's the score** — implement the Automated Readability Index (ARI).
4. **More formulas** — add the Flesch–Kincaid readability test and an "average age" calculation.
5. **Frequency Inc** — add the Dale-Chall readability index, which requires a second CLI argument: a path
   to a word list file (Longman Communication 3000) used to detect "difficult words".

Each stage's `task.html` (under `Readability Score (Python)/<Stage Name>/task.html`) contains the exact
formula, scoring table, and worked examples — read the relevant stage's `task.html` before implementing or
modifying that stage's behavior, since the expected output format (text wording, rounding, age ranges) must
match the examples exactly.

## Code location and structure

- All program code goes in:
  `Readability Score (Python)/task/readability/readability.py`
  This file is currently empty (`# Write your code here`) — it is the single entry point for every stage.
- Tests live in `Readability Score (Python)/task/test/tests.py` and are run via
  `Readability Score (Python)/task/tests.py`, which does:
  `TestStage1("readability.readability").run_tests()`
  This uses the `hstest` framework (installed from the `hs-test-python` repo, see `requirements.txt`) to
  drive `readability.py` as a subprocess with various stdin/CLI inputs and check stdout against expected
  output.
- `requirements.txt` lists dependencies: `nltk` and the `hs-test-python` test framework.

## Key implementation notes (from task descriptions)

- **Sentence tokenization**: use `nltk` to split text into sentences.
- **Word tokenization**: use `nltk.tokenize.regexp_tokenize()` with the pattern `[0-9A-z']+`.
- **Characters**: count all visible symbols except spaces, newlines, and tabs.
- **Syllable counting** (stage 4+): vowels are `a, e, i, o, u, y`; collapse consecutive vowels into one
  syllable (two if three vowels in a row), subtract silent trailing `e`, and treat 0-vowel words as one
  syllable. `re.findall()` is suggested for finding vowel groups.
- **Age bracket rounding**: round each score up with `math.ceil()` before mapping to an age bracket.
- **Difficult words** (stage 5): a word is "difficult" if it is not present (case-sensitive) in the
  Longman word list file passed as the second CLI argument.
- **Dale-Chall adjustment**: if difficult words make up 5% or more of all words, add `3.6365` to the raw
  score before bracket lookup.

## Running

There is no build step. Run/test the program directly with Python 3.10, e.g.:
```
python3 "Readability Score (Python)/task/readability/readability.py" in.txt [words.txt]
```

To run the stage tests:
```
python3 "Readability Score (Python)/task/tests.py"
```
