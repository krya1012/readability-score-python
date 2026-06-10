import sys
import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize, regexp_tokenize

with open(sys.argv[1], 'r') as f:
    text = f.read()

sentences = sent_tokenize(text)
total_words = sum(len(regexp_tokenize(sentence, r"[0-9A-z']+")) for sentence in sentences)
avg_words_per_sentence = total_words / len(sentences)

print(f"Text: {text}")

if avg_words_per_sentence > 10:
    print("Difficulty: HARD")
else:
    print("Difficulty: EASY")
