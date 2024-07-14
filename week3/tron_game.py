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

def handle_events(player1, player2):
    """
    Handle Pygame events, including player input.
    :param player1: Player object for player 1
    :param player2: Player object for player 2
    :return: False if the game should quit, True otherwise
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.change_direction([0, -1])
            elif event.key == pygame.K_DOWN:
                player1.change_direction([0, 1])
            elif event.key == pygame.K_LEFT:
                player1.change_direction([-1, 0])
            elif event.key == pygame.K_RIGHT:
                player1.change_direction([1, 0])
            elif event.key == pygame.K_w:
                player2.change_direction([0, -1])
            elif event.key == pygame.K_s:
                player2.change_direction([0, 1])
            elif event.key == pygame.K_a:
                player2.change_direction([-1, 0])
            elif event.key == pygame.K_d:
                player2.change_direction([1, 0])
    return True

def update_game_state(player1, player2, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player1: Player object for player 1
    :param player2: Player object for player 2
    :param game_board: GameBoard object to check collisions against
    :return: 0 if the game continues, 1 if player 1 loses, 2 if player 2 loses, 3 if it's a draw
    """
    # Store the next positions
    next_x1, next_y1 = player1.x + player1.direction[0], player1.y + player1.direction[1]
    next_x2, next_y2 = player2.x + player2.direction[0], player2.y + player2.direction[1]
    
    # Check for collisions at the next positions
    collision1 = game_board.is_collision(next_x1, next_y1)
    collision2 = game_board.is_collision(next_x2, next_y2)
    
    # Check for head-on collision
    head_on_collision = (next_x1, next_y1) == (next_x2, next_y2)
    
    if head_on_collision:
        return 3  # It's a draw
    elif collision1 and collision2:
        return 3  # It's a draw
    elif collision1:
        return 1  # Player 1 loses
    elif collision2:
        return 2  # Player 2 loses
    
    # If no collisions, update the positions
    player1.move()
    player2.move()
    
    # Update the game board
    game_board.grid[player1.y][player1.x] = 1
    game_board.grid[player2.y][player2.x] = 2
    
    return 0

def draw_game(screen, game_board, player1, player2):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player1: Player object for player 1
    :param player2: Player object for player 2
    """
    screen.fill((0, 0, 0))
    game_board.draw(screen)
    player1.draw(screen)
    player2.draw(screen)
    pygame.display.flip()

def main():
    """
    Main game loop.
    """
    screen = initialize_game()
    game_board = GameBoard(40, 30)
    player1 = Player(10, 15, (255, 0, 0), 1)
    player2 = Player(30, 15, (0, 0, 255), 2)
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events(player1, player2)
        if running:
            result = update_game_state(player1, player2, game_board)
            if result != 0:
                running = False
                if result == 1:
                    print("Player 2 wins!")
                elif result == 2:
                    print("Player 1 wins!")
                else:
                    print("It's a draw!")
        draw_game(screen, game_board, player1, player2)
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()