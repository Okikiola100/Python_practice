#!/usr/bin/python3
# Author: Oladapo Okikiola
print("""
Author: Oladapo Okikiola

Description: Input standard name
""")
name = input("Enter your name: ")
if len(name) < 3:
    print("Name should be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print(f"Hello {name}, your name looks good")
