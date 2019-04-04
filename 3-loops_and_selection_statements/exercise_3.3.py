"""
    File: exercise_3.3.py
    Author: William Gatharia
    This code demonstrates using a for while loop with decreasing number.
"""
#loop and print numbers backwards from 10 to 1 using a while loop

number = 10
while True:
    print(number)
    #increment number
    #short hand for decrease by 1
    #number -= 1
    number = number - 1

    #check if number is 1 exit loop using break
    if number == 1:
        break
    

