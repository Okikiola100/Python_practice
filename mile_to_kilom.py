#!/usr/bin/python3
# Author: Oladapo Okikiola
"""
Author: Oladapo Okikiola
Decription: Code that converts miles to kilometre
Steps:
1. Stored the number of miles in
Kilometre = miles * 1.60934
2. Ask the user to the number of miles to be comverted
3. Print the result
"""
miles = float(input("Enter the number of miles: "))  # ask the user to enter the number of mile and assign it to the variable miles
kilometre = miles * 1.60934  # maths operator that converts miles to kilometres
print("{} miles equals to {} kilometres\n\t\t = {:.2f} kilometres (2d.p)".format(miles, kilometre, kilometre))  # printing out the output
