from tkinter import *
from tkinter import ttk

root = Tk()

case_dict = {
    "Group Velocity = Phase Velocity": [3, 2, 3, 2],
    "Group Velocity = - Phase Velocity": [2, 5, 5, 2],
    "Group Velocity > Phase Velocity": [9, 7, 12, 11],
    "Group Velocity < Phase Velocity": [3, 2, 4, 2],
    "Group Velocity = 0, Phase Velocity > 0": [2, 2, 2, 5],
    "Group Velocity > 0, Phase Velocity = 0": [1, -1, 6, 2]
}


def assign_parameters():
    w1 = int(w1_value.get())
    w2 = int(w2_value.get())
    k1 = int(k1_value.get())
    k2 = int(k2_value.get())

    return w1, w2, k1, k2


root.resizable(False, False)
root.title('Phase and Group Velocity')

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

Submit = Button(buttons_frame, text="Submit", width=10, command=assign_parameters)
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


parameters_cb.bind('<<ComboboxSelected>>', parameters_change)

root.mainloop()
