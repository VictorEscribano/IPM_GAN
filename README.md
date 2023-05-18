# IPM_GAN
Generation of top view map form front camera view using Generative Adversial Networks.


# Dataset extration
The raw images from front view of the car have been extracted from the Kitty Dataset. In order to obtain the corresponding Homography top viwe transformation from the image a self developed calibration tool have been implemented in order to extract the homography matrix.
To execute the calibration too run:

`python calibrator.py`

This tool consist of 2 main windows:
1. The source image window
2. The template target image window

To complete the calibration you have to select 4 points on the source image and the corresponding 4 top viwe points from the target image. Finally make a 9th click on the target window and the homography matrix will be computed and a sample generated image will appear. In caso of missclick, click the right mouse buton to erease the last selection.

Look at the following tutorial video if you have some doubts:

[![Alt text](https://img.youtube.com/vi/ZAhMQnSIkVU/0.jpg)](https://www.youtube.com/watch?v=ZAhMQnSIkVU)
