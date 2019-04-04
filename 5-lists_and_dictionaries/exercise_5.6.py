"""
    File: exercise_5.6.py
    Author: William Gatharia
    This code demonstrates binary / decimal conversions using functions.
"""

def binary_to_decimal(bstring):
    decimal = 0
    exponent = len(bstring) - 1
    for digit in bstring:
        decimal = decimal + int(digit) * 2 ** exponent
        exponent = exponent - 1
    return decimal


def decimal_to_binary(decimal):
    if decimal == 0:
        print(0)
    else:
        bstring = ""
        while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bstring = str(remainder) + bstring
    return bstring

def main():
    decimal = int(input("Enter a decimal integer: "))
    print("Binary equivalent of ", decimal , " is ", \
          decimal_to_binary(decimal))
          
    bstring = input("Enter a string of binary number: ")
    print("Decimal equivalent of ", bstring , " is ", \
          binary_to_decimal(bstring))

if __name__ == "__main__":
    main()