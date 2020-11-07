import os
import json

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


    elif (choice == '2'):

      while True:

        try:
          with open('./order.json') as order:
            orders = json.load(order)
          order_num = input("Please enter your order number: \n")
          if not (order_num in orders):
            raise IndexError
          else:
            break
        except IndexError:
          print("Enter a valid order number")
          continue

      # TODO use order.json instead

      print("Options for Updating Order:")
      print("1. Add Pizza")
      print("2. Delete Pizza")
      print("3. Update Pizza")
      print("4. Add Drink")
      print("5. Update Drink")
      print("6. Exit")

      while True:

        try:
          selection = input("Select an Option\n")
          if (selection == '1'):

            while True:
              try:
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
                  orders[order_num]['pizza'].append({"pizzaType": pizzaType, "pizzaSize": pizzaSize,
                                                     "toppings": ([] if pizzaToppings[0] == '' else pizzaToppings)})
                  break
                else:
                  raise IndexError
              except IndexError:
                print('Invalid input please try to match the exact format')
                continue

          elif (selection == '2'):
            print(orders[order_num]['pizza'])

            while True:
              try:
                pizzaPosition = input(
                  "Please enter the number that corresponds to the pizza you wish to delete starting from 1, and from left to right\n")
                if (int(pizzaPosition) > len(orders[order_num]['pizza'] or int(pizzaPosition) <= 0)):
                  raise ValueError
                else:
                  orders[order_num]['pizza'].pop(int(pizzaPosition) - 1)
                  print("Pizza successfully deleted")
                  break
              except ValueError:
                print("Please enter the correct number")
                continue

          elif (selection == '3'):
            print(orders[order_num]['pizza'])

            while True:
              try:
                pizzaPosition = input(
                  "Please enter the number that corresponds to the pizza you wish to modify starting from 1, and from left to right\n")
                if (int(pizzaPosition) > len(orders[order_num]['pizza'] or int(pizzaPosition) <= 0)):
                  raise ValueError
                else:
                  print("Options for modifying pizza:")
                  print("1. Change Type")
                  print("2. Change Size")
                  print("3. Enter List of all Toppings")
                  print("4. Exit")
                  while True:
                    try:
                      options = input("Please enter a valid option number\n")
                      if (options == '1'):
                        while True:
                          try:
                            new_Pizza_Type = input("Please enter the new Pizza Type\n")
                            if (new_Pizza_Type.lower() in menu['pizzaTypes']):
                              orders[order_num]['pizza'][int(pizzaPosition) - 1]['pizzaType'] = new_Pizza_Type.lower()
                              break
                            else:
                              raise ValueError
                          except ValueError:
                            print("Enter valid pizza type")
                            continue
                      elif (options == '2'):
                        while True:
                          try:
                            new_Pizza_Size = input("Please enter the new Pizza Size\n")
                            if (new_Pizza_Size.lower() in menu['size']):
                              orders[order_num]['pizza'][int(pizzaPosition) - 1]['pizzaSize'] = new_Pizza_Size.lower()
                              break
                            else:
                              raise ValueError
                          except ValueError:
                            print("Enter valid pizza type")
                            continue
                      elif (options == '3'):
                        while True:
                          try:
                            new_Pizza_Toppings = input(
                              "Please enter the new list of toppings in format: [toppingA,toppingB,...]\n")
                            pizza_Topping_List = new_Pizza_Toppings.strip('[').strip(']').split(',')
                            for topping in pizza_Topping_List:
                              if not (topping in menu['toppings']):
                                raise IndexError
                            orders[order_num]['pizza'][int(pizzaPosition) - 1]['toppings'] = pizza_Topping_List
                            break
                          except IndexError:
                            print("Enter valid list of Toppings")
                            continue
                      elif (options == '4'):
                        break
                      else:
                        raise ValueError
                    except ValueError:
                      print("Enter valid option number")
                      continue


              except ValueError:
                print("Please enter the correct number")
                continue
          elif (selection == '4'):

            while True:
              try:
                new_Drink = input("Please enter the new drink you wish to add\n")
                new_Drink_Quantity = input("Please enter the quantity you wish to add of the new Drink")

                if (int(new_Drink_Quantity) <= 0 or (not (new_Drink.lower() in menu['drinks']))):
                  raise ValueError
                else:
                  if (new_Drink.lower() in orders[order_num]['drinks']):
                    orders[order_num]['drinks'][new_Drink.lower()] += int(new_Drink_Quantity)
                    break
                  else:
                    orders[order_num]['drins'][new_Drink.lower()] = int(new_Drink_Quantity)
                    break

              except ValueError:
                print("Enter a valid drink")
                continue

          elif (selection == '5'):
            while True:
              try:
                new_Drink = input("Please enter the name of the drink you wish to modify\n")
                new_Drink_Quantity = input("Please enter the updated quantity of the drink")
                if (int(new_Drink_Quantity) < 0 or (not (new_Drink.lower() in menu['drinks'])) or not (
                    new_Drink.lower() in orders[order_num]['drinks'])):
                  raise ValueError
                else:
                  orders[order_num]['drinks'][new_Drink.lower()] = int(new_Drink_Quantity)
                  break
              except ValueError:
                print("Enter a valid drink")
                continue
          elif (selection == '6'):
            break
          else:
            raise IndexError
        except IndexError:
          print("Enter a valid option")
          continue

      json_obj = json.dumps(orders, indent=4)

      str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/update_order -d '" + json_obj + "'"

      os.system(str_output)

    else:

      print("Enter a Valid Number\n")
      continue



if __name__ == "__main__":
  cli()
