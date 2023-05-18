# IPM_GAN
Generation of top view map form front camera view using Generative Adversial Networks.


# Dataset extration
The raw images from front view of the car have been extracted from the Kitty Dataset. In order to obtain the corresponding Homography top viwe transformation from the image a self developed calibration tool have been implemented in order to extract the homography matrix.
To execute the calibration too run:
`python calibrator.py`
