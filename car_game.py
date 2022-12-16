#!/C/Users/Azubike Chiefo/AppData/Local/Python/Python38-32/python
# Author: Oladapo Okikiola
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car

stop - to stop the car

quit - to exit the game
        """)
    elif command == "start":
        print("Car started\nIn motion now")
    elif command == "stop":
        print("Car stopped")
    elif command == "quit":
        break
    else:
        print("Sorry, i do not understand your command")
