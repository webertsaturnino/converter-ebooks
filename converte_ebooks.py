import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def select_files():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for file in files:
        filename, _ = os.path.splitext(file)
        output_file = filename + ".mobi"
        subprocess.run(["ebook-convert", file, output_file])

root = tk.Tk()
root.title("PDF to MOBI Converter")

select_button = tk.Button(root, text="Select PDF Files", command=select_files)
select_button.pack()

root.mainloop()
