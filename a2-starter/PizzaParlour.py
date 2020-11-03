from flask import Flask

app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    a = 1
    if a == 5:
        return 'blah'
    return 'Welcome to Pizza Planet!'

def sum():
    return 5 + 5

if __name__ == "__main__":
    app.run()
