# A program to compare file / folder size ration cause im testing compression algorithms
import os
import tkinter as tk
from tkinter import filedialog

# Create the main window
root = tk.Tk()
root.title("Size Ratio")

# Define the functions to handle button clicks
def choose_folder_1():
    folder_1_path.set(filedialog.askdirectory())

def choose_folder_2():
    folder_2_path.set(filedialog.askdirectory())



def choose_file_1():
    file_1_path.set(filedialog.askopenfilename())

def choose_file_2():
    file_2_path.set(filedialog.askopenfilename())

def calculate_ratio():
    path_1 = folder_1_path.get() or file_1_path.get()
    path_2 = folder_2_path.get() or file_2_path.get()

    size_1 = get_size(path_1)
    size_2 = get_size(path_2)

    ratio = size_1 / size_2

    result_label.config(text=f"Size ratio: {ratio:.2f} %")

def get_size(path):
    if os.path.isfile(path):
        return os.path.getsize(path)
    else:
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

# Create the GUI elements
folder_1_label = tk.Label(root, text="Folder/File 1:")
folder_1_label.grid(row=0, column=0)

folder_1_path = tk.StringVar()
folder_1_entry = tk.Entry(root, textvariable=folder_1_path)
folder_1_entry.grid(row=0, column=1)

folder_1_button = tk.Button(root, text="Choose folder", command=choose_folder_1)
folder_1_button.grid(row=0, column=2)

file_1_path = tk.StringVar()
file_1_entry = tk.Entry(root, textvariable=file_1_path)
file_1_entry.grid(row=1, column=1)

file_1_button = tk.Button(root, text="Choose file", command=choose_file_1)
file_1_button.grid(row=1, column=2)

folder_2_label = tk.Label(root, text="Folder/File 2:")
folder_2_label.grid(row=2, column=0)

folder_2_path = tk.StringVar()
folder_2_entry = tk.Entry(root, textvariable=folder_2_path)
folder_2_entry.grid(row=2, column=1)

folder_2_button = tk.Button(root, text="Choose folder", command=choose_folder_2)
folder_2_button.grid(row=2, column=2)

file_2_path = tk.StringVar()
file_2_entry = tk.Entry(root, textvariable=file_2_path)
file_2_entry.grid(row=3, column=1)

file_2_button = tk.Button(root, text="Choose file", command=choose_file_2)
file_2_button.grid(row=3, column=2)

calculate_button = tk.Button(root, text="Calculate ratio", command=calculate_ratio)
calculate_button.grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=1)

# Start the main loop
root.mainloop()
