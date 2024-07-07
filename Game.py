import pygame
import numpy as np
from pygame.locals import *
from GameObjects import Snake

class Game:
    def __init__(self, show):
        pygame.init()
        self.HEIGHT_GRID = 40
        self.WIDTH_GRID = 40
        self.TILE_SIZE = 15
        self.HEIGHT = self.HEIGHT_GRID * self.TILE_SIZE
        self.WIDTH = self.WIDTH_GRID * self.TILE_SIZE
        self.font = pygame.font.Font(None, 32)
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.snake1 = Snake(self.surface, self.WIDTH_GRID, self.HEIGHT_GRID, self.TILE_SIZE, (255, 0, 0))
        self.snake2 = Snake(self.surface, self.WIDTH_GRID, self.HEIGHT_GRID, self.TILE_SIZE, (0, 0, 255))
        self.clock = pygame.time.Clock()
        self.directions1 = {
            K_UP: (0, -1),
            K_DOWN: (0, 1),
            K_LEFT: (-1, 0),
            K_RIGHT: (1, 0)
        }
        self.directions2 = {
            K_w: (0, -1),
            K_s: (0, 1),
            K_a: (-1, 0),
            K_d: (1, 0)
        }
        self.current_direction1 = self.directions1[K_RIGHT]
        self.current_direction2 = self.directions2[K_d]
        self.show = show
        self.tick = 10

    def handle_input(self):
        for event in pygame.event.get():  
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key in self.directions1:
                    self.current_direction1 = self.directions1[event.key]
                elif event.key in self.directions2:
                    self.current_direction2 = self.directions2[event.key]

    def check_wall_col(self, snake):
        head = snake.cords[0]
        if head[0] < 0 or head[0] >= self.WIDTH or head[1] < 0 or head[1] >= self.HEIGHT:
            return True
        return False

    def check_snake_collision(self, snake1, snake2):
        head1 = snake1.cords[0]
        head2 = snake2.cords[0]
        # Check if snake1's head collides with snake2's body
        if tuple(head1) in set(map(tuple, snake2.cords)):
            return True
        # Check if snake2's head collides with snake1's body
        if tuple(head2) in set(map(tuple, snake1.cords)):
            return True
        # Check if snakes' heads collide with each other
        if head1 == head2:
            return True
        return False

    def draw(self):
        self.surface.fill((110, 110, 5))
        self.snake1.draw()
        self.snake2.draw()
        pygame.display.update()

    def run(self):
        if self.show:
            self.draw()
        while True:
            self.handle_input()
            self.snake1.change_dir(self.current_direction1)
            self.snake2.change_dir(self.current_direction2)
            self.snake1.move()
            self.snake2.move()
            
            if (self.check_wall_col(self.snake1) or self.snake1.check_self_col() or
                self.check_wall_col(self.snake2) or self.snake2.check_self_col() or
                self.check_snake_collision(self.snake1, self.snake2)):
                return "Game Over"
            
            self.snake1.update_cords_set()
            self.snake2.update_cords_set()
            
            if self.show:
                self.draw()
                self.clock.tick(self.tick)

if __name__ == "__main__":
    game = Game(show=True)
    game.run()