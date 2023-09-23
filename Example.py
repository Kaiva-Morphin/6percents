from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    print(f"New post request from {request.host}")
    try:
        file = request.files['file']
        print(f"Get file with name {file.filename}!")
    except:
        print(f"Corrupted or missied file!")
    return jsonify({"neuroId": 4 })
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=25601)