"""
    File: exercise_6.3.py
    Author: William Gatharia
    This code demonstrates function as first class data object in a function.
    i.e. passing a function as an argument in a function
"""

def runFunction(function_arg, data_arg):
    return function_arg(data_arg)

#run tests on math functions
import math

print('math.sqrt(2)=', runFunction(math.sqrt, 2))

print('math.factorial(8)=', runFunction(math.factorial, 8))
