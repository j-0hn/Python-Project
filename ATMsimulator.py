print("\n====================")
print("      ATM Menu")
print("====================\n")

myPin = 1234
attemptCount = 0
myBalance = 0
depositCash = 0
withdrawCash = 0
option = 0

def counter(count):
    count += 1
    return count

def get_input_pin():
    return int(input("Enter your PIN: "))

def check_balance(balance):
        print(f"\n**** CHECK BALANCE ****\nYour Balance is $ {balance}")
        if balance <= 0 or balance <= 100:
                print("Please Deposit in your account!\n")
        else: print("Thank you for Banking with us!\n")
        return balance

def get_deposit(prev_balance):
        print("\n**** DEPOSIT ****")
        depositCash = int(input("Enter Amount: "))
        print(f"Total Amount is: {prev_balance + depositCash}\n")
        prev_balance += depositCash
        return prev_balance

def get_withdraw(present_bal):
        withdrawCash = int(input("\nEnter amount to Withdraw: "))

        if present_bal <= 0:
                print("Insufficient Funds!\n")
        elif present_bal <= 100:
                print("Amount Invalid!\n")
        else:
                print("\n**** WITHDRAW CASH ****")
                print(f"The remaining balance is: {present_bal - withdrawCash}\n")
                present_bal -=withdrawCash
        return present_bal


while attemptCount < 3:
   try:
        pin = get_input_pin()
        if len(str(pin)) != 4:
                print("\nPIN must be 4 digits!")
                pin = get_input_pin()
                attemptCount = counter(attemptCount)
                print(f"\nAttempt(s): {attemptCount}")
                
        elif myPin != pin:
                print("\nWrong PIN!")
                pin = get_input_pin()
                attemptCount = counter(attemptCount)
                print(f"\nAttempt(s): {attemptCount}")

        elif len(str(pin)) == 4 and myPin == pin:
                print("Login Successful!\n")
                while True:
                        print("1. Check Balance")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Exit")

                        option = int(input("Choose an option: "))
                        if option == 1:
                                myBalance = check_balance(myBalance)

                        elif option == 2:
                        #to store value of balance and not vanished it
                                myBalance = get_deposit(myBalance)

                        elif option == 3:
                                myBalance = get_withdraw(myBalance)

                        elif option == 4:
                                print("\nGOODBYE! Thank you!")
                                break
   except ValueError:
        print("Please enter a valid number!") 
        attemptCount = counter(attemptCount)
        print(f"\nAttempt(s): {attemptCount}")

print("Attempts Exceeded!")
