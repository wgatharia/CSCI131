"""
    File: exercise_2.6.py
    Author: William Gatharia
    This code demonstrates decision making using if else statements.
    Determines if a car speed is too high for a ticket or warning
"""
speed = float(input("Enter a car speed: "))
if speed > 70:
    print("Driver speed is too high. Issue ticket to driver")
elif speed > 65:
     print("Driver speed is high. Issue warning to driver")
elif speed >= 55:
    print("Driver speed is within range")
elif speed >= 0:
    print("Driver speed is too low for interstate. Issue warning to driver") 
else:
    print("Invalid speed, speed cannot be less than 0!")