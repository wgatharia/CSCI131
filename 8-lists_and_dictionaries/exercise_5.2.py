"""
    File: exercise_5.2.py
    Author: William Gatharia
    This code demonstrates list methods.
"""

#create a list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print("----------------List before sort--------------------------")

print(colors)

#sort
colors.sort()
print("\n----------------List after sort--------------------------")
print(colors)

#append and add new color
colors.append('white')
print("\n----------------List after append--------------------------")
print(colors)

#pop list
colors.pop()

print("\n----------------List after pop (removes last color)--------------------------")
print(colors)

#insert at index 0
colors.insert(0, 'brown')
print("\n----------------List after insert at 0 (adds color at start)--------------------------")
print(colors)