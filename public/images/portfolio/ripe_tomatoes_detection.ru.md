---
title: Как определить, спелые ли помидоры
date: 2021-05-05
thumbnail: images/portfolio/tomatoes_detector.jpg
service: Детектор спелых помидор
client: Владислав З.
shortDescription: Нейронная сеть, определяющая, спелые помидоры или нет. Включает в себя детекцию и классификацию.
challenge: Написать нейронную сеть, обнаруживающию помидоры на изображении и классифицирующую их на спелые и не спелые.

solution: Выбрана архитектуру нейронной сети, собран, аугментирован и аннотирован датасет. Обучена нейронная сеть и проанализированы метрики. Подготовлен метод для вывода модели.
---

Датасет был собран, используя изображения из интернета. Всего было собрано 500 изображений, на которых были помидоры. Чтобы увеличить количество изображений, была применена аугментация. Так, я увеличил картинки в 1.5 раз.

Для аннотирования датасета использовался сервис roboflow:

![tomatoes_annotation](/images/portfolio/tomatoes_annotation.png)

олу.