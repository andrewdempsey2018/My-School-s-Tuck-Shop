from flask import Flask, render_template, request, jsonify
from flask_tinydb import TinyDB

app = Flask(__name__)
db = TinyDB(app).get_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all')
def all():
    products = db.all()
    return render_template('all.html', products=products)

@app.route('/health')
def health():
    return render_template('health.html')

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/special')
def special():
    return render_template('special.html')

@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    content = request.json
    db.insert(content)
    return f"added product to db"

@app.route('/getAll', methods=['GET'])
def getAll():
    return db.all()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404