"""
    File: exercise_4.5.py
    Author: William Gatharia
    This code demonstrates reading text from a text file.
"""

file_name = input("Enter file to read:")
file = open(file_name, 'r')

while True:
    line = file.readline()

    if line == "":
        break
    print(line.strip())
