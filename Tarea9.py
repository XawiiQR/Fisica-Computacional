import numpy as np
import matplotlib.pyplot as plt

def apply_rule(left, center, right):
    # Rule table as given in the problem
    rules = {
        (0,0,0): 0, (0,0,1): 1, (0,1,0): 1, (0,1,1): 1,
        (1,0,0): 1, (1,0,1): 0, (1,1,0): 0, (1,1,1): 0
    }
    return rules[(left, center, right)]

def evolve_automaton(size=100, steps=50):
    # Initialize grid
    grid = np.zeros((steps, size), dtype=int)
    # Set middle cell of first row to 1
    grid[0, size//2] = 1
    
    # Evolution
    for t in range(1, steps):
        for i in range(size):
            left = grid[t-1, (i-1) % size]
            center = grid[t-1, i]
            right = grid[t-1, (i+1) % size]
            grid[t, i] = apply_rule(left, center, right)
    
    return grid

def plot_automaton(grid):
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='binary')
    plt.title('Cellular Automaton Evolution')
    plt.xlabel('Cell Position')
    plt.ylabel('Time Step')
    plt.savefig('cellular_automaton.png')
    plt.close()

# Run simulation
grid = evolve_automaton()
plot_automaton(grid)