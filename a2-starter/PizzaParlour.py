from flask import Flask, request, jsonify
from Menu import Menu
import json

orderNumber = 0
app = Flask("Assignment 2")



@app.route('/pizza')
def welcome_pizza():
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

  return "Your order number is: " + str(currentOrderNumber) + "\n"

@app.route('/delete_order', methods=['POST'])
def delete_order():

  data = request.get_json()
  with open('./order.json', 'w') as items:
    json.dump(data, items)
  return "Order Deleted\n"

@app.route('/update_order', methods=['POST'])
def update_order():

  data = request.get_json()
  with open('./order.json', 'w') as items:
    json.dump(data, items)
  return "Order updated\n"

@app.route('/menu')
def display_menu():
  menu = Menu()
  return menu.return_Menu()

@app.route('/menu/<item_name>', methods = ['GET'])
def item_price(item_name):
  menu = Menu()
  for categories in menu.data:
    if item_name in menu.data[categories]:
      return item_name + ": " + "$" + str(menu.data[categories][item_name]) + '\n'

@app.route('/delivery', methods=['POST'])
def handle_Delivery():

  if (request.get_json() == None):
    return "Foodora Delivery Instructions Received\n"

  return "Delivery Instructions Received!\n"


if __name__ == "__main__":
    app.run()
