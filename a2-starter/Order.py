import json
from PizzaClass import *

class Order:
 
    drinkPrices = {}

    with open('./menu.json') as f:
            drinkPrices = json.load(f)['drinks']

    def __init__(self, orderNumber, userOrder):
        self.orderNumber = str(orderNumber)
        self.userOrder = userOrder

    def addPizza(self, pizza):
        """
        Add this item to the order
        """
        self.userOrder[self.orderNumber]['pizzas'].append(pizza)

    def removeItem(self, itemIndex):
        """
        Remove this item from the order
        """
        self.items.pop(itemIndex)

    def getOrderNumber(self):
        return self.orderNumber

    def getPrice(self):
        """
        Get the total price of this order
        """
        price = 0
        for item in self.items:
            if isinstance(item, Pizza):
                price += item.getPrice()
            elif type(item) == str:
                price += Order.drinkPrices[item]

