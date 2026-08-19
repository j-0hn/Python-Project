print("------------------------------")
print("*** Bar Inventory Checker ***")
print("------------------------------")

print("1. View Inventory")
print("2. Check Item Stock")
print("3. Add Stock")
print("4. Remove Stock")
print("5. Check Low Stock")
print("6. Search Item")
print("7. Show Total Items")
print("8. Exit")
print("\nPlease select an option from the menu above.")


menuOption = int(input("Enter your option: "))

while True:
    if menuOption <= 1 or menuOption <= 8:
        print("Correct option!")
    else: print("Incorrect option!")
    break

print("Program closed!")

