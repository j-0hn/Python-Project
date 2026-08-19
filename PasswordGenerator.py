import random
import string

print("\n----- > Password Generator <-----\n")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

print(varLetters)
print(varDigits)
print(varSpecialChars)

randomNum = random.randint(0, len(varDigits) - 1)
print(f"Random number: {randomNum}")

randomLetter = random.choice(varLetters)
print(f"Random letter: {randomLetter}")

randomSpecialChar = random.choice(varSpecialChars)
print(f"Random special character: {randomSpecialChar}")

print(f"Password Generator Options: {randomNum}{randomLetter}{randomSpecialChar}")