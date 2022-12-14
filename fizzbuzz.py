#!/usr/bin/python3
# Author: Oladapo Okikiola
"""
Author: Oladapo Okikiola
Description: Code that list num 1-30
For every multiple of 3 print fizz
For every multiple of 5 print buzz
For every multiple of 3 and 5 print fizzbuzz
"""
for i in range(1, 101):
    if (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz", end=" ")
    elif (i % 3) == 0:
        print("Fizz", end=" ")
    elif (i % 5) == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print("\n\n\n'done'\nAuthor: Oladapo Okikiola")
