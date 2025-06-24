# Lab 3

# Task 1: Working with Strings
food = 'Steak Burritos'
print(food[:3]) #Print first 3 characters
print(food[-3:]) #Print last 3 charcters
first_last = food[0] + food [-1] #combine first and last character
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)

# Task 2: Working with Lists
number_list = [1, 767564746, 32, -5, 0, 234]
number_list.append(23)
print(number_list)
number_list.insert(3, 1000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1]) 
print(number_list)
print(number_list[0:3])
print(number_list[-3:])

# Task 3: Working with Dictionaries
books = {'Jeff Kinney': 'Diary of a Wimpy Kid', 'Lauren Tarshis': 'I Survived', 'R.L. Stine': 'Goosebumps'} 
print(books.keys())
print(books.values())
print(books.get('Lauren Tarshis'))
print(books.pop('Jeff Kinney'))
print(books)
del books['Lauren Tarshis']
print(books)