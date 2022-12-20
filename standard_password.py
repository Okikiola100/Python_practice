# Author: Oladapo Okikiola
"""
For developer: 
length of password = pass_length
"""
print("""
Author: Oladapo Okikiola
Code that accepts and tell if a password is standard or not

Conditions:
1. Password must be eight(8) digit long
2. Uppercase character must be present
3. Lowercase charcater must be present
4. Number must be present
""")
Username = input("\nEnter your username: ")
password = input("Enter your password: ")
if len(password) < 8:
    print("\nPassword must be eight digit long")
elif not password.islower():
    print("\nLowercase character does not exit")
elif not password.isdigit():
    print("\nPassword does not contain a number")
elif not password.upper():
    print("Password does not contains uppercase character")
else:
    print("\nStandard password")
print("\n\n'done'\nAuthor: Oladapo Okikiola")
