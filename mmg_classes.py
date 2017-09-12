""" Classes for creating objects in the MacGyver Maze Game. """

import random

import pygame
from pygame.locals import *


class Maze:
    """ Creating the maze for the game with the maze_1 file, remplacing caracters with sprites """
    def __init__(self):
        """ Method to create the maze depending on the file. """
        self.matrix = []
        file = open('maze_1', 'r')
        for i in file:
            list_j = []      # generateur pour simplifier les 4 lignes qui suivent en une
            for car in i:
                list_j.append(car)
            self.matrix.append(list_j)

    def display_maze(self, screen):
        """ Method to display the level depending on the matrix. """
        # Loading of the images representing the Maze
        WALL = pygame.image.load("images/wall.png").convert()        # Wall tiles
        JAIL = pygame.image.load("images/jail.png").convert()        # Jail tile i.e. MacGyver's starting place
        FREEDOM = pygame.image.load("images/freedom.png").convert()  # MacGyver's leaving point
        MURDOC = pygame.image.load("images/murdoc.png").convert_alpha() # Murdoc's place i.e. freedom place
        # Game's locals for the size of the Maze
        SPRITE_SIDE = 15        # Number of sprites per side of the Maze
        SPRITE_SIZE = 40        # Size of the side of each sprite in pixels
        SIDE_SIZE = SPRITE_SIDE * SPRITE_SIZE   # Size of the Maze per side
        # Browsing the lists in the matrix
        line_number = 0
        for line in self.matrix:
            # Browsing the caracters of each list in the matrix
            column_number = 0
            for sprite in line:
                # Calculating the real position in pixels...
                x = column_number * SPRITE_SIZE
                y = line_number * SPRITE_SIZE
                # ... and blitting the right sprites at the right places
                if sprite == 'w':                       # w for wall
                    screen.blit(WALL, (x, y))
                elif sprite == 'j':                     # j for jail i.e. place of departure
                    screen.blit(JAIL, (x, y))
                elif sprite == 'f':                     # f for freedom i.e.  place of arrival
                    screen.blit(FREEDOM, (x, y))
                    screen.blit(MURDOC, (x + 4, y + 2))
                column_number += 1
            line_number += 1

    def objects_display(self, position):
        # Display in the Maze of the three objects : the needle, the tube and the potion
        # Loading of the image of the three objects
        self.needle = pygame.image.load("images/needle.png").convert_alpha()
        self.tube = pygame.image.load("images/tube.png").convert_alpha()
        self.potion = pygame.image.load("images/potion.png").convert_alpha()
		# Needle position in the Maze
        self.needle_pos = objects_display(needle_pos)
	    # Tube position in the Maze
        self.tube_pos = objects_display(tube_pos_x)
        # Potion position in the Maze
        self.potion_pos = objects_display(potion_pos)
        # Creation of a list of tuple of open space en the Maze
        objects_place = list(tuple(self.matrix))#[o][o]
        # Sort of 3 random numbers of the index of the objects_place
        rand_three = []
        while len(r) < 3:
            r = randint(0, len(objects_place) - 1)                	
            rand_three.append(r)
            if (rand_three[0] == rand_three[1]) or (rand_three[1] == rand_three[2]) or (rand_three[0] == rand_three[2]):
                rand_three.remove(r)
        # Assignment of one of the 3 random number to each object
        needle_rand = rand_three.pop()
        tube = rand_three.pop()
        potion_rand = rand_three.pop()
        # 
        needle_pos = objects_place[int(needle_rand)]
        tube_pos = objects_place[int(tube_rand)]
        potion_pos = objects_place[int(potion_rand)]
        # Display of the image of each object at the random place
        screen.blit(needle, needle_pos)
        screen.blit(tube, tube_pos)
        screen.blit(potion, potion_pos)


class Agent:
    """ Classe permettant de créer le personnage de MacGyver """
    def __init__(self, image=0, mg_pos_x=0, mg_pos_y=0, mg_x=0, mg_y=0):
        # Loading the image of MacGyver
        self.image = pygame.image.load("images/macgyver.png").convert_alpha()
        # MacGyver's position in the Maze in sprites and in pixels
        self.mg_pos_x = 0#find the index of 'j' in the matrix   # sprites x position of the jail in the Maze
        self.mg_pos_y = 0#find the index of 'j' in the matrix   # sprites y position of the jail in the Maze
        self.mg_x = 0#... * SIDE_SIZE          # sprites x position of the jail in the Maze in pixels
        self.mg_y = 0#... * SIDE_SIZE          # sprites y position of the jail in the Maze in pixels
 
    def move(self, direction):
        """ Method for MacGyver's moves """
        # Game's locals for the size of the Maze
        SPRITE_SIDE = 15        # Number of sprites per side of the Maze
        SPRITE_SIZE = 40        # Size of the side of each sprite in pixels
        SIDE_SIZE = SPRITE_SIDE * SPRITE_SIZE   # Size of the Maze per side
        # Move to the right
        if direction == 'right':
            # To avoid being out of screen
            if self.mg_pos_x < (SPRITE_SIDE - 1):
                # Checking for the wall
                if Maze().matrix[self.mg_pos_y][self.mg_pos_x + 1] != 'w':
                    # Move for one square
                    self.mg_pos_x += 1
                    # Calculation of the position in pixel
                    self.mg_x = self.mg_pos_x * SIDE_SIZE
                    # Checking presence of an object or freedom-Murdoc's sprite
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall
            #else:
                #send the sound wall.wav when hitting the border of the Maze
        # Move to the left
        if direction == 'left':
            if self.mg_pos_x > 0:
                if Maze().matrix[self.mg_pos_y][self.mg_pos_x - 1] != 'w':
                    self.mg_pos_x -= 1
                    self.mg_x = self.mg_pos_x * SIDE_SIZE
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall
            #else:
                #send the sound wall.wav when hitting the border of the Maze
        # Move up
        if direction == 'up':
            if self.mg_pos_y > 0:
                if Maze().matrix[self.mg_pos_y - 1][self.mg_pos_x - 1] != 'w':
                    self.mg_pos_y -= 1
                    self.mg_y = self.mg_pos_y * SIDE_SIZE
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall
            #else:
                #send the sound wall.wav when hitting the border of the Maze
        # Move down
        if direction == 'down':
            if self.mg_pos_y < (SPRITE_SIDE - 1):
                if Maze().matrix[self.mg_pos_y + 1][self.mg_pos_x] != 'w':
                    self.mg_pos_y += 1
                    self.mg_y = self.mg_pos_y * SIDE_SIZE
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall
            #else:
                #send the sound wall.wav when hitting the border of the Maze

    def collect(self, mg_x, mg_y):
        if (mg_pos_x, mg_pos_y) == (needle_pos):
            (needle_pos) = None
            objects_collected += 1
        elif (mg_pos_x, mg_pos_y) == (tube_pos):
            (tube_pos) = None
            objects_collected += 1
        elif (mg_pos_x, mg_pos_y) == (potion_pos):
            (potion_pos) = None
            objects_collected += 1

    def freedom(self):
        if (mg_pos_x, mg_pos_y) == (freedom_pos):
            if objects_collected == 3:
                pass
                # Murdoc meurt et le jeu s'arrête, MacGyver gagne
            else:
                pass
            	# MacGyver meurt et le jeu s'arrête



