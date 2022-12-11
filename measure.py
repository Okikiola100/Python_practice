#!/usr/bin/python3
# Author: Oladapo Okikiola
"""
Desciption: Code that print words in a list
Followed by the number of char in the words
"""
x, y, z = input("Please enter three words: ").split()
words = [x, y, z]
for w in words:
    print(w, len(w))
# Measure some strings
# example of the above
new_word = ['vitality', 'coder', 'is', 'awesome']
for n in new_word:
    print(n, len(n))
print("\n\n'done'")
print("Author: Oladapo Okikiola")
