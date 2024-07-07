# Week 2: Building Your Tron Game

Welcome back, this week, we're transforming our Pygame window into a basic version of Tron. We'll focus on creating a modular structure and provide test code for each component to help you verify your implementation.


## Your Mission This Week

1. Set up the game board
2. Create a player that responds to input
3. Implement basic collision detection

Let's break these down into specific functions and modules:


### 1. Setting Up the Game Board (game_board.py)

Create a `GameBoard` class with the following methods:

```python
class GameBoard:
    def __init__(self, width, height):
        """
        Initialize the game board.
        :param width: Width of the game board in grid cells
        :param height: Height of the game board in grid cells
        """
        # TODO: Initialize a 2D list to represent the game board
        # 0 can represent empty cells, 1 for player trails

    def draw(self, screen):
        """
        Draw the game board on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Iterate through the 2D list and draw rectangles for each cell
        # Empty cells can be one color, trails another

    def is_collision(self, x, y):
        """
        Check if the given coordinates collide with the board boundaries or a trail.
        :param x: X-coordinate to check
        :param y: Y-coordinate to check
        :return: True if collision, False otherwise
        """
        # TODO: Check if x and y are within board boundaries
        # Also check if the cell at (x, y) is not empty (i.e., has a trail)
```

**Tips:**
- Use a 2D list to represent your game board
- Each cell in your grid could be represented by a number (0 for empty, 1 for player, 2 for trail)
- Use Pygame's drawing functions to visualize this grid on the screen

**Resources:**
- Pygame drawing functions: https://www.pygame.org/docs/ref/draw.html
- 2D lists in Python: https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/

### 2. Creating a Player-Controlled 'Bike' (player.py)

Create a `Player` class with the following methods:

```python
class Player:
    def __init__(self, x, y, color):
        """
        Initialize the player.
        :param x: Initial x-coordinate
        :param y: Initial y-coordinate
        :param color: Color of the player's trail
        """
        # TODO: Set initial position, color, direction (e.g., [1, 0] for right)
        # Initialize an empty list for the player's trail

    def move(self):
        """
        Move the player based on their current direction.
        """
        # TODO: Update the player's position based on their direction
        # Add the new position to the trail

    def change_direction(self, direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        # TODO: Update the player's direction
        # Ensure the new direction is not opposite to the current direction

    def draw(self, screen):
        """
        Draw the player and their trail on the screen.
        :param screen: Pygame screen object to draw on
        """
        # TODO: Draw the player's current position and their entire trail
```

**Tips:**
- Store the player's position, direction, and trail
- Use Pygame's event handling to capture keyboard input in your main game loop
- Update the player's position based on their direction

**Resources:**
- Pygame event handling: https://www.pygame.org/docs/ref/event.html
- Pygame color objects: https://www.pygame.org/docs/ref/color.html

### 3. Implementing the Main Game Loop (tron_game.py)

Create the following functions in your main game file:

```python
def initialize_game():
    """
    Initialize Pygame and create the game window.
    :return: Pygame screen object
    """
    # TODO: Initialize Pygame
    # Create and return a Pygame screen object

def handle_events(player):
    """
    Handle Pygame events, including player input.
    :param player: Player object to update based on input
    :return: False if the game should quit, True otherwise
    """
    # TODO: Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction

def update_game_state(player, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    # TODO: Move the player
    # Check for collisions with game_board
    # Update game_board with new player position

def draw_game(screen, game_board, player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    # TODO: Clear the screen
    # Draw the game board
    # Draw the player
    # Update the display

def main():
    """
    Main game loop.
    """
    # TODO: Initialize the game
    # Create game objects (game_board, player)
    # Run the game loop:
    #   - Handle events
    #   - Update game state
    #   - Draw game
    #   - Control game speed
```

**Tips:**
- Use Pygame's clock to control the game speed
- Implement collision detection in the `update_game_state` function
- Create a game over state when a collision is detected

**Resources:**
- Pygame display module: https://www.pygame.org/docs/ref/display.html
- Pygame time module (for controlling game speed): https://www.pygame.org/docs/ref/time.html

## Testing Your Implementation

We've provided test files for each component in the `tests/` directory. After implementing each part, run the corresponding test (Make sure you're in the week2 directory):

1. For GameBoard: `python tests/test_game_board.py`
2. For Player: `python tests/test_player.py`
3. For the main game: `python tests/test_tron_game.py`

These tests will help you verify that your implementation meets the basic requirements. However, remember that passing all tests doesn't guarantee a perfect game - always test by playing it yourself too!

## Bringing It All Together

Your task is to implement these functions and create a basic, playable version of Tron. Here's a general flow of how your game should work:

1. Initialize the game (create window, game board, and player)
2. Enter the game loop:
   - Handle events (player input)
   - Update game state (move player, check for collisions)
   - Draw the game
   - Control game speed
3. End the game when a collision is detected

Remember, the goal is to understand these concepts deeply. Focus on getting the core functionality working, and don't worry if it doesn't look exactly like a polished Tron game yet.

## Bonus Challenges

If you finish early or want to push yourself:

1. Implement a scoring system
2. Add a "game over" screen with the option to restart

Next week, we'll expand on this foundation to create a two-player version and start thinking about how we'll integrate our AI. Keep up the great work!