# Asteroids Class
import pygame
import random

from logger import log_event
from constants import LINE_WIDTH
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle (screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")

            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            degrees = random.uniform(20, 50)

            new_vector_1 = self.velocity.rotate(degrees)
            new_vector_2 = self.velocity.rotate(-degrees)
            
            new_aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_aster_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_aster_1.velocity = new_vector_1 * 2
            new_aster_2.velocity = new_vector_2 * 2






