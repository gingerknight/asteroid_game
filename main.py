import sys
import pygame

# Asteroid Imports
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullets import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time_object = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        player.shoot_timer -= dt

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = time_object.tick(60) / 1000
    

if __name__ == "__main__":
    main()
