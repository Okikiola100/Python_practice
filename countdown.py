# Author: Oladapo Okikiola
# countdown to 0
def countdown(n):
    if n >= 4:
        print("Countdown to christmas")
    elif n == 0:
        print("Happy Xmas")
        exit()
    else:
        print(n)
    countdown(n-+1)
countdown(4)
