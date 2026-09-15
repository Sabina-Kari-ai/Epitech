import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)
word = random.choice(list(words))

print("_ " * len(word))

letter = input("Letter: ").lower()

if letter in word:
    print("Found!")
else:
    print("Not found!")