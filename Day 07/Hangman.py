import random
import argparse
from english_words import get_english_words_set


def lose(penalty, limit):
    if penalty >= limit:
        print("You lose!")
        return True
    return False


def choose_word(length):
    words = get_english_words_set(["web2"], lower=True)

    short_words = []

    for word in words:
        if len(word) == length:
            short_words.append(word)

    return random.choice(short_words)


def hide(word):
    return ["_"] * len(word)


parser = argparse.ArgumentParser()

parser.add_argument("--penalty", type=int, default=12)
parser.add_argument("--length", type=int, default=5)

args = parser.parse_args()


word = choose_word(args.length)
hidden = hide(word)

penalty = 0


while penalty < args.penalty:

    print()
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

    if lose(penalty, args.penalty):
        break