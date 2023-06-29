prices = {
    "Denim Jacket": 65,
    "Sunglasses": 20,
    "Trainers": 150
}

customer_balance = 100


def purchase(item, customer_balance):
    if customer_balance >= prices.get(item):
        return True
    else:
        return False


def welcome_message():
    print("Hello & welcome to Kelli's Closet!\nCurrently we have these items for sale:")
    for item in prices:
        print(f"{item} - £{prices.get(item)}")

    choice = input("\nWould you like to buy anything?\nEnter 'exit' to exit the shop\n")

    if choice == "exit":
        exit(0)
    elif choice in prices.keys():
        if purchase(choice, customer_balance):
            goodbye_greeting(choice)
        else:
            retry_purchase(choice, customer_balance)
    else:
        raise ValueError("Not a valid answer, please try again")


def goodbye_greeting(item):
    print(f"Here is your {item}!\n See you again soon!")
    exit(0)

