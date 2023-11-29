import random


def toss_coin():
    toss_value = ["heads", "tails"]
    chosen_value = random.choice(toss_value)
    return chosen_value


def user_coin_choices(tossed_value):
    print("Choose between heads or tails")
    player_1 = input("player one Enter your prediction: ")
    if tossed_value == player_1:
        print("Player one won the toss")
        return "player_one"
    else:
        print("Player two won the toss")
        return "player_two"


def choose_x_or_o(chosen_player):
    player1_choice = input(f"{chosen_player} choose first between x or o: ")
    player2_choice = ""
    if player1_choice == "x":
        player2_choice = "o"
    else:
        player2_choice = "x"
    return [player1_choice, player2_choice]


def create_matrix(length):
    parent_list = []
    for i in range(0, length):
        parent_list.append(["_", "_", "_"])
    return parent_list


def play_turn(game_board, player_turn):
    updated_game_board = game_board
    correct_condition = False

    while not correct_condition:
        coordinates = input(f"{player_turn} Enter coordinates with spaces: ").split(" ")
        row_coordinate = int(coordinates[0])
        column_coordinate = int(coordinates[1])

        if updated_game_board[row_coordinate][column_coordinate] != "_":
            print("The position is already taken, choose another position")
        else:
            updated_game_board[row_coordinate][column_coordinate] = player_turn
            print(updated_game_board)
            correct_condition = True

    return updated_game_board


def main():
    game_over = False
    turn = 0
    game_board = create_matrix(3)
    chosen_turns = choose_x_or_o(user_coin_choices(toss_coin()))
    while not game_over:
        game_board = play_turn(game_board, chosen_turns[turn])
        if not play_turn(game_board, chosen_turns[turn]):
            turn = turn
        else:
            turn = (turn + 1) % 2



main()
