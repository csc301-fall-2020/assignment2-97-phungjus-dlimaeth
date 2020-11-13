import os
import json
import pandas as pd
from Order import Order
from Order import menu


def cli():
    os.system('curl http://127.0.0.1:5000/pizza')

    while True:

        print("What would you like to do?:\n1. Place a new order\n2. Update an existing order\n"
              "3. Cancel an order\n4. View the menu\n5. Exit")

        choice = input("Enter the number of the action you wish to do:\n")

        if choice == '1':

            while True:
                num_pizzas = input("How many pizzas would you like to order?\n")
                try:
                    int(num_pizzas)
                    break
                except ValueError:
                    print("Enter valid number")
                    continue

            while True:
                num_drinks = input("How many drinks would you like to order?\n")
                try:
                    int(num_drinks)
                    break
                except ValueError:
                    print("Enter a valid number")
                    continue

            cur_order = Order()

            while True:

                try:

                    if cur_order.countPizza == int(num_pizzas):
                        break
                    pizza_order = input("Enter your pizza order in the format: PizzaType Size [ToppingA,ToppingB,..]\n")
                    cur_order.add_pizza(pizza_order)

                except IndexError:
                    print('Invalid input please try to match the exact format')
                    continue

            while True:

                try:

                    if cur_order.countDrinks == int(num_drinks):
                        break
                    drink = input("Enter the drink you wish to order\n")
                    cur_order.add_drink(drink, 1)
                except ValueError:
                    print("Invalid drink please try again")
                    continue

            json_obj = json.dumps(cur_order.user_order)

            str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/order -d '" \
                         + json_obj + "'"

            os.system(str_output)

            with open('./order.json') as order:
                orders = json.load(order)

            while True:
                print("How would like to receive your pizza: \n1. Pizza Parlour's Delivery Person\n"
                      "2. Uber Eats\n3. Foodora")
                delivery_type = input("Enter your the number of your choice of delivery:\n")
                try:

                    if delivery_type != "1" and delivery_type != "2" and delivery_type != "3":
                        raise ValueError
                    else:

                        delivery_details = {}

                        while True:
                            try:
                                order_number = input("Enter your order number\n")
                                if not (order_number in orders):
                                    raise ValueError
                                else:
                                    address = input(
                                        "Please enter the address you wish to have the pizza delivered to\n")
                                    break
                            except ValueError:
                                print("Enter a valid order number")
                                continue
                        order_details = orders[order_number]

                        delivery_details["orderNumber"] = order_number
                        delivery_details["orderDetails"] = order_details
                        delivery_details["address"] = address
                        delivery_details_json = json.dumps(delivery_details)

                        if delivery_type == "1" or delivery_type == "2":
                            str_output = "curl -X POST -H 'Content-Type: application/json' " \
                                         "http://127.0.0.1:5000/delivery -d '" + \
                                         delivery_details_json + "'"
                            os.system(str_output)
                            break
                        else:
                            json_df = pd.read_json(delivery_details_json)
                            csv = json_df.to_csv()
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

            cur_order = Order(orders[order_num])
            while True:

                try:
                    print("Options for Updating Order:\n1. Add Pizza\n2. Delete Pizza\n3. Update Pizza\n"
                          "4. Add Drink\n5. Update Drink\n6. Exit")

                    selection = input("Select an Option\n")
                    if selection == '1':

                        while True:
                            try:
                                pizza_order = input(
                                    "Enter your pizza order in the format: PizzaType Size [ToppingA,ToppingB,..]\n")

                                cur_order.add_pizza(pizza_order)
                                break
                            except IndexError:
                                print('Invalid input please try to match the exact format')
                                continue

                    elif selection == '2':
                        print(cur_order.user_order['pizza'])

                        while True:
                            try:
                                pizza_position = input(
                                    "Please enter the number that corresponds to the pizza you wish to delete "
                                    "starting from 1, and from left to right\n")
                                if int(pizza_position) > cur_order.countPizza or int(pizza_position) <= 0:
                                    raise ValueError
                                else:
                                    cur_order.delete_pizza(int(pizza_position) - 1)
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
                                pizza_position = input(
                                    "Please enter the number that corresponds to the pizza you wish to modify "
                                    "starting from 1, and from left to right\n")
                                if int(pizza_position) > cur_order.countPizza or int(pizza_position) <= 0:
                                    raise ValueError
                                else:
                                    index = int(pizza_position) - 1

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
                                                        new__pizza__toppings = input(
                                                            "Please enter the new list of toppings in format: ["
                                                            "toppingA,toppingB,...]\n")
                                                        cur_order.change_toppings(index, new__pizza__toppings)
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
                                new__drink = input("Please enter the new drink you wish to add\n")
                                new__drink__quantity = input(
                                    "Please enter the quantity you wish to add of the new Drink\n")

                                cur_order.add_drink(new__drink, int(new__drink__quantity))
                                break

                            except ValueError:
                                print("Enter a valid drink")
                                continue

                    elif selection == '5':
                        while True:
                            try:
                                new__drink = input("Please enter the name of the drink you wish to modify\n")
                                new__drink__quantity = input("Please enter the updated quantity of the drink\n")
                                cur_order.change_drink_quantity(new__drink.lower(), int(new__drink__quantity))
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

            str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/update_order -d '" \
                         + json_obj + "'"

            os.system(str_output)

        elif choice == "3":

            with open('./order.json') as order:
                orders = json.load(order)

            while True:
                try:
                    order__number__cancel = input("Please enter the order number that you wish to cancel\n")
                    if not (order__number__cancel in orders):
                        raise ValueError

                    order__to__delete = {order__number__cancel: orders[order__number__cancel]}

                    order__to__delete_json = json.dumps(order__to__delete)

                    str_output = "curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/delete_order -d '" + order__to__delete_json + "'"

                    os.system(str_output)

                    break

                except ValueError:
                    print("Enter a valid order number")
                    continue

        elif choice == "4":

            while True:
                try:
                    print("View Menu Options:\n1. See Full Menu\n2. See Item Price")

                    menu_option = input("Please select which menu option you would like\n")

                    if menu_option != "1" and menu_option != "2":
                        raise ValueError
                    else:
                        if menu_option == "1":
                            os.system("curl http://127.0.0.1:5000/menu")
                            break
                        else:
                            while True:
                                try:
                                    item_name = input("Enter the name of the item you wish to know the price of\n")
                                    lower__item__name = item_name.lower()
                                    if ((not (lower__item__name in menu['drinks'])) and (
                                            not (lower__item__name in menu['pizzaTypes'])) and (
                                            not (lower__item__name in menu['toppings'])) and (
                                            not (lower__item__name in menu['size']))):
                                        raise ValueError

                                    os.system("curl http://127.0.0.1:5000/menu/" + lower__item__name)
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
