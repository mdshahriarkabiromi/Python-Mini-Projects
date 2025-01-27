import art
import random

print(art.logo)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]
N=nr_letters
for letter in range(N):
    l_pass=random.choice(letters)
    password_list+=l_pass

N=nr_symbols
for symbol in range(N):
    s_pass=random.choice(symbols)
    password_list+=s_pass

N=nr_numbers
for number in range(N):
    n_pass=random.choice(numbers)
    password_list+=n_pass

random.shuffle(password_list)

password=""
for char in password_list:
    password+=char

print(f"Your Password is: {password}")


