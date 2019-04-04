"""
    File: exercise_6.6.py
    Author: William Gatharia
    This code demonstrates reducing data using lambda functions. The result is a single output.
    Note: reduce runs from left to right
"""
#import reduce
from functools import reduce

#source data
source_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print('----------------------Source data ----------------------------')
print(source_data)

print('----------------------Reduced data using addition ----------------------------')
print(reduce(lambda x, y: x + y, source_data))

print('----------------------Reduced data using multiplication ----------------------------')
print(reduce(lambda x, y: x * y, source_data))