import pygame
import random

# Asteroid Game imports
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

# Inherit from CircleShape Class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        blue_angle = random.uniform(20, 50)
        asteroid1.velocity = self.velocity.rotate(blue_angle)
        asteroid2.velocity = self.velocity.rotate(-blue_angle)

        asteroid1.velocity *= 1.2
        asteroid2.velocity *= 1.2