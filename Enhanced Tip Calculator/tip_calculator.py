import logo
print(logo.calculator_logo)

tip_percentage = 0
print("Welcome to Green Bay Restaurants!")

enjoyment = input("Did you enjoy your meal? (Yes or No)\n").lower()
if enjoyment == "yes":
    service_quality = input("How would you rate our service? (Excellent, Good, Average, Poor)\n")

    if service_quality == "Excellent":
        tip_percentage += 5
    elif service_quality == "Good":
        tip_percentage += 3
    elif service_quality == "Average":
        tip_percentage += 1
    elif service_quality == "Poor":
        tip_percentage -= 2
else:
    print("We're sorry to hear that you didn't enjoy your meal. We appreciate your feedback.")

bill = float(input("What is your total bill amount?\n"))
additional_tip = int(input("What percentage of tip would you like to give? (5, 10, 20)\n"))
tip_percentage += additional_tip
num_people = int(input("How many people are splitting the bill?\n"))

tip_amount = bill * (tip_percentage / 100)
total_amount = bill + tip_amount
amount_per_person = total_amount / num_people

print(f"\nSummary of your bill:")
print(f"Selected tip percentage: {tip_percentage}%")
print(f"Calculated tip amount: ${tip_amount:.2f}")
print(f"Total bill amount including tip: ${total_amount:.2f}")
print(f"Each person should pay: ${amount_per_person:.2f}")
