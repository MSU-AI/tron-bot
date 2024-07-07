import pygame
import random

class Snake:
    def __init__(self, parent_screen, parent_width, parent_height, tile_size, color):
        self.parent_screen = parent_screen
        self.tile_size = tile_size
        self.color = color
        cords = (random.randint(0, parent_width - 1) * tile_size, 
                 random.randint(0, parent_height - 1) * tile_size)
        self.cords = [list(cords)]
        self.cords_set = {cords}
        self.directions = [[1, 0]]

    def draw(self):
        for cord in self.cords:
            pygame.draw.rect(self.parent_screen, self.color, 
                             (cord[0], cord[1], self.tile_size, self.tile_size))

    def change_dir(self, dir):
        if not (self.directions[0][0] == -1 * dir[0] and self.directions[0][1] == -1 * dir[1]):
            self.directions[0] = list(dir)
    
    def move(self):
        new_head = [self.cords[0][0] + self.directions[0][0] * self.tile_size,
                    self.cords[0][1] + self.directions[0][1] * self.tile_size]
        self.cords.insert(0, new_head)
        return self.cords

    def check_self_col(self):
        return tuple(self.cords[0]) in set(map(tuple, self.cords[1:]))

    def get_length(self):
        return len(self.cords)

    def update_cords_set(self):
        self.cords_set = set(map(tuple, self.cords))