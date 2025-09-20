import pygame
from constants import *


def main():
    pygame.init()
    running = True
    
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(color=black)
        dt = clock.tick(60) / 1000
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
