# Author: Oladapo Okikiola
number = 21
guess = int(input("Guess the integer: "))
if guess == number:
    print("Congrats, you got it right")
elif guess < number:
    print("No, number is higher than that")
else:
    print("No, number is lower than that")
print("\n\n'done'\nAuthor: Oladapo Okikiola")
