#!/bin/python
# Author: Oladapo Okikiola
play = input("Do you wanna guess(True or False): ")
while play == "True":
    print("get ready to play")
    break
else:
    print("goodbye!")
    exit()
secret_num = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_num:
        print('You won')
        break
    elif guess_count == 1:
        print('two more trials')
    elif guess_count == 2:
        print('last trial')
else:
    print('Sorry you failed, please try again')
