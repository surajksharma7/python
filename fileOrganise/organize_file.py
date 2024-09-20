import os
import shutil

# Define the source directory (D drive) and destination directory
source_dir = "D:/"
destination_dir = "C:/Users/YourUsername/suraj/"

# File type categories and their extensions
file_types = {
    'images': ['.png', '.jpg', '.jpeg', '.gif', '.bmp'],
    'videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'pdfs': ['.pdf'],
    'audio': ['.mp3', '.wav', '.flac'],
    'stickers': ['.webp', '.tiff']  # Add file extensions for stickers
}

# Ensure destination subdirectories (images, videos, pdfs, audio, stickers) exist
for folder in file_types.keys():
    folder_path = os.path.join(destination_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create subfolders if they don't exist

# Function to move files based on their extension
def move_files_by_type(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            # Check the file extension and move to the appropriate subfolder
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    destination_path = os.path.join(destination_dir, folder, file)
                    shutil.move(file_path, destination_path)
                    print(f"Moved {file} to {folder} folder.")

# Call the function to move the files
move_files_by_type(source_dir, destination_dir)

print("File transfer complete!")
