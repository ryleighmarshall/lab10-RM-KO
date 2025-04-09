"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypot(a, b):
    return math.hypot(a, b)


import math


def add(a, b):
    return a+b

def sub(a, b):
    return a -b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def multiply(a, b):
    return a * b

def divide(a, b):

    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a,b):
    if a<=0 or b<=0:

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(a,b)

def exp(a,b):
    return a**b

def exponent(a, b):
    return a ** b

