# Author: Oladapo Okikiola
def count(n):
    while True:
        if n <= -1:
            print("Count")
        elif n >= 10:
            print("Loop have been reached")
            break
        else:
            print(n)
        count(n --1)
count(-1)
