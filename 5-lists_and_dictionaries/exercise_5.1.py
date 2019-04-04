"""
    File: exercise_5.1.py
    Author: William Gatharia
    This code demonstrates creating python lists, printing data in the lists.
"""

#create a list of colors

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print(colors)

#create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7]

print(numbers)

#create a mixed list

mixed_list = ['A', ' ', 'tree', ' ', ' ', 'that', ' ', ' ' , 'has', ' ', 10, ' ' , 'branche(s),', ' ', 'and', ' ', 1, ' ', 'trunk.']

#use a for loop to print items in list
for item in mixed_list:
    print(item, end='')