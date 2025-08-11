import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    pygame.init()
    gameclock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for object in updatable:
            object.update(dt)
        for d_object in drawable:
            d_object.draw(screen)
        pygame.display.flip()
        dt = gameclock.tick(60) / 1000        


if __name__ == "__main__":
    main()


