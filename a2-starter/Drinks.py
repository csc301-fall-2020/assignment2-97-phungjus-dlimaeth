import json

class Drinks:

  '''
  Represents a Drink on the Menu
  '''

  def __init__(self, drink_Name):

    #Add Try/Catch for Key Errors

    with open('./menu.json') as f:
      self.data = json.load(f)['drinks']

    self.name = drink_Name
    self.price = self.data[drink_Name]

  def get_Price(self):

    '''
    Gets the price of the current drink and returns a float
    '''

    print(self.price)
    return self.price

  def get_Name(self):
    '''
    Gets the name of the current drink and returns a string
    '''
    print(self.name)
    return self.name

  def set_Name(self, new_Name):
    '''
    Updates the drink with a new drink from the menu, it takes the name of the new
    drink and updates the current drinks price and anme
    '''
    self.name = new_Name
    self.price = self.data[new_Name]

  def set_Price(self, new_Price):
    '''
    Sets the new price of the drink
    '''
    self.price = new_Price


