import random
print("\n***** Welcome to the Number Guessing Game! *****\n")

attempt = 0

def getGuess():
    return int(input("Input your guess number! "))

def randomNum():
    return random.randint(1, 4)

userGuess = getGuess()
while True:
    hiddenNumber = randomNum()
    while hiddenNumber != userGuess:
        print("Incorrect guess!")
        attempt += 1
        userGuess = getGuess()
    print(f"You Got it! \nAttemp(s): {attempt}")

    userPlay = input("Play again? Press Y or Enter to Exit: ")
    if userPlay == "Y" or userPlay == "y":
        attempt = 0
        hiddenNumber = randomNum()
        userGuess = getGuess()
    else:
       break

print("Thanks for playing")