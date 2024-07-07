# Week 1: Getting Started with Tron AI - A Step-by-Step Guide

Welcome to our Tron AI project! This week, we're setting up everything you need to start building an AI that plays Tron. Don't worry if you're new to this - we'll go through every step together.

Welcome to the AI Tron AI project, we're so glad you've decided to join us! This week, we're setting up everything you need to start building an AI that plays Tron. Don't worry if you're new to programming, 
we'll be going through each step together for this first week.


## 1. Understanding Tron

Before we dive into coding, let's understand the game we're working with.

**Task:** Play Tron online to familiarize yourself with the game mechanics.
1. Go to https://www.crazygames.com/game/fl-tron
2. Play a few rounds against the computer or a friend
3. Pay attention to:
   - How the light trails work
   - How collisions are handled
   - The strategies you use to avoid collisions and trap opponents


## 2. Setting Up Your Development Environment

Now, let's set up your computer for Python development. We will be using Pygame, OpenAI Gym, and Stable-Baselines3. Again don't worry if you don't know what these are, for today we'll only be using the Pygame library.


### 2.1 Installing Python

1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or later for your operating system
3. Run the installer
   - On Windows, make sure to check "Add Python to PATH"
4. Verify the installation:
   - Open a command prompt or terminal
   - Type `python --version` and press Enter
   - You should see the Python version number


### 2.2 Setting Up Your Repo

1. If you're the one making the repo go to ##LINK HERE##/fork and make a copy of the MSUAIClub/FINALREPONAME repo.
2. Go the that repo and click on the green code button and copy the link.
3. Go in the IDE of your choice and clone the repo by pasting the link you copied in the previous step. (if
you are using VS Code, you can do this by clicking the Clone Gite Repository button and pasting the link in the input field)


### 2.3 Setting Up Your Virtual Environment

Virtual environments help keep your projects organized. It allows you to install libraries and packages specific to this project without affecting your system's Python installation.

1. Open a command prompt or terminal in the folder where your repo is cloned.
2. Create a virtual environment:
   - On Windows:
     ```
     python -m venv venv
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     ```
3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```


### 2.4 Installing Required Libraries

Now that your virtual environment is active, let's install the necessary libraries.

1. Ensure you're in your project directory with the virtual environment activated
2. Install the libraries using pip:
   ```
   pip install pygame gym stable-baselines3
   ```
3. Verify the installations:
   ```
   pip list
   ```
   You should see pygame, gym, and stable-baselines3 in the list

## 3. Creating Your First Pygame Window

Let's write some code to create a basic Pygame window.

1. In the week1 folder of your project directory, open the file called `tron_game.py`
2. Copy and paste the following code:

```python
import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Tron Game")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black background

    # Draw a simple shape (a rectangle)
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 50, 30))  # Red rectangle

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
```

4. Save the file
5. Run the script:
   - Make sure you're in the week1 folder in your terminal:
     ```
     cd week1
     ```
   - In the terminal (with your virtual environment activated):
     ```
     python tron_game.py
     ```
   - You should see a window with a black background and a red rectangle

## 4. Understanding the Code

Let's break down what each part of the code does:

- `pygame.init()`: This initializes all pygame modules.
- `pygame.display.set_mode((WIDTH, HEIGHT))`: This creates the game window.
- The main game loop:
  - Checks for the quit event (closing the window)
  - Fills the screen with black
  - Draws a red rectangle
  - Updates the display
- `pygame.quit()`: This closes pygame when we exit the loop

## 5. Testing Your Code

Let's make sure your environment is set up correctly to ensure the coming weeks go smoothtly.

1. Make sure you're in the week1 folder in your terminal.
   ```
   cd week1
   ```
2. In the week1 folder of your project directory, open the file called `test.py`.
   ```
   python test.py
   ```
3. You should see the following output:
   ```
   pygame 2.5.2 (SDL 2.28.3, Python 3.11.4)
   Hello from the pygame community. https://www.pygame.org/contribute.html
   Test 1 passed: Pygame is installed and initialized successfully.
   Test 2 passed: Pygame window created successfully.
   Test 3 passed: OpenAI Gym and Stable-Baselines3 are installed.

   Tests passed: 3/3
   All tests passed! Your environment is set up correctly.
   ```

- Common Troubleshooting Tips
1. Make sure you've activated your virtual environment before running the script.
2. Make sure you're in the week1 folder in your terminal.
3. Make sure you've installed the libraries correctly, you can test this by running `pip list` in your terminal.
4. Please reach out to @aidangollan in the MSUAIClub Discord if you're having further trouble!

## Wrapping Up

By the end of this week, you should have:
1. Played Tron and understood its basic mechanics
2. Set up a Python development environment with a virtual environment
3. Installed Pygame, OpenAI Gym, and Stable-Baselines3
4. Created and run a basic Pygame window with a simple shape

## Bonus Challenge

Try modifying the Pygame window code to:
1. Change the window size
2. Change the background color
3. Draw a different shape or multiple shapes
4. Make a shape move across the screen

Next week, we'll start building the actual Tron game board and implementing game logic. Great job on getting everything set up!