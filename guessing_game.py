#  Guessing Game - Joram, Johnny, Beckham

#Step 2
import random


#Step 3
#This function generates and returns a random number between 1 and 100
def generate_random_number():
    return random.randint(1,100)


#Asks user to guess a number between 1 and 100
def get_user_guess():

    while True:
        try:
            guess = int(input("Enter a number between 1-100: "))  #Asks user for input
            if 1 <= guess <= 100:     #Checks if the guess is in the valid range
                return guess
            else:
                print("not in range, guess again") 
        except ValueError:
            print("Invalid Input, please enter a valid number") #Gives error message for a non number input


# Step 4 
def play_guessing_game(): 
    secret_number = generate_random_number() #gets a random number to guess
    attempts = 0 #keeps track of wrongful attempts
    print("i am thinking of a number 1-100, guess and you win")

    while True:  #checks to see if guess is correct guess, too low, or too high and gives feedback.
        guess = get_user_guess()
        attempts += 1

        if guess == secret_number:
            print(f"correct you got it! It took you {attempts} attempts.")
            break

        elif guess < secret_number:
            print("too low, try again")
        else:
            print("too high, try again")

# Step 5
# restarts or ends game based on users choice
def game_loop():
    while True:
        play_guessing_game()
        play_again = input("do you want to play again??? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    game_loop()