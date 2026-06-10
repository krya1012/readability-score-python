# Readability Score (Python)

A Hyperskill (JetBrains Academy) project that builds a command-line program for assessing the
readability of a text and predicting the grade level needed to understand it.

## Stages

This project is split into 5 stages (see `Readability Score (Python)/lesson-info.yaml`):

1. **Simple estimation** — classify text as `EASY`/`HARD` based on character and sentence count. ✅ Implemented (superseded by Stage 2)
2. **Words and sentences** — classify based on average words per sentence. ✅ Implemented (superseded by Stage 3)
3. **What's the score** — implement the Automated Readability Index (ARI). ✅ Implemented (superseded by Stage 4)
4. **More formulas** — add the Flesch–Kincaid readability test and average age. ✅ Implemented (superseded by Stage 5)
5. **Frequency Inc** — add the Dale-Chall readability index. ✅ Implemented

Each stage's `task.html` (under `Readability Score (Python)/<Stage Name>/task.html`) contains the
formula, scoring table, and worked examples for that stage.

## Setup

```
pip install -r requirements.txt
```

## Usage

Run the program with the path to a text file and a word-list file (one word per line, e.g. the Longman
Communication 3000 list — used to detect "difficult words" not in the list). It prints the text followed
by its character, sentence, word, difficult word, and syllable counts; the Automated Readability Index,
Flesch-Kincaid Readability Test, and Dale-Chall Readability Index scores (each with a predicted reader
age range); and an overall average reader age:

```
python3 "Readability Score (Python)/task/readability/readability.py" in.txt words.txt
```

## Tests

```
python3 "Readability Score (Python)/task/tests.py"
```
