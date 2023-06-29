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


def goodbye_greeting(item):
    print(f"Here is your {item}!\n See you again soon!")
    exit(0)

