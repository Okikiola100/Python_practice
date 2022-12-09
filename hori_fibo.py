# Author: Oladapo Okikiola
a, b = 0, 1  # fibonacci series code
while a < 100:
    print(a, end=', ')  # end= tells the interpreter to print a the ',' the ' '(space)
    a, b = b, a + b  # fibonacci series style
