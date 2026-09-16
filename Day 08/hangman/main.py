import pygame
from pathlib import Path

pygame.init()

window = pygame.display.set_mode((600, 600))

folder = Path(__file__).resolve().parent
background_path = folder / "images" / "background.jpg"

background = pygame.image.load(str(background_path))


def draw_stickman():
    color = (0, 0, 0)

    pygame.draw.circle(window, color, (300, 200), 30, 3)

    pygame.draw.line(window, color, (300, 230), (300, 350), 3)

    pygame.draw.line(window, color, (300, 270), (250, 320), 3)
    pygame.draw.line(window, color, (300, 270), (350, 320), 3)

    pygame.draw.line(window, color, (300, 350), (260, 420), 3)
    pygame.draw.line(window, color, (300, 350), (340, 420), 3)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.blit(background, (0, 0))

    draw_stickman()

    pygame.display.update()

pygame.quit()