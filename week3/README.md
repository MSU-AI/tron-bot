# Week 3: Expanding Tron to Two Players

Welcome to Week 3 of our Tron game development! This week, we'll be expanding our single-player Tron game into a two-player version. We'll modify our existing codebase to accommodate two players, update the collision detection, and implement separate controls for each player.

## Your Mission This Week

1. Modify the GameBoard class to support two players
2. Update the Player class to distinguish between two players
3. Implement two-player controls and game logic in the main game loop
4. Refine collision detection for two players

Let's break these down into specific steps for each file:

### 1. Modifying the GameBoard (game_board.py)

Update the `GameBoard` class to support two players:

1. In the `draw` method, add logic to use different colors for each player's trail. Think about how you can represent different players in your grid (e.g., using different numbers).

2. Consider if any changes are needed in the `is_collision` method to accommodate two players.

### 2. Updating the Player (player.py)

Modify the `Player` class to accommodate two players:

1. Add a `player_id` parameter to the `__init__` method. How can you use this to differentiate between players?

2. Update the initial direction based on the player_id. For example, player 1 could start moving right, and player 2 could start moving left.

3. Consider if any changes are needed in the `draw` method to use the player's unique color.

### 3. Implementing Two-Player Game Logic (tron_game.py)

Update the main game file to handle two players:

1. Modify the `handle_events` function to accept two players and implement separate controls. Think about which keys each player should use.

2. Update the `update_game_state` function to handle both players. Consider the following:
   - How will you move both players?
   - How will you check for collisions for both players?
   - What should happen if both players collide simultaneously?

3. Modify the `draw_game` function to draw both players.

4. Update the `main` function to create and manage two players.

### 4. Refining Collision Detection

The current collision detection might allow players to move through each other. To fix this:

1. In the `update_game_state` function, think about the order of operations:
   - Should you move the players first, then check for collisions?
   - Or should you check where the players are about to move, then update if it's safe?

2. Consider adding a check for head-on collisions where both players move into the same cell.

## Testing Your Implementation

After implementing these changes, test your game thoroughly. Verify that:

1. Two players appear on the screen with different colors.
2. Each player can be controlled independently with different keys.
3. Collisions are detected correctly for both players.
4. The game ends appropriately when one or both players collide.

## Bringing It All Together

Your task this week is to implement these changes and create a functional two-player version of Tron. Here's a general flow of how your updated game should work:

1. Initialize the game (create window, game board, and two players)
2. Enter the game loop:
   - Handle events (input for both players)
   - Update game state (move both players, check for collisions)
   - Draw the game (board and both players)
   - Control game speed
3. End the game when a collision is detected, announcing the winner or a draw

Remember to test thoroughly and ensure that both players can control their characters independently.

## Bonus Challenges

If you finish early or want to push yourself:

1. Implement a score system that keeps track of wins for each player across multiple rounds
2. Add power-ups that temporarily change game mechanics (e.g., speed boost, ability to pass through walls once)
3. Create an AI opponent for single-player mode

Next week, we'll start thinking about how to integrate AI into our Tron game. Keep up the excellent work!