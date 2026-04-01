# code von copilot (simplest q-learning example)
'''
import numpy as np
import random

# 3x3 grid, 4 possible actions (up, down, left, right)
grid_size = 3
num_actions = 4
num_states = grid_size * grid_size

Q = np.zeros((num_states, num_actions))  # Q-table
learning_rate = 0.1
discount_factor = 0.95
episodes = 1000

for episode in range(episodes):
    state = random.randint(0, num_states - 1)  # Random starting position
    
    while True:
        # Pick random action
        action = random.randint(0, num_actions - 1)
        
        # Calculate next state
        row, col = state // grid_size, state % grid_size
        if action == 0: row = max(0, row - 1)      # up
        elif action == 1: row = min(grid_size-1, row + 1)  # down
        elif action == 2: col = max(0, col - 1)    # left
        elif action == 3: col = min(grid_size-1, col + 1)  # right
        
        next_state = row * grid_size + col
        
        # Reward: +1 at goal (bottom-right), -0.01 per step
        reward = 1 if next_state == num_states - 1 else -0.01
        
        # Q-learning update
        old_value = Q[state, action]
        max_future = np.max(Q[next_state])
        Q[state, action] = old_value + learning_rate * (reward + discount_factor * max_future - old_value)
        
        state = next_state
        if state == num_states - 1:  # Reached goal
            break

print("Agent learned!")
'''
# experimenting (modifing copilot code)
import numpy as np
import random
import time
import subprocess, sys

# Q-table: shape (5, 5, 4) → rows, cols, actions
Q = np.zeros((5, 5, 4))

learning_rate = 0.1
discount_factor = 0.9
episodes = 2000

OBSTACLES = {(3,1), (3,2), (3,3), (3,4)}
GOAL = (4, 4)

def clear_screen():
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], check=True, shell=True)

def print_grid(position):
    for i in range(5):
        for j in range(5):
            if (i, j) == position:
                print("P ", end="")
            elif (i, j) == GOAL:
                print("G ", end="")
            elif (i, j) in OBSTACLES:
                print("X ", end="")
            else:
                print(". ", end="")
        print()

def get_next_position(position, action):
    r, c = position
    if action == 0: return (r, max(0, c - 1))        # left
    if action == 1: return (r, min(4, c + 1))        # right
    if action == 2: return (max(0, r - 1), c)        # up
    if action == 3: return (min(4, r + 1), c)        # down

for episode in range(episodes):
    position = (2, 2)

    while True:
        # Exploration vs exploitation
        epsilon_initial = 1.0
        epsilon_decay = 0.995
        epsilon_min = 0.01
        epsilon = max(epsilon_min, epsilon_initial * (epsilon_decay ** episode))
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[position])  # Best action from Q-table

        next_position = get_next_position(position, action)

        # Reward
        if next_position == GOAL:
            reward = 10
        elif next_position in OBSTACLES:
            reward = -9
        else:
            reward = -1

        # Q-learning update: Q(s,a) += lr * (r + γ * max_Q(s') - Q(s,a))
        best_next = np.max(Q[next_position])
        Q[position][action] += learning_rate * (reward + discount_factor * best_next - Q[position][action])

        position = next_position

        if episode % 100 == 0:  # Print every 100 episodes
            clear_screen()
            print_grid(position)
            time.sleep(0.05)

        if position == GOAL:
            break   # ends if we move right to the edge

    #print(f"Episode {episode + 1}: q-values = \n{Q}")



