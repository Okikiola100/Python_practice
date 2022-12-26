#!/~/AppData/Local/Python/Python38-32/Python
print("""
Author: Oladapo Okikiola

Description: Code that prints a random number and tell if it's a postive or negative number
""")
import random
number = random.randint(-10, 10)
def random(number):
    if number < 0:
        print(f"{number} is negative")
    elif number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is zero(0)")
random(number)
