# Week 4: Balancing Act - Teaching AI to Play Cart-Pole

Welcome to Week 4 of our Tron AI journey! This week, we're diving into the fascinating world of Deep Reinforcement Learning (DRL) by tackling a classic problem: balancing a pole on a moving cart. Don't worry if this sounds complex - we'll break it down step by step, using everyday examples to explain the concepts.

## Table of Contents
1. [Introduction to Deep Reinforcement Learning](#introduction-to-deep-reinforcement-learning)
2. [The Cart-Pole Problem](#the-cart-pole-problem-a-balancing-act)
3. [Building Our AI: Step by Step](#building-our-ai-step-by-step)
   - [Step 1: Setting Up the Environment](#step-1-setting-up-the-environment)
   - [Step 2: Creating Our AI Agent](#step-2-creating-our-ai-agent)
   - [Step 3: Putting It All Together](#step-3-putting-it-all-together)
4. [Running the Simulation](#running-the-simulation)
5. [Understanding the Results](#understanding-the-results)
6. [Conclusion and Next Steps](#conclusion-and-next-steps)

## Introduction to Deep Reinforcement Learning

Imagine you're teaching your little sister to ride a bike. You can't ride the bike for her, but you can give her tips and encouragement. When she keeps the bike upright, you cheer. When she wobbles or falls, you give her advice on how to improve. Over time, through trial and error and your feedback, she learns to balance and ride smoothly.

This is the essence of Reinforcement Learning:
1. Your sister is the **Agent** - the learner trying to master a skill.
2. The bike and the environment around her is the **Environment** - the world in which she's operating.
3. The position of the bike, its speed, the angle of lean, etc., is the **State** - the current situation.
4. Turning the handlebars, pedaling, leaning, etc., are **Actions** - things she can do to affect her state.
5. Your cheers or advice are the **Reward** - feedback on how well she's doing.

The "Deep" in Deep Reinforcement Learning comes from using Deep Neural Networks - think of these as a really smart, trainable calculator that can recognize patterns and make decisions.

## The Cart-Pole Problem: A Balancing Act

Now, let's look at our specific challenge: the Cart-Pole problem. Imagine you're at a carnival, and there's a game where you need to balance a broomstick on your palm. The broomstick is the pole, and your hand is the cart. You can move your hand left or right to keep the broomstick upright.

In our AI version:
- The **Agent** is our AI program.
- The **Environment** is a simulated world with a cart and a pole.
- The **State** includes the cart's position, its speed, the pole's angle, and how fast the pole is tipping.
- The **Actions** are moving the cart left or right.
- The **Reward** is +1 for each time step the pole stays upright.

Our goal is to create an AI that can keep the pole balanced for as long as possible.

## Building Our AI: Step by Step

Let's break down each part of our code and understand what it does.

### Step 1: Setting Up the Environment

Before we can teach our AI to balance a pole, we need to create a world for it to practice in. In the real world, we might build a physical cart with a pole. But in the world of AI, we can create a simulated environment on our computer. This is where the `gym` library comes in handy.

#### What is Gym?

`gym` is a toolkit for developing and comparing reinforcement learning algorithms. It provides a wide variety of simulated environments, from simple text-based games to complex physics simulations. Think of it as a massive virtual playground where AIs can learn and practice different skills.

In our case, we'll be using the Cart-Pole environment, which simulates a cart that can move left or right, with a pole balanced on top of it.

Let's break down the code step by step:

1. Create a new file called `cart_pole_env.py` and add the following code:

```python
# cart_pole_env.py
import gym
from gym.wrappers import FlattenObservation

def create_env(render_mode=None):
    env = gym.make('CartPole-v1', render_mode=render_mode)
    return FlattenObservation(env)
```

Now, let's explain each line:

```python
import gym
```
This line imports the gym library, giving us access to all its pre-built environments and tools.

```python
from gym.wrappers import FlattenObservation
```
Gym provides "wrappers" that can modify the behavior of environments. `FlattenObservation` is one such wrapper. We'll explain its purpose soon.

```python
def create_env(render_mode=None):
```
This line defines a function named `create_env`. The `render_mode` parameter is optional (that's what `=None` means) and determines how the environment will be displayed.

```python
env = gym.make('CartPole-v1', render_mode=render_mode)
```
This line creates our Cart-Pole environment. `gym.make()` is like a factory that produces environments. 'CartPole-v1' is the specific environment we want. The 'v1' means it's version 1 of the Cart-Pole environment.

```python
return FlattenObservation(env)
```
This line wraps our environment with `FlattenObservation`. But why do we need this?

#### Understanding FlattenObservation

In reinforcement learning, the AI needs to understand the current state of the environment to make decisions. This state information is often represented as a list of numbers.

Some environments provide this state information in a complex format, like a list of lists or a dictionary. `FlattenObservation` takes this complex format and "flattens" it into a simple list of numbers. This makes it easier for our AI to process the information.

Real-world analogy: Imagine you're teaching someone to ride a bike. Instead of giving them separate pieces of information like "the bike is leaning 5 degrees left, you're going 2 mph, the handlebars are turned 10 degrees right", you might simplify it to "you're about to fall to the left, pedal faster and turn right a bit". That's what `FlattenObservation` does - it simplifies the information for our AI.

#### Why This Matters

By setting up the environment this way, we're creating a consistent, simplified world for our AI to learn in. It's like creating a safe, flat area for a child to practice riding a bike, with clear markers and simple instructions. This setup allows our AI to focus on learning the core task (balancing the pole) without getting confused by complex environmental details.

In the next step, we'll create our AI agent that will learn to navigate this environment and balance the pole!

### Step 2: Creating Our AI Agent

Now that we have our environment set up, it's time to create our AI agent - the "brain" that will learn to balance the pole. We'll use a technique called Deep Q-Network (DQN), which combines deep learning (the "deep" part) with Q-learning (a type of reinforcement learning).

Let's break this down step by step:

#### 1. Setting Up the File

Create a new file called `dqn_agent.py` and add the following import statements at the top:

```python
import numpy as np
import random
from collections import deque
import tensorflow as tf
from keras import models, layers, optimizers
```

Let's explain each import:
- `numpy` (imported as `np`): A library for numerical computations. We'll use it for handling arrays and mathematical operations.
- `random`: Used for generating random numbers, which is important for exploration in reinforcement learning.
- `deque` from `collections`: A double-ended queue, which we'll use to store the agent's memories.
- `tensorflow`: A powerful machine learning library. We're using it as the backend for Keras.
- `models`, `layers`, and `optimizers` from `keras`: These are the building blocks we'll use to create our neural network.

#### 2. Creating the DQNAgent Class

Now, let's create our DQNAgent class:

```python
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0   # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()
        self.target_model = self._build_model()
        self.update_target_model()
```

This `__init__` method sets up our agent with all the necessary attributes:

- `state_size` and `action_size`: These define the "shape" of our problem - how much information the agent receives about the world, and how many different actions it can take.
- `memory`: This is like the agent's diary. It can store up to 2000 experiences that the agent can learn from later.
- `gamma`: This is the "discount rate". It determines how much the agent cares about future rewards compared to immediate rewards. A value of 0.95 means it cares quite a bit about the future.
- `epsilon`, `epsilon_min`, and `epsilon_decay`: These control the agent's exploration vs. exploitation behavior. We'll explain this more later.
- `learning_rate`: This determines how quickly the agent updates its knowledge based on new information.
- `model` and `target_model`: These are the neural networks that the agent will use to make decisions and learn. We use two models to make the learning process more stable.

Real-world analogy: Imagine you're setting up a new student to learn a skill. You give them a notebook (memory), teach them to value long-term success (gamma), encourage them to try new things but also to rely on what they know (epsilon), and give them a brain to process information (model and target_model).

#### 3. Building the Neural Network

Next, let's look at the `_build_model` method:

```python
def _build_model(self):
    model = models.Sequential([
        layers.Dense(24, activation='relu', input_dim=self.state_size),
        layers.Dense(24, activation='relu'),
        layers.Dense(self.action_size, activation='linear')
    ])
    model.compile(loss='mse', optimizer=optimizers.Adam(learning_rate=self.learning_rate))
    return model
```

This method creates a neural network:
- It's a "Sequential" model, which means the layers are stacked one after another.
- It has three "Dense" layers. Dense layers are fully connected, meaning each neuron in one layer is connected to every neuron in the next layer.
- The first two layers have 24 neurons each and use the 'relu' activation function, which helps the network learn complex patterns.
- The last layer has as many neurons as there are possible actions, allowing the network to estimate the value of each action.
- We compile the model with mean squared error (mse) as the loss function and Adam as the optimizer.

Real-world analogy: This is like creating a brain for our AI. The layers are like different levels of understanding, from basic recognition to complex decision-making.

#### 4. Remembering Experiences

The `remember` method is simple but crucial:

```python
def remember(self, state, action, reward, next_state, done):
    self.memory.append((state, action, reward, next_state, done))
```

This method stores a single experience in the agent's memory. Each experience includes:
- The current state
- The action taken
- The reward received
- The next state
- Whether the episode is done

Real-world analogy: This is like writing in a diary after each practice session, noting what you did, what happened, and how it turned out.

#### 5. Choosing Actions

The `act` method determines what action the agent will take:

```python
def act(self, state):
    if np.random.rand() <= self.epsilon:
        return random.randrange(self.action_size)
    act_values = self.model.predict(state, verbose=0)
    return np.argmax(act_values[0])
```

This method implements an "epsilon-greedy" strategy:
- With probability `epsilon`, the agent chooses a random action (exploration).
- Otherwise, it chooses the action that its model predicts will be best (exploitation).
- As training progresses, `epsilon` decreases, so the agent explores less and exploits more.

Real-world analogy: This is like deciding whether to try a new technique or stick with what you know when learning a skill. At first, you try lots of new things, but as you get better, you rely more on what you've learned works well.

#### 6. Learning from Experiences

The `replay` method is where the actual learning happens:

```python
def replay(self, batch_size):
    minibatch = random.sample(self.memory, batch_size)
    states = np.array([i[0] for i in minibatch]).reshape(-1, self.state_size)
    actions = np.array([i[1] for i in minibatch])
    rewards = np.array([i[2] for i in minibatch])
    next_states = np.array([i[3] for i in minibatch]).reshape(-1, self.state_size)
    dones = np.array([i[4] for i in minibatch])

    targets = rewards + self.gamma * np.amax(self.target_model.predict(next_states, verbose=0), axis=1) * (1 - dones)
    targets_full = self.model.predict(states, verbose=0)
    targets_full[np.arange(batch_size), actions] = targets

    self.model.fit(states, targets_full, epochs=1, verbose=0, batch_size=batch_size)

    if self.epsilon > self.epsilon_min:
        self.epsilon *= self.epsilon_decay
```

This method:
1. Samples a batch of experiences from memory.
2. Calculates the target Q-values using the Bellman equation.
3. Updates the model to better predict these target Q-values.
4. Decreases the exploration rate (epsilon) over time.

Real-world analogy: This is like reviewing your diary entries, figuring out what techniques worked best in different situations, and updating your strategy based on this review.

#### 7. Saving and Loading the Model

Finally, we have methods to save and load the model's weights:

```python
def load(self, name):
    self.model.load_weights(name)

def save(self, name):
    self.model.save_weights(name)
```

These methods allow us to save our agent's learned knowledge and reload it later, so we don't have to retrain from scratch every time.

Real-world analogy: This is like writing down everything you've learned in a book, so you can quickly refresh your memory later instead of having to relearn everything from the beginning.

In the next step, we'll put all of this together and actually train our agent to balance the pole!

### Step 3: Putting It All Together

Now that we have our environment (Step 1) and our AI agent (Step 2), it's time to bring everything together and actually train our AI to balance the pole. We'll do this in our main script.

Create a new file called `main.py` and let's break it down section by section:

#### 1. Importing Libraries and Suppressing Warnings

```python
import numpy as np
from cart_pole_env import create_env
from dqn_agent import DQNAgent
import time
import os
import tensorflow as tf

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
```

Here's what each import does:
- `numpy` (as `np`): For numerical operations.
- `create_env` from `cart_pole_env`: The function we created in Step 1 to set up our Cart-Pole environment.
- `DQNAgent` from `dqn_agent`: Our AI agent class from Step 2.
- `time`: We'll use this to add small delays in our visualization.
- `os` and `tensorflow`: These are used to suppress some warning messages that TensorFlow might produce.

The last two lines are just telling TensorFlow to be quiet and not print out a bunch of messages that might confuse us.

#### 2. Helper Functions

```python
def process_state(state):
    if isinstance(state, tuple):
        return np.concatenate(state).ravel()
    return state

def visualize_agent(env, agent, episode):
    state = env.reset()
    if isinstance(state, tuple):
        state = state[0]
    state = process_state(state)
    state = np.reshape(state, [1, state_size])
    
    total_reward = 0
    t = 0
    done = False
    
    while not done:
        env.render()
        action = np.argmax(agent.model.predict(state, verbose=0)[0])
        next_state, reward, done, truncated, _ = env.step(action)
        if isinstance(next_state, tuple):
            next_state = next_state[0]
        next_state = process_state(next_state)
        next_state = np.reshape(next_state, [1, state_size])
        state = next_state
        total_reward += reward
        t += 1
        
        time.sleep(0.02)  # Add a small delay to make the visualization visible
        
        if done or truncated:
            time.sleep(0.5)  # Pause briefly to show the final state
            break

    print(f"Visualization Episode {episode} lasted for {t} steps with total reward {total_reward}")
    env.close()  # Close the environment after the episode is done
```

The `process_state` function is a utility that ensures our state data is in the right format for our agent to use.

The `visualize_agent` function is more complex. It:
1. Resets the environment to start a new episode.
2. Runs the episode, letting the agent make decisions at each step.
3. Renders the environment so we can see what's happening.
4. Keeps track of how long the episode lasts and what the total reward is.
5. Adds small delays so the visualization isn't too fast for us to see.

Real-world analogy: This is like setting up a camera to record a student's bike-riding attempt, and then playing back the recording in slow motion so we can see exactly what happened.

#### 3. The Main Training Loop

```python
if __name__ == "__main__":
    env = create_env()
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)
    batch_size = 32
    EPISODES = 1000

    for e in range(EPISODES):
        state = env.reset()
        if isinstance(state, tuple):
            state = state[0]
        state = process_state(state)
        state = np.reshape(state, [1, state_size])
        total_reward = 0
        for cur_time in range(500):
            action = agent.act(state)
            next_state, reward, done, truncated, _ = env.step(action)
            done = done or truncated
            reward = reward if not done else -10
            next_state = process_state(next_state)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            if done:
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        agent.update_target_model()
        print(f"Episode: {e}/{EPISODES}, Score: {cur_time}, Total Reward: {total_reward}, Epsilon: {agent.epsilon:.2f}")

        # Visualize the agent's performance every 5 episodes
        if e % 5 == 0:
            vis_env = create_env(render_mode="human")  # Create a new environment for each visualization
            visualize_agent(vis_env, agent, e)
            vis_env.close()  # Ensure the environment is closed after visualization

        if e % 50 == 0:
            agent.save(f"cartpole-dqn-{e}.weights.h5")

    print("Training completed.")
```

This is where the magic happens. Let's break it down:

1. We create our environment and our agent, setting up the size of the state and action spaces.

2. We set up our training parameters:
   - `batch_size = 32`: This is how many experiences the agent will learn from at once.
   - `EPISODES = 1000`: This is how many full games (episodes) the agent will play.

3. We enter a big loop that runs for each episode:
   - We reset the environment to start a new game.
   - We run the game for up to 500 time steps or until it's over.
   - At each step, the agent chooses an action, we apply it to the environment, and we store this experience.
   - If the agent has enough memories, it learns from a batch of them.
   - We keep track of the total reward.

4. After each episode:
   - We update the agent's target model (this helps stabilize learning).
   - We print out information about how the episode went.
   - Every 5 episodes, we visualize the agent's performance.
   - Every 50 episodes, we save the agent's learned knowledge.

Real-world analogy: This is like setting up a series of bike-riding lessons. Each episode is one lesson. During each lesson, the student (our agent) tries to ride the bike many times. After each attempt, they remember what happened. When they have enough memories, they reflect on them to try to improve. After each lesson, we make a note of how they did. Every so often, we record a video of their attempt, and periodically we write down everything they've learned so far.

#### Running the Simulation

To run this simulation:

1. Make sure you have all the required libraries installed. You can do this with pip:
   ```
   pip install gym numpy tensorflow
   ```

2. Put all three Python files (`cart_pole_env.py`, `dqn_agent.py`, and `main.py`) in the same directory.

3. Run the main script:
   ```
   python main.py
   ```

4. Watch as your AI learns to balance the pole!

As the simulation runs, you'll see output like this:

```
Episode: 0/1000, Score: 17, Total Reward: 17.0, Epsilon: 0.98
Episode: 1/1000, Score: 23, Total Reward: 23.0, Epsilon: 0.97
Episode: 2/1000, Score: 15, Total Reward: 15.0, Epsilon: 0.96
...
```

- **Episode**: The current training session number.
- **Score**: How many steps the pole stayed balanced.
- **Total Reward**: The total reward received (in this case, equal to the score).
- **Epsilon**: The exploration rate. It starts high (lots of random actions) and decreases over time (more calculated actions).

Every 5 episodes, you'll see a visualization of how the AI is performing. At first, it might drop the pole quickly, but over time, it should learn to keep it balanced for longer periods.

Congratulations! You've just built and trained an AI to balance a pole on a cart. This is a great introduction to the world of Deep Reinforcement Learning. Remember, learning AI is a journey. It's okay if some concepts are still fuzzy - they'll become clearer with practice and experience. Keep experimenting, asking questions, and most importantly, have fun with it!

## Running the Simulation

To run the simulation:

1. Make sure you have the required libraries installed. You can install them using pip:
   ```
   pip install gym numpy tensorflow
   ```

2. Save the three Python files (`cart_pole_env.py`, `dqn_agent.py`, and `main.py`) in the same directory.

3. Run the main script:
   ```
   python main.py
   ```

4. Watch as your AI learns to balance the pole!

## Understanding the Results

As the simulation runs, you'll see output like this:

```
Episode: 0/1000, Score: 17, Total Reward: 17.0, Epsilon: 0.98
Episode: 1/1000, Score: 23, Total Reward: 23.0, Epsilon: 0.97
Episode: 2/1000, Score: 15, Total Reward: 15.0, Epsilon: 0.96
...
```

- **Episode**: The current training session number.
- **Score**: How many steps the pole stayed balanced.
- **Total Reward**: The total reward received (in this case, equal to the score).
- **Epsilon**: The exploration rate. It starts high (lots of random actions) and decreases over time (more calculated actions).

Every 5 episodes, you'll see a visualization of how the AI is performing. At first, it might drop the pole quickly, but over time, it should learn to keep it balanced for longer periods.

## Conclusion and Next Steps

Congratulations! You've just built an AI that can learn to balance a pole on a cart. This is a great introduction to the world of Deep Reinforcement Learning.

Remember, learning AI is a journey. It's okay if some concepts are still fuzzy - they'll become clearer with practice and experience. Keep experimenting, asking questions, and most importantly, have fun with it!

### Bonus Challenges

If you're feeling adventurous, here are some ways to extend your Cart-Pole AI:

1. Try modifying the reward structure. What happens if you give a bigger penalty for dropping the pole?
2. Experiment with different neural network architectures. What if you add more layers or change the number of neurons?