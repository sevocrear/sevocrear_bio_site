---
title: Guardian
date: 2021-05-05
thumbnail: images/portfolio/techtrans.jpg
service: System for monitoring the safety of workers on the railroads
client: "TechTrans"
ShortDescription: A system designed to minimize the risks of injury or fatality during operations performed by workers on railroad infrastructure facilities.
Challenge: The complex shall be able to manually and automatically determine the guard zone at the objects of railroad infrastructure, guaranteed detection of a person in the specified guard zone and automatic determination of man crossing the boundaries of the guard zone with the issuance of appropriate warning signals.

The following features: the neural network for people detection was selected, the checkers for cameras overlapping and pollution were prepared, the light-weight tracker was selected, the algorithm was written, the model was trained and a prototype of the system in two versions (mono and stereo cameras) was made, the tests were carried out
---

The Guardian contained:

- **OpenCV** - to work with computer vision algorithms and cameras
- **PyTorch** - framerate for neural networks
- **TensorRT** - framework for neural network acceleration (selective)
- **NumPy** - a framework for working with arrays
- **Shapely** - for polygon shaping
- **ROS2 Galactic** (selective) - to provide interconnection between the nodes of the system
- **clearML** - for training neural networks, hypothesis testing and metrics estimation
- **RoboFlow, CVAT** - for annotation, dataset augmentation

More details can be seen [here](https://yandexwebcache.net/yandbtm?fmode=inject&tm=1680956716&tld=ru&lang=ru&la=1677483264&text=ТехТранс+Стражник&url=https%3A//techtrans.ru/catalog/4-2-programmno-apparatnyy-kompleks-strazhnik/&l10n=ru&mime=html&sign=ad0919da5276784ce3117d95cfa4a1fc&keyno=0)