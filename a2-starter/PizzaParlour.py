from flask import Flask, request, jsonify
from Menu import Menu

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    a = 1
    if a == 5:
        return 'blah'
    return 'Welcome to Pizza Planet!\n'


@app.route('/order', methods=['POST'])
def place_order():
  data = request.get_json()
  return "Order Successfully Placed"

def sum():
    return 5 + 5

if __name__ == "__main__":
    app.run()
