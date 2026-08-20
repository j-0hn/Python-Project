import random
import string

print("\n----- > Password Generator <-----\n")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

passWord = ""

def get_input_range():
    return int(input("\nHow many characters do you want in your password? "))

while True:
    try:
        get_range_password = get_input_range()
        if get_range_password < 4:
            print("Password must be at least 4 characters long!")

        elif get_range_password > 8:
            print("Password must not exceed 8 characters!")
        else:
            for i in range(get_range_password):
                passWord += random.choice(varLetters + varDigits + varSpecialChars)
                    
            print("\nYour Password is: ", passWord)
            print("Total Characters: ", len(passWord))
            passWord = ""

            print("\nEnter Y / N")
            regenerate = input("Generate Again? : ")
            if regenerate == "Y" or regenerate == "y":
                continue #this will continue the loop and ask agin inputs
            else:
                break

    except ValueError:
        print("Please enter a valid number!")
        
print("Please keep your password safe and secure!")
print("Thank you for using the Password Generator!\n")
