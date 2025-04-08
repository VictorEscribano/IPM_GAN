# IPM_GAN
Generation of top view map (Inverse Perspecive Mapping) from front camera view using Generative Adversial Networks.
![video_results](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/0d453868-30b0-432b-8f92-36941246c761)


# Dataset extration
The raw images from front view of the car have been extracted from the Kitty Dataset. In order to obtain the corresponding Homography top view transformation from the image a self developed calibration tool has been implemented in order to extract the homography matrix.
To execute the calibration run:

`python calibrator.py`

This tool consist of 2 main windows:
1. The source image window
2. The template target image window

To complete the calibration you have to select 4 points on the source image and the corresponding 4 top viwe points from the target image. Finally make a 9th click on the target window and the homography matrix will be computed and a sample generated image will appear. In caso of missclick, click the right mouse buton to erease the last selection.

Look at the following tutorial video if you have some doubts:


https://github.com/VictorEscribano/IPM_GAN/assets/70441479/286031fb-61b2-4c86-ad14-be3c0abf6e22


(YT video can be found on: [https://img.youtube.com/vi/FLBrwnHSxnk/0.jpg](https://www.youtube.com/watch?v=FLBrwnHSxnk).)

Before obtaining the target images of the dataset the raw images need to be filtered, for that consecutive frame images are removed to avoid repeated images on the dataset. To filter the images run:

`python rmv_repeated.py`

Now that the raw images are filtered and the calibration matrix is obtained we can complete the dataset by computing the corresponding target images running:

`python obtain_targets.py`

# Train the model
Now that the dataset is selected it can be called from the colab notebook.
![generator_loss_plot](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/c823d43d-ca3e-40e9-bdd1-a841f087cfcf)
![discriminator_loss_plot](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/c92e03cb-6522-41fe-85a4-1a550eeab2d0)


![discriminator_accuracies](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/7b49559d-9f8b-43cc-b079-a4f41f4a99a1)

# Results

![test_5](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/67f048e4-533a-4e70-aacd-857290aeba36)
![test_4](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/d6f12cd2-86e1-4cfd-b920-2625ec618413)
![test_7](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/52444786-1bbe-4914-8945-7f482a23308d)
![test_9](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/7ff2d68b-7447-4cc1-8fee-6bee2953024c)
![test_0](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/c522b945-651c-4c19-8ede-5589bd96a898)
![test_1](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/1f21dffb-0ace-4be6-abb6-16713a788e48)
![test_2](https://github.com/VictorEscribano/IPM_GAN/assets/70441479/516e550e-07f2-4929-96d9-36e24f87b048)

### 📄 Citation

If you use this work in your research, please cite it as follows:

```bibtex
@misc{2023ipmgan,
  author = {Víctor Escribano García, Alejandro Acosta Montilla and Oriol Contreras Pérez},
  title = { Inverse Perspective Mapping generation on road vehicle images using Generative Adversial Networks},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/VictorEscribano/IPM_GAN}},
  note = {
    ORCID Víctor: https://orcid.org/0009-0006-1058-6393,
    ORCID Alejandro: 0009-0000-9956-5906,
    ORCID Oriol: 0009-0001-9970-5427
  }
}


