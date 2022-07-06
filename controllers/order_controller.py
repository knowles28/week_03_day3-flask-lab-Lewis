from flask import render_template
from app import app
from models.customer_orders import customer_orders

@app.route('/')
def index():
    return render_template('index.html', all_orders=customer_orders)

@app.route('/orders/<index>')
def order():
    return render_template("order.html", )
