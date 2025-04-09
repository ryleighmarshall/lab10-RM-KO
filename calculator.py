#https://github.com/ryleighmarshall/lab10-RM-KO
#Partner 1: Kalista Oberes
#Partner 2: Ryleigh Marshall

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a+b

def subtract(a, b):
    return a -b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(a,b)

def exp(a,b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotnuse(a, b):
    return math.hypot(a, b)