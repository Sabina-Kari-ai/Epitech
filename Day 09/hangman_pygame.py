import pygame
import sys
import random
import os

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
BACKGROUND = (30, 30, 40)

title_font = pygame.font.Font(None, 70)
word_font = pygame.font.Font(None, 60)
text_font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 70)


# Get the correct file path
def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)

    return os.path.join(os.path.dirname(__file__), filename)

background = pygame.image.load(
    resource_path("background.png")
).convert()

background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

# Read words
try:
    with open(resource_path("words.txt"), "r", encoding="utf-8") as file:
        words = [word.strip().lower() for word in file if word.strip()]
except FileNotFoundError:
    print("Error: words.txt not found")
    pygame.quit()
    sys.exit(1)


if not words:
    print("Error: word list is empty")
    pygame.quit()
    sys.exit(1)


# Start a new game
def new_game():
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    return word, guessed_letters, attempts


# Draw hangman
def draw_hangman(errors):
    HANGMAN_COLOR = (45, 180, 220)

    # Gallows
    pygame.draw.line(screen, HANGMAN_COLOR, (60, 460), (280, 460), 5)
    pygame.draw.line(screen, HANGMAN_COLOR, (150, 460), (150, 110), 5)
    pygame.draw.line(screen, HANGMAN_COLOR, (150, 110), (320, 110), 5)
    pygame.draw.line(screen, HANGMAN_COLOR, (320, 110), (320, 160), 5)

    # Head
    if errors >= 1:
        pygame.draw.circle(screen, HANGMAN_COLOR, (320, 195), 35, 4)

    # Body
    if errors >= 2:
        pygame.draw.line(
            screen,
            HANGMAN_COLOR,
            (320, 230),
            (320, 330),
            4
        )

    # Left arm
    if errors >= 3:
        pygame.draw.line(
            screen,
            HANGMAN_COLOR,
            (320, 260),
            (275, 300),
            4
        )

    # Right arm
    if errors >= 4:
        pygame.draw.line(
            screen,
            HANGMAN_COLOR,
            (320, 260),
            (365, 300),
            4
        )

    # Left leg
    if errors >= 5:
        pygame.draw.line(
            screen,
            HANGMAN_COLOR,
            (320, 330),
            (280, 390),
            4
        )

    # Right leg
    if errors >= 6:
        pygame.draw.line(
            screen,
            HANGMAN_COLOR,
            (320, 330),
            (360, 390),
            4
        )

word, guessed_letters, attempts = new_game()

running = True


while running:
    won = all(letter in guessed_letters for letter in word)
    lost = attempts == 0

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # Escape closes the game
            if event.key == pygame.K_ESCAPE:
                running = False

            # Restart after win or loss
            if won or lost:
                if event.key == pygame.K_r:
                    word, guessed_letters, attempts = new_game()

            else:
                guess = event.unicode.lower()

                if guess.isalpha() and len(guess) == 1:

                    if guess not in guessed_letters:
                        guessed_letters.append(guess)

                        if guess not in word:
                            attempts -= 1


    # Build the hidden word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "


    # Background
    screen.blit(background, (0, 0))


    # Title
    title = title_font.render(
        "HANGMAN",
        True,
        WHITE
    )

    screen.blit(
        title,
        (WIDTH // 2 - title.get_width() // 2, 25)
    )


    # Draw hangman
    errors = 6 - attempts
    draw_hangman(errors)


    # Hidden word
    word_text = word_font.render(
        display,
        True,
        WHITE
    )

    screen.blit(
        word_text,
        (560 - word_text.get_width() // 2, 210)
    )


    # Attempts
    attempts_text = text_font.render(
        f"Attempts left: {attempts}",
        True,
        WHITE
    )

    screen.blit(
        attempts_text,
        (560 - attempts_text.get_width() // 2, 300)
    )


    # Used letters
    letters_text = text_font.render(
        "Letters: " + " ".join(guessed_letters),
        True,
        WHITE
    )

    screen.blit(
        letters_text,
        (560 - letters_text.get_width() // 2, 350)
    )


    # Win screen
    if won:
        win_text = big_font.render(
            "YOU WIN!",
            True,
            GREEN
        )

        screen.blit(
            win_text,
            (WIDTH // 2 - win_text.get_width() // 2, 450)
        )

        restart_text = text_font.render(
            "Press R to play again",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                525
            )
        )


    # Game over screen
    elif lost:
        lose_text = big_font.render(
            "GAME OVER",
            True,
            pygame.Color("red")
        )

        screen.blit(
            lose_text,
            (WIDTH // 2 - lose_text.get_width() // 2, 430)
        )

        answer_text = text_font.render(
            f"The word was: {word}",
            True,
            WHITE
        )

        screen.blit(
            answer_text,
            (
                WIDTH // 2 - answer_text.get_width() // 2,
                500
            )
        )

        restart_text = text_font.render(
            "Press R to play again",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                545
            )
        )


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()