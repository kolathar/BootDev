Hello there!

This is a repository for all projects created while taking course through Boot.dev. 
Some are simple, learning the fundamentals of coding languages like python. 
Some have been improved after course completion during my free time. 

Below is a list and summary of each project folder in this repository. Enjoy!


Projects: 

1. BookBot_v1
   ..Language: Python
   ..Developed in: WSL2 Ubuntu Distro
   ..Purpose: Public domain book stat analysis 
   ..Summary: Using simple python language, analyze text files of full-length books, and return stats: word count, character count, order character count. 

2. Asteroids_V1
   ..Language: Python
   ..Developed in: VM dedicated to Boot.dev work, WSL2 Ubuntu Distro, Visual Studio 
   ..Purpose: Simplified python version Asteroids ; focus on Class usage in python
   ..Summary: Using skills learned in Object Oriented Programming course, write a python version of the classic arcade game, Asteroid. Program opens a window that displays the player's triangle space ship
   and asteroids (V1 shows these as circles). Play can rotate ship, move forward and backward, and fire small circle "bullets". Asteroids will split in two upon contact with bullets, with child asteroids
   receiving a two times boost to their movement speed (V1 is 2x). Child asteroids will continue parent's direction of travel with an added variance of 20 to 50 degrees. Children of children will follow
   same behavior, meaning max speed will be 4x the grandparent. Player will lose game and prompt sys.exit() if ship collides with asteroid's hitbox. This however, needs improvement, as the current astroids
   hitboxes are smaller than the visual circle, thus the player can effective fly through large portions of asteroid bodies without consequence. Also, unlike classic Asteroids, there is no area boundary or
   loop, meaning the player and asteroids can leave the display area and disappear from view. 
