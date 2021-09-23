from flask import Flask, request
from operations import *

app = Flask(__name__)


operation = {
    "add":add,
    "sub":sub,
    "mult":mult,
    "div":div
    }

@app.route('/math/<oper>')
def do_math(oper):
    """Do math on a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = operation[oper](a, b)
    return str(result)






