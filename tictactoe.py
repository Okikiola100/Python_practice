# Author: Oladapo Okikiola
from getpass import getpass as input
print("E P I C     B A T T L E (T I C_T A C_T O E)")
print()
print("Select your move")
print("R - for rock, P - paper, S - scissors")

play_limit = 3
player1score = 0
player2score = 0
playerscore = player1score + player2score
while playerscore < play_limit:
    player1move = input("Player 1> ")
    player2move = input("\nPlayer 2> ")
    print()
    if player1move == "R":
        if player2move == "R":
            print("Draw")
        elif player2move == "P":
            print("Player 2 wins")
            player2score += 1
        elif player2move == "S":
            print("Player 1 wins")
            player1score += 1
        else:
            print("invalid input by player2")
    elif player1move == "P":
        if player2move == "P":
            print("draw")
        elif player2move == "R":
            print("player 1 wins")
            player1score += 1
        elif player2move == "S":
            print("player 2 wins")
            player2score += 1
        else:
            print("Invalid input entered by player2")
    elif player1move == "S":
        if player2move == "S":
            print("draw")
        elif player2move == "P":
            print("player 1 wins")
            player1score += 1
        elif player2move == "R":
            print("player 2 wins")
            player2score += 1

print("Player 1 has {} wins.".format(player1score))
print("Player 2 has {} wins.".format(player2score))