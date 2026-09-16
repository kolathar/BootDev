# Welcome to the main game file for our little Astroids project!
# Dev started 09/14/2026


#=========================================
# Imports
#=========================================
import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event


#=========================================
# Define Main Function
#=========================================

def main():
    print("Hello from astroids-project-v1!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")


    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2

    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Create Containsers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    # Create Objects
    asteroidfield = AsteroidField()
    player = Player(x, y)


    # Game Loop
    while True:
      log_state()

      # Exit is Closed
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
         return

      #Timing
      dt = clock.tick(60) / 1000
      updatable.update(dt)

      #Collision Loop for Player vs Asteroids
      for asters in asteroids:
         if asters.collides_with(player) == True:
            log_event("player_hit")
            print("Game over!")
            sys.exit()

      #Collosion loop for Asteroids vs ShotsFired
      for asters in asteroids:
         for shot in shots:
            if asters.collides_with(shot) == True:
               log_event("asteroid_shot")
               asters.split()
               shot.kill()

      #Screen and Draw stuff
      screen.fill("black")
      for drawings in drawable:
         drawings.draw(screen)
      pygame.display.flip()


#=========================================
# Run Main Function
#=========================================


if __name__ == "__main__":
    main()
