#loop
#ask user if they want to roll the dice
#if the ans is yes, generate two random number and print them
#if the ans is no, then print a message and terminate the program
#if the ans is not yes or no, print invalid choice
import random
import art

print(art.logo)
while True:
    ans = input("Do you want to roll the dice? (yes/no): ").lower()
    if ans == "yes":
        print("Rolling the dice...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"Dice 1: {dice1}")
        print(f"Dice 2: {dice2}")
    elif ans == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter yes or no.")
    
