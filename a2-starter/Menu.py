import json

class Menu:

  '''
  The Menu class represents a food menu, it contains drinks, different types of pizza
  different pizza sizes and different toppings
  '''

  def __init__(self):

    with open('./menu.json', 'r') as f:
      self.data = json.load(f)

  def add_New_Pizza(self, pizza_Name, pizza_Price):
    '''
    Takes a new pizza name and pizza price as arguments and adds the pizza to
    the menu.json
    '''
    self.data['pizzaTypes'].update({pizza_Name: pizza_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Drink(self, drink_Name, drink_Price):
    '''
    Takes a new drink name and price as arguments and adds the drink to the
    menu.json
    '''
    self.data['drinks'].update({drink_Name: drink_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Toppings(self, topping_Name, topping_Price):
    '''
    Takes a new topping name and price as arguments and adds the topping to the
    menu.json
    '''
    self.data['toppings'].update({topping_Name: topping_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Size(self, size_Name, size_Price):
    '''
    Takes a new pizza size and price as arguments and adds the pizza size to the
    menu.json
    '''
    self.data['size'].update({size_Name: size_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Pizza(self, pizza_Name):
    '''
    Takes a pizza name as an argument and removes that pizza type from the
    menu.json
    '''
    self.data['pizzaTypes'].pop(pizza_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Drink(self, drink_Name):
    '''
    Takes a drink name as an argument and removes that drink from the
    menu.json
    '''
    self.data['drinks'].pop(drink_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Toppings(self, topping_Name):
    '''
    Takes a topping name as an argument and removes that topping from the
    menu.json
    '''
    self.data['toppings'].pop(topping_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Size(self, size_Name):
    '''
    Takes a pizza size as an argument and removes that pizza size from the
    menu.json
    '''
    self.data['size'].pop(size_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def return_Menu(self):
    '''
    Returns the string form of the menu
    '''
    return json.dumps(self.data, indent=4, sort_keys=True).replace('{', '').replace('}', '')

  def return_Menu_Item(self, item_Name):
    '''
    Takes an item name as an argument and returns the price of the item
    '''
    for x in self.data:
      if self.data[x].get(item_Name) != None:
        return self.data[x].get(item_Name)

