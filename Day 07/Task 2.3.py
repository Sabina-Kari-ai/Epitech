import random
import argparse
from english_words import get_english_words_set

parser = argparse.ArgumentParser()

parser.add_argument("--length", type=int, default=5)

args = parser.parse_args()

words = get_english_words_set(["web2"], lower=True)

short_words = []

for word in words:
    if len(word) == args.length:
        short_words.append(word)

word = random.choice(short_words)

print(word)