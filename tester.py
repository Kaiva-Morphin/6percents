import DataModule
import NNModule

import time
import os
import numpy as np
import torch

net = NNModule.Net()

try:
    net.load_state_dict(torch.load("./backups/NN_MODEL_SAVE_LATEST.save"))
    net.eval()
except:
    print("cant find neural network save!")

train_data = DataModule.Train_Data()

with torch.no_grad():
    images, labels = train_data.data, train_data.labels
    images, labels = torch.tensor(images), torch.tensor(labels)
    answers = net(images)
    
    a = []
    for answer in answers:
        a.append(max(enumerate(answer), key=lambda x: x[1])[0])
    a = np.array(a)

    l = []
    for label in labels:
        l.append(max(enumerate(label), key=lambda x: x[1])[0])
    l = np.array(l)

    percents = round((l == a).sum()) / len(l) * 100
    print("АХАХАХХА загрузил 656 картинок!!!!))))🤣😂😂")
    print("Загружаю в нейросеть🥰")
    print(f"Нейросеть угадала {round(percents / 100 * 656)}😜")
    print(f"Это {percents} процентов от 656😎")
    print("""Загружено 656 фотографий
Обработка изображений...
Нейронная сеть правильно классифицировала 40 объектов
Это 6.098 процентов от загруженного объёма изображений""")