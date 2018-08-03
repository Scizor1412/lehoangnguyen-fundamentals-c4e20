prices = {
    'banana' : 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}

stock = {
    'banana' : 6,
    'apple' : 0,
    'orange' : 32,
    'pear': 15
}

total_money = 0

for key, value in prices.items():
    money = value*(stock[key])
    print (money)
    total_money += money
    
print(total_money)