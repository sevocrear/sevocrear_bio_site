---
title: How to determine if tomatoes are ripe
date: 2021-05-05
thumbnail: images/portfolio/tomatoes_detector.jpg
service: Ripe Tomatoes NN Detector
client: Vladislav Z.
shortDescription: A neural network that determines if tomatoes are ripe or not.  It includes both detection and classification.
challenge: Make a neural network that detects tomatoes in the image and classifies them into ripe and not ripe.

solution: The architecture of the neural network is chosen, the dataset is assembled, augmented and annotated. The neural network is trained and its metrics analysed. Method for model inference is prepared.
---

The dataset was compiled using images from the Internet. In total, 500 images of tomatoes were collected. To increase the number of images, augmentation was applied. So, I enlarged the number of pictures in 1.5 times.

The roboflow service was used to annotate the dataset:

![tomatoes_annotation](/images/portfolio/tomatoes_annotation.png)

For the inference, a method was written in Python and a GUI was prepared.

Below you can see examples of how the program works:

![tomatoes_annotation1](/images/portfolio/tomatoes_classification_1.png)
![tomatoes_annotation2](/images/portfolio/tomatoes_classification_2.png)
