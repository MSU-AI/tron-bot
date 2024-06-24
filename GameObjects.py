import pygame
import random
import copy
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen, parent_width, parent_height):
        self.parent_screen = parent_screen
        cords = (random.randint(0,parent_width - 1) * 50, random.randint(0,parent_height - 1) * 50)
        self.cords = [list(cords)]
        self.cords_set = {cords}
        self.directions = [[0,0]]
        self.length = 1
        self.block = pygame.image.load("block.png").convert()
        self.possible_cords = set()
        for i in range(parent_width - 1):
            for j in range(parent_height - 1):
                self.possible_cords.add((i * 50, j * 50))
        self.open_cords = self.possible_cords - self.cords_set

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.cords[i][0], self.cords[i][1]))

    def change_dir(self, dir):
        if not (self.directions[0][0] == -1 * dir[0] and self.directions[0][1] == -1 * dir[1]):
            self.directions[0] = list(dir)
    
    def update_dir(self):
        previous_directions = copy.deepcopy(self.directions)
        for i in range(1, self.length):
            self.directions[i][0] = previous_directions[i-1][0]
            self.directions[i][1] = previous_directions[i-1][1]
    
    def move(self):
        self.cords_set.clear()
        previous_positions = copy.deepcopy(self.cords)
        self.cords[0][0] += self.directions[0][0] * 50
        self.cords[0][1] += self.directions[0][1] * 50
        self.cords_set.add(tuple(self.cords[0]))
        for i in range(1, self.length):
            self.cords[i][0] = previous_positions[i-1][0]
            self.cords[i][1] = previous_positions[i-1][1]
            self.cords_set.add(tuple(self.cords[i]))
        self.update_dir()
        self.open_cords = self.possible_cords - self.cords_set
        return previous_positions

    def check_self_col(self, previous_positions):
        for i in range(1, self.length):
            if self.cords[0] == previous_positions[i]:
                return True
        return False

    def add_length(self):
        self.cords.append([self.directions[-1][0] * -50, self.directions[-1][1] * -50])
        self.cords_set.add(tuple(self.cords[-1]))
        self.directions.append(copy.deepcopy(self.directions)[-1])
        self.open_cords = self.possible_cords - self.cords_set
        self.length += 1

class Apple:
    def __init__(self, parent_screen, parent_width, parent_height):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("apple.png").convert()
        self.cords = (random.randint(0,parent_width - 1) * 50, random.randint(0,parent_height - 1) * 50)
        self.parent_screen.blit(self.block, (self.cords[0], self.cords[1]))

    def draw(self):
        self.parent_screen.blit(self.block, (self.cords[0], self.cords[1]))

    def update_pos(self, open_cords):
        self.cords = random.choice(list(open_cords))
    
    def check_col(self, snake_cords, open_cords):
        col = self.cords == tuple(snake_cords[0])
        if col:
            self.update_pos(open_cords)
        return col