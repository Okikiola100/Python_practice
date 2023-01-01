#!/usr/bin/python3
# Author: Oladapo Okikiola
def to_base2():

    """
    Base10 to Base2 covertor function
    
    Args:
    number: int
    Return:
    number(base10) = number(base2)
    """
    try:
        number = int(input("\nEnter decimal number to be converted: "))
    except ValueError:
        print('Please enter a number')
    except:
        print('An unkwown error occured, Please try again')
    convert = bin(number)
    convert = convert.lstrip('-0b')
    print('''
    {}(base10) = {}(base2)
    '''.format(number, convert))
def to_base10():

    """
    Base2 to Base10 covertor function
    
    Args:
    number: int
    Return:
    number(base2) = number(base10)
    """
    print('Not yet available now')
print('to_base2 function documentation:\n' + to_base2.__doc__)
print('to_base10 function documentation:\n' + to_base10.__doc__)