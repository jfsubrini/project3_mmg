#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MacGyver Maze Game

To be free, MacGyver needs to get out of jail,
collect three objects in the maze, and find the way out
after killing Murdoc, the prison guard.

Python's Scripts
Files : mmg_game.py, mmg_classes.py, maze_1 and 10 images y 6 sounds.

Copyright Jean-François Subrini, student DA Python at OpenClassrooms.
"""


# Importation of the PYGAME Library and locals.
import pygame
from pygame.locals import *

# Importation of the other files of the application game.
from mmg_classes import *

# Initialization of the PYGAME Library.
pygame.init()

# Opening of the screen with the background
screen = pygame.display.set_mode((Constants().SIDE_DIM, Constants().SIDE_DIM))
pygame.display.set_caption("MacGyver Maze Game")	           # Title of the game.
FLOOR_IMAGE = pygame.image.load("images/floor.png").convert()  # Loading of the Maze's floor image.

# Sounds for the game
#pygame.mixer.music.load("sounds/opening_theme.wav")
#sound_move = pygame.mixer.Sound("sounds/move.wav") 

# Creation of the instances of MacGyver, the Maze and the three objects.
macgyver = Agent("images/macgyver.png")
maze = Maze()
needle = Object("images/needle.png", maze)
tube = Object("images/tube.png", maze)
potion = Object("images/potion.png", maze)


# GAME LOOP
cont = 1
# INFINITE LOOP
while cont:
    # Slowdown the game loop.
    pygame.time.Clock().tick(40)
    for event in pygame.event.get():
        # Close the game by closing the window game or typing 'escape'.
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            cont = 0
        if event.type == KEYDOWN:
            # Keys to move MacGyver
            if event.key == K_RIGHT:
                macgyver.move('right', maze)
                #sound_move.play()
            elif event.key == K_LEFT:
                macgyver.move('left', maze)
            elif event.key == K_UP:
                macgyver.move('up', maze)
            elif event.key == K_DOWN:
                macgyver.move('down', maze)
    #pygame.mixer.music.play()
    # Blitting of the floor, the Maze and the three objects.
    screen.blit(FLOOR_IMAGE, (0, 0))
    maze.display_maze(screen)
    screen.blit(needle.image, (needle.x, needle.y))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    screen.blit(tube.image, (tube.x, tube.y))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    screen.blit(potion.image, (potion.x, potion.y))  # Change the tuple with NEEDLE_POS when random positionning is ready in mmg_classes.py
    # Blitting of the new position of MacGyver.
    screen.blit(macgyver.image, (macgyver.mg_x, macgyver.mg_y))
    # Refreshing of the Maze and all the objects.
    pygame.display.flip()
