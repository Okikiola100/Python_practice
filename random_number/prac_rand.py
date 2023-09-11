# Author: Oladapo Okikiola
def firstDigit(n):
    while n >= 10:
        n = n / 10
    return int(n)
def lastDigit(n):
    return (n % 10)

n = 98562
print(firstDigit(n), end=" ")
print(lastDigit(n))