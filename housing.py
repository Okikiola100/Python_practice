#!/usr/bin/python3
# Author: Oladapo Okikiola
print("""
Author: Oladapo Okikiola
Description: The price of a house is $1M\nif the buyer is "Vitality' the buyer has good credit,\n\tthey need to put down 10%\notherwisw\n\tthe user needs to put down 20%\nprint the down payment
""")
price = 1000000
good_credit = input("Enter username: ")
if good_credit == "Vitality":
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down_payment: {down_payment}")
