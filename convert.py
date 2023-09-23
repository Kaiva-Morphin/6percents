from PIL import Image

import PIL
import os
path = "C:\\Users\\Morphin\\Downloads\\Коблик\\КобликГрупп\\Детали"
out_path = "./train_data/"

from PIL import Image

#img = Image.new('RGB', (width, height))
#img.putdata(my_list)
#img.save('image.png')

size = 128
for subdir, dirs, files in os.walk(path):
    print(subdir.split("\\")[-1])
for subdir, dirs, files in os.walk(path):
    folder_name = subdir.split("\\")[-1]
    out_folder_path = out_path + folder_name
    try: os.mkdir(out_folder_path)
    except: pass
    print(out_folder_path)
    for file_name in files:
        filepath = path + "\\" + folder_name + "\\" + file_name
        img = Image.open(filepath)
        img = img.resize((size,size), Image.Resampling.LANCZOS)
        img.save(out_folder_path + "\\" + file_name)




