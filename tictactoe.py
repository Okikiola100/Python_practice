# Author: Oladapo Okikiola
print("E P I C     B A T T L E (T I C_T A C_T O E)")
print()
print("Select your move")
print("R - for rock, P - paper, S - scissors")

while True:
    player1move = input("Player 1> ")
    player2move = input("\nPlayer 2> ")
    print()
    if player1move == "R":
        if player2move == "R":
            print("Draw")
        elif player2move == "P":
            print("Player 2 wins")
            player2score += 1
        else:
            print("Player 1 wins")
            player1score += 1
