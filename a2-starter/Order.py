import json

with open('./menu.json') as items:
    menu = json.load(items)


class Order:
    orderNum = 0

    def __init__(self, user_order=None):
        if user_order is None:
            user_order = {'pizza': [], 'drinks': {}}

        self.user_order = user_order
        # Number of pizzas
        self.countPizza = len(self.user_order['pizza'])
        # Number of unique drinks
        self.countDrinks = len(user_order['drinks'])

    def add_pizza(self, pizza_order):
        """
        Add this item to the order
        """
        pizza_type = pizza_order.split(' ')[0].lower()
        pizza_size = pizza_order.split(' ')[1].lower()
        pizza_toppings = pizza_order.split(' ')[2].strip('[').strip(']').split(',')

        if pizza_type in menu['pizzaTypes'] and pizza_size in menu['size']:
            for topping in pizza_toppings:
                if topping == '':
                    break
                elif not (topping in menu['toppings']):
                    raise IndexError
            self.user_order['pizza'].append({"pizzaType": pizza_type, "pizzaSize": pizza_size,
                                            "toppings": ([] if pizza_toppings[0] == '' else pizza_toppings)})
            self.countPizza += 1
            return True
        else:
            raise IndexError

    def add_drink(self, drink, quantity):
        if drink.lower() in menu['drinks'] and quantity > 0:
            if drink.lower() in self.user_order['drinks']:
                self.user_order['drinks'][drink.lower()] += quantity
            else:
                self.user_order['drinks'][drink.lower()] = quantity
            self.countDrinks += 1
        else:
            raise ValueError

    def change_drink_quantity(self, drink, quantity):
        if (quantity < 0 or (not (drink in menu['drinks'])) or not (
                drink in self.user_order['drinks'])):
            raise ValueError
        else:
            if quantity == 0:
                self.user_order['drinks'].pop(drink)
                self.countDrinks -=1
            else:
                self.user_order['drinks'][drink] = quantity

    def delete_pizza(self, index):
        self.user_order['pizza'].pop(index)
        self.countPizza -= 1

    # Changes the type of pizza at this index
    def change_type(self, index, new_pizza_type):
        if new_pizza_type.lower() in menu['pizzaTypes']:
            self.user_order['pizza'][index]['pizzaType'] = new_pizza_type.lower()
            return True
        else:
            raise ValueError

    # Changes the size of pizza at this index
    def change_size(self, index, new_size):
        if new_size.lower() in menu['size']:
            self.user_order['pizza'][index]['pizzaSize'] = new_size.lower()
        else:
            raise ValueError

    # Changes the toppings of pizza at this index
    def change_toppings(self, index, new_pizza_toppings):
        pizza_topping_list = new_pizza_toppings.strip('[').strip(
            ']').split(',')
        for topping in pizza_topping_list:
            if not (topping in menu['toppings']):
                raise IndexError
        self.user_order['pizza'][index]['toppings'] = pizza_topping_list
