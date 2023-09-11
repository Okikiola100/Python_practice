#!/bin/env python
# Author: Oladapo Okikiola
islower = __import__("islower").islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("z is {}".format("lower" if islower("z") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))