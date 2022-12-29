#!/bin/python
# Author: Oladapo Okikiola
def fizzbuzz():
    for num in range(100):
        if num % 15 == 0:
            print("FizzBuzz", end=' ')
        elif num % 3 == 0:
            print("Fizz", end=' ')
        elif num % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(num, end=' ')