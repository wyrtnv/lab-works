import tkinter as tk


def on_button_click():
    my_button.config(text="Clicked!")


root = tk.Tk()
root.title("Button Clicker App")
tk.Label(root, text="Hello, World!").pack(pady=10)
my_button = tk.Button(root, text="Click Me", command=on_button_click)
my_button.pack(padx=30, pady=30)
root.mainloop()
