# Password Generator Project

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

my_list = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


password_list = []
password = ""

for letter in range(0, nr_letters):
    password_list += random.choice(my_list[0])

for symbols in range(0, nr_symbols):
    password_list += random.choice(my_list[2])

for numbers in range(0, nr_numbers):
    password_list += random.choice(my_list[1])

random.shuffle(password_list)

for item in password_list:
    password += item
    print(item)

print(password)



