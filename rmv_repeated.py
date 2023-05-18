import os
import shutil

# Define the path to the directory containing the images
directory_path = 'Dataset/data'

# Get a list of all the image files in the directory
image_files = [f for f in os.listdir(directory_path) if f.endswith('.jpg') or f.endswith('.png')]

# Sort the list of image files by name
image_files.sort()

# Keep every 5th image and remove the rest
for i, image_file in enumerate(image_files):
    if i % 5 != 0:
        # Remove the image file
        os.remove(os.path.join(directory_path, image_file))
    else:
        # Keep the image file and rename it
        file_path = os.path.join(directory_path, image_file)
        new_file_name = f"{os.path.basename(directory_path)}_{i}.jpg"
        new_file_path = os.path.join(directory_path, new_file_name)
        shutil.move(file_path, new_file_path)