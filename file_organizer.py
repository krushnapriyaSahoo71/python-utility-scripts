import os
import shutil

def organize_files(folder):
    for filename in os.listdir(folder):
        name, ext = os.path.splitext(filename)
        ext = ext[1:]
        if ext == "":
            continue
        if not os.path.exists(f"{folder}/{ext}"):
            os.mkdir(f"{folder}/{ext}")
        shutil.move(f"{folder}/{filename}", f"{folder}/{ext}/{filename}")

folder_path = input("Enter folder path: ")
organize_files(folder_path)
print("Files organized successfully!")
