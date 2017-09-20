""" Classes for creating objects in the MacGyver Maze Game. """

import random

import pygame
from pygame.locals import *


class Constants:
    """ Game's locals for the size of the Maze. """

    SPRITE_NUM = 15        # Number of sprites per side of the Maze.
    SPRITE_DIM = 40        # Dimension of the side of each sprite in pixels.
    SIDE_DIM = SPRITE_DIM * SPRITE_NUM   # Dimension of the Maze per side.
    #COLLECT_SOUND = pygame.mixer.Sound("sounds/collect.m4a") # Sound when collecting an object.
    #DEATH_SOUND = pygame.mixer.Sound("sounds/death.m4a") # Sound when MacGyver dies.
    #FREEDOM_SOUND = pygame.mixer.Sound("sounds/freedom.m4a") # Sound when MacGyver is free.
    #WALL_SOUND = pygame.mixer.Sound("sounds/wall.m4a") # Sound when hitting the walls of the maze.


class Maze:
    """ Creating the matrix (list of list) based on the maze_1 file. """

    def __init__(self):
        """ Constructor to create the maze depending on the file. """
        self.matrix = []
        file = open('maze_1', 'r')
        for i in file:
            j = []
            for car in i:
                j.append(car)
            self.matrix.append(j)

    def display_maze(self, screen):
        """ Method to create and display the Maze based on the matrix. """
        # Loading of the images representing the Maze.
        WALL = pygame.image.load("images/wall.png").convert() # Wall tiles.
        JAIL = pygame.image.load("images/jail.png").convert() # Jail : MacGyver's starting point.
        FREEDOM = pygame.image.load("images/freedom.png").convert() # MacGyver's leaving point.
        MURDOC = pygame.image.load("images/murdoc.png").convert_alpha() # Murdoc's : freedom place.
        # Browsing the lists in the matrix.
        line_number = 0
        for line in self.matrix:
            # Browsing the caracters of each list in the matrix.
            column_number = 0
            for sprite in line:
                # Calculating the real position in pixels...
                x = column_number * Constants.SPRITE_DIM
                y = line_number * Constants.SPRITE_DIM
                # ... and blitting the right sprites at the right places.
                if sprite == 'w':          # 'w' for wall.
                    screen.blit(WALL, (x, y))
                elif sprite == 'j':        # 'j' for jail i.e. place of departure.
                    screen.blit(JAIL, (x, y))
                # 'f' for freedom i.e. arrival and '2' when MacGyver comes without 3 objects.
                elif sprite == 'f' or sprite == '2':
                    screen.blit(FREEDOM, (x, y))
                    screen.blit(MURDOC, (x + 4, y + 2))
                elif sprite == 'a': # 'a' i.e. arrival place without Murdoc (who is dead !).
                    screen.blit(FREEDOM, (x, y))
                column_number += 1
            line_number += 1


class Object:
    """ Class to create the three objects for MacGyver to collect. """

    # Number of objects created.
    number = 0

    def __init__(self, image_file, my_maze):
        """ Constructor to create the objects : by loading and positioning at random. """
        self.image_o = pygame.image.load(image_file).convert_alpha()
        # Find a place at random, in the Maze, for the needle, the tube and the potion.
        num = 0
        while num < 1:
            self.x = random.randint(0, len(my_maze.matrix) - 1)
            self.y = random.randint(0, len(my_maze.matrix) - 1)
            if my_maze.matrix[self.y][self.x] == 'o':
                my_maze.matrix[self.y][self.x] = '1'
                num += 1
                Object.number += 1


class Agent:
    """ Class to create MacGyver. """

    objects_collected = 0

    def __init__(self, image_mg, my_maze):
        """ Constructor to create MacGyver : loading and positioning. """
        self.image = pygame.image.load(image_mg).convert_alpha()
        # MacGyver's position in the Maze in sprites and in pixels.
        self.mg_pos_y = 0 ###my_maze.matrix.index('j')
        self.mg_pos_x = 0 ###my_maze.matrix.index(index('j'))
        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM

    def move(self, direction, my_maze):
        """ Method for MacGyver's moves. """
        # Move to the right.
        if direction == 'right':
            # To avoid being out of screen.
            if self.mg_pos_x < (Constants.SPRITE_NUM - 1):
                # Checking for the wall.
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] != 'w':
                    # Checking the presence of an object.
                    if my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] == '1':
                        # Move for one sprite.
                        self.mg_pos_x += 1
                        # Calculation of the position in pixel.
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                        # Cancelling the object by replacing the '1' by an 'o' in the matrix.
                        my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'o'
                        # Sending the sound collect.m4a when an object is collected by MacGyver.
                        #pygame.mixer.Sound.play(Constants.COLLECT_SOUND)
                        # Adding a new collected object
                        Agent.objects_collected += 1
                    elif my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] == 'f':
                        self.mg_pos_x += 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                        # Checking how many objects MacGyver collected when on the freedom sprite.
                        if Agent.objects_collected == 3:
                            # Sending the sound freedom.m4a for MacGyver's victory.
                            #pygame.mixer.Sound.play(Constants.FREEDOM_SOUND)
                            # Murdoc dies and disappear, MacGyver wins.
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'a'
                        else:
                            # MacGyver dies and disappear, Murdoc stays and wins.
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = '2'
                            # Sending the sound death.m4a for MacGyver's failure.
                            #pygame.mixer.Sound.play(Constants.DEATH_SOUND)
                    else:
                        self.mg_pos_x += 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                else:
                    # Sending the sound wall.m4a when hitting a wall.
                    #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                    pass
            else:
                # Sending the sound wall.m4a when hitting the border of the Maze.
                #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                pass

        # Move to the left
        if direction == 'left':
            if self.mg_pos_x > 0:
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] != 'w':
                    if my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] == '1':
                        self.mg_pos_x -= 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                        my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'o'
                        #pygame.mixer.Sound.play(Constants.COLLECT_SOUND)
                        Agent.objects_collected += 1
                    elif my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] == 'f':
                        self.mg_pos_x -= 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                        if Agent.objects_collected == 3:
                            #pygame.mixer.Sound.play(Constants.FREEDOM_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'a'
                        else:
                            #pygame.mixer.Sound.play(Constants.DEATH_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = '2'
                    else:
                        self.mg_pos_x -= 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                else:
                    #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                    pass
            else:
                #pygame.mixer.Sound.play(Constants.WALL_SOUND
                pass

        # Move up
        if direction == 'up':
            if self.mg_pos_y > 0:
                if my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] != 'w':
                    if my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] == '1':
                        self.mg_pos_y -= 1
                        self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM
                        my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'o'
                        #pygame.mixer.Sound.play(Constants.COLLECT_SOUND)
                        Agent.objects_collected += 1
                    elif my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] == 'f':
                        self.mg_pos_y -= 1
                        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM
                        if Agent.objects_collected == 3:
                            #pygame.mixer.Sound.play(Constants.FREEDOM_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'a'
                        else:
                            #pygame.mixer.Sound.play(Constants.DEATH_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = '2'
                    else:
                        self.mg_pos_y -= 1
                        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM
                else:
                    #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                    pass
            else:
                #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                pass

        # Move down
        if direction == 'down':
            if self.mg_pos_y < (Constants.SPRITE_NUM - 1):
                if my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] != 'w':
                    if my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] == '1':
                        self.mg_pos_y += 1
                        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM
                        my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'o'
                        #pygame.mixer.Sound.play(Constants.COLLECT_SOUND)
                        Agent.objects_collected += 1
                    elif my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] == 'f':
                        self.mg_pos_y += 1
                        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM
                        if Agent.objects_collected == 3:
                            #pygame.mixer.Sound.play(Constants.FREEDOM_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'a'
                        else:
                            #pygame.mixer.Sound.play(Constants.DEATH_SOUND)
                            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = '2'
                    else:
                        self.mg_pos_y += 1
                        self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM
                else:
                    #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                    pass
            else:
                #pygame.mixer.Sound.play(Constants.WALL_SOUND)
                pass
