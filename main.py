import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation
from IPython.display import HTML
from pathlib import Path


def main():
    FPS = 60

    x = np.arange(0, 2 * np.pi, 0.01)
    #f = lambda x, t: 1 * np.sin(10 * t - 2 * x + 0)  # 1: ang. vel., 2: wave numb., 3: init. phase
    #y = f(x, t)

    # Initialize plot
    figure, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_ylim(-4, 4)
    ax.set_xlim(0, 2 * np.pi)
    ax.set_title(r"Simulation")

    def animate(t):
        y = 1 * np.sin(10 * t / FPS - 1 * x)
        line.set_data(x, y)

        return line

    wave = animation.FuncAnimation(figure, animate, interval=1000 / FPS, blit=True)

    plt.show()


if __name__ == '__main__':
    main()
