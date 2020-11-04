import sys
import os
import click

@click.command()
@click.option('--option')
def option():
  if option == 'start':
    os.system('curl http://127.0.0.1:5000/pizza')

# def cli():
#
#     if (sys.argv[1] == 'start'):
#       os.system('curl http://127.0.0.1:5000/pizza')
#     elif (sys.argv[1] == 'menu'):
#       os.system('curl http://127.0.0.1:5000/menu')
#     elif (sys.argv[1] == 'order'):
#       choice = input("Do you wish to place an order (Y/N)? \n")
#       if (choice == 'Y'):
#         os.system('curl http://127.0.0.1:5000/order')



if __name__ == "__main__":
  option()
