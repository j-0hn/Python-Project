import random
print("\n***** Welcome to the Number Guessing Game! *****\n")


attempt = 0
hiddenNumber = random.randint(1, 4)


userGuess = int(input("Input your guess number! "))

while hiddenNumber != userGuess:
    
    if userGuess != hiddenNumber:
        print("Incorrect guess!")
        attempt += 1
        userGuess = int(input("Input your guess number! "))

print(f"You Got it! \nAttemp(s): {attempt}")