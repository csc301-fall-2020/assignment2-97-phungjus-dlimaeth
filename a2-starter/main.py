import os
import json

#TEST VALUES
orders = {'01234':
            {"drinks":{"water": 1},"pizza":[{"pizzaSize":"small","pizzaType":"vegetarian","toppings":["beef","chicken"]}]},
          '52311':
            {"drinks": {},"pizza":[{"pizzaSize":"xl","pizzaType":"pepperoni","toppings":[]}]}
          }
#TEST VALUES

with open('./menu.json') as items:
  menu = json.load(items)


def cli():

  os.system('curl http://127.0.0.1:5000/pizza')

  while True:

    print("What would you like to do?:")
    print("1. Place a new order")
    print("2. Update an existing order")
    print("3. Cancel an order")
    print("4. View the menu")
    print("5. Exit")

    choice = input("Enter the number of the action you wish to do:\n")

    if (choice == '1'):

      while True:
        numPizzas = input("How many pizzas would you like to order?\n")
        try:
          int(numPizzas)
          break
        except ValueError:
          print("Enter valid number")
          continue

      while True:
        numDrinks = input("How many drinks would you like to order?\n")
        try:
          int(numDrinks)
          break
        except ValueError:
          print("Enter a valid number")
          continue

      countPizza = 0
      countDrinks = 0

      curOrder = {'pizza': [], 'drinks': {}}

      while True:

        try:

          if (countPizza == int(numPizzas)):
            break
          pizzaOrder = input("Enter your pizza order in the format: PizzaType Size [ToppingA,ToppingB,..]\n")
          pizzaType = pizzaOrder.split(' ')[0].lower()
          pizzaSize = pizzaOrder.split(' ')[1].lower()
          pizzaToppings = pizzaOrder.split(' ')[2].strip('[').strip(']').split(',')

          if (pizzaType in menu['pizzaTypes'] and pizzaSize in menu['size']):
            for topping in pizzaToppings:
              if topping == '':
                break
              elif (not (topping in menu['toppings'])):
                raise IndexError
            curOrder['pizza'].append({"pizzaType": pizzaType, "pizzaSize": pizzaSize, "toppings": ([] if pizzaToppings[0] == '' else pizzaToppings)})
            countPizza += 1
          else:
            raise IndexError

        except IndexError:
          print('Invalid input please try to match the exact format')
          continue


      while True:

        try:

          if (countDrinks == int(numDrinks)):
            break
          drink = input("Enter the drink you wish to order\n")
          if (drink.lower() in menu['drinks']):
            if (drink.lower() in curOrder['drinks']):
              curOrder['drinks'][drink.lower()] += 1
            else:
              curOrder['drinks'][drink.lower()] = 1
            countDrinks += 1
          else:
            raise IndexError
        except IndexError:
          print("Invalid drink please try again")
          continue

      json_obj = json.dumps(curOrder, indent=4)

      str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/order -d '" + json_obj + "'"

      os.system(str_output)


    else:

      print("Enter a Valid Number\n")
      continue



if __name__ == "__main__":
  cli()
