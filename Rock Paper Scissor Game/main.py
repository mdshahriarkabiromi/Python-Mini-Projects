import random
import art

choice_list=["rock","paper","scissor"]
computer_choice=random.choice(choice_list)
user_choice=input("Enter your choice: rock, paper or scissor? ").lower()
if user_choice=="rock":
  print("You chose rock")
  print(art.rock)
  if computer_choice=="rock":
    print(f"Computer chose rock\n")
    print(art.rock)
    print("It's a draw")
  elif computer_choice=="paper":
    print(f"Computer chose paper\n")
    print(art.paper)
    print("You lose")
  else:
    print(f"Computer chose scissor\n")
    print(art.scissors)
    print("You win")
elif user_choice=="paper":
  print("You chose paper")
  print(art.paper)
  if computer_choice=="rock":
    print(f"Computer chose rock\n")
    print(art.rock)
    print("You win")
  elif computer_choice=="paper":
    print(f"Computer chose paper\n")
    print(art.paper)
    print("It's a draw")
  else:
    print(f"Computer chose scissor\n")
    print(art.scissors)
    print("You lose")
else:
  print("You chose scissor")
  print(art.scissors)
  if computer_choice=="rock":
    print(f"Computer chose rock\n")
    print(art.rock)
    print("You lose")
  elif computer_choice=="paper":
    print(f"Computer chose paper\n")
    print(art.paper)
    print("You win")
  else:
    print(f"Computer chose scissor\n")
    print(art.scissors)
    print("It's a draw")