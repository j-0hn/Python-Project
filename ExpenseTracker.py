print("------------------------------\n**** Mini Expense Tracker ****\n------------------------------" 
"\n 1. Add Expense" 
"\n 2. View Expense"
"\n 3. Calculate Expense"
"\n 4. Exit \n ------------------------------")

def option():
    print("1. Add, 2. View, 3. Calculate, 4. Exit\n")

def get_option():
   return int(input("Enter Option: "))

while True:
    num_option = get_option()

    if num_option == 1:
        print("add")
    elif num_option == 2:
        print("view")
    elif num_option == 3:
        print("calculate")
    else:
        break


print("Program Closed!")
