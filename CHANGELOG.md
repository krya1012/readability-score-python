# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- README and CHANGELOG.
- Stage 1 "Simple estimation": classify input text as `Difficulty: EASY` or `Difficulty: HARD` based on
  character count (>100) and sentence count (>3), using `nltk` for sentence tokenization.
- Stage 2 "Words and sentences": print the file's text and classify it as `Difficulty: EASY` or
  `Difficulty: HARD` based on the average number of words per sentence (>10), using
  `nltk.tokenize.regexp_tokenize` with the pattern `[0-9A-z']+` for word tokenization.
- Stage 3 "What's the score": compute and print character, sentence, and word counts and the Automated
  Readability Index (ARI), with a predicted reader age range looked up from the score.
- Stage 4 "More formulas": count syllables per word, compute the Flesch-Kincaid Readability Test score,
  and print an overall average reader age derived from the ARI and Flesch-Kincaid age ranges.

### Changed
- Input is now read from a text file passed as a command-line argument, replacing Stage 1's stdin
  input.
- Program output no longer prints `Difficulty: EASY/HARD` (superseded by the ARI score and age-range
  output from Stage 3).
- Age-range wording for the ARI (and now Flesch-Kincaid) score changed from "this text should be
  understood by ... year olds" to "(about ... year olds)." per Stage 4's examples.
