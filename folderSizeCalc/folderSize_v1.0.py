import os
import tkinter as tk
from tkinter import filedialog

# Create a GUI file dialog box to select the directory
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Get all the folders in the directory
folders = [f.path for f in os.scandir(path) if f.is_dir()]

# Calculate the size of each folder
for folder in folders:
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
        for file in files:
            file_path = os.path.join(path, file)
            folder_size += os.path.getsize(file_path)
    print("Size of {} is {:.2f} MB".format(folder, folder_size / (1024 * 1024)))
