import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    FPS = 60
    N = 4

    A = 1
    w1 = 10
    k1 = 12
    w2 = 8
    k2 = 11

    vp1 = w1 / k1
    vp2 = w2 / k2

    vg = (w2 - w1) / (k2 - k1)

    x = np.arange(0, N * np.pi, 0.01)

    figure, ax = plt.subplots()
    line, = ax.plot([], [], lw=2, color='blue')
    line1, = ax.plot([], [], lw=1, color='green', alpha=0.5)
    line2, = ax.plot([], [], lw=1, color='orange', alpha=0.5)

    group_vel, = ax.plot([], [], marker='o', color='red')
    group_vel.set_data(0, 2 * A)
    phase_vel1, = ax.plot([], [], marker='o', color='green')
    phase_vel2, = ax.plot([], [], marker='o', color='orange')

    ax.set_ylim(-4, 4)
    ax.set_xlim(0, N * np.pi)
    ax.set_title(r"Simulation")

    def animate(t):
        y1 = A * np.cos(w1 * t / FPS - k1 * x)
        y2 = A * np.cos(w2 * t / FPS - k2 * x)
        y = y1 + y2

        line.set_data(x, y)

        line1.set_data(x, y1)
        line2.set_data(x, y2)

        group_vel.set_data(t * vg / FPS % (N * np.pi), 2 * A)

        phase_vel1.set_data(t * vp1 / FPS % (N * np.pi), A)
        phase_vel2.set_data(t * vp2 / FPS % (N * np.pi), A)

        return line, line1, line2, group_vel, phase_vel1, phase_vel2

    wave = animation.FuncAnimation(figure, animate, interval=1000 / FPS, blit=True)

    plt.show()


if __name__ == '__main__':
    main()
