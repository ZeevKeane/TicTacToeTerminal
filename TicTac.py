# ======== Global variables =========
still_going = True
winner = None
current_player = "X"
correct_position = True


# TODO board
# a dict type is used to gather the positional inputs of the players.
class Board:
    def __init__(self):
        pass

    the_board = {1: " ", 2: " ", 3: " ",
                 4: " ", 5: " ", 6: " ",
                 7: " ", 8: " ", 9: " "}


game_board = Board


# TODO display board
# adds extra spaces and formatting to make it more into a tic tac toe board.
def board_display(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[1], board[2], board[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[4], board[5], board[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board[7], board[8], board[9]))
    print("\t     |     |")
    print("\n")


# board_display(game_board.the_board)


# TODO play the game
def play_game():
    # display the initial board:
    board_display(game_board.the_board)

    # a while loop is used since this should run until one condition isn't satisfied anymore, it's easier to coed this
    # than a for loop imo.
    while still_going:
        handle_turn(current_player)
        # calls upon handle_turn to get the position the player wants to place x or o:
        while not correct_position:
            print("Please try another position, this position is already taken")
            handle_turn(current_player)

        check_gameover()
        change_turns()

    if winner == "X" or winner == "O":
        print("The winner is {}.".format(winner))
    elif winner is None:
        print("There is no winner, it's a tie.")

    # TODO handle turns


# takes input of a position to place either x or o depending on which player's turn it is
def handle_turn(player_symbol):
    global correct_position

    print("Player {}'s turn".format(player_symbol))
    position = int(input("Position: "))

    # checks for the validity of the input
    while position not in [x for x in range(1, 10, 1)]:
        position = int(input("Invalid position. Position: "))

    # checks if the position is already taken:
    if game_board.the_board[position] == " ":
        # displaying the choice on the board:
        game_board.the_board[position] = player_symbol
        correct_position = True
    else:
        correct_position = False
    board_display(game_board.the_board)
    return


def check_gameover():
    check_win()
    check_tie()
    return


# TODO check for winner
# checks rows, columns, and diagonals for winning combinations for a player (x or o)
def check_win():
    global winner

    # types of winner:
    r_winner = check_rows()
    c_winner = check_columns()
    d_winner = check_diagonals()

    if check_rows():
        winner = r_winner
    elif check_columns():
        winner = c_winner
    elif check_diagonals():
        winner = d_winner
    else:
        winner = None


# TODO check rows
def check_rows():
    global still_going

    # checks if the row is True but also doesn't mislabel the empty rows as a winning situation.
    row_1 = game_board.the_board[1] == game_board.the_board[2] == game_board.the_board[3] != " "
    row_2 = game_board.the_board[4] == game_board.the_board[5] == game_board.the_board[6] != " "
    row_3 = game_board.the_board[7] == game_board.the_board[8] == game_board.the_board[9] != " "

    # stops the game if someone one!
    if row_1 or row_2 or row_3:
        still_going = False

    # checks and returns who won!
    if row_1:
        return game_board.the_board[1]
    elif row_2:
        return game_board.the_board[4]
    elif row_3:
        return game_board.the_board[7]
    return


# TODO check columns
def check_columns():
    global still_going

    # checks if the columns is True but also doesn't mislabel the empty rows as a winning situation.
    col_1 = game_board.the_board[1] == game_board.the_board[4] == game_board.the_board[7] != " "
    col_2 = game_board.the_board[2] == game_board.the_board[5] == game_board.the_board[8] != " "
    col_3 = game_board.the_board[3] == game_board.the_board[6] == game_board.the_board[9] != " "

    # stops the game if someone one!
    if col_1 or col_2 or col_3:
        still_going = False

    # checks and returns who won!
    if col_1:
        return game_board.the_board[1]
    elif col_2:
        return game_board.the_board[2]
    elif col_3:
        return game_board.the_board[3]
    return


# TODO check diagonals
def check_diagonals():
    global still_going

    # checks if the diagonal is True but also doesn't mislabel the empty rows as a winning situation.
    diagonal_1 = game_board.the_board[1] == game_board.the_board[5] == game_board.the_board[9] != " "
    diagonal_2 = game_board.the_board[3] == game_board.the_board[5] == game_board.the_board[7] != " "

    # stops the game if someone one!
    if diagonal_1 or diagonal_2:
        still_going = False

    # checks and returns who won!
    if diagonal_1:
        return game_board.the_board[1]
    elif diagonal_2:
        return game_board.the_board[3]
    return


# TODO check tie
# if not a win and the game is over
def check_tie():
    global still_going
    if " " not in game_board.the_board.values():
        still_going = False
    return


# TODO flip player
# changes/flips from one player to another, checks x or o and flips it
def change_turns():
    global current_player, correct_position
    if correct_position:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    return


# to initialize the game
play_game()
