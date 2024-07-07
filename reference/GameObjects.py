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
        self.direction = [1, 0]
        self.rect = pygame.Rect(cords[0], cords[1], tile_size, tile_size)

    def draw(self):
        for cord in self.cords:
            self.rect.topleft = cord
            pygame.draw.rect(self.parent_screen, self.color, self.rect)

    def change_dir(self, new_dir):
        if not (self.direction[0] == -new_dir[0] and self.direction[1] == -new_dir[1]):
            self.direction = list(new_dir)
    
    def move(self):
        new_head = [self.cords[0][0] + self.direction[0] * self.tile_size,
                    self.cords[0][1] + self.direction[1] * self.tile_size]
        self.cords.insert(0, new_head)
        self.cords_set.add(tuple(new_head))

    def check_self_col(self):
        return tuple(self.cords[0]) in set(map(tuple, self.cords[1:]))

    def get_length(self):
        return len(self.cords)