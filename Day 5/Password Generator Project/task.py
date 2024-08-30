import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy version
pwd_easy = ""
for i in range(0, nr_letters-nr_symbols-nr_numbers):
    pwd_easy += random.choice(letters)

for i in range(0, nr_symbols):
    pwd_easy += random.choice(symbols)

for i in range(0, nr_numbers):
    pwd_easy += random.choice(numbers)

print(f"Password using easy method is {pwd_easy}")

#Hard version
pwd_arr = []
for i in range(0, nr_letters-nr_symbols-nr_numbers):
    pwd_arr.append(random.choice(letters))

for i in range(0, nr_symbols):
    pwd_arr.append(random.choice(symbols))

for i in range(0, nr_numbers):
    pwd_arr.append(random.choice(numbers))

random.shuffle(pwd_arr)

pwd_hard = ""
for char in pwd_arr:
    pwd_hard += char

print(f"Password using hard method is {pwd_hard}")

