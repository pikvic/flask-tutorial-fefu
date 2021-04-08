from flask import Flask, render_template, request, make_response, jsonify
from base64 import decodestring
import json
from PIL import Image, ImageOps
import numpy as np

def to_grayscale(img):
    image = Image.open(img)
    gray = ImageOps.grayscale(image)
    gray.save(img)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text="This is My!!! Text")

@app.route('/upload', methods=['post'])
def upload():
    with open("temp.png","wb") as f:
        data = json.loads(request.data)['image']
        data = data.replace("data:image/png;base64,", '')
        f.write(decodestring(data.encode()))
    to_grayscale("temp.png")

    return make_response(jsonify({"success": "true"}), 200)