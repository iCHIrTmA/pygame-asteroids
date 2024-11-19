import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    SHOT_RADIUS = 5

    def __init__(self, x, y, velocity):
        super().__init__(x, y, Shot.SHOT_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt * PLAYER_SHOOT_SPEED

