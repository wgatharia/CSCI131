"""
    File: exercise_2.2.py
    Author: William Gatharia
    This code demonstrates basic string methods and escape sequences.
"""
#Use of Escape Sequences
print("I love python programming\n\t\"CSCI 131 students also love python programming\"")

#create a string variable
astring = "Hello world!"
print(len(astring))

print(astring.index("o")) #Prints the first index of letter "o"

#another string variable
s = "Welcome" 
s1 = s.lower() 
# Invoke the lower method 
print(s1)  #output will be welcome 
s2 = s.upper() 
# Invoke the upper method 
print(s2) #output will be WELCOME
astring = "hello world!"

#slice string
print(astring[0:1].upper() + astring[1:])
