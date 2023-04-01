import zipfile
import os

def zip_images():
    image_folder_path = "static/images/"
    zip_file_path = "config/images.zip"
    with zipfile.ZipFile(zip_file_path, 'w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(image_folder_path):
            for file in files:
                if file.endswith('.jpg') or file.endswith('.png'):  # Change the file extensions as per your needs
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, arcname=file)
