"""
    File: exercise_6.4.py
    Author: William Gatharia
    This code demonstrates mapping ( applying a function to a sequence)
"""

#a function for converting tempratures to fahrenheit
def fahrenheit(T): return round((float(9)/5)*T + 32, 2)

#a function for converting tempratures to celsius

def celsius(T): return round((float(5)/9)*(T - 32), 2)

#run mapping

data_in_celsius = [39.2, 36.5, 37.3, 37.8, 0, -4]

print('----------------------Source data in celsuis----------------------------')
print(data_in_celsius)

F = list(map(fahrenheit, data_in_celsius))

print('----------------------Mapped data in fahrenheit----------------------------')
print(F)

C = list(map(celsius, F))

print('----------------------Mapped data in celsuis----------------------------')
print(C)