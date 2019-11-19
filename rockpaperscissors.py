import random

print("Welcome to the Rock Paper Scissors Game, this is how it works: \n"
      + "Rock vs paper - Paper wins \n"
      + "Rock vs scissor - Rock wins \n"
      + "paper vs scissor -scissor wins \n")


while True:
    userInput = int(
        input("Enter your choice \n 1. Rock 2. Paper 3. Scissors \n"))
    while userInput < 1 or userInput > 3:
        userInput = int(
            input("Please enter a value between 1 and 4 \n"))
    if userInput == 1:
        print("User input is Rock")
    elif userInput == 2:
        print("User input is Paper")
    elif userInput == 3:
        print("User input is Scissors")

    print("\nComputer Turn\n")

    computerInput = random.randint(1, 2)
    if computerInput == 1:
        print("Computer input is Rock\n")
    elif computerInput == 2:
        print("Computer input is Paper\n")
    elif computerInput == 3:
        print("Computer input is Scissors\n")

    if computerInput == userInput:
        computerInput = random.randint(1, 3)
        print("It is a draw")

    if ((userInput == 1 and computerInput == 2) or
            (userInput == 2 and computerInput == 1)):
        print("Paper wins", end="")
        result = "paper"

    elif ((userInput == 1 and computerInput == 3) or
            (userInput == 1 and computerInput == 3)):
        print("Rock wins", end="")
        result = "Rock"

    else:
        print("Scissors wins", end="")
        result = "Scissors"

    if result ==
