#!/usr/bin/env python3
if __name__ == "__main__":
    from my_cal import *
    
    a, b = input("Enter the value of a and b(a space b): ").split()
    a = int(a)
    b = int(b)
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} // {} = {}".format(a, b, quot(a, b)))
    print("{} % {} = {}".format(a, b, mod(a, b)))
print("\n\n'done'\nAuthor: Oladapo Okikiola")