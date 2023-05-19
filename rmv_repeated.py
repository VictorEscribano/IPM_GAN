import os
import shutil

##############################################################################################
# This code remove the consecutive frames of the car on the dataset, to aoid repeated images #
# Also have a function to automatically move the generated images to the desired folder #
'''
remove_consecutive_frames
    Input
        - directory_path

move_directory_content
    Input
        - source_directory
        - destination_directory
'''
##############################################################################################

def remove_consecutive_frames(directory_path):
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

def move_directory_content(source_directory, destination_directory):
    # Crear el directorio de destino si no existe
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    for file in os.listdir(source_directory):
        source_file_path = os.path.join(directory_path, file)
        destination_file_path = os.path.join(destination_directory, file)
        shutil.move(source_file_path, destination_file_path)


# directory_path = r'Dataset\data9'
# remove_consecutive_frames(directory_path)
destination_directory = r'Dataset\new_inputs'

for i in range(2, 24):
    directory_path = rf'Dataset\data{i}'
    # remove_consecutive_frames(directory_path)
    move_directory_content(directory_path, destination_directory)