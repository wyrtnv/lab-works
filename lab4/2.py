import tkinter as tk  # 1
from tkinter import messagebox  # 2


def show_spinbox_value():
    selected_value = spinbox_var.get()
    messagebox.showinfo("Spinbox Selection (Q2)",
                        f"You selected the value: {selected_value}")


root = tk.Tk()
root.title("Q2: Spinbox and Messagebox")

spinbox_var = tk.StringVar(root, value=10)

spinbox = tk.Spinbox(
    root,
    from_=1,
    to=50,
    textvariable=spinbox_var,
    width=10
)
spinbox.pack(pady=10)

q2_button = tk.Button(
    root,
    text="Show Value",
    command=show_spinbox_value
)
q2_button.pack(pady=5)

root.mainloop()
