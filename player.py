import pygame
from circleshape import *
from constants import *

# Base class for game objects
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        # sub-classes must override
        # print('triangle', self.triangle())
        playerVisual = pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

        # print('player', playerVisual)


    def update(self, dt):
        # sub-classes must override
        pass

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
