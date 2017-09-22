""" Classes for creating objects in the MACGYVER MAZE GAME. """

# Importation of the module random of PYTHON 3.
import random

# Importation of the PYGAME Library and locals.
import pygame
from pygame.locals import *

# Initialization of the mixer module of PYGAME with the right frequency to play the soundtrack.
pygame.mixer.init(frequency=44100)


class Constants:
    """ Game's constants for the size of the Maze and the 4 sounds. """

    SPRITE_NUM = 15    # Number of sprites per side of the Maze.
    SPRITE_DIM = 40    # Dimension in pixels of the side of each sprite.
    SIDE_DIM = SPRITE_DIM * SPRITE_NUM # Dimension in pixels of the Maze per side.
    COLLECT_SOUND = pygame.mixer.Sound("sounds/collect.wav") # Sound when collecting an object.
    DEATH_SOUND = pygame.mixer.Sound("sounds/death.wav")     # Sound when MacGyver dies.
    FREEDOM_SOUND = pygame.mixer.Sound("sounds/freedom.wav") # Sound when MacGyver is free.
    WALL_SOUND = pygame.mixer.Sound("sounds/wall.wav") # Sound when hitting the walls of the maze.


class Maze:
    """ Creating the matrix (list of list) based on the maze_1 file and the maze to display. """

    def __init__(self):
        """ Constructor to create the matrix depending on the file. """
        self.matrix = [] # Cration of the attribut matrix.
        file = open('maze_1', 'r') # To open and read the file maze_1 in order to build the maze.
        for i in file:  # Iteration in the file maze_1.
            j = [] # Creation of a list.
            for car in i:
                j.append(car) # Fill up a list with each item per line in the file.
            self.matrix.append(j) # Add each new list in the matrix (list of list).

    def display_maze(self, screen):
        """ Method to create and display the Maze based on the matrix. """
        # Loading of the images representing the Maze.
        WALL = pygame.image.load("images/wall.png").convert() # Wall tiles.
        JAIL = pygame.image.load("images/jail.png").convert() # Jail i.e. MacGyver's starting point.
        FREEDOM = pygame.image.load("images/freedom.png").convert() # Freedom = MG's leaving point.
        MURDOC = pygame.image.load("images/murdoc.png").convert_alpha() # Murdoc's = freedom place.
        # Browsing the lists in the matrix.
        line_number = 0 # List index in the matrix = line number in the maze.
        for line in self.matrix: # Iteration of each list in the matrix.
            # Browsing the caracters within of each list in the matrix.
            column_number = 0 # Index of each item in the list = column number in the maze.
            for sprite in line:
                # Calculating the real position in pixels...
                x = column_number * Constants.SPRITE_DIM
                y = line_number * Constants.SPRITE_DIM
                # ... and blitting the right sprites at the right places.
                if sprite == 'w':          # 'w' for wall.
                    screen.blit(WALL, (x, y))
                elif sprite == 'j':        # 'j' for jail i.e. place of departure.
                    screen.blit(JAIL, (x, y))
                # 'f' for freedom i.e. arrival and '2' when MacGyver arrives without the 3 objects.
                elif sprite == 'f' or sprite == '2':
                    screen.blit(FREEDOM, (x, y)) # Arrival and...
                    screen.blit(MURDOC, (x + 4, y + 2)) # Murdoc stand at the same place.
                # At the Agent class will be created a new item in the matrix : 'a'.
                elif sprite == 'a': # 'a' (arrival place) without Murdoc who has been put to sleep.
                    screen.blit(FREEDOM, (x, y)) # Here only the freedom place is blitted.
                column_number += 1
            line_number += 1


class Object:
    """ Class to create the three objects for MacGyver to collect. """

    # Number of objects created.
    number = 0 # Class variable to count the number of objects created.

    def __init__(self, image_file, my_maze):
        """ Constructor to create the objects : by loading and positioning at random. """
        # The attribut use the image of the instance created in mmg_game.py.
        self.image_o = pygame.image.load(image_file).convert_alpha()
        # Find a place at random, in the Maze, for the needle, the tube and the potion.
        num = 0
        while num < 1: # One iteration to create only one "1" in the matrix for each instance.
            # Using the random module, find a random integer for x and y.
            self.x = random.randint(0, len(my_maze.matrix) - 1) # Number not higher than the...
            self.y = random.randint(0, len(my_maze.matrix) - 1) # items in each line in the maze.
            # The random tuple (x, y) representing the position of the object...
            # must point an open place in the maze (i.e. 'o'). Otherwise, starts another iteration.
            if my_maze.matrix[self.y][self.x] == 'o': # When the place in the maze is empty...
                my_maze.matrix[self.y][self.x] = '1' # the object ("1") can be put.
                num += 1 # Enough object for one instance (only 1, than the iteration stops).
                Object.number += 1 # A new object is created.


class Agent:
    """ Class to create MacGyver. """

    objects_collected = 0 # Class variable to count the number of collected objects.

    def __init__(self, image_mg, my_maze):
        """ Constructor to create MacGyver : loading and positioning. """
        # The attribut use the image of the instance created in mmg_game.py.
        self.image = pygame.image.load(image_mg).convert_alpha()
        # Searching for the 'j' position in the Maze (MacGyver's place at the start of the game).
        for i in range(len(my_maze.matrix)):
            if 'j' in my_maze.matrix[i]: # When the place of 'j' is found in the matrix then...
                # MacGyver's position in the Maze in sprites and in pixels.
                self.mg_pos_y = i # list index in the matrix, corresponding to the line number (y).
                self.mg_pos_x = my_maze.matrix[i].index('j') # index of 'j' in that list (x).
                self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM # X position in pixels.
                self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM # Y position in pixels.

    def move(self, direction, my_maze):
        """ Method for MacGyver's moves. """

        def move_right():
            """ Function to move MacGyver to the right. """
            self.mg_pos_x += 1 # Move for one sprite right.
            self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM # Position in pixels.

        def move_left():
            """ Function to move MacGyver to the left. """
            self.mg_pos_x -= 1 # Move for one sprite left.
            self.mg_x = self.mg_pos_x * Constants.SPRITE_DIM # Position in pixels.

        def move_up():
            """ Function to move MacGyver up. """
            self.mg_pos_y -= 1 # Move for one sprite up.
            self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM # Position in pixels.

        def move_down():
            """ Function to move MacGyver down. """
            self.mg_pos_y += 1 # Move for one sprite down.
            self.mg_y = self.mg_pos_y * Constants.SPRITE_DIM # Position in pixels.

        def collect_func():
            """ Function for the object collection """
            # Canceling the object by replacing the '1' by an 'o' in the matrix.
            my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'o' # MG's position when collecting.
            # Sending the sound collect.wav when an object is collected.
            Constants.COLLECT_SOUND.play()
            # Adding a new collected object
            Agent.objects_collected += 1

        def arrival_func():
            """ Function dealing with MacGyver arrival at the exit gate """
            # Checking how many objects MacGyver collected when reaching the freedom sprite.
            if Agent.objects_collected == 3: # MacGyver is ready to put to sleep Murdoc !
                # Sending the sound freedom.wav for MacGyver's victory.
                Constants.FREEDOM_SOUND.play()
                # Murdoc is put to sleep and disappears, MacGyver wins.
                my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = 'a' # Adds 'a' item in the matrix.
            else: # MacGyver forgot to collect 1, 2 or 3 objects.
                # MacGyver dies and disappear, Murdoc stays and wins.
                my_maze.matrix[self.mg_pos_y][self.mg_pos_x] = '2' # Adds '2' item in the matrix.
                # Sending the sound death.wav for MacGyver's failure.
                Constants.DEATH_SOUND.play()

        # Move to the right.
        if direction == 'right': # Parameter sent by mmg_game.py when MacGyver is moving.
            # To avoid being out of the maze.
            if self.mg_pos_x < (Constants.SPRITE_NUM - 1):
                # Checking that MG is not hitting a wall ('w' in the matrix).
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] != 'w':
                    # Checking the presence of an object ("1").
                    if my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] == '1':
                        move_right() # Calling the function that moves MacGyver one sprite right.
                        collect_func() # Calling the function that manages the object collection.
                    # Checking the presence of the freedom place ("f").
                    elif my_maze.matrix[self.mg_pos_y][self.mg_pos_x + 1] == 'f':
                        move_right()
                        arrival_func() # Calling the function that manages the exit of MacGyver.
                    else:
                        move_right()
                else:
                    Constants.WALL_SOUND.play() # Sending the sound when hitting a wall.

            else:
                Constants.WALL_SOUND.play() # Sending the sound when hitting the border of the Maze.

        # Move to the left (same comments than above).
        if direction == 'left':
            if self.mg_pos_x > 0:
                if my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] != 'w':
                    if my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] == '1':
                        move_left() # Calling the function that moves MacGyver one sprite left.
                        collect_func()
                    elif my_maze.matrix[self.mg_pos_y][self.mg_pos_x - 1] == 'f':
                        move_left()
                        arrival_func()
                    else:
                        move_left()
                else:
                    Constants.WALL_SOUND.play()
            else:
                Constants.WALL_SOUND.play()

        # Move up (same comments than above).
        if direction == 'up':
            if self.mg_pos_y > 0:
                if my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] != 'w':
                    if my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] == '1':
                        move_up() # Calling the function that moves MacGyver one sprite up.
                        collect_func()
                    elif my_maze.matrix[self.mg_pos_y - 1][self.mg_pos_x] == 'f':
                        move_up()
                        arrival_func()
                    else:
                        move_up()
                else:
                    Constants.WALL_SOUND.play()
            else:
                Constants.WALL_SOUND.play()

        # Move down (same comments than above).
        if direction == 'down':
            if self.mg_pos_y < (Constants.SPRITE_NUM - 1):
                if my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] != 'w':
                    if my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] == '1':
                        move_down() # Calling the function that moves MacGyver one sprite down.
                        collect_func()
                    elif my_maze.matrix[self.mg_pos_y + 1][self.mg_pos_x] == 'f':
                        move_down()
                        arrival_func()
                    else:
                        move_down()
                else:
                    Constants.WALL_SOUND.play()
            else:
                Constants.WALL_SOUND.play()
