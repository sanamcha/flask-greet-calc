# Put your app in here.
from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route('/add')
def for_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
  
    return str(add(a, b))


@app.route('/sub')
def for_sub():
    """Substract a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a, b))

@app.route('/mult')
def for_mult():
    """Multiply a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a, b))

@app.route('/div')
def for_div():
    """Divide a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a, b))





