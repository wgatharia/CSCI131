"""
    File: exercise_6.1.py
    Author: William Gatharia
    This code demonstrates elimination of redundancy with functions.
"""

def summation(lower, upper):
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result

#test
print('The summation of numbers 1...4 is: ', summation(1, 4))


print('The summation of numbers 50..100 is: ', summation(50, 100))