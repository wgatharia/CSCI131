"""
    File: exercise_5.5.py
    Author: William Gatharia
    This code demonstrates defining simple functions and using the main function.
"""

def main():
    myList = [1,2,3,4,5,6,7,8,9,10]

    print("The average of: ", myList, " is ", average(myList))

def average(alist):
    theSum = 0
    for i in alist:
        theSum+=i

    return theSum / len(alist)

def cube(x):
    pass

#entry point of your program
if __name__ == "__main__":
    main()
