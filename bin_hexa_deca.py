# Author: Oladapo Okikiola
ranges = int(input("Print binary, hexadecimal and decagon numbers number up to: "))
def binary(ranges):
    for num in range(int(ranges)):
        print(f"{num} = {bin(num)}")
def hexa(ranges):
    for i in range(ranges):
        print(f"{i} = {hex(i)}")
print("\nBinary numbers")
binary(ranges)
print("\nHexadecimal numbers")
hexa(ranges)