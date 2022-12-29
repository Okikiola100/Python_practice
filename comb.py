# Author: Oladapo Okikiola
for num in range(100):
    if num == 99:
        print(num)
    elif num < 10:
        print('0' + str(num), end=", ")
    else:
        print("{}".format(num), end=", ")