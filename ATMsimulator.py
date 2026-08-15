print("\n====================")
print("      ATM Menu")
print("====================\n")

myPin = 1234
attempCount = 0

myBalance = 0
depositCash = 0
withdrawCash = 0
option = 0

#To check the PIN if Correct
pin = input("Enter your PIN: ")

if len(str(pin)) != 4 or len(str(pin)) > 4:
        print("PIN must be 4 digits!")
        while myPin != int(pin):
           print("\nWrong PIN!")
           pin = input("Re-Enter PIN: ")
        
           attempCount += 1
           print(f"\nAttempt(s): {attempCount}")
           if attempCount > 2:
              break
        
elif not pin.isdigit():
        print("Please Input Numbers only!")
        while myPin != int(pin):
           print("\nWrong PIN!")
           pin = input("Re-Enter PIN: ")
        
           attempCount += 1
           print(f"\nAttempt(s): {attempCount}")
           if attempCount > 2:
              break
elif pin.isdigit() and len(str(pin)) == 4:
        
        while myPin != int(pin):
           print("\nWrong PIN!")
           pin = input("Re-Enter PIN: ")
        
           attempCount += 1
           print(f"\nAttempt(s): {attempCount}")
           if attempCount > 2:
              break
else:
        print("Remember your PIN!")



if myPin == int(pin):
    print("Login Successful!\n")

    while option != 4:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
        option = int(input("Choose an option: "))
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
else:
    print("Attempts Exceeded!")
