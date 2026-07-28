import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letter = input("would you like letters in your password? (yes or no)")
password = ""
if letter == "yes":
    for _ in range(0, 4):
        random_letter = random.choice(letters)
        password += random_letter

symbol = input("would you like symbols in your password? (yes or no)")
if symbol == "yes":
    for _ in range(0, 2):
        random_symbol = random.choice(symbols)
        password += random_symbol

number = input("would you like numbers in your password? (yes or no)")
if number == "yes":
    for _ in range(0, 3):
        random_number = random.choice(numbers)
        password += random_number

print(password)

#////////////////////////////

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

initial_password = ""
for _ in range(nr_letters):
    chosen_letter = random.choice(letters)
    initial_password += chosen_letter

for _ in range(nr_symbols):
    chosen_symbol = random.choice(symbols)
    initial_password += chosen_symbol

for _ in range(nr_numbers):
    chosen_number = random.choice(numbers)
    initial_password += chosen_number
password_list = list(initial_password)

random.shuffle(password_list)

final_password = "".join(password_list)
print(final_password)


