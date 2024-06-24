import pygame
import numpy as np
from util import print_grid
from pygame.locals import *
from GameObjects import Snake, Apple

class Game:
    def __init__(self, show):
        pygame.init()
        self.HEIGHT_GRID = 20
        self.WIDTH_GRID = 20
        self.HEIGHT = (self.HEIGHT_GRID * 50) - 50
        self.WIDTH = (self.WIDTH_GRID * 50) - 50        
        self.score = 0
        self.fitness = 0
        self.font = pygame.font.Font(None, 32)
        self.surface = pygame.display.set_mode((self.WIDTH_GRID * 50, self.HEIGHT_GRID * 50))
        self.score_surf = self.font.render(str(self.score), False, (64, 64, 64))
        self.score_rect = self.score_surf.get_rect(center = (self.WIDTH_GRID * 25, 50))
        self.snake = Snake(self.surface, self.WIDTH_GRID, self.HEIGHT_GRID)
        self.apple = Apple(self.surface, self.WIDTH_GRID, self.HEIGHT_GRID)
        self.clock = pygame.time.Clock()
        self.directions = {
            K_UP: (0, -1),
            K_DOWN: (0, 1),
            K_LEFT: (-1, 0),
            K_RIGHT: (1, 0)
        }
        self.current_direction = self.directions[K_RIGHT]
        self.show = show
        self.max_frames = 300
        self.frames = 0
        self.tick = 3

    def handle_quit(self):
        for event in pygame.event.get():  
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN and event.key in self.directions:
                self.current_direction = self.directions[event.key]

    def display_score(self):
        self.score_surf = self.font.render(str(self.score), False, (64, 64, 64))
        self.score_rect = self.score_surf.get_rect(center = (self.WIDTH_GRID * 25, 50))
        self.surface.blit(self.score_surf, self.score_rect)

    def check_wall_col(self):
        if self.snake.cords[0][0] < 0 or self.snake.cords[0][0] > self.WIDTH:
            return True
        elif self.snake.cords[0][1] < 0 or self.snake.cords[0][1] > self.HEIGHT:
            return True
        return False

    def draw(self):
        self.surface.fill((110, 110, 5))
        self.apple.draw()
        self.snake.draw()
        self.display_score()
        pygame.display.update()

    def run(self):
        if self.show:
            self.draw()
        while True:
            self.handle_quit()
            self.snake.change_dir(self.current_direction)
            previous_positions = self.snake.move()
            if self.check_wall_col() or self.snake.check_self_col(previous_positions):
                return self.fitness
            hit = self.apple.check_col(self.snake.cords, self.snake.open_cords)
            if hit:
                self.score += 1
                self.fitness += 100
                self.frames = 0
            if self.show:
                self.draw()
                self.clock.tick(self.tick)
            if hit:
                self.snake.add_length()
            self.fitness -= 1
            self.frames += 1
            if self.frames > self.max_frames:
                return 0

# Example usage:
if __name__ == "__main__":
    game = Game(show=True)
    game.run()
