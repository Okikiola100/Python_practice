#/usr/bin/python3
# Author: Oladapo Okikiola
"""
Description: Code that prints the addition, substraction, multiplication and division of two int(input) inputed by the user
"""
num1, num2 = input("Please enter a number: ").split()  # split() enable you to input two variable
# The two int variable are stored in num1 and num2
# The format of the split is: var1 (space) var2
num1 = int(num1)
num2 = int(num2)  # Converting the string to int
sum = num1 + num2  # Declaring the sum variable that stores the addition of the two integer
difference = num1 - num2  # Declaring the diiference variable that stores the substraction of the two integer
multiplication = num1 * num2  # The multiplication variable stores the multiplication of the two inputted integers
division = num1 / num2  # It stores the division of num1 by num2
final_div = num1 // num2
modulus = num1 % num2
print("{} + {} = {}".format(num1, num2, sum)) # num1 + num2 = sum of the two num
print("{} - {} = {}".format(num1, num2, difference))  # num1 - num2 = difference between the num
print("{} * {} = {}".format(num1, num2, multiplication))
print("{} / {} = {}".format(num1, num2, division))
print("{} // {} = {}".format(num1, num2, final_div))
print("{} % {} = {}".format(num1, num2, modulus))
