#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
#################### MACGYVER MAZE GAME ####################
#                                                          #
#  MacGyver needs to get out of jail and find his way out  #
#  of the maze reaching the place where Murdoc stands,     #
#  the prison guard.                                       #
#  To be free, MacGyver needs to put to sleep Murdoc,      #
#  reaching the exit gate with the three objects collected #
#  in the maze : the needle, the tube and the potion.      #
#  If not, MacGyver dies : game over !                     #
#                                                          #
############################################################

Python's Scripts
Files : mmg_game.py, mmg_classes.py, maze_1,
        and 9 images, 4 sounds and one music.

Copyright Jean-François Subrini, student DA Python at OpenClassrooms, 24/09/2017.

"""


# Importation of the PYGAME Library and locals.
import pygame
from pygame.locals import *

# Importation of the class file for the application game.
from mmg_classes import *

# Initialization of the PYGAME Library and the font module.
pygame.init()
pygame.font.init()

# Opening of the screen with the Maze at the top and some message space at the bottom (70px height).
screen = pygame.display.set_mode((Constants.SIDE_DIM, Constants.SIDE_DIM + 70))
# Setting the title of the game.
pygame.display.set_caption("MacGyver Maze Game")
# Loading the background of the Maze, i.e. the floor image.
FLOOR_IMAGE = pygame.image.load("images/floor.png").convert()

# Welcoming message at the beggining of the game explaining the rules to win.
FONT_1 = pygame.font.Font(None, 22)    # Default font with a size of 22 pixels.
MESSAGE_WELCOME = FONT_1.render(\
    "Welcome ! Move MacGyver out of the maze with all the objects collected.",\
    True, (0, 0, 0), (255, 255, 255))  # To draw a smooth black text on a new white Surface.
screen.blit(MESSAGE_WELCOME, (40, 615)) # Blitting the message on the screen at a special position.

# Creation of the instances of MacGyver, the Maze and the three objects (calling mmg_classes.py).
maze = Maze()
macgyver = Agent("images/macgyver.png", maze)
needle = Object("images/needle.png", maze)
tube = Object("images/tube.png", maze)
potion = Object("images/potion.png", maze)

# MacGyver Soundtrack
pygame.mixer.music.load("sounds/opening_theme.mp3")  # Loading the file.
pygame.mixer.music.play(-1)  # Playing the MacGyver Theme all over the game.
pygame.mixer.music.set_volume(0.1)  # Setting a low volume.


# GAME LOOP
cont = 1
# INFINITE LOOP
while cont: # The game is playing while the variable cont is "1" and stops when "0".
    for event in pygame.event.get(): # Get the events created by the gamer.
        # Ending the game when the gamer closes the window game or enter 'esc' on the keyboard.
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            cont = 0 # End of the infinite loop and closing of the window.
        if event.type == KEYDOWN:
            # Keys to move MacGyver (to the right, left, up and down),
            # calling the move method in mmg_classes.py.
            if event.key == K_RIGHT:
                macgyver.move('right', maze)
            elif event.key == K_LEFT:
                macgyver.move('left', maze)
            elif event.key == K_UP:
                macgyver.move('up', maze)
            elif event.key == K_DOWN:
                macgyver.move('down', maze)
    # Blitting the floor and the Maze (walls, jail, Murdoc and exit gate) at the top of the screen.
    screen.blit(FLOOR_IMAGE, (0, 0))
    maze.display_maze(screen)
    # Blitting the image of the 3 objects at their random position sorted out at mmg_classes.py.
    # By finding all "1" in the matrix and returning the tuple as the position of each object.
    if maze.matrix[needle.y][needle.x] == '1':
        screen.blit(needle.image_o, \
            (needle.x * Constants.SPRITE_DIM, needle.y * Constants.SPRITE_DIM))
    if maze.matrix[tube.y][tube.x] == '1':
        screen.blit(tube.image_o, \
            (tube.x * Constants.SPRITE_DIM, tube.y * Constants.SPRITE_DIM))
    if maze.matrix[potion.y][potion.x] == '1':
        screen.blit(potion.image_o, \
            (potion.x * Constants.SPRITE_DIM, potion.y * Constants.SPRITE_DIM))
    # While MacGyver is not at the Murdoc's place without the 3 objects, he can move.
    if maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] != '2': # '2' means MacGyver dies.
        # Blitting the new position of MacGyver + 5px to center the image in the sprite.
        screen.blit(macgyver.image, (macgyver.mg_x + 5, macgyver.mg_y))
    # Refreshing, updating the contents of the entire display (Maze, MacGyver, objects).
    pygame.display.flip()
    # Messages at the bottom of the screen.
    FONT_2 = pygame.font.Font(None, 30) # Default font with a size of 30 pixels.
    # Score : number of collected objects / number of existing objects.
    score_objects = f"Collected objects : {str(Agent.objects_collected)}/{str(Object.number)}"
    # To draw a smooth black text on a new white Surface.
    MESSAGE_SCORE = FONT_2.render(score_objects, True, (0, 0, 0), (255, 255, 255))
    # Blitting the updated score message on the screen at the bottom position (150, 635).
    screen.blit(MESSAGE_SCORE, (150, 635))
    # Final message at the end of the game depending on the success or the failure of MacGyver.
    MESSAGE_LOSE = FONT_2.render("Game Over ! MacGyver is dead.", True,\
        (0, 0, 0), (255, 255, 255))
    MESSAGE_WIN = FONT_2.render("Congratulations ! MacGyver is free.", True,\
        (0, 0, 0), (255, 255, 255))
    # End of the game when it's Game over.
    if maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] == '2': # '2' means MacGyver dies.
        screen.blit(MESSAGE_LOSE, (150, 635)) # Blitting the lose message.
        pygame.display.flip()  # Refreshing all the contents in order to see the lose message.
        pygame.time.wait(6000) # Pause the program for 6 seconds.
        cont = 0               # End of the infinite loop and closing of the window.
    # End of the game when it's a Victory.
    elif maze.matrix[macgyver.mg_pos_y][macgyver.mg_pos_x] == 'a':
        screen.blit(MESSAGE_WIN, (150, 635)) # Blitting the win message.
        pygame.display.flip()
        pygame.time.wait(6000)
        cont = 0
