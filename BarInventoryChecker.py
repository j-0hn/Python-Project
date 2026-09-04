import json

with open("jsonFile/liqour.json", "r") as file:
    liquor = json.load(file)

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
    #to display list together
    for item in liquor:
        print(f"{item['name']}: {item['stock']}")

get_menu()

while True:
   try:
    menuOption = get_option()
    if menuOption >= 1 and menuOption <= 7:
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
            #liquor.append({"name": add_list, "stock": int(add_stock)})

            with open("jsonFile/liqour.json", "a") as file:
                file.write({"name": add_list, "stock": int(add_stock)})


            display_list()
            menuOption = get_option()

        elif menuOption == 3:
            remove_item = input("Remove Stock: ")
            for index, item in enumerate(liquor):
                if item['name'] == remove_item:
                    remove_item = liquor.pop(index)

            print(f"\nYou removed -> {remove_item['name']}: {remove_item['stock']}\n")
            display_list()

        elif menuOption == 4:
            print("Checking Low Stocks")
            lowest_stock = min(item['stock'] for item in liquor)
            #high_stock = max(stock)
            for item in liquor:
                if item['stock'] == lowest_stock:
                    print(f"{item['name']} is the lowest stock: {item['stock']}")
            menuOption = get_option()

        elif menuOption == 5:
            search_item = input("Search Item: ")
            if search_item in [item['name'] for item in liquor]:
                index = next(i for i, item in enumerate(liquor) if item['name'] == search_item)
                print(f"{search_item} : {liquor[index]['stock']}")
            else:
                print(f"{search_item} is not in the inventory.")
            menuOption = get_option()

        elif menuOption == 6:
            total_items = sum(item['stock'] for item in liquor)
            print(f"Total Items in Stock: {total_items}")
            menuOption = get_option()
            
        elif menuOption == 7:
            break

    else: 
        print("Incorrect option!\n")
        get_menu()
        menuOption = get_option()
   except ValueError:
    print("Please enter a valid number!") 
print("\n*** Program CLOSDE! ***\n")
