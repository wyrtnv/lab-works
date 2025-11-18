import tkinter as tk


def on_entry_focus(event):
    status_label.config(text="Entry (Q4) is now focused!")


def on_entry_unfocus(event):
    status_label.config(text="Click on the entry field above.")


root = tk.Tk()
root.title("Q4: Entry Widget and Events")

entry_field = tk.Entry(root, width=40)
entry_field.pack(pady=10, padx=10)

entry_field.bind("<FocusIn>", on_entry_focus)

entry_field.bind("<FocusOut>", on_entry_unfocus)

status_label = tk.Label(
    root, text="Click on the entry field above!", fg="blue")
status_label.pack(pady=5)

entry_field.focus_set()

root.mainloop()
