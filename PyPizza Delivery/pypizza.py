import logo
print(logo.pypizza_logo)
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L: ").upper()
while size not in ["S", "M", "L"]:
    print("Invalid input. Please choose S, M, or L.")
    size = input("What size pizza do you want? S, M, or L: ").upper()

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
while pepperoni not in ["Y", "N"]:
    print("Invalid input. Please choose Y or N.")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
while extra_cheese not in ["Y", "N"]:
    print("Invalid input. Please choose Y or N.")
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

mushrooms = input("Do you want mushrooms on your pizza? Y or N: ").upper()
while mushrooms not in ["Y", "N"]:
    print("Invalid input. Please choose Y or N.")
    mushrooms = input("Do you want mushrooms on your pizza? Y or N: ").upper()

olives = input("Do you want olives on your pizza? Y or N: ").upper()
while olives not in ["Y", "N"]:
    print("Invalid input. Please choose Y or N.")
    olives = input("Do you want olives on your pizza? Y or N: ").upper()

bill = 0

# Base price based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add-ons
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

if mushrooms == "Y":
    bill += 1.5

if olives == "Y":
    bill += 1.5

# Apply discount for large orders
if bill > 30:
    bill *= 0.9  # 10% discount

print(f"Your final bill is: ${bill:.2f}.")
