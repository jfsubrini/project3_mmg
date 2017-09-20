#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MacGyver Maze Game

To be free, MacGyver needs to get out of jail,
collect three objects in the maze, and find the way out
after killing Murdoc, the prison guard.

Python's Scripts
Files : mmg_game.py, mmg_classes.py, maze_1 and 9 images, 4 sounds and one music.

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
screen = pygame.display.set_mode((Constants.SIDE_DIM, Constants.SIDE_DIM))
pygame.display.set_caption("MacGyver Maze Game")               # Title of the game.
FLOOR_IMAGE = pygame.image.load("images/floor.png").convert()  # Loading of the Maze's floor image.

# Creation of the instances of MacGyver, the Maze and the three objects.
maze = Maze()
macgyver = Agent("images/macgyver.png", maze)
needle = Object("images/needle.png", maze)
tube = Object("images/tube.png", maze)
potion = Object("images/potion.png", maze)

# MacGyver Soundtrack loading.
pygame.mixer.music.load("sounds/opening_theme.mp3")

# MMG's Theme playing all over the game.
pygame.mixer.music.play(-1) # Too slow !!!
pygame.mixer.music.set_volume(0.5)


# GAME LOOP
cont = 1
# INFINITE LOOP
while cont:
    # Slowdown the game loop.
    pygame.time.Clock().tick(20)
    for event in pygame.event.get():
        # Close the game by closing the window game or typing 'escape'.
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            cont = 0
        if event.type == KEYDOWN:
            # Keys to move MacGyver
            if event.key == K_RIGHT:
                macgyver.move('right', maze)
            elif event.key == K_LEFT:
                macgyver.move('left', maze)
            elif event.key == K_UP:
                macgyver.move('up', maze)
            elif event.key == K_DOWN:
                macgyver.move('down', maze)
    # Blitting of the floor, the Maze and the three objects.
    screen.blit(FLOOR_IMAGE, (0, 0))
    maze.display_maze(screen)
    # Display of the three objects at their random position sorted out in the module mmg_classes.py.
    if maze.matrix[needle.y][needle.x] == '1':
        screen.blit(needle.image_o, \
            (needle.x * Constants.SPRITE_DIM, needle.y * Constants.SPRITE_DIM))
    if maze.matrix[tube.y][tube.x] == '1':
        screen.blit(tube.image_o, \
            (tube.x * Constants.SPRITE_DIM, tube.y * Constants.SPRITE_DIM))
    if maze.matrix[potion.y][potion.x] == '1':
        screen.blit(potion.image_o, \
            (potion.x * Constants.SPRITE_DIM, potion.y * Constants.SPRITE_DIM))
    # Blitting of the new position of MacGyver.
    # When MacGyver isn't at the exit gate (Murdoc's place) without the 3 objects collected.
    if maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] != '2':
        screen.blit(macgyver.image, (macgyver.mg_x + 5, macgyver.mg_y))
    # Refreshing of the Maze and all the objects.
    pygame.display.flip()
    # End of the game : Game over.
    if maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] == '2':
        pygame.time.wait(4000)
        cont = 0
    # End of the game : Victory.
    elif maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] == 'a':
        pygame.time.wait(4000)
        cont = 0
