"""
    File: exercise_6.5.py
    Author: William Gatharia
    This code demonstrates filtering ( applying a filter to a sequence)
"""

#a function that determines if a number is odd
def odd(x): return x % 2 == 1

#source data
source_data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132]

print('----------------------Source data ----------------------------')
print(source_data)

filtered_data = list(filter(odd, source_data))
print('----------------------Filtered data (odd numbers in list) ----------------------------')
print(filtered_data)
