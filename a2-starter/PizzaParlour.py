from flask import Flask, request, jsonify
from Menu import Menu
import json

orderNumber = 0
app = Flask("Assignment 2")



@app.route('/pizza')
def welcome_pizza():
    a = 1
    if a == 5:
        return 'blah'
    return 'Welcome to Pizza Planet!\n'


@app.route('/order', methods=['POST'])
def place_order():
  with open('./order.json', 'r+') as items:
    order = json.load(items)
  data = request.get_json()
  global orderNumber
  order[orderNumber] = data
  orderNumber += 1
  with open('./order.json', 'w') as items:
    json.dump(order, items)

  currentOrderNumber = orderNumber - 1

  return "Your order number is: " + str(currentOrderNumber)

@app.route('/update_order', methods=['POST'])
def update_order():

  data = request.get_json()
  with open('./order.json', 'w') as items:
    json.dump(data, items)
  return "Order updated"

def sum():
    return 5 + 5

if __name__ == "__main__":
    app.run()
