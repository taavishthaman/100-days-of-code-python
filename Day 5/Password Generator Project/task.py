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
pwd_hard = ""
total_letters = nr_letters - nr_symbols - nr_numbers
i = 0
while i < nr_letters:
    #Take a choice of either choosing a letter = 0, symbol = 1 or number = 2
    choice = random.randint(0,2)

    if choice == 0 and total_letters > 0:
        pwd_hard += random.choice(letters)
        total_letters -= 1
        i += 1
    elif choice == 1 and nr_symbols > 0:
        pwd_hard += random.choice(symbols)
        nr_symbols -= 1
        i += 1
    elif choice == 2 and nr_numbers > 0:
        pwd_hard += random.choice(numbers)
        nr_numbers -= 1
        i += 1

print(f"Password using hard method is {pwd_hard}")

