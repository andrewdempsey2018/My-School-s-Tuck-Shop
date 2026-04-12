from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Clarence Bodiker'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/about')
def about():
    name = 'Clarence Bodiker'
    return render_template('about.html', title='aoutere', username=name)

@app.route('/all')
def all():
    name = 'asdf adf'
    return render_template('all.html', title='alltitle', username=name)

@app.route("/test")
def hello_world():
    return "<p>Hello, school!</p>"