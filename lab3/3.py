import tkinter as tk

root = tk.Tk()
root.title("Fruit Listbox")

# Создаем Listbox и указываем размер
listbox = tk.Listbox(root, width=20, height=6, fg="white", bg="black")
listbox.pack(padx=20, pady=20)

# Добавляем элементы
fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]
for fruit in fruits:
    listbox.insert(tk.END, fruit)

root.mainloop()
