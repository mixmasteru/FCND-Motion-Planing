import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = 12, 12


def plot_all(grid, start_ne, goal_ne, path, skel):
    plt.imshow(grid, cmap='Greys', origin='lower')
    plt.imshow(skel, cmap='Greys', origin='lower', alpha=0.7)

    plt.plot(start_ne[1], start_ne[0], 'x')
    plt.plot(goal_ne[1], goal_ne[0], 'x')

    pp = np.array(path)
    plt.plot(pp[:, 1], pp[:, 0], 'r')

    plt.xlabel('EAST')
    plt.ylabel('NORTH')
    plt.show()
