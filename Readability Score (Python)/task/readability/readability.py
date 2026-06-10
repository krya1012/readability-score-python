import sys
import re
import math
import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize, regexp_tokenize

with open(sys.argv[1], 'r') as f:
    text = f.read()

with open(sys.argv[2], 'r') as f:
    common_words = set(f.read().split())

words = regexp_tokenize(text, r"[0-9A-z']+")
num_sentences = len(sent_tokenize(text))
num_words = len(words)
num_chars = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
num_difficult = sum(1 for word in words if word not in common_words)


def count_syllables(word):
    word = word.lower()
    vowel_groups = re.findall(r'[aeiouy]+', word)
    syllables = sum(2 if len(group) >= 3 else 1 for group in vowel_groups)
    if word.endswith('e'):
        syllables -= 1
    return max(syllables, 1)


num_syllables = sum(count_syllables(word) for word in words)

ari = math.ceil(4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sentences) - 21.43)
fk = math.ceil(0.39 * (num_words / num_sentences) + 11.8 * (num_syllables / num_words) - 15.59)

dc_score = 0.1579 * (num_difficult / num_words) * 100 + 0.0496 * (num_words / num_sentences)
if num_difficult / num_words >= 0.05:
    dc_score += 3.6365
dc = math.ceil(dc_score)

AGE_RANGES = {
    1: "5-6", 2: "6-7", 3: "7-8", 4: "8-9", 5: "9-10",
    6: "10-11", 7: "11-12", 8: "12-13", 9: "13-14",
    10: "14-15", 11: "15-16", 12: "16-17", 13: "17-18",
}


def age_range(score):
    return AGE_RANGES.get(score, "24+")


def age_midpoint(score):
    return score + 4.5 if score in AGE_RANGES else 24.5


average_age = round((age_midpoint(ari) + age_midpoint(fk) + age_midpoint(dc)) / 3, 1)

print(f"Text: {text}")
print()
print(f"Characters: {num_chars}")
print(f"Sentences: {num_sentences}")
print(f"Words: {num_words}")
print(f"Difficult words: {num_difficult}")
print(f"Syllables: {num_syllables}")
print()
print(f"Automated Readability Index: {ari}. The text can be understood by {age_range(ari)} year olds.")
print(f"Flesch-Kincaid Readability Test: {fk}. The text can be understood by {age_range(fk)} year olds.")
print(f"Dale-Chall Readability Index: {dc}. The text can be understood by {age_range(dc)} year olds.")
print(f"This text should be understood in average by {average_age} year olds.")
