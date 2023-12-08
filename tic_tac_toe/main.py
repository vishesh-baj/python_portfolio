import random


def toss_coin():
    toss_value = ["heads", "tails"]
    chosen_value = random.choice(toss_value)
    return chosen_value


def user_coin_choices(tossed_value):
    print("Choose between heads or tails")
    player_1 = input("Player one, enter your prediction: ").lower()
    if tossed_value == player_1:
        print("Player one won the toss")
        return "player_one"
    else:
        print("Player two won the toss")
        return "player_two"


def choose_x_or_o(chosen_player):
    while True:
        player1_choice = input(f"{chosen_player}, choose X or O: ").upper()
        if player1_choice in ["X", "O"]:
            player2_choice = "O" if player1_choice == "X" else "X"
            return [player1_choice, player2_choice]
        else:
            print("Invalid choice. Please choose X or O.")


def print_board(game_matrix):
    for row in game_matrix:
        print(" ".join(row))
    print()


def check_win_condition(game_matrix):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (game_matrix[i][0] == game_matrix[i][1] == game_matrix[i][2] != "_") or \
                (game_matrix[0][i] == game_matrix[1][i] == game_matrix[2][i] != "_"):
            return True
    if (game_matrix[0][0] == game_matrix[1][1] == game_matrix[2][2] != "_") or \
            (game_matrix[0][2] == game_matrix[1][1] == game_matrix[2][0] != "_"):
        return True
    return False


def is_board_full(game_matrix):
    return all(cell != "_" for row in game_matrix for cell in row)


def play_turn(game_board, player_turn):
    while True:
        print_board(game_board)
        coordinates = input(f"{player_turn}, enter row and column (e.g., 0 1): ").split()

        if len(coordinates) != 2:
            print("Invalid input. Please enter row and column separated by a space.")
            continue

        row_coordinate, col_coordinate = map(int, coordinates)

        if not (0 <= row_coordinate < 3 and 0 <= col_coordinate < 3):
            print("Invalid coordinates. Row and column must be between 0 and 2.")
            continue

        if game_board[row_coordinate][col_coordinate] != "_":
            print("The position is already taken. Choose another position.")
        else:
            game_board[row_coordinate][col_coordinate] = player_turn
            break

    if check_win_condition(game_board):
        print_board(game_board)
        print(f"{player_turn} wins!")
        return True
    elif is_board_full(game_board):
        print_board(game_board)
        print("It's a tie!")
        return True

    return False


def create_matrix(length):
    parent_list = []
    for i in range(0, length):
        parent_list.append(["_", "_", "_"])
    return parent_list


# random walk
def random_walk():


def main():
    game_over = False
    turn = 0
    game_board = create_matrix(3)
    chosen_turns = choose_x_or_o(user_coin_choices(toss_coin()))

    while not game_over:
        game_over = play_turn(game_board, chosen_turns[turn])
        turn = (turn + 1) % 2


if __name__ == "__main__":
    main()



