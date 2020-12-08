# Create a function which takes as input two dicts with structure mentioned below,
# then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0

for key, value in stock.items():
    print(key, '-', value,'*', prices[key], '=', value * prices[key])
    total_price +=  value * prices[key]
print('Total price:', format(float(total_price), '.2f'))