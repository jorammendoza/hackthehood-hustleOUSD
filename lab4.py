#Task 1: 
checking = "yes" 

while checking == "yes": 
    print("What is your age: ")
    user_input = input()
    if int(user_input) >= 18:
        print("Yes you can vote")
    else:
        print("You can't vote")
    print ("Would you like to check another age?")
    user_input2 = input()
    checking = user_input2
#Task 2:

List = [-9,  7,  0,  -2,  5]
for i in List:
    if i > 0:
        print(f"{i} is positive")
    elif i < 0:
        print(f"{i} is negative")
    else:
        print(f"{i} is zero") 

#Task 3:

inventory = ["TNT", "Glass", "Grass", "Gold", "Oak Stairs"]

for i in (inventory):
    if i =="gold":
        print(f"You found {i} ,Congrats!")
    else:
        print(f"You have {i}")