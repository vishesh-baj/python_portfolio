import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

total_letters = int(input("How many letters should be in a password?: "))
total_symbols = int(input("How many symbols should be in a password?: "))
total_numbers = int(input("How many numbers should be in a password?: "))

random_letters = ""
random_numbers = ""
random_symbols = ""
for number in range(0, total_letters):
    random_letters += letters[random.randint(0, len(letters) - 1)]

for number in range(0, total_numbers):
    random_numbers += numbers[random.randint(0, len(numbers) - 1)]

for symbol in range(0, total_symbols):
    random_symbols += symbols[random.randint(0, len(symbols) - 1)]

generated_password = random_letters + random_numbers + random_symbols
randomized_password = ""

for item in generated_password:
    randomized_password += generated_password[random.randint(0, len(generated_password) - 1)]

print(randomized_password)


