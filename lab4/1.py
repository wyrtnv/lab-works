import tkinter as tk  # 6
from tkinter import filedialog  # 7


def save_text():
    # from 1 to 12 (end)
    text_to_save = text_area.get("1.0", tk.END)

    # 4
    file_path = filedialog.asksaveasfilename(  # 10
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            # 11
            with open(file_path, "w") as file:
                file.write(text_to_save)
            print(f"File successfully saved to: {file_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


root = tk.Tk()
root.title("Q1: Save Text to File")

text_area = tk.Text(root, height=10, width=50)
text_area.pack(pady=10, padx=10)

# 9
save_button = tk.Button(root, text="Save Text to File", command=save_text)
save_button.pack(pady=5)

root.mainloop()
