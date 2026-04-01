# experimenting with python arrays-manipulation
import numpy as np
Q = np.zeros((5,5))
position = (2,2)
Q[position] = 1
print(f"position: {position} Q-value:\n {Q}")
position = (position[0] + 1, position[1])
Q[position] = 1
print(f"position: {position} Q-value:\n {Q}")
position = (position[0], position[1]+1)
Q[position] = 1
print(f"position: {position} Q-value:\n {Q}")