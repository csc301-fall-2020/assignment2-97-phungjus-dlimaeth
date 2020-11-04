import json

class Menu:

  def __init__(self):

    with open('./menu.json', 'r') as f:
      self.data = json.load(f)

  def add_New_Pizza(self, pizza_Name, pizza_Price):

    self.data['pizzaTypes'].update({pizza_Name: pizza_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Drink(self, drink_Name, drink_Price):

    self.data['drinks'].update({drink_Name: drink_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Toppings(self, topping_Name, topping_Price):
    self.data['toppings'].update({topping_Name: topping_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def add_New_Size(self, size_Name, size_Price):
    self.data['size'].update({size_Name: size_Price})
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Pizza(self, pizza_Name):
    self.data['pizzaTypes'].pop(pizza_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Drink(self, drink_Name):
    self.data['drinks'].pop(drink_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Toppings(self, topping_Name):
    self.data['toppings'].pop(topping_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def remove_Size(self, size_Name):
    self.data['size'].pop(size_Name)
    with open('./menu.json', 'w') as json_file:
      json.dump(self.data, json_file)

  def return_Menu(self):

    return json.dumps(self.data, indent=4, sort_keys=True).replace('{', '').replace('}', '')

  def return_Menu_Item(self, item_Name):

    for x in self.data:
      if self.data[x].get(item_Name) != None:
        return self.data[x].get(item_Name)

