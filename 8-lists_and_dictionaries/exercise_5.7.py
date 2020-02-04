"""
    File: exercise_5.7.py
    Author: William Gatharia
    This code demonstrates using a dictionary.
"""

phonebook = { "Savannah":"425-000-0000", "Bill": "206-000-0000"}

print(phonebook)
#editing item 
phonebook["Savannah"] = "426-000-0000"

print("Edit Savannah's number")
print(phonebook)
#removing an item
#remove savannah's number
phonebook.pop("Savannah")
print(phonebook)
#adding new item
print("Adding peter")
phonebook["Peter"] = "433-000-0000"
print(phonebook)

