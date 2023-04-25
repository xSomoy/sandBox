import os

directory_path = 'D:/Work/Personal DevOps/sandBox/File Manager/testFolder'

# use listdir to get a list of all the files in the directory
files = os.listdir(directory_path)

# print the list of files
# print(files)

# loop through all files in the directory and categorize them based on their file extension
# for files in os.listdir(directory_path):
#     files = os.path.join(directory_path, files)
#     if os.path.isfile(files):
#         extension = os.path.splitext(files)[1][1:].lower()
#         print(extension)
       
for i in files:
    print(i)