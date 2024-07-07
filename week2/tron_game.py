import pygame
from game_board import GameBoard
from player import Player

def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tron Game")
    return screen

def handle_events(player):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.change_direction([0, -1])
            elif event.key == pygame.K_DOWN:
                player.change_direction([0, 1])
            elif event.key == pygame.K_LEFT:
                player.change_direction([-1, 0])
            elif event.key == pygame.K_RIGHT:
                player.change_direction([1, 0])
    return True

def update_game_state(player, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    player.move()
    if game_board.is_collision(player.x, player.y):
        return False
    game_board.grid[player.y][player.x] = 1
    return True

def draw_game(screen, game_board, player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    screen.fill((0, 0, 0))
    game_board.draw(screen)
    player.draw(screen)
    pygame.display.flip()

def main():
    """
    Main game loop.
    """
    screen = initialize_game()
    game_board = GameBoard(40, 30)
    player = Player(20, 15, (255, 0, 0))
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events(player)
        if running:
            running = update_game_state(player, game_board)
        draw_game(screen, game_board, player)
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()