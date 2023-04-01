import zipfile
import os

def unzip_images(zip_file_path, extract_folder_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Extract all files to the specified folder
        zip_file.extractall(extract_folder_path)

