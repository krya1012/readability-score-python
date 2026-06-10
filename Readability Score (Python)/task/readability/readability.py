import sys
import math
import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize, regexp_tokenize

with open(sys.argv[1], 'r') as f:
    text = f.read()

num_sentences = len(sent_tokenize(text))
num_words = len(regexp_tokenize(text, r"[0-9A-z']+"))
num_chars = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))

score = 4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sentences) - 21.43
ari = math.ceil(score)

AGE_RANGES = {
    1: "5-6", 2: "6-7", 3: "7-8", 4: "8-9", 5: "9-10",
    6: "10-11", 7: "11-12", 8: "12-13", 9: "13-14",
    10: "14-15", 11: "15-16", 12: "16-17", 13: "17-18",
}
age_range = AGE_RANGES.get(ari, "24+")

print(f"Text: {text}")
print()
print(f"Characters: {num_chars}")
print(f"Sentences: {num_sentences}")
print(f"Words: {num_words}")
print(f"Automated Readability Index: {ari} "
      f"(this text should be understood by {age_range} year olds).")
