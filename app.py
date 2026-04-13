from flask import Flask, render_template, request, jsonify
from flask_tinydb import TinyDB

app = Flask(__name__)
db = TinyDB(app).get_db()

@app.route('/')
def index():
    return render_template('index.html', show_cards=False)

@app.route('/about')
def about():
    return render_template('about.html', show_cards=False)

@app.route('/all')
def all():
    products = db.all()
    return render_template('all.html', products=products, show_cards=True)

@app.route('/health')
def health():
    return render_template('health.html', show_cards=True)

@app.route('/budget')
def budget():
    return render_template('budget.html', show_cards=True)

@app.route('/special')
def special():
    return render_template('special.html', show_cards=True)

@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    content = request.json
    db.insert(content)
    return f"added product to db"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', show_cards=True), 404