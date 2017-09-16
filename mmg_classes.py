""" Classes for creating objects in the MacGyver Maze Game """

import random

import pygame
from pygame.locals import *


class Constants:
    """ Game's locals for the size of the Maze """
    SPRITE_NUM = 15        # Number of sprites per side of the Maze.
    SPRITE_DIM = 40        # Dimension of the side of each sprite in pixels.
    SIDE_DIM = SPRITE_DIM * SPRITE_NUM   # Dimension of the Maze per side.


class Maze:
    """ Creating the matrix (list of list) based on the maze_1 file """ 
    def __init__(self):
        """ Method to create the maze depending on the file """
        self.matrix = []
        file = open('maze_1', 'r')
        for i in file:
            j = []      # generateur pour simplifier les 4 lignes qui suivent en une ?
            for car in i:
                j.append(car)
            self.matrix.append(j)

    def display_maze(self, screen):
        """ Method to create and display the Maze based on the matrix """
        # Loading of the images representing the Maze.
        WALL = pygame.image.load("images/wall.png").convert()        # Wall tiles.
        JAIL = pygame.image.load("images/jail.png").convert()        # Jail tile i.e. MacGyver's starting place.
        FREEDOM = pygame.image.load("images/freedom.png").convert()  # MacGyver's leaving point.
        MURDOC = pygame.image.load("images/murdoc.png").convert_alpha() # Murdoc's place i.e. freedom place.
        # Browsing the lists in the matrix.
        line_number = 0
        for line in self.matrix:
            # Browsing the caracters of each list in the matrix.
            column_number = 0
            for sprite in line:
                # Calculating the real position in pixels...
                x = column_number * Constants().SPRITE_DIM
                y = line_number * Constants().SPRITE_DIM
                # ... and blitting the right sprites at the right places.
                if sprite == 'w':                       # w for wall.
                    screen.blit(WALL, (x, y))
                elif sprite == 'j':                     # j for jail i.e. place of departure.
                    screen.blit(JAIL, (x, y))
                elif sprite == 'f':                     # f for freedom i.e.  place of arrival.
                    screen.blit(FREEDOM, (x, y))
                    screen.blit(MURDOC, (x + 4, y + 2))
                column_number += 1
            line_number += 1


class Object:
    def __init__(self, image_file, my_maze):
        # Image attribut (by loading) for the 3 objects : needle, tube and potion.
        self.image = pygame.image.load(image_file).convert_alpha()
        # Find a place at random, in the Maze, for the three objects.
        objects_num = 0
        while objects_num < 3:                  
            self.x = random.randint(0, len(my_maze.matrix) - 1)
            self.y = random.randint(0, len(my_maze.matrix) - 1)
            if my_maze.matrix[self.x][self.y] == 'o':
                my_maze.matrix[self.x][self.y] = '1'
                objects_num += 1
        print(my_maze.matrix) ## A SUPPRIMER
        #### Il fait 3 matrix car il y a 3 instances !
        

class Agent:
    """ Classe permettant de créer le personnage de MacGyver """
    def __init__(self, image_mg):
        # Loading the image of MacGyver.
        self.image = pygame.image.load(image_mg).convert_alpha()
        # MacGyver's position in the Maze in sprites and in pixels.
        self.mg_pos_x = 0#find the index of 'j' in the matrix   # sprites x position of the jail in the Maze.
        self.mg_pos_y = 0#find the index of 'j' in the matrix   # sprites y position of the jail in the Maze.
        self.mg_x = 0#... * SIDE_SIZE          # sprites x position of the jail in the Maze in pixels.
        self.mg_y = 0#... * SIDE_SIZE          # sprites y position of the jail in the Maze in pixels.
 
    def move(self, direction, my_maze):
        """ Method for MacGyver's moves """
        # Move to the right.
        if direction == 'right':
            # To avoid being out of screen.
            if self.mg_pos_x < (Constants().SPRITE_NUM - 1):
                # Checking for the wall.
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] != 'w':
                    # Move for one sprite.
                    self.mg_pos_x += 1
                    # Calculation of the position in pixel.
                    self.mg_x = self.mg_pos_x * Constants().SPRITE_DIM
                    # Checking presence of an object or freedom-Murdoc's sprite.
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall.
            #else:
                #send the sound wall.wav when hitting the border of the Maze.
        # Move to the left
        if direction == 'left':
            if self.mg_pos_x > 0:
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] != 'w':
                    self.mg_pos_x -= 1
                    self.mg_x = self.mg_pos_x * Constants().SPRITE_DIM
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall.
            #else:
                #send the sound wall.wav when hitting the border of the Maze.
        # Move up
        if direction == 'up':
            if self.mg_pos_y > 0:
                if my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] != 'w':
                    self.mg_pos_y -= 1
                    self.mg_y = self.mg_pos_y * Constants().SPRITE_DIM
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall.
            #else:
                #send the sound wall.wav when hitting the border of the Maze.
        # Move down
        if direction == 'down':
            if self.mg_pos_y < (Constants().SPRITE_NUM - 1):
                if my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] != 'w':
                    self.mg_pos_y += 1
                    self.mg_y = self.mg_pos_y * Constants().SPRITE_DIM
                    #freedom((self.mg_x, self.mg_y))
                    #collect((self.mg_x, self.mg_y))
                #else:
                    #send the sound wall.wav when hitting a wall.
            #else:
                #send the sound wall.wav when hitting the border of the Maze.

####### A REVOIR
    #def collect(self, mg_x, mg_y):
        #objects_collected = 0
        #if (mg_x, mg_y) == '1' in the matrix:
            #matrix[x,y] = mg
            #objects_collected += 1

    #def freedom(self):
        #if (mg_pos_x, mg_pos_y) == 'f' dans la matrix:
            #if objects_collected == 3:
                #pass
                # Murdoc meurt et le jeu s'arrête, MacGyver gagne.
            #else:
                #pass
            	# MacGyver meurt et le jeu s'arrête.