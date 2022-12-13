#!/usr/bin/python3
# Author: Oladapo Okikiola
taking = "Python For Absolute Beginners"
print(taking)
print(len(taking))  # len counts the number of character in a string or list
print(taking.upper())  # .lower() returns a copy of the string converted to upper_case
print(taking.lower()) # .upper() returns a copy of the string converted to lower_case
print(taking.capitalize())  # .capitalize() returns a capitalized version of the string according to the standard english capitalization
print(taking.isalnum())
if taking.isalnum() == True:
    print("talking.isalnum = True i.e.\nThe string contains both alphabet and numeral(alphanumeric")
else:
    print("taking.isalnum = False \ti.e.\nThe string does not contain both alphabet and numeral(alphanumeric)")
print(taking.join('alaba'))  # .join Concatenate any number of strings\nIt prints the first letter of the word entered followed by the string then the second letter at the end of the string then another string then the third letter at the end e.t.c.
taking.startswith('Python')  # startswith tell true or false whether the set of words of character entered in the argument is in the beginning of the string
if taking.startswith('Jython') == True:
    print("The taking variable starts with the word 'Jython'")
else:
    print("The taking variable string does not starts with the word 'Jython'")
taking.endswith('Beginners')  # just like startswith, endswith tells whether or not he string ends with the string entered in the iterable
taking.casefold()  # Returns a version of the string suitable for caseless comparisons
taking.lstrip()  # Returns a copy of the string with leading whitespace removed
taking.strip()  # Returns a copy of the string with leading and trailing whitespace removed
taking.swapcase()  # convert uppercase to lowercase and lowercase to uppercase
taking.title()  # Returns a version of the string where each word is titlecased
taking.find('n')  # It tells what number is the letter entered
