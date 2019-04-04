"""
    File: exercise_4.2.py
    Author: William Gatharia
    This code demonstrates slicing strings.
"""

name = "myfile.txt"
print('name[0:]=', name[0:]) #print all characters from index 0 to end

print('name[0:1]=', name[0:1]) #print first character

print('name[0:2]=', name[0:2]) #print first two characters

print('name[:len(name)]=', name[:len(name)]) #print entire string

print('name[-3:]=', name[-3:]) #print last 3 characters

print('name[2:6]=', name[2:6]) #extract the name file from string

