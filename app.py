from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Clarence Bodiker'
    return render_template('index.html', title='Welcome', username=name)

@app.route("/test")
def hello_world():
    return "<p>Hello, school!</p>"