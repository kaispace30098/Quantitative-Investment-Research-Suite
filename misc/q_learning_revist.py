import numpy as np
import random

# Parameters setting
alpha = 0.1       # Learning rate
gamma = 0.9       # Discount factor
epsilon = 1.0     # Initial exploration probability
epsilon_min = 0.1 # Minimum exploration probability
epsilon_decay = 0.995 # Decay factor
episodes = 500    # Number of training episodes

# Maze size, state, and actions
grid_size = 3
actions = [0, 1, 2, 3]  # Up, Down, Left, Right
Q = np.zeros((grid_size, grid_size, len(actions)))  # Q-Table initialization

# Reward function
def get_reward(state):
    return 1 if state == (2, 2) else -0.1

# Next state function
def get_next_state(state, action):
    x, y = state
    if action == 0 and x > 0:        # Up
        x -= 1
    elif action == 1 and x < grid_size - 1:  # Down
        x += 1
    elif action == 2 and y > 0:      # Left
        y -= 1
    elif action == 3 and y < grid_size - 1:  # Right
        y += 1
    return (x, y)

# Training process
for ep in range(episodes):
    state = (0, 0)  # Initial state
    while state != (2, 2):
        # Select action
        if random.uniform(0, 1) < epsilon:  # Exploration
            action = random.choice(actions)
        else:  # Exploitation
            action = np.argmax(Q[state[0], state[1], :])

        # Perform action and receive feedback
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # Update Q-Table
        Q[state[0], state[1], action] += alpha * (
            reward + gamma * np.max(Q[next_state[0], next_state[1], :]) - Q[state[0], state[1], action]
        )
        #The action value 𝑄(𝑠,𝑎) is updated by adding the learning rate times the TD error, 
        # where the TD error is calculated as the current reward plus the discounted future reward, based on the Bellman equation.
        # Move to next state
        state = next_state

    # Decay epsilon to reduce exploration probability
    epsilon = max(epsilon_min, epsilon * epsilon_decay)

# View the results
print("Trained Q-Table:")
print(Q)
