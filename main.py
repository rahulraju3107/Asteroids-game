import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True
    dt = 0
    black = (0, 0, 0)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(color=black)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
