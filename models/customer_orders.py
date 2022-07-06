from importlib import import_module
from models.order import Order

customer_order1 = Order("John", "06/07/2022", 5)
customer_order2 = Order("Sam", "05/07/2022", 2)
customer_order3 = Order("Jane","04/07/2022", 1)

customer_orders = [customer_order1, customer_order2, customer_order3]