import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    FPS = 60

    x = np.arange(0, 4 * np.pi, 0.01)

    figure, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_ylim(-4, 4)
    ax.set_xlim(0, 4 * np.pi)
    ax.set_title(r"Simulation")

    def animate(t):
        y1 = 1 * np.cos(10 * t / FPS - 12 * x)
        y2 = 1 * np.cos(8 * t / FPS - 11 * x)
        y = y1 + y2
        line.set_data(x, y)

        return line,

    wave = animation.FuncAnimation(figure, animate, interval=1000 / FPS, blit=True)

    plt.show()


if __name__ == '__main__':
    main()
