import os
import sys
import pytest
import pygame
from unittest.mock import Mock, patch

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from tron_game import (
    initialize_game,
    handle_events,
    update_game_state,
    draw_game,
    main
)
from player import Player
from game_board import GameBoard

@pytest.fixture
def mock_pygame():
    with patch('tron_game.pygame') as mock:
        yield mock

@pytest.fixture
def mock_screen():
    return Mock()

@pytest.fixture
def mock_game_board():
    mock = Mock(spec=GameBoard)
    mock.grid = [[0 for _ in range(40)] for _ in range(30)]  # Create a 2D list to mimic the real grid
    return mock

@pytest.fixture
def mock_player1():
    return Mock(spec=Player, player_id=1)

@pytest.fixture
def mock_player2():
    return Mock(spec=Player, player_id=2)

def test_initialize_game(mock_pygame, mock_screen):
    mock_pygame.display.set_mode.return_value = mock_screen
    result = initialize_game()
    assert result == mock_screen
    mock_pygame.init.assert_called_once()
    mock_pygame.display.set_mode.assert_called_once_with((800, 600))
    mock_pygame.display.set_caption.assert_called_once_with("Tron Game")

def test_handle_events_quit(mock_pygame):
    mock_pygame.QUIT = pygame.QUIT
    mock_pygame.event.get.return_value = [Mock(type=pygame.QUIT)]
    result = handle_events(Mock(), Mock())
    assert result == False

@pytest.mark.parametrize("key, player, direction", [
    (pygame.K_UP, "player1", [0, -1]),
    (pygame.K_DOWN, "player1", [0, 1]),
    (pygame.K_LEFT, "player1", [-1, 0]),
    (pygame.K_RIGHT, "player1", [1, 0]),
    (pygame.K_w, "player2", [0, -1]),
    (pygame.K_s, "player2", [0, 1]),
    (pygame.K_a, "player2", [-1, 0]),
    (pygame.K_d, "player2", [1, 0]),
])
def test_handle_events_movement(mock_pygame, key, player, direction):
    mock_pygame.KEYDOWN = pygame.KEYDOWN
    mock_pygame.K_UP, mock_pygame.K_DOWN, mock_pygame.K_LEFT, mock_pygame.K_RIGHT = pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
    mock_pygame.K_w, mock_pygame.K_s, mock_pygame.K_a, mock_pygame.K_d = pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
    mock_pygame.event.get.return_value = [Mock(type=pygame.KEYDOWN, key=key)]
    player1 = Mock()
    player2 = Mock()
    result = handle_events(player1, player2)
    assert result == True
    if player == "player1":
        player1.change_direction.assert_called_once_with(direction)
    else:
        player2.change_direction.assert_called_once_with(direction)

def test_update_game_state_no_collision(mock_game_board, mock_player1, mock_player2):
    mock_game_board.is_collision.return_value = False
    mock_player1.x, mock_player1.y = 5, 5
    mock_player2.x, mock_player2.y = 15, 15
    mock_player1.direction = [1, 0]
    mock_player2.direction = [-1, 0]
    mock_player1.player_id = 1
    mock_player2.player_id = 2
    
    result = update_game_state(mock_player1, mock_player2, mock_game_board)
    
    assert result == 0
    mock_player1.move.assert_called_once()
    mock_player2.move.assert_called_once()
    
    # Check if the grid was updated for both players
    assert mock_game_board.grid[mock_player1.y][mock_player1.x] == mock_player1.player_id
    assert mock_game_board.grid[mock_player2.y][mock_player2.x] == mock_player2.player_id

def test_update_game_state_collision_player1(mock_game_board, mock_player1, mock_player2):
    mock_game_board.is_collision.side_effect = [True, False]
    mock_player1.x, mock_player1.y = 5, 5
    mock_player2.x, mock_player2.y = 15, 15
    mock_player1.direction = [1, 0]
    mock_player2.direction = [-1, 0]
    result = update_game_state(mock_player1, mock_player2, mock_game_board)
    assert result == 1

def test_update_game_state_collision_player2(mock_game_board, mock_player1, mock_player2):
    mock_game_board.is_collision.side_effect = [False, True]
    mock_player1.x, mock_player1.y = 5, 5
    mock_player2.x, mock_player2.y = 15, 15
    mock_player1.direction = [1, 0]
    mock_player2.direction = [-1, 0]
    result = update_game_state(mock_player1, mock_player2, mock_game_board)
    assert result == 2

def test_update_game_state_draw(mock_game_board, mock_player1, mock_player2):
    mock_game_board.is_collision.return_value = True
    mock_player1.x, mock_player1.y = 5, 5
    mock_player2.x, mock_player2.y = 15, 15
    mock_player1.direction = [1, 0]
    mock_player2.direction = [-1, 0]
    result = update_game_state(mock_player1, mock_player2, mock_game_board)
    assert result == 3

@patch('tron_game.pygame.display.flip')
def test_draw_game(mock_flip, mock_screen, mock_game_board, mock_player1, mock_player2):
    draw_game(mock_screen, mock_game_board, mock_player1, mock_player2)
    mock_screen.fill.assert_called_once_with((0, 0, 0))
    mock_game_board.draw.assert_called_once_with(mock_screen)
    mock_player1.draw.assert_called_once_with(mock_screen)
    mock_player2.draw.assert_called_once_with(mock_screen)
    mock_flip.assert_called_once()

@patch('tron_game.initialize_game')
@patch('tron_game.GameBoard')
@patch('tron_game.Player')
@patch('tron_game.handle_events')
@patch('tron_game.update_game_state')
@patch('tron_game.draw_game')
@patch('tron_game.pygame.time.Clock')
def test_main(mock_clock, mock_draw, mock_update, mock_handle, mock_player, mock_board, mock_init):
    mock_screen = Mock()
    mock_init.return_value = mock_screen
    mock_board.return_value = Mock()
    mock_player.side_effect = [Mock(), Mock()]
    mock_clock.return_value = Mock()
    
    # Simulate game loop running twice, then ending
    mock_handle.side_effect = [True, True, False]
    mock_update.side_effect = [0, 0, 2]  # Added one more update call
    
    main()
    
    mock_init.assert_called_once()
    mock_board.assert_called_once_with(40, 30)
    assert mock_player.call_count == 2
    assert mock_handle.call_count == 3
    assert mock_update.call_count == 2
    assert mock_draw.call_count == 3  # Updated to expect 3 calls
    mock_clock.return_value.tick.assert_called_with(10)

if __name__ == "__main__":
    pytest.main()