"""
    File: exercise_3.2.py
    Author: William Gatharia
    This code demonstrates using a while loop.
"""
#loop and print numbers from 1 to 10 using a while loop

number = 1
while True:
    print(number)
    #increment number
    #short hand for increasing number by 1
    #number += 1
    number = number + 1

    #check if number is greater than 10 and exit loop using break
    if number > 10:
        break
    

