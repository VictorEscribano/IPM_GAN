# IPM_GAN
Generation of top view map from front camera view using Generative Adversial Networks.


# Dataset extration
The raw images from front view of the car have been extracted from the Kitty Dataset. In order to obtain the corresponding Homography top view transformation from the image a self developed calibration tool has been implemented in order to extract the homography matrix.
To execute the calibration run:

`python calibrator.py`

This tool consist of 2 main windows:
1. The source image window
2. The template target image window

To complete the calibration you have to select 4 points on the source image and the corresponding 4 top viwe points from the target image. Finally make a 9th click on the target window and the homography matrix will be computed and a sample generated image will appear. In caso of missclick, click the right mouse buton to erease the last selection.

Look at the following tutorial video if you have some doubts:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/FLBrwnHSxnk/0.jpg)](https://www.youtube.com/watch?v=FLBrwnHSxnk)

Before obtaining the target images of the dataset the raw images need to be filtered, for that consecutive frame images are removed to avoid repeated images on the dataset. To filter the images run:

`python rmv_repeated.py`

Now that the raw images are filtered and the calibration matrix is obtained we can complete the dataset by computing the corresponding target images running:

`python obtain_targets.py`

# Train the model
Now that the dataset is selected it can be called from the colab notebook.

# Results
![test_5](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/41e83eb5-0db8-4fd6-b81a-a6cfcf38f185)
![test_9](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/15bf31a0-7bda-4b03-92f0-1be16a1803c5)
![test_0](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/a383fdd8-a1c5-40a5-95e4-7c5a5f8be55e)
![test_1](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/df7a3b34-c186-4828-b30e-279627a16714)
![test_2](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/b4367e98-4cdf-458b-8012-a03bef20e750)
![test_4](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/9a2c5374-c108-44d6-bbbd-ffb7b202a7b2)
![test_6](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/15ba7a70-d78c-49e5-8712-d0429c0517f2)
![test_7](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/08aedba4-f04d-4723-8f25-08febfbe2cb5)
