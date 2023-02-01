from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    """Perform addition"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result_addition = add(a, b)

    # return f"{a} + {b} = {result_addition}"
    return f"{result_addition}"

@app.route("/sub")
def subtraction():
    """Perform subtraction"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result_subtraction = sub(a, b)

    # return f"{a} - {b} = {result_subtraction}"
    return f"{result_subtraction}"

@app.route("/mult")
def multiplication():
    """Perform multiplication"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result_multiplication = mult(a, b)

    # return f"{a} * {b} = {result_multiplication}"
    return f"{result_multiplication}"

@app.route("/div")
def division():
    """Perform division"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result_division = div(a, b)

    # return f"{a} / {b} = {result_division}"
    return f"{result_division}"


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<oper>")
def do_math(oper):
    """perform specified math on a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = operators[oper](a,b)

    return f"{answer}"
