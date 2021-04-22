from flask import Flask, render_template, request, make_response, jsonify
from base64 import decodestring
import json
from PIL import Image, ImageOps
from tensorflow import keras
import numpy as np
import uuid
import random

model = keras.models.load_model('model')

sessions = {}

def to_grayscale(img):
    image = Image.open(img)
    gray = ImageOps.grayscale(image).resize((28, 28), Image.NEAREST)
    gray.save(img)

app = Flask(__name__)

@app.route('/')
def index():
    session_id = str(uuid.uuid4())
    sessions[session_id] = random.choice(list(range(10)))
    return render_template('index.html', session=session_id, number=sessions[session_id])

@app.route('/upload', methods=['post'])
def upload():
    print(sessions)
    session_id = request.headers.get("session")
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
    digit = np.argmax(result[0])
    number = sessions[session_id]
    res = {
        "digit": digit,
        "number": number,
        "result": str(result)
    }
    if digit == number:
        res["success": True]
    else:
        res["success": False]
    return make_response(jsonify(res), 200)
