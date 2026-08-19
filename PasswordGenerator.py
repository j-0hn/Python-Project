import random
import string

print("\n----- > Password Generator <-----\n")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

passWord = []

for randomLetter in range(3):
    randomLetter = random.choice(varLetters)
    passWord.append(randomLetter)
    random.shuffle(passWord)

for randomNumber in range(4):
    randomNumber = random.choice(varDigits)
    passWord.append(randomNumber)
    random.shuffle(passWord)

for randomSpecialChar in range(3):
    randomSpecialChar = random.choice(varSpecialChars)
    passWord.append(randomSpecialChar)
    random.shuffle(passWord)

print(passWord)

