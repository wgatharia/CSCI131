"""
    File: exercise_6.6.py
    Author: William Gatharia
    This code demonstrates reducing data using functions. The result is a single output.
    Note: reduce runs from left to right
"""
#import reduce
from functools import reduce

#a function that adds two numbers
def add(x, y): return x + y

#a function that multiplies two numbers
def multiply(x, y): return x * y

#source data
source_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print('----------------------Source data ----------------------------')
print(source_data)

print('----------------------Reduced data using addition ----------------------------')
print(reduce(add, source_data))

print('----------------------Reduced data using multiplication ----------------------------')
print(reduce(multiply, source_data))