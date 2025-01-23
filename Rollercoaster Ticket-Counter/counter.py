import logo
print(logo.counter_logo)

print("Welcome to the Python Rollercoaster Adventure!")

# Get and validate height input
height = int(input("What is your height in cm? "))
while height <= 0:
    print("Height must be a positive number.")
    height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    # Get and validate age input
    age = int(input("What is your age? "))
    while age <= 0:
        print("Age must be a positive number.")
        age = int(input("What is your age? "))

    # Determine ticket price based on age
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Senior Citizen tickets are free.")
    elif age > 55:
        bill = 8
        print("Senior tickets are $8.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # Ask if the user wants a photo
    wants_photo = input("Do you want a photo taken? Y or N: ").upper()
    while wants_photo not in ["Y", "N"]:
        print("Please enter Y or N.")
        wants_photo = input("Do you want a photo taken? Y or N: ").upper()

    if wants_photo == "Y":
        bill += 3

    # Ask if the user is booking for a group
    group_booking = input("Are you booking for a group of 4 or more? Y or N: ").upper()
    while group_booking not in ["Y", "N"]:
        print("Please enter Y or N.")
        group_booking = input("Are you booking for a group of 4 or more? Y or N: ").upper()

    if group_booking == "Y":
        group_size = int(input("How many people are in your group? "))
        while group_size < 4:
            print("Group size must be 4 or more for a discount.")
            group_size = int(input("How many people are in your group? "))
        
        total_bill = bill * group_size
        total_bill *= 0.9  # 10% discount for group bookings
    else:
        total_bill = bill

    print(f"Your final bill is ${total_bill:.2f}")

else:
    print("Sorry, you have to grow taller before you can ride.")
