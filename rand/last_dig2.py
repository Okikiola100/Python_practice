# Author: Oladapo Okikiola
import random
number = random.randint(-10000, 10000)
if number >= 10:
    last_digit = number % 10
else:
    last_digit = (-number % 10) *.1
msg = f"Last digit of {number} is {last_digit}"
if last_digit > 5 and not last_digit == 0:
    print(f"{msg} and is greater than 6 and not 0")
elif last_digit == 0:
    print(f"{msg} and is zero(0)")
else:
    print(f"{msg} and is less than 6 and not 0")