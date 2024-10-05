# Question 7: Backup a folder into a ZIP file

import shutil
import os

def backup_folder_to_zip(folder_path):
    zip_file = f"{folder_path}.zip"
    shutil.make_archive(folder_path, 'zip', folder_path)
    print(f"Folder {folder_path} has been backed up as {zip_file}")

folder_path = input("Enter the folder path to backup: ")
backup_folder_to_zip(folder_path)
