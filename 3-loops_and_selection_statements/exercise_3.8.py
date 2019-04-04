"""
    File: exercise_3.8.py
    Author: William Gatharia
    This code demonstrates using nested for loops.
"""
#Loop through numbers from 1 to 6

for i in range(1, 6 + 1):
    #Loop backwards from 6 to 0
    for j in range(6, 0, -1):
        if j <= i:
            #print number and keep cursor on same line
            print(j, end = "")
        else:
            print("", end = "")
    #for every i this statement will print
    print()

    

