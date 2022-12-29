#!/bin/python
# Author; Oladapo Okikiola
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            diff  = 32
        else:
            diff = 0
        print("{:c}".format(ord(str[i]) - diff), end=" ")
    print()