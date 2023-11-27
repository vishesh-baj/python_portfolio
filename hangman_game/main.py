import random

word_list = ["awesome", "baboon", "camel"]

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
game_counter = len(chosen_word) + 1

blank_word = []
for letter in range(0, len(chosen_word)):
    blank_word.append("_")

while game_counter > 0:
    if game_counter == 0:
        print("Game Over")
    else:
        if blank_word.count("_") == 0:
            print("You Won")
            game_counter = 0
        else:
            print(f"You have {game_counter} tries left")
            guess = input("Enter your guessed letter: ").lower()
            for index in range(0, len(chosen_word)):
                letter = chosen_word[index]
                if letter == guess:
                    blank_word[index] = letter
                    print(blank_word)

    game_counter -= 1
