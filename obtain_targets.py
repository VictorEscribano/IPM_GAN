import cv2
import numpy as np
import matplotlib.pyplot as plt
import yaml 
import os


TARGET_H, TARGET_W = 500, 500
M = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

input_folder = 'Dataset/all_input'
output_folder = 'Dataset/all_target'


def load_yalm(file):
    global M
    with open(file, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        M = data['M']
        M = np.array(M).reshape(3,3)
    f.close()

def ipm_from_opencv(image):
    global M
    warped = cv2.warpPerspective(image, M, (TARGET_W, TARGET_H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return warped



load_yalm('homography_calib.yaml')

# Loop through all the images in the input folder
for image_file in os.listdir(input_folder):
    # Check if the file is an image file
    if not image_file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        continue
    
    # Load the image
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path)
    
    # Apply the transformation to the image
    transformed_image = ipm_from_opencv(image)
    
    # Save the transformed image to the output folder with the same name as the input image
    output_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_path, transformed_image)



image = cv2.cvtColor(cv2.imread('Dataset/data5/data5_0.jpg'), cv2.COLOR_BGR2RGB)
warped2 = ipm_from_opencv(image)
#show cv2
cv2.imshow('warped2',warped2)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
