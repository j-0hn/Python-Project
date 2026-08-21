liquor = [
    "Vodka",
    "Gin",
    "Rum",
    "Tequila",
    "Whiskey",
    "Brandy",
]
stock = [5, 3, 8, 2, 6, 4]

def get_menu():
    print("------------------------------")
    print("*** Bar Inventory Checker ***")
    print("------------------------------")
    print("1. View Inventory")
    print("2. Add Stock")
    print("3. Remove Stock")
    print("4. Check Low Stock")
    print("5. Search Item")
    print("6. Show Total Items")
    print("7. Exit")
    print("\nPlease select an option from the menu above.")

def get_option():
    return int(input("Enter your option: "))


get_menu()
menuOption = get_option()

while True:
    if menuOption <= 1 or menuOption <= 8:
        if menuOption == 1:
            print("\n---> View Inventory <---")
            #to show the list together with stocks list
            for i in range(len(liquor)):
                print(f"{liquor[i]} : {stock[i]}")
            menuOption = get_option()

        elif menuOption == 2:
            add_list = input("Add Stock: ")
            add_stock = input("How many: ")
            liquor.append(add_list)
            stock.append(add_stock)
            for i in range(len(liquor)):
                print(f"{liquor[i]} : {stock[i]}")
            menuOption = get_option()

        elif menuOption == 3:
            remove_list = input("Remove Stock: ")
            
            liquor.remove(remove_list)
            print("\n".join(liquor))

    else: 
        print("Incorrect option!\n")
        get_menu()
        menuOption = get_option()
        
print("Program closed!")

