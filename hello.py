import random

print("Hello, Welcome to the guess game")

generatedNumber = random.randint(1, 4)


while True:
    guessedNumber = int(input("Please enter your guess:  "))
    if guessedNumber < generatedNumber:
        print('To low, please guess a higher number')
    elif guessedNumber > generatedNumber:
        print('To High, Please guess a lower number')
    else:
        break
print('You guessed right')
