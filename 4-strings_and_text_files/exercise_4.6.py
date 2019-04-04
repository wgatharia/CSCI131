"""
    File: exercise_4.6.py
    Author: William Gatharia
    This code demonstrates reading numbers from a text file.
"""
#create a file object for reading
f = open('integers.txt', 'r')

#create variable for sum
theSum = 0
for line in f:
    line = line.strip()
    theSum += int(line)

f.close()
print("The sum of integers in file is:", theSum)

