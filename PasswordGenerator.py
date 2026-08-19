import random
import string

print("\n----- > Password Generator <-----\n")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

passWord = []
getRangeLetters = int(input("How many letters do you want in your password? "))
for randomLetter in range(getRangeLetters):
    randomLetter = random.choice(varLetters)
    passWord.append(randomLetter)
    random.shuffle(passWord)

getRangeDigits = int(input("How many digits do you want in your password? "))
for randomNumber in range(getRangeDigits):
    randomNumber = random.choice(varDigits)
    passWord.append(randomNumber)
    random.shuffle(passWord)

getRangeSpecialChars = int(input("How many special characters do you want in your password? "))
for randomSpecialChar in range(getRangeSpecialChars):
    randomSpecialChar = random.choice(varSpecialChars)
    passWord.append(randomSpecialChar)
    random.shuffle(passWord)

finalPassword = "".join(passWord)
print("\nYour Password is: " + finalPassword)
print("Total Characters: " + str(len(finalPassword)))
print("Please keep your password safe and secure!")
print("Thank you for using the Password Generator!\n")
