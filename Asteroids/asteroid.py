import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        split_vectora = self.velocity.rotate(angle)
        split_vectorb = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_a.velocity = split_vectora * 1.2
        split_asteroid_b.velocity = split_vectorb * 1.2
        