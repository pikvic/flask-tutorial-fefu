from flask import Flask, render_template, request, make_response, jsonify
from base64 import decodestring
import json
from PIL import Image, ImageOps
from tensorflow import keras
import numpy as np



def to_grayscale(img):
    image = Image.open(img)
    gray = ImageOps.grayscale(image).resize((28, 28), Image.NEAREST)
    gray.save(img)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text="This is My!!! Text")

@app.route('/upload', methods=['post'])
def upload():
    model = keras.models.load_model('model')
    with open("temp.png","wb") as f:
        data = json.loads(request.data)['image']
        data = data.replace("data:image/png;base64,", '')
        f.write(decodestring(data.encode()))
    to_grayscale("temp.png")
    im_frame = Image.open("temp.png")
    np_frame = np.array(im_frame)
    np_frame = np.expand_dims(np_frame, -1) / 255
    np_frame = np.expand_dims(np_frame, 0)

    result = model.predict(np_frame)
    return make_response(jsonify({"success": "true", "digit": str(np.argmax(result[0])), "result": str(result[0])}), 200)