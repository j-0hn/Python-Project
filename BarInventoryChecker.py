import json

with open("jsonFile/liqour.json", "r") as file:
    liquor = json.load(file)

menuOption = None
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
    get_option()

def get_option():
    global menuOption
    menuOption = int(input("Enter your option: "))
    return

def display_list():
    for index, item in enumerate(liquor):
        print(f"{index + 1}. {item['name']}: {item['stock']}")
    get_option()

def add_item():
    add_item = input("Add Stock: ")
    add_stock = input("How many: ")

    liquor.append({
        "name": add_item,
        "stock": int(add_stock)
                })

    write_to_file()
    display_list()
    get_option()

def remove_item():
    remove_item = input("Remove Stock: ")
    for index, item in enumerate(liquor):
        if item['name'] == remove_item or (remove_item.isdigit() and index == (int(remove_item) - 1)):
            remove_item = liquor.pop(index)
            break  
    else:
        print(f"{remove_item} is not in the inventory.")
        return

    write_to_file() 
    print(f"\nYou removed -> {remove_item['name']}: {remove_item['stock']}\n")
    display_list()
    get_option()
    
def check_low_stock():
    lowest_stock = min(item['stock'] for item in liquor)
    for item in liquor:
        if item['stock'] == lowest_stock:
            print(f"{item['name']} is the lowest stock: {item['stock']}")

    get_option()

def search_item():
    search_item = input("Search Item: ")
    if search_item in [item['name'] for item in liquor]:
        index = next(i for i, item in enumerate(liquor) if item['name'] == search_item)
        print(f"{search_item} : {liquor[index]['stock']}")
    else:
        print(f"{search_item} is not in the inventory.")

    get_option()

def total_items():
    total_items = sum(item['stock'] 
    for item in liquor)
    print(f"Total Items in Stock: {total_items}")
    print(f"Total Item: {len(liquor)}")

    get_option()

def write_to_file():
    with open("jsonFile/liqour.json", "w") as file:
        json.dump(liquor, file, indent=2)
            
get_menu()

while True:
   try:
    
    if menuOption >= 1 and menuOption <= 7:
        if menuOption == 1:
            print("\n---> View Inventory <---")
            display_list()

        elif menuOption == 2:
            add_item()
           
        elif menuOption == 3:
            remove_item()
           
        elif menuOption == 4:
            check_low_stock()
           
        elif menuOption == 5:
            search_item()
           
        elif menuOption == 6:
            total_items()
           
        elif menuOption == 7:
            break

    else: 
        print("Incorrect option!\n")
        get_menu()
   except ValueError:
    print("Please enter a valid number!") 
print("\n*** Program CLOSDE! ***\n")
