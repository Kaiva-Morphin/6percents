import NNModule
import DataModule
import torch
import io
from PIL import Image

from flask import Flask, request, jsonify
import werkzeug.datastructures
app = Flask(__name__)



@app.route('/', methods=['POST'])
def result():
  

    print(f"New post request from {request.host}")
    try:
        file = request.files["file"]
        print(f"Get file with name {file.filename}!")
    except:
        print(f"Corrupted or missied file!")
        return
    path = "./latest.jpg"
        # не уверен насчет функции сохранентя и пути
    file.save(path) # проверить сохраняет ли файл как картинку
    #print(data)
    
    #img = Image.open(str.encode(data))
    #print(img)

    data = td.get_data_from_image(path)

    data = torch.tensor(data)
    #print(data.shape)
    data = data.reshape(1, 3, 128, 128)
    with torch.no_grad():
        result = net(data).numpy()[0]
    print(result)

    i_result = max(enumerate(result), key=lambda x: x[1])[0] 
    print(i_result)
    return jsonify({"neuroId": i_result + 1 })


if __name__ == '__main__':
    td = DataModule.Train_Data()
    net = NNModule.Net()
    net.load_state_dict(torch.load("./backups/NN_MODEL_SAVE_LATEST.save"))
    net.eval()
    
    app.run(host = '0.0.0.0', port=25601)