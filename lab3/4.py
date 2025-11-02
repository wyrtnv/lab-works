import tkinter as tk


def add_item():
    item_text = entry_field.get()

    if item_text:
        fruit_listbox.insert(tk.END, item_text)

        entry_field.delete(0, tk.END)


root = tk.Tk()
root.title("LAB 3 - Final Tkinter App")

fruit_listbox = tk.Listbox(root, height=5, width=30)
initial_fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]

for fruit in initial_fruits:
    fruit_listbox.insert(tk.END, fruit)

fruit_listbox.pack(pady=10)

entry_field = tk.Entry(root, width=40)
entry_field.pack(pady=5, padx=10)

add_button = tk.Button(root, text="Add Item to List", command=add_item)
add_button.pack(pady=10)

root.mainloop()
