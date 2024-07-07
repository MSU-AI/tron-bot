import pygame
from pygame.locals import *
from GameObjects import Snake
import time

class Game:
    def __init__(self, show):
        pygame.init()
        self.HEIGHT_GRID = 40
        self.WIDTH_GRID = 40
        self.TILE_SIZE = 15
        self.HEIGHT = self.HEIGHT_GRID * self.TILE_SIZE
        self.WIDTH = self.WIDTH_GRID * self.TILE_SIZE
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
        self.tick = 60
        self.frame_times = []

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

    def check_collisions(self):
        head1, head2 = self.snake1.cords[0], self.snake2.cords[0]
        
        if (head1[0] < 0 or head1[0] >= self.WIDTH or head1[1] < 0 or head1[1] >= self.HEIGHT or
            head2[0] < 0 or head2[0] >= self.WIDTH or head2[1] < 0 or head2[1] >= self.HEIGHT):
            return True

        if (self.snake1.check_self_col() or self.snake2.check_self_col()):
            return True

        if (tuple(head1) in self.snake2.cords_set or
            tuple(head2) in self.snake1.cords_set or
            head1 == head2):
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
            start_time = time.time()
            
            self.handle_input()
            self.snake1.change_dir(self.current_direction1)
            self.snake2.change_dir(self.current_direction2)
            self.snake1.move()
            self.snake2.move()
            
            if self.check_collisions():
                self.print_benchmark()
                return "Game Over"
            
            if self.show:
                self.draw()
            
            end_time = time.time()
            self.frame_times.append(end_time - start_time)
            
            self.clock.tick(self.tick)

    def print_benchmark(self):
        if sum(self.frame_times) == 0 or len(self.frame_times) == 0:
            print("No frames recorded")
            return
        
        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        fps = 1 / avg_frame_time
        print(f"Average frame time: {avg_frame_time:.6f} seconds")
        print(f"Average FPS: {fps:.2f}")

if __name__ == "__main__":
    game = Game(show=True)
    game.run()