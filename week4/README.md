# Week 4: Balancing Act - Teaching AI to Play Cart-Pole

Welcome to Week 4 of our Tron AI journey! This week, we're diving into the fascinating world of Deep Reinforcement Learning (DRL) by tackling a classic problem: balancing a pole on a moving cart. Don't worry if this sounds complex - we'll break it down step by step, using everyday examples to explain the concepts.

## What is Deep Reinforcement Learning?

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

### Step 1: Setting Up the Environment (cart_pole_env.py)

```python
import gym
from gym.wrappers import FlattenObservation

def create_env(render_mode=None):
    env = gym.make('CartPole-v1', render_mode=render_mode)
    return FlattenObservation(env)
```

This code sets up our Cart-Pole world:
- We use the `gym` library, which provides a variety of pre-built environments for reinforcement learning.
- `gym.make('CartPole-v1')` creates our Cart-Pole environment.
- `FlattenObservation` is like making sure all the information about the game is laid out neatly for our AI to understand.

Real-world analogy: This is like setting up a practice area for bike riding, with safety gear and a flat surface.

### Step 2: Creating Our AI Agent (dqn_agent.py)

Now, let's create our AI agent - the player who's going to learn to balance the pole. We'll use something called a Deep Q-Network (DQN).

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

This initializes our AI agent:
- `memory`: This is like the AI's memory, storing past experiences to learn from.
- `gamma`: This determines how much the AI cares about future rewards vs. immediate rewards.
- `epsilon`: This controls how often the AI tries new things vs. sticking to what it knows.
- `model` and `target_model`: These are our smart notebooks. We use two to help the AI learn more stably.

Real-world analogy: This is like setting up a learner with a notebook to write down experiences, a way to remember important lessons, and a strategy for when to try new things.

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

This creates our neural network - our smart calculator that will learn to predict the best actions.

Real-world analogy: This is like creating a brain for our AI, with different layers representing different levels of understanding, from basic recognition to complex decision-making.

```python
def remember(self, state, action, reward, next_state, done):
    self.memory.append((state, action, reward, next_state, done))

def act(self, state):
    if np.random.rand() <= self.epsilon:
        return random.randrange(self.action_size)
    act_values = self.model.predict(state, verbose=0)
    return np.argmax(act_values[0])
```

- `remember`: This stores experiences in the AI's memory.
- `act`: This decides what action to take based on the current state.

Real-world analogy: `remember` is like writing in a diary after each bike riding session. `act` is like deciding whether to try a new technique or stick with what you know.

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

This is where the AI learns from its past experiences.

Real-world analogy: This is like reviewing your diary entries about bike riding, figuring out what techniques worked best, and updating your riding strategy based on this review.

### Step 3: Putting It All Together (main.py)

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

def process_state(state):
    if isinstance(state, tuple):
        return np.concatenate(state).ravel()
    return state
```

This sets up our main script and includes a helper function to process the state information.

Real-world analogy: This is like setting up your practice area and making sure you have all your gear ready.

```python
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

This function visualizes how our AI is performing.

Real-world analogy: This is like watching a video replay of your bike riding session, seeing how long you managed to ride and how well you did.

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

This is the main training loop where our AI learns to balance the pole.

Real-world analogy: This is like setting up a series of bike riding practice sessions. Each episode is a practice session where you try to ride the bike, learn from your mistakes, and gradually improve your skills. The visualization every 5 episodes is like recording a video of your progress every so often to see how you're improving.

## Conclusion

By building this Cart-Pole balancing AI, we've taken our first steps into the world of Deep Reinforcement Learning. We've seen how an AI can learn from experience, gradually improving its performance on a task through trial and error, much like humans do.

Remember, learning AI is a journey. It's okay if some concepts are still fuzzy - they'll become clearer with practice and experience. Keep experimenting, asking questions, and most importantly, have fun with it!

## Bonus Challenges

If you're feeling adventurous, here are some ways to extend your Cart-Pole AI:

1. Try modifying the reward structure. What happens if you give a bigger penalty for dropping the pole?
2. Experiment with different neural network architectures. What if you add more layers or change the number of neurons?
3. Visualize the learning process. Can you create a graph that shows how the AI's performance improves over time?

Good luck, and happy coding!