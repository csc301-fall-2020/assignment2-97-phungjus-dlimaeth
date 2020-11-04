import json

class Pizza:
    """ 'Toppings that the pizza parlour has available'
    availableToppings = {"olives", "tomatoes", "mushrooms", "jalapenos", "chicken", "beef", "pepperoni"}

    availabePizzaTypes = {
        'pepperoni': {'pepperoni', 'tomatoes'}, 
        'margherita': {'tomatoes'},
        'vegetarian': {'olives', 'tomatoes', 'mushrooms', 'jalapenos'},
        'Neapolitan': {'tomatoes'}
    } """
    availableToppings = {}
    availabePizzaTypes = {}
    availableSizes = {}

    with open('./menu.json') as f:
            availableToppings = json.load(f)['toppings']
            availabePizzaTypes = json.load(f)['pizzaTypes']
            availableSizes = json.load(f)['size']

    def __init__(self, size, pizzaType):

        self.size = size
        self.type = pizzaType
        self.toppings = set()

    def addTopping(self, topping):
        """
        Add this topping to the pizza
        """
        self.toppings.add(topping)

    def getPrice(self):
        """
        Get the total price of this pizza
        """
        price = Pizza.availabePizzaTypes[self.type] + Pizza.availableSizes[self.size]
        for topping in self.toppings:
            price += Pizza.availableToppings[topping]

