import random
import string

print("\n----- > Password Generator <-----\n")

varLetters = string.ascii_letters
varDigits = string.digits
varSpecialChars = string.punctuation

passWord_list = []

def get_input_range():
    return int(input("How many characters do you want in your password? "))

generate = True

while generate:

    while True:
        try:
            get_range_password = get_input_range()
            if get_range_password < 4:
                print("Password must be at least 4 characters long!")
                
            elif get_range_password > 8:
                print("Password must not exceed 8 characters!")

            else:
                for i in range(get_range_password):
                    i = random.choice(varLetters + varDigits + varSpecialChars)
                    passWord_list.append(i)

            random.shuffle(passWord_list)
            print("\nYour Password is: " + "".join(passWord_list))
            print("Total Characters: " + str(len("".join(passWord_list))))
            passWord_list.clear() #this is to clear the list so that it can be used again for another password generation
            generate = False
        except ValueError:
            print("Please enter a valid number!")

print("Please keep your password safe and secure!")
print("Thank you for using the Password Generator!\n")
