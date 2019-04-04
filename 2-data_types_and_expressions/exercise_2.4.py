#testing booleans
#data types and expressions

x = 5
y = 6

print("x:", x, "y:", y)
#Test equals ==
print("Is x equal to y? : ", x == y) #returns False

#Test with strings
s1 = "Hello"
s2 = "hello"

print("Is s1 equal to s2? : ", s1 == s2) #returns False
print("Is s1.upper() equal to s2.upper()? : ", s1.upper() == s2.upper()) #returns True

#Test not equal !=
print("Is x not equal to y? : ", x != y) #returns True

print("Is s1 not equal to s2? : ", s1 != s2) #returns True
print("Is s1.upper() not equal to s2.upper()? : ", s1.upper() != s2.upper()) #returns False

#Test greater than >
print("Is x greater than y? : ", x > y) #returns False
print("Is y greater than x? : ", y > x) #returns True

#Test less than <
print("Is x less than y? : ", x < y) #returns True
print("Is y less than x? : ", y < x) #returns False

#Test greater or equals >=
print("Is x greater or equal to y? : ", x >= y) #returns False
print("Is y greater or equal to x? : ", y >= x) #returns True

#Test less or equals <=
print("Is x less or equal to y? : ", x <= y) #returns True
print("Is y less or equal to x? : ", y <= x) #returns False

