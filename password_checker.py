# Author: Oladapo Okikiola
# Code that checks a password if its correct
user_name = input("Enter Username: ")
pass_word = input("Enter password: ")
pass_length = len(pass_word)
hidden_pass = "*" * pass_length
print(f"hello {user_name}, your password is {hidden_pass} and it is {pass_length} long")
