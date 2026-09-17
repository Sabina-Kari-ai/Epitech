import sys
import random
from datetime import date


# Check command-line argument
if len(sys.argv) < 2:
    print("Error: missing argument", file=sys.stderr)
    sys.exit(1)


filename = sys.argv[1]
highscore_file = "highscores.txt"


# Read the word list
try:
    with open(filename, "r", encoding="utf-8") as file:
        words = [word.strip().lower() for word in file if word.strip()]
except FileNotFoundError:
    print("Error: file not found", file=sys.stderr)
    sys.exit(1)


# Check if the word list is empty
if len(words) == 0:
    print("Error: word list is empty", file=sys.stderr)
    sys.exit(1)


# Select a random word
word = random.choice(words)


# Game variables
guessed_letters = []
attempts = 6
attempt_count = 0

display = "_" * len(word)

print(display)


# Main game loop
while attempts > 0 and "_" in display:
    guess = input("Enter a letter: ").lower()

    # Validate user input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already used
    if guess in guessed_letters:
        print("You already tried that letter.")
        continue

    guessed_letters.append(guess)
    attempt_count += 1

    display = ""

    # Reveal guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    # Check the guess
    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong!")
        print("Attempts left:", attempts)

    print(display)


# Player wins
if "_" not in display:
    today = str(date.today())

    best_attempts = None
    best_date = None

    # Read previous high scores
    try:
        with open(highscore_file, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")

                if len(parts) >= 2:
                    try:
                        score = int(parts[0])
                        score_date = parts[1]

                        if best_attempts is None or score < best_attempts:
                            best_attempts = score
                            best_date = score_date

                    except ValueError:
                        continue

    except FileNotFoundError:
        pass

    # Save a new high score
    if best_attempts is None or attempt_count < best_attempts:
        with open(highscore_file, "a", encoding="utf-8") as file:
            file.write(f"{attempt_count},{today},{word}\n")

        print(
            f"Best ever! You guessed '{word}' "
            f"in {attempt_count} attempts."
        )

    # Show the existing high score
    else:
        print(
            f"You guessed '{word}' in {attempt_count} attempts, "
            f"but the record from {best_date} "
            f"is {best_attempts} attempts."
        )


# Player loses
else:
    print("Game over!")
    print("The word was:", word)