import random
print("Welcome to banker Roulette")
total_bankers = input("Enter all bankers separated by a ',': ")


def get_random_banker(string):
    string_list = string.split(',')
    random_banker = string_list[random.randint(0, len(string_list) - 1)]
    print(f"{random_banker} should pay the bill")


get_random_banker(total_bankers)

