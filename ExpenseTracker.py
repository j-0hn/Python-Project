import json
from datetime import date

print("------------------------------\n**** Mini Expense Tracker ****\n------------------------------" 
"\n 1. Add Expense" 
"\n 2. View Expense"
"\n 3. Calculate Expense"
"\n 4. Exit \n ------------------------------")

expenseTracker = None
def expense_list():
    global expenseTracker
    with open("jsonFile/expenseTracker.json", "r") as file:
        expenseTracker = json.load(file)

def option():
    print("1. Add, 2. View, 3. Calculate, 4. Exit\n")

def get_option():
   return int(input("Enter Option: "))

while True:
    num_option = get_option()

    if num_option == 1:
        print("\n--> Add Expense <--")
        name = input("Expense name: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        expense_date = date.today().strftime("%Y-%m-%d") #this is ti convert into string before saving into json file


        expense_list()
        expenseTracker.append({
            "name": name,
            "amount": amount,
            "category": category,
            "date": expense_date
        })

        with open("jsonFile/expenseTracker.json", "w") as file:
                json.dump(expenseTracker, file, indent=2)

        print("Expense Recorded!")


    elif num_option == 2:
        print("\n--> View Expense <--")
        expense_list()
        if expenseTracker == [] or expenseTracker == {}:
            print("No Expenses recorded yet!")
        else:
            expenseTracker.sort(key=lambda item: item["date"])
            for item in expenseTracker:
                print(f"{item['date']}: {item['name']}: {item['amount']}: {item['category']}")

    elif num_option == 3:
        print("\n--> Calculate <--")
        expense_list()
        for item in expenseTracker:
            print(sum(item['amount']))
        

    else:
        break

print("Program Closed!")
