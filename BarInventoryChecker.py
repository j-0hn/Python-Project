liquor = [
    "Vodka",
    "Gin",
    "Rum",
    "Tequila",
    "Whiskey",
]
stock = [5, 3, 8, 2, 6]

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

def display_list():
    for my_liquors, my_stocks in zip(liquor, stock):
        print(my_liquors, my_stocks)

get_menu()
menuOption = get_option()



while True:
    if menuOption <= 1 or menuOption <= 8:
        if menuOption == 1:
            print("\n---> View Inventory <---")
            #to show the list together with stocks list
            display_list()
            #for i in range(len(liquor)):
             #   print(f"{liquor[i]} : {stock[i]}")
            menuOption = get_option()

        elif menuOption == 2:
            add_list = input("Add Stock: ")
            add_stock = input("How many: ")
            liquor.append(add_list)
            stock.append(add_stock)
            display_list()
            menuOption = get_option()

        elif menuOption == 3:
            remove_list = input("Remove Stock: ")
            #i used index() here to get the index of my list
            if remove_list in liquor:
                index = liquor.index(remove_list)
                #pop() it will remove from your list and
                #and return what you removed
                remove_item = liquor.pop(index)
                remove_stock = stock.pop(index)
                print(f"\nYou removed -> {remove_item} : {remove_stock}\n")
                display_list()

        elif menuOption == 4:
            print("Checking Low Stocks")
            lowest_stock = min(stock)
            #high_stock = max(stock)
            for my_liquors, my_stocks in zip(liquor, stock):
                if lowest_stock == my_stocks:
                    print(my_liquors, "is the lowest stock" ,my_stocks)
            menuOption = get_option()

        elif menuOption == 7:
            break

    else: 
        print("Incorrect option!\n")
        get_menu()
        menuOption = get_option()
        
print("\n*** Program CLOSDE! ***\n")

