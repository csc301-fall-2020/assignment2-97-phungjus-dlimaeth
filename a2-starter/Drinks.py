import json

class Drinks:

  def __init__(self, drink_Name):

    #Add Try/Catch for Key Errors

    with open('./menu.json') as f:
      self.data = json.load(f)['drinks']

    self.name = drink_Name
    self.price = self.data[drink_Name]

  def get_Price(self):
    print(self.price)
    return self.price

  def get_Name(self):
    print(self.name)
    return self.name

  def set_Name(self, new_Name):
    self.name = new_Name
    self.price = self.data[new_Name]

  def set_Price(self, new_Price):
    self.price = new_Price


