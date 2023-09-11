#!/usr/bin/python3
# Author: Oladapo Okikiola
word = input("Enter a word/string: ")
print("""
The first letter of the word is: {},
The last letter of the word is: {},
The length of the word is: {}
""".format(word[0], word[-1], len(word)))