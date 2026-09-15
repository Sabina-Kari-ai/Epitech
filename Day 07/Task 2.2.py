import random
import argparse
from english_words import get_english_words_set

parser = argparse.ArgumentParser()
parser.add_argument("--penalty", type=int, default=12)
args = parser.parse_args()

words = get_english_words_set(["web2"], lower=True)
word = random.choice(list(words))

hidden = ["_"] * len(word)
penalty = 0

while penalty < args.penalty:
    print(" ".join(hidden), "/", penalty, "penalty")

    guess = input("Letter or word: ").lower()

    if len(guess) == 1:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden[i] = guess
        else:
            penalty += 1
            print("Not found!")

    else:
        if guess == word:
            print("You win!")
            break
        else:
            penalty += 5
            print("Wrong word!")

    if "_" not in hidden:
        print("You win!")
        break

if penalty >= args.penalty:
    print("You lose!")
    