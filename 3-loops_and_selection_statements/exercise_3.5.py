"""
    File: exercise_3.5.py
    Author: William Gatharia
    This code demonstrates using nested for loops.
"""
for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
        if j <= i :
            print(j, end = " ")
        else:
            print(" ", end = " ")
    print()

    

