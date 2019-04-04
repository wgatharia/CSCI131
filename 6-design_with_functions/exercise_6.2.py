"""
    File: exercise_6.2.py
    Author: William Gatharia
    This code demonstrates a recursive function for calculating the nth Fibonacci number.
"""

def Fib(n):
    if n < 3:
        return 1
    else:
        return Fib(n -1) + Fib(n - 2)

#test
for i in range(1, 11):
    print('Fib(', i , ')=', Fib(i))