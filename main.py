import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main():
    FPS = 60
    N = 4

    A = 1

    w1 = 10
    k1 = 12
    w2 = 11
    k2 = 11

    vp1 = w1 / k1
    vp2 = w2 / k2

    vg = (w2 - w1) / (k2 - k1)

    lbd1 = 2 * np.pi / k1
    lbd2 = 2 * np.pi / k2

    lbd = (lbd1 + lbd2) / 2
    dlbd = np.abs(lbd1 - lbd)

    lbd_env = lbd**2 / dlbd
    v_env = vg
    k_env = 2 * np.pi / lbd_env
    w_env = v_env * k_env

    x = np.arange(0, N * np.pi, 0.01)

    figure, ax = plt.subplots()
    line, = ax.plot([], [], lw=2, color='purple', label='y(x, t) = y_1 + y_2')
    line1, = ax.plot([], [], lw=0.67, color='blue', alpha=0.2, label='y_1(x, t)')
    line2, = ax.plot([], [], lw=0.67, color='red', alpha=0.2, label='y_2(x, t)')

    envelope_up, = ax.plot([], [], lw=1, ls='--', color='orange', alpha=0.5, label='Envelope')
    envelope_dn, = ax.plot([], [], lw=1, ls='--', color='orange', alpha=0.5)

    group_vel, = ax.plot([], [], marker='o', color='orange', label='Group velocity')
    group_vel.set_data(0, 2 * A)
    phase_vel1, = ax.plot([], [], marker='o', color='blue', label='Phase velocity of y_1')
    phase_vel2, = ax.plot([], [], marker='o', color='red', label='Phase velocity of y_2')

    ax.set_ylim(-3, 5)
    ax.set_xlim(0, N * np.pi)
    ax.set_title(r"Group and phase velocities simulation")
    ax.legend(loc='upper right', fontsize='xx-small')

    def animate(t):
        y1 = A * np.cos(w1 * t / FPS - k1 * x)
        y2 = A * np.cos(w2 * t / FPS - k2 * x)
        y = y1 + y2

        env = 2 * A * np.cos(w_env * t / FPS - k_env * x)

        line.set_data(x, y)

        line1.set_data(x, y1)
        line2.set_data(x, y2)

        envelope_up.set_data(x, np.abs(env))
        envelope_dn.set_data(x, -np.abs(env))

        group_vel.set_data(t * vg / FPS % (N * np.pi), 2 * A)

        phase_vel1.set_data(t * vp1 / FPS % (N * np.pi), A)
        phase_vel2.set_data(t * vp2 / FPS % (N * np.pi), A)

        return line, line1, line2, envelope_up, envelope_dn, group_vel, phase_vel1, phase_vel2

    wave = animation.FuncAnimation(figure, animate, interval=1000 / FPS, blit=True)

    plt.show()


if __name__ == '__main__':
    main()
