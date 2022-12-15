#!/usr/bin/python3

# Author: Oladapo Okikiola

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()
fib(2000)
f = fib
f(100)
f(10)
