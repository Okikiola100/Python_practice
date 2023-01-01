#!/usr/bin env python3
# Author: Oladapo Okikiola
if __name__ == "__main__":
    from convert import to_base2, to_base10

    print(' BASE NUMBERS OPERATIONS')
    print('''
Choose operations to be performed
1. Conversion from base10(decimal) to base2(binary)
2. Conversion from base2 to base10
''')
    try:
        reply = int(input("Reply: "))
    except ValueError:
        print("Please enter a number(either option 1 or 2")
    except:
        print('An unkwown error occured, Please try again')
    if reply == 1:
        to_base2()
    else:
        to_base10()