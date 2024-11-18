# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
# import everything from a module
# into the current file
from constants import *
from player import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    print('center', x, y)

    player = Player(x, y)

    while True:
        print("Starting asteroids!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        player.update(dt)


        # update display Surface
        pygame.display.flip()

        delta_ms = clock.tick(60)
        dt = delta_ms/1000


if __name__ == "__main__":
    main()