# Readability Score (Python)

A Hyperskill (JetBrains Academy) project that builds a command-line program for assessing the
readability of a text and predicting the grade level needed to understand it.

## Stages

This project is split into 5 stages (see `Readability Score (Python)/lesson-info.yaml`):

1. **Simple estimation** — classify text as `EASY`/`HARD` based on character and sentence count. ✅ Implemented (superseded by Stage 2)
2. **Words and sentences** — classify based on average words per sentence. ✅ Implemented (superseded by Stage 3)
3. **What's the score** — implement the Automated Readability Index (ARI). ✅ Implemented (superseded by Stage 4)
4. **More formulas** — add the Flesch–Kincaid readability test and average age. ✅ Implemented
5. **Frequency Inc** — add the Dale-Chall readability index. ⏳ Pending

Each stage's `task.html` (under `Readability Score (Python)/<Stage Name>/task.html`) contains the
formula, scoring table, and worked examples for that stage.

## Setup

```
pip install -r requirements.txt
```

## Usage

Run the program with the path to a text file. It prints the text followed by its character, sentence,
word, and syllable counts, the Automated Readability Index and Flesch-Kincaid Readability Test scores
(each with a predicted reader age range), and an overall average reader age:

```
python3 "Readability Score (Python)/task/readability/readability.py" in.txt
```

## Tests

```
python3 "Readability Score (Python)/task/tests.py"
```
