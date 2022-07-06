from os import link
from flask import render_template
from app import app
from models.customer_orders import customer_orders


@app.route('/')
def index():
    return render_template('index.html', all_orders=customer_orders)

@app.route('/orders/<int:index>')
def order(index):
    link_order = customer_orders[index]
    return render_template('order.html', link_order=link_order, all_orders=customer_orders)


