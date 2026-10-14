import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_letter():
    file_path = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    text_edit.delete("1.0", tk.END)
    with open(file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    window.title(f"Letter Editor - {file_path}")

def save_letter_as():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, "w", encoding="utf-8") as output_file:
        text = text_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Letter Editor - {file_path}")

def clear_letter():
    text_edit.delete("1.0", tk.END)
    window.title("Letter Editor - New Letter")

window = tk.Tk()
window.title("Letter Editor - New Letter")

window.rowconfigure(1, minsize=400, weight=1)
window.columnconfigure(0, minsize=500, weight=1)

frame_buttons = tk.Frame(window)
text_edit = tk.Text(window)

btn_open = tk.Button(frame_buttons, text="Open Letter", command=open_letter)
btn_save = tk.Button(frame_buttons, text="Save As...", command=save_letter_as)
btn_clear = tk.Button(frame_buttons, text="New Letter", command=clear_letter)

btn_open.grid(row=0, column=0, padx=5, pady=5)
btn_save.grid(row=0, column=1, padx=5, pady=5)
btn_clear.grid(row=0, column=2, padx=5, pady=5)

frame_buttons.grid(row=0, column=0, sticky="ew")
text_edit.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

window.mainloop()
