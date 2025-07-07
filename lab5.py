# Lab 5 Joram Mendoza

# Step 1
def cat_greeting(word):
    print(f'Cat says {word}')
    print('Cat says im cool')

cat_greeting("meow")

# Step 2
def generate_superhero_power():
    name = "Jimmy"
    power = "teleportation"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# Step 3
def generate_superhero_power1():
    power = "teleportation"
    return power

print(generate_superhero_power1())

# Step 4
def generate_superpower_power2(user_name, super_power):
    message = user_name + " has the power of " + super_power + "!"
    return message

print(generate_superpower_power2("manny", "super speed"))

# Step 5
def cat_greeting_loop(greeting):
    for i in range(5):
        print(f'The cat says {greeting}')

cat_greeting_loop("meow")

# Step 6
def generate_multiple_powers(powers_list):
    for i in powers_list:
        print(i)
powers_test = ["flying", "super jump", "telekinesis"]
generate_multiple_powers(powers_test)