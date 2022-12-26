# Author: Oladapo Okikiola
# Print random floating point numbers
import random
print(random.random())  # print random float between the range of 0.00 to 1.00
print(random.uniform(-10.0, 10.0))  # print float number between the range of -10.0 to 10.0
print(randrange(10))  # print random int from 0 to 9 inclusive, but 10 exclusive
print(random.choice(["win", "draw", "lose"]))  # choose a random element from a sequence and print it to the output
furniture = ["table", "chair", "wardrope", "door"]
print(random.shuffle(furniture)) # shuffle a items in a list(furniture)
