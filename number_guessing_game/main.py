import random

print("Welcome to Number Guessing Game")

game_over = False


def generate_random_guess():
    arr = []
    for number in range(0, 100):
        arr.append(number)
    return random.choice(arr)


def check_if_correct_guess(user_number, generated_number):
    if user_number > generated_number:
        print("Your guess is too high")
        return "high"

    elif user_number < generated_number:
        print("Your guess is too low")
        return "low"
    elif user_number == generated_number:
        print("You guessed correct")
        return "correct"


total_chances = ""
print("I am guessing a number between 0 and 100")
difficulty = input("Select a difficulty between easy and hard: ")
if difficulty == "easy":
    total_chances = 10
else:
    total_chances = 5

random_number = generate_random_guess()

while not game_over:
    if total_chances == 0:
        game_over = True
        break
    else:
        user_guess = int(input("Guess a number: "))
        outcome = check_if_correct_guess(user_guess, random_number)
        if outcome == "high":
            total_chances -= 1
            print(f"You have {total_chances} chances remaining")
        elif outcome == "low":
            total_chances -= 1
            print(f"You have {total_chances} chances remaining")
        elif outcome == "correct":
            print("Your guess is CORRECT")
            game_over = True
            break



