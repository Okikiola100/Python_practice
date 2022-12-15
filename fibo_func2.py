#!/usr/bin/python3
# Author: Oladapo Okikiola
def fib2(n):
    """ Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
f100 = fib2(100)
f100
