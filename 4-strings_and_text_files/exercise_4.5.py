"""
    File: exercise_4.5.py
    Author: William Gatharia
    This code demonstrates writing random numbers to a text file.
"""

import random

file_name = input("Enter file name: ")
#open file
file = open(file_name, 'w')

for i in range(500):
    r = random.randint(0, 500)
    #write random number to file
    file.write(str(r) + "\n")

#close file
file.close()
