# a2-starter

# INSTRUCTIONS
Create an environement inside a2 folder using command: 
  `python3 -m venv venv`
  
Activate the environment using command:
`. venv/bin/activate`

Install Flask using command:
`pip install Flask`

Install Pandas using command: `pip install pandas`

Run the main Flask module by running `python3 PizzaParlour.py`

Start the CLI by running `python3 main.py` in a separate terminal window.

Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`

# PAIR PROGRAMMING

The features we selected to be pair programmed were the add order feature and update order feature.

We began the paired programming by working on the add order feature,
Justin was the driver while Ethan was the navigator during this period
Ethan directed Justin to create an initial template for the place_order() function inside the Flask module PizzaParlour.py and completed the implementation of the CLI for the first feature. We then switched roles and Justin directed Ethan to complete the CLI
method place_order() and with the completion of this we finished paired programming the first feature.

The second feature we paired programmed was updating orders, to start off Ethan was the navigator while Justin was the driver, during this time we finished implementing a draft inside the CLI for updating orders and the Flask module. We then switched roles and finished implmenting the CLI by making a few edits to the code code to fix some bugs from the original draft

Reflection:

Through the process of paired programming there were many positives and negatives to the process itself. Some positives were fewer coding mistakes as the other person could point out any issues they see immediately, it also increased efficiency as we could share knowledge immediately as opposed to wasting time searching for it online. Some negatives were sustainability because you cannot pair program for long periods of time, and it puts a strain on your communication skills because if you cannot communicate your idea effectively your partner won't understand either.

# PROGRAM DESIGN

We decided to use the SOLID design principles. We chose to use the SOLID design principles because using these principles allows for the code to be easily refactored, maintained, and extend.

We had 3 classes: Menu.py, Order.py, and PizzaClass.py for these three classes the code has high cohesion as each class is focused on what it has to do, the methods inside each class only pertain to the intention of each class, for example in Order.py all the methods pertain to creating, updating, and deleting elements inside an order. Our classes also have low coupling as the classes depend on eachother changes in any classes won't affect the others.

For the design of our functions we ensured that each function was precise and only did one specific tasks in order to follow the single responsibilit principle from the SOLID design principles.

# CODE CRAFTSMANSHIP
To keep our code clean and consistent we used PyCharm's IDE tools.
Whenever PyCharm would make a suggestion to reformat our code we took the suggestion.

