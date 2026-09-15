import random
from english_words import get_english_words_set

words = get_english_words_set(["web2"], lower=True)
word = random.choice(list(words))

hidden = ["_"] * len(word)
penalty = 0

while penalty < 12:
    print(" ".join(hidden))

    guess = input("Letter or word: ").lower()

    if len(guess) == 1
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

if penalty >= 12:
    print("You lose!")
    