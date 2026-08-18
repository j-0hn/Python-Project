import random
print("\n***** Welcome to the Number Guessing Game! *****\n")


attempt = 0
playAgain = True
hiddenNumber = random.randint(1, 4)


userGuess = int(input("Input your guess number! "))

while playAgain: #this means already true
    
    while hiddenNumber != userGuess:
        
        if hiddenNumber != userGuess:
            print("Incorrect guess!")
            attempt += 1
            userGuess = int(input("Input your guess number! "))

    print(f"You Got it! \nAttemp(s): {attempt}")
    userPlay = input("Enter Y or N: ")
    print("Play again? Y/N")
    if userPlay == "Y" or userPlay == "y":
        playAgain = True
        userGuess = int(input("Input your guess number! "))
    else:
        playAgain = False
print("Thanks for playing")