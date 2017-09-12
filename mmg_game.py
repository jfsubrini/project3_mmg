#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MacGyver Maze Game

To be free, MacGyver needs to get out of jail,
collect three objects in the maze, and find the way out
after killing Murdoc, the prison guard.

Python's Scripts
Files : mmg_game.py, mmg_classes.py, maze_1 and 10 images y 6 sounds

Copyright Jean-François Subrini, student DA Python at OpenClassrooms.
"""


# Importation of the PYGAME Library and locals
import pygame
from pygame.locals import *

# Importation of the other files of the application game
from mmg_classes import *

# Initialization of the PYGAME Library
pygame.init()

# Game's locals for the size of the Maze
SPRITE_SIDE = 15		# Number of sprites per side of the Maze        # STAY HERE or in mmg_classes.py ?
SPRITE_SIZE = 40		# Size of the side of each sprite in pixels     # STAY HERE or in mmg_classes.py ?
SIDE_SIZE = SPRITE_SIDE * SPRITE_SIZE	# Size of the Maze per side     # STAY HERE or in mmg_classes.py ?

# Opening of the screen with the background
screen = pygame.display.set_mode((SIDE_SIZE, SIDE_SIZE))
pygame.display.set_caption("MacGyver Maze Game")	           # Title of the game
FLOOR_IMAGE = pygame.image.load("images/floor.png").convert()  # Loading of the Maze's floor image

# Creation of the instances of MacGyver, the Maze and the three objects
macgyver = Agent()
maze = Maze()
needle = Objects()
tube = Objects()
potion = Objects()


# GAME LOOP
cont = 1
# INFINITE LOOP
while cont:
    # Slowdown the game loop
    pygame.time.Clock().tick(40)
    for event in pygame.event.get():
        # Close the game by closing the window game or typing 'escape'
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            cont = 0
        if event.type == KEYDOWN:
            # Keys to move MacGyver
            if event.key == K_RIGHT:
                macgyver.move('right')
            elif event.key == K_LEFT:
                macgyver.move('left')
            elif event.key == K_UP:
                macgyver.move('up')
            elif event.key == K_DOWN:
                macgyver.move('down')
    # Blitting of the floor, the Maze and the three objects
    screen.blit(FLOOR_IMAGE, (0, 0))
    maze.display_maze(screen)
    screen.blit(needle.image_n, (0, 160))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    screen.blit(tube.image_t, (560, 120))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    screen.blit(potion.image_p, (280, 400))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    # Blitting of the new position of MacGyver
    screen.blit(macgyver.image, (macgyver.mg_x, macgyver.mg_y))
    # Refreshing of the Maze and all the objects
    pygame.display.flip()
