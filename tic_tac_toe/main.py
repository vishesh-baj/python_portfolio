import random


def toss_coin():
    toss_value = ["heads", "tails"]
    chosen_value = random.choice(toss_value)
    return chosen_value


def user_coin_choices(tossed_value):
    print("Choose between heads or tails")
    player_1 = input("player one Enter your prediction: ")
    if tossed_value == player_1:
        print("Player one won the coss")
        return "player_one"
    else:
        print("Player two won the toss")
        return "player_two"


def choose_x_or_o(chosen_player):
    player1_choice = input(f"{chosen_player} choose first between x or o")
    player2_choice = ""
    if player1_choice == "x":
        player2_choice = "o"
    else:
        player2_choice = "x"
    return [
        {chosen_player: player1_choice},
        {"another_player": player2_choice}
    ]


def main():
    chosen_turns = choose_x_or_o(user_coin_choices(toss_coin()))



main()
