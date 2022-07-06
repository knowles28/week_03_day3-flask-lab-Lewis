from os import link
from flask import render_template
from app import app
from models.customer_orders import customer_orders


@app.route('/orders')
def index():
    return render_template('index.html', all_orders=customer_orders)

@app.route('/orders/<int:index>')
def order(index):
    return render_template('order.html', order=customer_orders[index])


