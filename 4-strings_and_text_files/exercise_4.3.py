"""
    File: exercise_4.3.py
    Author: William Gatharia
    This code demonstrates working with character sets.
    Caeser Cypher is used for demonstrating encyption.
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"

#add new line 
print("%-13s" % ("ASCII value:"), end="")
#print the ASCII values
for character in alphabet:
    print("%3d," % (ord(character)), end="")
#add new line 
print()
print("%-13s" % ("plain text:"), end="")
for character in alphabet:
    print( "%3s," % (character), end="")#add new line 
print()
#caeser cypher (add 3 to ord value and if value > 122 start at 97)
print("%-13s" % ("Cypher text:"), end="")
for character in alphabet:
    encrypted = ord(character) + 3
    if encrypted > 122:
        encrypted = encrypted - 26
    print("%3s," % (chr(encrypted)), end="")
print()
print("%-13s" % ("ASCII Value:"), end="")
for character in alphabet:
    encrypted = ord(character) + 3
    if encrypted > 122:
        encrypted = encrypted - 26
    print("%d," % (encrypted), end="")

