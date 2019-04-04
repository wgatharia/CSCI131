"""
    File: exercise_3.7.py
    Author: William Gatharia
    This code demonstrates using nested for loops.
"""
for i in range(100, 151):
    sum = 0
    for j in str(i):
        sum += int(j)
    print("Sum of digits in %d is %d" % (i, sum))


    

