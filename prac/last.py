#!/bin/python
# Author: Oladapo Okikiola
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = number % -10
        last_digit *= -1
    print("{:d}".format(last_digit), end='')
    return (last_digit)