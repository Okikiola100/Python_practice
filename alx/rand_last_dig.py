#!/bin/Python
# Author: Oladapo Okikiola
import random
number = random.randint(-10000, 10000)
if number[-1] >= 6:
    print(f"Last digit of {number} is {number[-1]} and is greater than 5")
elif number[-1] == 0:
    print(f"Last digit of {number} is {number[-1]} and is zero(0)")
else:
    print(f"Last digit of {number} is {number[-1]} and is less than 6 and not 0")
