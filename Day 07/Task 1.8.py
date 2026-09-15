import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)
word = random.choice(list(words))

hidden = ["_"] * len(word)

print(" ".join(hidden))

letter = input("Letter: ").lower()

if letter in word:
    for i in range(len(word)):
        if word[i] == letter:
            hidden[i] = letter

    print(" ".join(hidden))
else:
    print("Not found!")
