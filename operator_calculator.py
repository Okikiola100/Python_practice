#!/usr/bin/python3
# Author: Oladapo Okikiola
"""
Descriptions: Code that accepts input of number and operator from user and print the deaired output
Steps:
1. 
"""
num1, operator, num2 = input("Enter calculations with operator: ").split()  # Accepts integer and operator from the user and store it in the num1, num2, and operator variable
num1 = int(num1)  # Convert the num1 string into integer
num2 = int(num2)  # Convert the num2 string into integer
if operator == "+":
    print("{} + {} = {sum}".format(num1, num2, sum = num1 + num2))
elif operator == "-":
    print("{} - {} = {sub}".format(num1, num2, sub = num1 - num2))
elif operator == "*":
    print("{} * {} = {mul}".format(num1, num2, mul = num1 * num2))
elif operator == "/":
    print("{} / {} = {div}".format(num1, num2, div = num1 / num2))
elif operator == "//":
    print("{} // {} = {rem}".format(num1, num2, rem = num1 // num2))
elif operator == "%":
    print("{} % {} = {mod}".format(num1, num2, mod = num1 % num2))
print("\n\n\ndone")
print("Author: Oladapo Okikiola")
