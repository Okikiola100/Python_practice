#!/usr/bin/python3
# Author: Oladapo Okikiola
"""
Author: Oladapo Okikiola
Description: Code that print age if birthday is important or not- from alx
"""
age = eval(input("Enter your age: "))  # eval(evaluate) automatically convert a string, float or int entered into an integer
if (age >= 1) and (age <= 18):  # if age is 1-18 print: Important birthday
    print("Important birthday")
elif (age == 21) or (age == 50):
    print("Important birthday")
elif not(age < 65):  # not turns the sentence to the opposite it now means: if age >= 65 print important birthday
    print("Important birthday")
else:
    print("Not important birthday")
print("\n\n\n'done'\nAuthor: Oladapo Okikiola")
