import tkinter as tk

root = tk.Tk()
root.title("Q3: 3x3 Grid of Labels")

grid_frame = tk.Frame(root, padx=10, pady=10)
grid_frame.pack()

for row in range(3):
    for col in range(3):
        label_text = f"Cell ({row},{col})"

        label = tk.Label(
            grid_frame,
            text=label_text,
            relief="solid",
            borderwidth=1,
            width=15,
            height=3,
            bg="lightblue"
        )

        label.grid(
            row=row,
            column=col,
            padx=10,
            pady=10
        )

root.mainloop()
