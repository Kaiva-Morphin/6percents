import os
from PIL import Image
import numpy as np
import pickle
import random

class Train_Data():
    def __init__(self):
        self.data = []
        self.labels = []
        self.label_to_i = {
            "CS120.01.413": 0,
            "CS120.07.442": 1,
            "CS150.01.427-01": 2,
            "SU160.00.404": 3,
            "SU80.01.426": 4,
            "SU80.10.409A": 5,
            "ЗВТ86.103К-02": 6,
            "СВМ.37.060": 7,
            "СВМ.37.060А": 8,
            "СВП-120.00.060": 9,
            "СВП120.42.020": 10,
            "СВП120.42.030": 11,
            "СК20.01.01.01.406": 12,
            "СК20.01.01.02.402": 13,
            "СК30.01.01.02.402": 14,
            "СК30.01.01.03.403": 15,
            "СК50.01.01.404": 16,
            "СК50.02.01.411": 17,
            "СПО250.14.190": 18,
        }
        self.eye = np.eye(19)
        self.init_train_data()

    def get_random_batch(self, batch_size):
        images = []
        labels = []
        for _ in range(batch_size):
            i = random.randrange(len(self.data))
            images.append(self.data[i])
            labels.append(self.labels[i])
        images = np.array(images, dtype=np.float32)
        labels = np.array(labels, dtype=np.float32)
        return (images, labels)
    
    def get_data_from_image(self, path):
        img = Image.open(path)
        size = 128
        img = img.resize((size,size), Image.Resampling.LANCZOS)
        xsize, ysize = img.size
        r_data = [[] for _ in range(ysize)]
        g_data = [[] for _ in range(ysize)]
        b_data = [[] for _ in range(ysize)]
        for x in range(xsize):
            for y in range(ysize):
                r, g, b = img.getpixel((x, y))
                r_data[y].append(r)
                g_data[y].append(g)
                b_data[y].append(b)
        array = np.array([r_data, g_data, b_data], dtype=np.float32) / 256
        #exc_result = self.eye[self.label_to_i[label]]
        return array

    def init_train_data(self):
        path = "./train_data"
        try:
            with open(".\\TRAIN_DATA.save", "rb") as f:
                self.data = pickle.load(f)
            with open(".\\TRAIN_LABELS_SAVE.save", "rb") as f:  
                self.labels = pickle.load(f)
            print("train data loaded from save!")
        except:
            print("cant load train data!")
            for subdir, _, files in os.walk(path):
                folder_name = subdir.split("\\")[-1]

                label = folder_name

                for file_name in files:
                    filepath = path + "\\" + folder_name + "\\" + file_name
                    img = Image.open(filepath)
                    xsize, ysize = img.size

                    r_data = [[] for _ in range(ysize)]
                    g_data = [[] for _ in range(ysize)]
                    b_data = [[] for _ in range(ysize)]

                    for x in range(xsize):
                        for y in range(ysize):
                            r, g, b = img.getpixel((x, y))
                            r_data[y].append(r)
                            g_data[y].append(g)
                            b_data[y].append(b)

                    array = np.array([r_data, g_data, b_data], dtype=np.float32) / 256
                    self.data.append(array)
                    self.labels.append(self.eye[self.label_to_i[label]])
            with open(".\\TRAIN_DATA.save", "wb") as f:
                pickle.dump(self.data, f)
            with open(".\\TRAIN_LABELS.save", "wb") as f:
                pickle.dump(self.labels, f)
        print("train data inited!")
        
        

if __name__ == "__main__":
    d = Train_Data()
    

    


    #for subdir, dirs, files in os.walk(path):
    #folder_name = subdir.split("\\")[-1]
    #out_folder_path = out_path + folder_name
    #try: os.mkdir(out_folder_path)
    #except: pass
    #print(out_folder_path)
    #for file_name in files:
    #    filepath = path + "\\" + folder_name + "\\" + file_name
    #    img = Image.open(filepath)
    #    img = img.resize((size,size))
    #    img.save(out_folder_path + "\\" + file_name)



