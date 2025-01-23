import sys
import logo
print(logo.calculator_logo)
print("Hello there! Welcome to the BMI Calculator.")
print("Would you like to calculate your BMI?")
print("1. Yes")
print("2. No")
choice = input("Please enter your choice (1 or 2): \n").lower()

if choice == "1" or "yes":
    print("Great! Please provide the following information.")
    height = float(input("Enter your height in meters: \n"))
    weight = float(input("Enter your weight in kilograms: \n"))
    bmi = weight / (height * height)
    
    print(f"\nYour BMI is: {bmi:.2f}")
    
    if bmi < 18.5:
        print("You are classified as Underweight.")
    elif 18.5 <= bmi < 25:
        print("You are classified as Normal weight.")
    elif 25 <= bmi < 30:
        print("You are classified as Overweight.")
    else:
        print("You are classified as Obese.")
else:
    print("Thank you for using the BMI Calculator. Have a great day!")
    sys.exit()
