liquor = [
    "Vodka",
    "Gin",
    "Rum",
    "Tequila",
    "Whiskey",
    "Brandy",
]

def getMenu():
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
    return int(input("Enter your option: "))

while True:
    menuOption = getMenu()
    if menuOption <= 1 or menuOption <= 8:
        if menuOption == 1:
            print("---> View Inventory <---")
            print("\n".join(liquor))
            getMenu()
        elif menuOption == 3:
            add_list = input("Add Stock: ")
            liquor.append(add_list)
            print("\n".join(liquor))
        elif menuOption == 4:
            remove_list = input("Remove Stock: ")
            liquor.remove(remove_list)
            print("\n".join(liquor))
    else: 
        print("Incorrect option!")
        getMenu()
    

print("Program closed!")

