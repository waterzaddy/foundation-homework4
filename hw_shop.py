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

