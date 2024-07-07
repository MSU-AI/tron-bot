import pygame

class Player:
    def __init__(self, x, y, color):
        """
        Initialize the player.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param color: Color of the player's trail
        """
        self.x = x
        self.y = y
        self.color = color
        self.direction = [1, 0]
        self.trail = [(x, y)]

    def move(self):
        """
        Move the player based on their current direction.
        """
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.trail.append((self.x, self.y))

    def change_direction(self, direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        if self.direction[0] * direction[0] + self.direction[1] * direction[1] == 0:
            self.direction = direction

    def draw(self, screen):
        """
        Draw the player and their trail on the screen.
        :param screen: Pygame screen object to draw on
        """
        for x, y in self.trail:
            pygame.draw.rect(screen, self.color, 
                             (x * 20, y * 20, 20, 20))