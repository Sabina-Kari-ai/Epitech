import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)

word = random.choice(list(words))

print(word)

