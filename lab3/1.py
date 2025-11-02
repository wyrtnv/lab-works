import tkinter as tk

root = tk.Tk()
root.title("Tkinter Hello World")
hello_label = tk.Label(root, text="Hello, World!")
hello_label.pack(padx=20, pady=20)
root.mainloop()
