print("Case 1:----")
x = 10
y = 5
# encountered a zerodivision error, fixed by dividing by 5
result = x / y
print("Result:", result)

print ("Case 2:----")
numbers = [1, 2, 3, 4, 5]
# encountered a list index error thats out of range, fixed by removing +1 from print statement.
for i in range(len(numbers)):
   print(numbers[i])

print ("Case 3:-----")
def calculate_area(radius):
   #encountered a syntax error, fixed by adding a colon.
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

print("Case 4:-------")
# 2 missing colons in if and else
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

print("Case 5:------")
# missing colon 
for i in range(5):
   print(i)


print("Case 6:-----")
# invalid syntax, fixed it by adding a +
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

print("Case 7:-----")
# indentation error, fixed by adding correct indentation.
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

print("Case 8:----")
# recursion error, took away the + and replaced it with a -
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

print("Case 9:-----")
#logical error, fixed this by adding "name == "Bob"
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")

print("Case 10:----")
# zero division error, fixed by changing 0 to 2
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))
