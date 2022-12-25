# Author: Oladapo Okikiola
def count(n):
    if n <= -1:
        print("Started counting")
    elif n == 10:
        print("Loop have been reached")
        exit()
    else:
        print(n)
    count(n--1)
count(-1)