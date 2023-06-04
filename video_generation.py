import os
import cv2
import re

def create_video_from_images(folder_path, output_path, fps=30):
    # Obtener la lista de archivos en la carpeta y ordenarlos cronológicamente
    files = sorted(os.listdir(folder_path), key=lambda x: int(re.sub('\D', '', x)))

    # Crear un objeto VideoWriter
    video_width, video_height = None, None
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = None

    for file_name in files:
        if file_name.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Leer la imagen
            image_path = os.path.join(folder_path, file_name)
            image = cv2.imread(image_path)
            
            # Obtener las dimensiones de la imagen
            if video_width is None or video_height is None:
                video_height, video_width, _ = image.shape

            # Inicializar el objeto VideoWriter si no se ha hecho antes
            if video is None:
                video = cv2.VideoWriter(output_path, fourcc, fps, (video_width, video_height))

            # Agregar el marco actual al video
            video.write(image)

    # Liberar los recursos
    if video is not None:
        video.release()

    print("¡Video creado exitosamente!")

# Ruta de la carpeta de imágenes
folder_path = r"C:\Users\Alejandro\Desktop\Iter3"

# Ruta de salida del video
output_path = r"C:\Users\Alejandro\Desktop\Iter3\video.mp4"

# Crear el video a partir de las imágenes
create_video_from_images(folder_path, output_path)