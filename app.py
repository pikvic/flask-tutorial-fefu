from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', text="This is Text")

@app.route('/<name>')
def hello(name):
    return f"<h1>Hello, {name.capitalize()}!</h1>"