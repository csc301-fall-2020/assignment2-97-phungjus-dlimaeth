from PizzaParlour import app
from Menu import Menu
from Order import Order
import json


def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == 'Welcome to Pizza Planet!\n'


################# Menu tests ######################
def test_add_and_remove_pizza():
    menu = Menu()
    menu.add_New_Pizza('chocolate', 6.99)
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert data["pizzaTypes"]["chocolate"] == 6.99

    menu.remove_Pizza("chocolate")
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert not ("chocolate" in data["pizzaTypes"])


def test_add_and_remove_drink():
    menu = Menu()
    menu.add_New_Drink('clamato', 2.99)
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert data["drinks"]["clamato"] == 2.99

    menu.remove_Drink("clamato")
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert not ("clamato" in data["drinks"])


def test_add_and_remove_topping():
    menu = Menu()
    menu.add_New_Toppings('pineapple', 0.99)
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert data["toppings"]["pineapple"] == 0.99

    menu.remove_Toppings("pineapple")
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert not ("pineapple" in data["toppings"])


def test_add_and_remove_size():
    menu = Menu()
    menu.add_New_Size('kiddie', -0.99)
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert data["size"]["kiddie"] == -0.99

    menu.remove_Size("kiddie")
    with open('./menu.json', 'r') as f:
        data = json.load(f)
    assert not ("kiddie" in data["size"])


###################### Order Tests ###################
def test_pizza_methods():
    order = Order()
    assert order.countPizza == 0 and order.countDrinks == 0

    order.add_pizza("pepperoni small []")
    assert order.countPizza == 1
    assert order.user_order['pizza'][0] == \
           {"pizzaType": "pepperoni", "pizzaSize": "small", "toppings": []}

    order.change_type(0, "vegetarian")
    assert order.user_order['pizza'][0] == \
           {"pizzaType": "vegetarian", "pizzaSize": "small", "toppings": []}

    order.change_size(0, "medium")
    assert order.user_order['pizza'][0] == \
           {"pizzaType": "vegetarian", "pizzaSize": "medium", "toppings": []}

    order.change_toppings(0, "[jalapenos,olives]")
    assert order.user_order['pizza'][0] == \
           {"pizzaType": "vegetarian", "pizzaSize": "medium", "toppings": ['jalapenos', 'olives']}

    try:
        order.change_type(0, "Obama")
    except ValueError:
        assert order.user_order['pizza'][0] == \
               {"pizzaType": "vegetarian", "pizzaSize": "medium", "toppings": ['jalapenos', 'olives']}

    assert order.countPizza == 1
    order.delete_pizza(0)
    assert order.countPizza == 0


def test_drink_methods():
    order = Order()
    assert order.countPizza == 0 and order.countDrinks == 0

    order.add_drink("coke", 2)
    assert order.countDrinks == 1
    assert order.user_order['drinks'] == {"coke": 2}

    order.add_drink("water", 2)
    assert order.user_order['drinks'] == {"water": 2, "coke": 2}
    assert order.countDrinks == 2

    order.change_drink_quantity("water", 7)
    assert order.user_order['drinks'] == {"water": 7, "coke": 2}

    order.change_drink_quantity("coke", 0)
    assert order.user_order['drinks'] == {"water": 7}
    assert order.countDrinks == 1

    order.add_drink("water", 2)
    assert order.user_order['drinks'] == {"water": 9}

    try:
        order.change_drink_quantity("coke", 3)
    except ValueError:
        assert order.user_order['drinks'] == {"water": 9}

    try:
        order.add_drink("ciroc", 2)
    except ValueError:
        assert order.user_order['drinks'] == {"water": 9}
