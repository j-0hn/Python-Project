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

#To check the PIN if Correct
pin = input("Enter your PIN: ")

while attemptCount < 3:

   if len(pin) != 4:
        print("\nPIN must be 4 digits!")
        pin = input("Re-Enter PIN: ")
        attemptCount = counter(attemptCount)
        print(f"\nAttempt(s): {attemptCount}")

   elif not pin.isdigit():
        print("\nPlease Input Numbers only!")
        pin = input("Re-Enter PIN: ")
        attemptCount = counter(attemptCount)
        print(f"\nAttempt(s): {attemptCount}")

   elif myPin != int(pin):
        print("\nWrong PIN!")
        pin = input("Re-Enter PIN: ")
        attemptCount = counter(attemptCount)
        print(f"\nAttempt(s): {attemptCount}")

   elif pin.isdigit() and len(pin) == 4:
        pin = int(pin)
        print("Login Successful!\n")
        
        if myPin == pin:

           while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                option = input("Choose an option: ")
                option = int(option)
                if option == 1:
                        print(f"\n**** CHECK BALANCE ****\nYour Balance is $ {myBalance}")
                        if myBalance <= 0 or myBalance <= 100:
                           print("Please Deposit in your account!\n")
                        else: print("Thank you for Banking with us!\n")

                elif option == 2:
                        print("\n**** DEPOSIT ****")
                        depositCash = int(input("Enter Amount: "))
                        print(f"Total Amount is: {myBalance + depositCash}\n")
                        myBalance +=depositCash

                elif option == 3:
                        withdrawCash = int(input("\nEnter amount to Withdraw: "))
                        
                        if myBalance <= 0:
                                print("Insufficient Funds!\n")
                        elif myBalance <= 100:
                                print("Amount Invalid!\n")
                        else:
                                print("\n**** WITHDRAW CASH ****")
                                print(f"The remaining balance is: {myBalance - withdrawCash}\n")
                                myBalance -=withdrawCash

                elif option == 4:
                        print("\nGOODBYE! Thank you!")
                        break
        
print("Attempts Exceeded!")
