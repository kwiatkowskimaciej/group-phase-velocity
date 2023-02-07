import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def main():
    FPS = 60
    N = 4

    A = 1

    wrong_values = ""
    try:
        w1 = int(w1_value.get())
    except ValueError:
        wrong_values += "w1, "
    try:
        w2 = int(w2_value.get())
    except ValueError:
        wrong_values += "w2, "
    try:
        k1 = int(k1_value.get())
    except ValueError:
        wrong_values += "k1, "
    try:
        k2 = int(k2_value.get())
    except ValueError:
        wrong_values += "k2, "

    if len(wrong_values) > 0:
        messagebox.showinfo("Wrong data", f"Enter the correct data for {wrong_values[:-2]}!")
        return

    vp1 = w1 / k1
    vp2 = w2 / k2

    vg = (w2 - w1) / (k2 - k1)

    x = np.arange(0, N * np.pi, 0.01)

    figure, ax = plt.subplots()
    line, = ax.plot([], [], lw=1.5, color='purple', label='y(x, t) = y_1 + y_2')
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

        env = 2 * A * np.cos((w1 * t / FPS - w2 * t / FPS - k1 * x + k2 * x) / 2)

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


root = Tk()
root.option_add("*Font", "Arial 20")

case_dict = {
    "Group Velocity = Phase Velocity": [3, 2, 3, 2],
    "Group Velocity = - Phase Velocity": [2, 5, 5, 2],
    "Group Velocity > Phase Velocity": [9, 7, 12, 11],
    "Group Velocity < Phase Velocity": [3, 2, 4, 2],
    "Group Velocity = 0, Phase Velocity > 0": [2, 2, 2, 5],
    "Group Velocity > 0, Phase Velocity = 0": [1, -1, 6, 2]
}

root.resizable(False, False)
root.title('Phase and Group Velocities')

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0)

label = ttk.Label(mainframe, text="Choose option:")
label.grid(column=0, row=0)

selected_parameters = StringVar()
parameters_cb = ttk.Combobox(mainframe, textvariable=selected_parameters)
parameters_cb.grid(column=0, row=1)
parameters_cb['values'] = list(case_dict.keys())
parameters_cb['state'] = 'readonly'
parameters_cb['width'] = 30

parameters_frame = ttk.Frame(root, padding="3 3 12 12")
parameters_frame.grid(column=0, row=1)

w1_label = ttk.Label(parameters_frame, text="w1:")
w1_label.grid(column=0, row=0)
w1_value = StringVar()
w1_entry = ttk.Entry(parameters_frame, width=7, textvariable=w1_value)
w1_entry.grid(column=1, row=0)

w2_label = ttk.Label(parameters_frame, text="w2:")
w2_label.grid(column=0, row=1)
w2_value = StringVar()
w2_entry = ttk.Entry(parameters_frame, width=7, textvariable=w2_value)
w2_entry.grid(column=1, row=1)

k1_label = ttk.Label(parameters_frame, text="k1:")
k1_label.grid(column=0, row=2)
k1_value = StringVar()
k1_entry = ttk.Entry(parameters_frame, width=7, textvariable=k1_value)
k1_entry.grid(column=1, row=2)

k2_label = ttk.Label(parameters_frame, text="k2:")
k2_label.grid(column=0, row=3)
k2_value = StringVar()
k2_entry = ttk.Entry(parameters_frame, width=7, textvariable=k2_value)
k2_entry.grid(column=1, row=3)

buttons_frame = ttk.Frame(root, padding="3 3 12 12")
buttons_frame.grid(column=0, row=2)

Submit = Button(buttons_frame, text="Submit", width=10, command=main)
Submit.grid(column=1, row=0)

Exit = Button(buttons_frame, text="Exit", width=10, command=root.destroy)
Exit.grid(column=0, row=0)


def parameters_change(event):
    parameters = case_dict[selected_parameters.get()]
    w1_entry.delete(0, END)
    w1_entry.insert(0, parameters[0])

    w2_entry.delete(0, END)
    w2_entry.insert(0, parameters[1])

    k1_entry.delete(0, END)
    k1_entry.insert(0, parameters[2])

    k2_entry.delete(0, END)
    k2_entry.insert(0, parameters[3])


root.bind('<Return>', lambda event=None: Submit.invoke())
parameters_cb.bind('<<ComboboxSelected>>', parameters_change)
root.mainloop()
