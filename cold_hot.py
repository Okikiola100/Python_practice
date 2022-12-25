# Author: Oladapo Okikiola
print("""
Author: Oladapo Okikiola

Description: Code that tells if the temperature of a place is code
""")
def temperature(n):
    if n >= 23:
        print("Room temperture is high(hot)")
    elif n <= 17:
        print("Room temperature is low(cold)")
    else:
        print("Room temperature is at the average(neither is hot nor cold)")
temperature(int(input("Enter the room temperature: ")))
