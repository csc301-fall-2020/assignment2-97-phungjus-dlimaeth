import os
import json
import pandas as pd
from Order import Order
from Order import menu


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
        print(choice)
        if choice == '1':

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

            cur_order = Order()

            while True:

                try:

                    if cur_order.countPizza == int(numPizzas):
                        break
                    pizzaOrder = input("Enter your pizza order in the format: PizzaType Size [ToppingA,ToppingB,..]\n")
                    cur_order.add_pizza(pizzaOrder)

                except IndexError:
                    print('Invalid input please try to match the exact format')
                    continue

            while True:

                try:

                    if cur_order.countDrinks == int(numDrinks):
                        break
                    drink = input("Enter the drink you wish to order\n")
                    cur_order.add_drink(drink, 1)
                except ValueError:
                    print("Invalid drink please try again")
                    continue

            json_obj = json.dumps(cur_order.user_order)

            str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/order -d '" + json_obj + "'"

            os.system(str_output)

            with open('./order.json') as order:
                orders = json.load(order)

            while True:
                print("How would like to receive your pizza: ")
                print("1. Pizza Parlour's Delivery Person")
                print("2. Uber Eats")
                print("3. Foodora")
                deliveryType = input("Enter your the number of your choice of delivery:\n")
                try:

                    if deliveryType != "1" and deliveryType != "2" and deliveryType != "3":
                        raise ValueError
                    else:

                        deliveryDetails = {}

                        while True:
                            try:
                                orderNumber = input("Enter your order number\n")
                                if not (orderNumber in orders):
                                    raise ValueError
                                else:
                                    address = input(
                                        "Please enter the address you wish to have the pizza delivered to\n")
                                    break
                            except ValueError:
                                print("Enter a valid order number")
                                continue
                        orderDetails = orders[orderNumber]

                        deliveryDetails["orderNumber"] = orderNumber
                        deliveryDetails["orderDetails"] = orderDetails
                        deliveryDetails["address"] = address
                        deliveryDetailsJSON = json.dumps(deliveryDetails)

                        if deliveryType == "1" or deliveryType == "2":
                            str_output = "curl -X POST -H 'Content-Type: application/json' " \
                                         "http://127.0.0.1:5000/delivery -d '" + \
                                         deliveryDetailsJSON + "'"
                            os.system(str_output)
                            break
                        else:
                            jsonDF = pd.read_json(deliveryDetailsJSON)
                            csv = jsonDF.to_csv()
                            str_output = "curl -X POST http://127.0.0.1:5000/delivery -d '" + \
                                         csv + "'"
                            os.system(str_output)
                            break
                except ValueError:
                    print("Enter a valid delivery number")
                    continue

        elif choice == '2':

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
            cur_order = Order(orders[order_num])
            while True:

                try:
                    print("Options for Updating Order:")
                    print("1. Add Pizza")
                    print("2. Delete Pizza")
                    print("3. Update Pizza")
                    print("4. Add Drink")
                    print("5. Update Drink")
                    print("6. Exit")
                    selection = input("Select an Option\n")
                    if selection == '1':

                        while True:
                            try:
                                pizzaOrder = input(
                                    "Enter your pizza order in the format: PizzaType Size [ToppingA,ToppingB,..]\n")

                                cur_order.add_pizza(pizzaOrder)
                                break
                            except IndexError:
                                print('Invalid input please try to match the exact format')
                                continue

                    elif selection == '2':
                        print(cur_order.user_order['pizza'])

                        while True:
                            try:
                                pizzaPosition = input(
                                    "Please enter the number that corresponds to the pizza you wish to delete "
                                    "starting from 1, and from left to right\n")
                                if int(pizzaPosition) > cur_order.countPizza or int(pizzaPosition) <= 0:
                                    raise ValueError
                                else:
                                    cur_order.delete_pizza(int(pizzaPosition) - 1)
                                    print("Pizza successfully deleted")
                                    break
                            except ValueError:
                                print("Please enter the correct number")
                                continue

                    elif selection == '3':
                        print(cur_order.user_order['pizza'])

                        done = False
                        while not done:
                            try:
                                pizzaPosition = input(
                                    "Please enter the number that corresponds to the pizza you wish to modify "
                                    "starting from 1, and from left to right\n")
                                if int(pizzaPosition) > cur_order.countPizza or int(pizzaPosition) <= 0:
                                    raise ValueError
                                else:
                                    index = int(pizzaPosition) - 1

                                    while True:
                                        try:
                                            print("Options for modifying pizza:")
                                            print("1. Change Type")
                                            print("2. Change Size")
                                            print("3. Enter List of all Toppings")
                                            print("4. Exit")
                                            options = input("Please enter an option number\n")
                                            if options == '1':
                                                while True:
                                                    try:
                                                        new_pizza_type = input("Please enter the new Pizza Type\n")
                                                        cur_order.change_type(index, new_pizza_type)
                                                        break

                                                    except ValueError:
                                                        print("Enter valid pizza type")
                                                        continue
                                            elif options == '2':
                                                while True:
                                                    try:
                                                        new_size = input("Please enter the new Pizza Size\n")
                                                        cur_order.change_size(index, new_size)
                                                        break

                                                    except ValueError:
                                                        print("Enter valid pizza type")
                                                        continue
                                            elif options == '3':
                                                while True:
                                                    try:
                                                        new_Pizza_Toppings = input(
                                                            "Please enter the new list of toppings in format: ["
                                                            "toppingA,toppingB,...]\n")
                                                        cur_order.change_toppings(index, new_Pizza_Toppings)
                                                        break
                                                    except IndexError:
                                                        print("Enter valid list of Toppings")
                                                        continue
                                            elif options == '4':
                                                done = True
                                                break
                                            else:
                                                raise ValueError
                                        except ValueError:
                                            print("Enter valid option number")
                                            continue

                            except ValueError:
                                print("Please enter the correct number")
                                continue
                    elif selection == '4':

                        while True:
                            try:
                                new_Drink = input("Please enter the new drink you wish to add\n")
                                new_Drink_Quantity = input(
                                    "Please enter the quantity you wish to add of the new Drink\n")

                                cur_order.add_drink(new_Drink, int(new_Drink_Quantity))
                                break

                            except ValueError:
                                print("Enter a valid drink")
                                continue

                    elif selection == '5':
                        while True:
                            try:
                                new_Drink = input("Please enter the name of the drink you wish to modify\n")
                                new_Drink_Quantity = input("Please enter the updated quantity of the drink\n")
                                cur_order.change_drink_quantity(new_Drink.lower(), int(new_Drink_Quantity))
                                break
                            except ValueError:
                                print("Enter a valid drink")
                                continue
                    elif selection == '6':
                        break
                    else:
                        raise IndexError
                except IndexError:
                    print("Enter a valid option")
                    continue

            json_obj = json.dumps(orders)

            str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/update_order -d '" + json_obj + "'"

            os.system(str_output)

        elif choice == "3":

            with open('./order.json') as order:
                orders = json.load(order)

            while True:
                try:
                    order_Number_Cancel = input("Please enter the order number that you wish to cancel\n")
                    if not (order_Number_Cancel in orders):
                        raise ValueError

                    str_output = "curl http://127.0.0.1:5000/delete_order/<" + order_Number_Cancel + ">"

                    os.system(str_output)

                except ValueError:
                    print("Enter a valid order number")
                    continue

        elif choice == "4":

            while True:
                try:
                    print("View Menu Options:")
                    print("1. See Full Menu")
                    print("2. See Item Price")

                    menuOption = input("Please select which menu option you would like\n")

                    if menuOption != "1" and menuOption != "2":
                        raise ValueError
                    else:
                        if menuOption == "1":
                            os.system("curl http://127.0.0.1:5000/menu")
                            break
                        else:
                            while True:
                                try:
                                    item_name = input("Enter the name of the item you wish to know the price of\n")
                                    lower_Item_Name = item_name.lower()
                                    if ((not (lower_Item_Name in menu['drinks'])) and (
                                            not (lower_Item_Name in menu['pizzaTypes'])) and (
                                            not (lower_Item_Name in menu['toppings'])) and (
                                            not (lower_Item_Name in menu['size']))):
                                        raise ValueError
                                    else:
                                        os.system("curl http://127.0.0.1:5000/menu/<" + lower_Item_Name + ">")
                                        break
                                except ValueError:
                                    print("Enter Valid Item Name")
                                    continue
                            break
                except ValueError:
                    print("Enter valid menu option")
                    continue
        elif choice == "5":

            break

        else:

            print("Enter a Valid Number\n")
            continue


if __name__ == "__main__":
    cli()
