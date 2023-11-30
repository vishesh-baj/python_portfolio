import random
print("Welcome to black jack game")

# todo: create an array with 1 - 10 with 3  more 10 for J Q and K cards
# todo: randomly pick two cards out of the deck for computer and user that is playing the game
# todo: ask for another card for user, if the sum of all cards exceed by 21, computer will win the game else, user wins
# todo: Show the final result and cards for computer and user
# todo: ask user to play the game again

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def pick_cards_at_random(list_of_cards,num_of_cards_to_pick):
    random_cards = []
    for card in range(0, num_of_cards_to_pick):
        random_cards.append(random.choice(list_of_cards))
    print(random_cards)
    return random_cards


game_over = False


while not game_over:
    play_blackjack = input("Would you like to play blackjack? 'y' for yes. 'n' for no ")
    if play_blackjack == "y":
        player_cards = pick_cards_at_random(deck, 2)
        computer_cards = pick_cards_at_random(deck, 2)
        print("Your Cards are: ", player_cards)
        print("One of Computer Cards is: ", random.choice(computer_cards))
        want_another_card = input("Would you like to draw another card? 'y' for yes, 'n' for no: ")
        if want_another_card == "n":
            player_result = sum(player_cards)
            computer_result = sum(computer_cards)
            if player_result > computer_result:
                print(f"You Won, You have total of {player_result} score")
            else:
                print(f"Computer won with total of {computer_result} score ")
        elif want_another_card == "y":
            player_cards.extend(pick_cards_at_random(deck, 1))
            print(player_cards)
            if sum(player_cards) > 21:
                print("You loose as total of your cards exceeds 21")
                game_over = True
            elif sum(player_cards) > sum(computer_cards):
                print("You won")
            else:
                print("Computer won")
    else:
        game_over = True








