import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number= random.randint(1,100)
while True:
    try:
     guess=(input("Guess a number: "))
     guess=int(guess)
     if guess==number:
      print("You got it! The answer was ",number)
      break
     elif guess>number:
      print("Too high")
     else:
      print("Too low")
    except ValueError:
      print("Please enter a valid number")
    


