# Author: Oladapo Okikiola
import random
number = random.randint(-10000, 10000)  # print random number from the range of -10000 to 10000
last_digit = int(repr(number)[-1])
if last_digit >= 6:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero(0)")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
