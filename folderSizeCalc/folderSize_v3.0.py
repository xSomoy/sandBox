import os
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from PIL import Image
import datetime
now = datetime.datetime.now()
timeStamp = now.strftime("%H%M%d%m%y")


# Create a GUI file dialog box to select the directory
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Reserving the original path variable 
imgSave = path

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
    folder_sizes.append(folder_size / (1024 * 1024 * 1024))  # Convert to GB
    folder_names.append(os.path.basename(folder))


# Create a bar chart of the folder sizes
plt.bar(folder_names, folder_sizes)
plt.xticks(rotation=90)
plt.ylabel('Folder Size (GB)')
plt.title('Folder Sizes in {}'.format(imgSave))


# Save the bar chart as a JPEG image file in the selected directory
img_name = imgSave + timeStamp
print(img_name)
image_path = os.path.join(imgSave)
print(image_path)
plt.savefig(image_path, dpi=300, bbox_inches='tight')

# # Display the image file
# img = Image.open(image_path)
# img.show()
