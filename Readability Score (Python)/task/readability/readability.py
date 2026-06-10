import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
from nltk.tokenize import sent_tokenize

text = input()

num_chars = len(text)
num_sentences = len(sent_tokenize(text))

if num_chars > 100 or num_sentences > 3:
    print("Difficulty: HARD")
else:
    print("Difficulty: EASY")
