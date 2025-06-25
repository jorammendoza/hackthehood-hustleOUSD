menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

# Step 2
def total_price(item1, item2):
    total_sum = menu[item1] + menu[item2]
    return total_sum 

print(total_price('Pizza', 'Burger'))

# Step 3
def price_difference(item3, item4):
    total_difference = abs(menu[item3] - menu[item4])
    return total_difference

print(price_difference('Cheese', 'Hot dog'))

# Step 4
def inflation(item, number):
    menu[item] = menu[item] * number
    return menu 

print (inflation('Ice cream' , 2))

# Step 5
def deflation(item, number):
    menu[item] = menu [item] / number
    return menu

print (deflation('Burger' , 3))

# Step 6
def churrotax():
    menu['Churro'] = menu['Churro'] + 2
    return menu

print(churrotax())