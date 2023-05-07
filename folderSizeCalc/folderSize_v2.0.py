import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

# Create a GUI file dialog box to select the directory
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Get all the folders in the directory and calculate their sizes
folders = [f.path for f in os.scandir(path) if f.is_dir()]
folder_sizes = []
folder_names = []
for folder in folders:
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
        for file in files:
            file_path = os.path.join(path, file)
            folder_size += os.path.getsize(file_path)
    folder_sizes.append(folder_size / (1024 * 1024))
    folder_names.append(os.path.basename(folder))

# Create a bar chart of the folder sizes
plt.bar(folder_names, folder_sizes)
plt.xticks(rotation=90)
plt.ylabel('Folder Size (MB)')
plt.title('Folder Sizes in {}'.format(path))

# Save the bar chart as an image file
