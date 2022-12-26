# Author: Oladapo Okikiola
def random(x):
    if x < 0:
        print("The number is enter is a negative number")
    elif x == 0:
        print("The number you entered 0(zero)")
    else:
        print("The number is a positive number")
random(x = int(input("Please enter a number: ")))
print("done")
