from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def greet():
    return "Welcome"

@app.route('/welcome/home')
def greet_home():
    return "Welcome home"

@app.route('/welcome/back')
def greet_back():
    return "Welcome back"