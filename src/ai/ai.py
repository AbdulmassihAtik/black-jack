import numpy as np
import random
import time
import subprocess
import sys

OBSTACLES = {(3,1), (3,2), (3,3), (3,4)}
GOAL      = (4, 4)
START     = (2, 2)

Q             = np.zeros((5, 5, 4))
learning_rate = 0.1
discount_factor = 0.9
episodes      = 2000

epsilon       = 1.0
epsilon_decay = 0.995
epsilon_min   = 0.01

def clear_screen():
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], check=True)

def get_next_position(position, action):
    r, c = position
    if action == 0: return (r, max(0, c - 1))   # left
    if action == 1: return (r, min(4, c + 1))   # right
    if action == 2: return (max(0, r - 1), c)   # up
    if action == 3: return (min(4, r + 1), c)   # down

def get_reward(position, next_position):
    if next_position == GOAL:       return 10
    if next_position in OBSTACLES:  return -9
    if next_position == position:   return -2   # hit wall
    return -1

def print_grid(position):
    for i in range(5):
        for j in range(5):
            if (i, j) == position:      print("P ", end="")
            elif (i, j) == GOAL:        print("G ", end="")
            elif (i, j) in OBSTACLES:   print("X ", end="")
            else:                        print(". ", end="")
        print()

def print_stats(episode, epsilon, ep_reward):
    print(f"\nEpisode:  {episode}/{episodes}")
    print(f"Epsilon:  {epsilon:.3f}")
    print(f"Reward:   {ep_reward}")

for episode in range(episodes):
    position  = START
    ep_reward = 0

    for step in range(200):
        if random.random() < epsilon:
            action = random.randint(0, 3)
        else:
            action = np.argmax(Q[position])

        next_position = get_next_position(position, action)
        reward        = get_reward(position, next_position)
        ep_reward    += reward

        best_next = np.max(Q[next_position])
        Q[position][action] += learning_rate * (reward + discount_factor * best_next - Q[position][action])

        position = next_position

        if episode % 100 == 0:
            clear_screen()
            print_grid(position)
            print_stats(episode, epsilon, ep_reward)
            time.sleep(0.05)

        if position == GOAL:
            break

    epsilon = max(epsilon_min, epsilon * epsilon_decay)

print("\nTraining complete!")
print_grid(GOAL)