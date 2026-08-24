print("----- Cocktail Ordering System -----\n")

#use list[] and dictionaries{}
drinks = [
    {"name" : "Shanghai Essence", "price" : 128},
    {"name" : "Shanghai Savor", "price" : 120},
    {"name" : "Mojito", "price" : 110},
    {"name" : "Negroni", "price" : 128},
    {"name" : "Old Fashion", "price" : 128}
]
option = 0
while True:
    try:
        print("1. View list \n2. Order")
        option = int(input("\nChoose an option: \n"))
        if option == 1:
            print("\n*** Cocktails ***")

            for index, myDrink in enumerate(drinks, start = 1):
                my_index = index
                my_order_name = myDrink["name"]
                my_order_price = myDrink["price"]
                print(index, myDrink["name"], myDrink["price"])
            
            go_to_order = input("\nProceed to Order? Y or N: ")
            if go_to_order == "Y" or go_to_order == "y":
                continue
            else:
                break
            
        elif option == 2:
            print("Order when you ready!")
            for index, myDrink in enumerate(drinks, start = 1):
                print(index, myDrink["name"], myDrink["price"])
            choice = int(input("Enter Order: "))
            my_order = drinks[choice - 1]
            print("You selected: ", my_order["name"])
            print("Price is: ", my_order["price"])


    except ValueError:
        print("Input valid number!")

print("Thank you Using Ordering Systen!")
