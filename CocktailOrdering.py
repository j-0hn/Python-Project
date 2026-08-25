print("----- Cocktail Ordering System -----\n")

#use list[] and dictionaries{}
drinks = [
    {"name" : "Shanghai Essence", "price" : 128},
    {"name" : "Shanghai Savor", "price" : 120},
    {"name" : "Mojito", "price" : 110},
    {"name" : "Negroni", "price" : 128},
    {"name" : "Old Fashion", "price" : 128}
]

order_list = []
total = 0
while True:
    try:
        print("1. View list \n2. Order")
        option = int(input("\nChoose an option: "))
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
            
            while True:
                print("\nOrder when you ready!")
                for index, myDrink in enumerate(drinks, start = 1):
                    print(index, myDrink["name"], myDrink["price"])
                choice = int(input("\nEnter Order: "))
                drink_name = drinks[choice - 1]
                #print(f"Order: {drink_name["name"]} : {drink_name["price"]}")
                
                order_list.append({"name" : drink_name["name"], "price" : drink_name["price"]})

                order_again = input("Order Again Y or N: ")
                if order_again == "Y" or order_again == "y":
                    continue
                else: 
                    print("\nYour Order is:")
                    for index, my_order in enumerate(order_list, start = 1):
                        print(index, my_order["name"], my_order["price"])

                    for order in order_list:
                        total += order["price"]
                    print("Total: ", total)
                    break

    except ValueError:
        print("Input valid number!")
print("Thank you Using Ordering Systen!")
