import pygame
import sys
import os
import pytest
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from player import Player

@pytest.fixture
def player():
    return Player(10, 10, (255, 0, 0), 1)

def test_player_initialization(player):
    assert player.x == 10 and player.y == 10, "Player position not set correctly"
    assert player.color == (255, 0, 0), "Player color not set correctly"
    assert player.player_id == 1, "Player ID not set correctly"
    assert player.direction == [1, 0], "Player 1 should start moving right"
    assert player.trail == [(10, 10)], "Player trail should be initialized with starting position"

def test_player_initialization_player2():
    player2 = Player(30, 15, (0, 0, 255), 2)
    assert player2.direction == [-1, 0], "Player 2 should start moving left"

def test_move(player):
    initial_x, initial_y = player.x, player.y
    player.move()
    assert player.x == initial_x + 1, "Player should move right"
    assert player.y == initial_y, "Player y-coordinate should not change"
    assert (player.x, player.y) in player.trail, "New position should be added to trail"

@pytest.mark.parametrize("initial_dir,new_dir,expected", [
    ([1, 0], [0, 1], [0, 1]),
    ([1, 0], [0, -1], [0, -1]),
    ([1, 0], [-1, 0], [1, 0]),  # Can't reverse direction
    ([0, 1], [1, 0], [1, 0]),
    ([0, -1], [-1, 0], [-1, 0])
])
def test_change_direction(player, initial_dir, new_dir, expected):
    player.direction = initial_dir
    player.change_direction(new_dir)
    assert player.direction == expected, f"Direction should change from {initial_dir} to {expected}"

def test_draw(player):
    pygame.init()
    screen = pygame.Surface((400, 300))
    player.trail = [(10, 10), (11, 10), (12, 10)]
    player.draw(screen)
    
    for x, y in player.trail:
        assert screen.get_at((x * 20, y * 20)) == player.color, f"Trail cell at {(x, y)} not drawn correctly"

def test_reset(player):
    player.move()
    player.move()
    player.reset(15, 15)
    assert player.x == 15 and player.y == 15, "Player position not reset correctly"
    assert player.trail == [(15, 15)], "Player trail not reset correctly"
    assert player.direction == [1, 0] if player.player_id == 1 else [-1, 0], "Player direction not reset correctly"

if __name__ == "__main__":
    pytest.main([__file__])