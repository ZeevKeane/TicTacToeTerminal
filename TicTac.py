# ======== Global variables =========
still_going = True
winner = None
current_player = "X"

# TODO board
# a dict type is used to gather the positional inputs of the players.
the_board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}


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


# board_display(the_board)


# TODO play the game
def play_game():
    # display the initial board:
    board_display(the_board)

    # a while loop is used since this should run until one condition isn't satisfied anymore, it's easier to coed this
    # than a for loop imo.
    while still_going:
        # calls upon handle_turn to get the position the player wants to place x or o:
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
    position = int(input("Position: "))

    # displaying the choice on the board:
    the_board[position] = player_symbol
    board_display(the_board)


def check_gameover():
    check_win()
    check_tie()
    return


# TODO check for winner
# checks rows, columns, and diagonals for winning combinations for a player (x or o)
def check_win():
    global winner

    if check_rows() or check_columns() or check_diagonals():
        winner = True
    else:
        winner = None
    return
    

# TODO check rows
def check_rows():
    global still_going

    # checks if the row is True but also doesn't mislabel the empty rows as a winning situation.
    row_1 = the_board[1] == the_board[2] == the_board[3] != " "
    row_2 = the_board[4] == the_board[5] == the_board[6] != " "
    row_3 = the_board[7] == the_board[8] == the_board[9] != " "

    # stops the game if someone one!
    if row_1 or row_2 or row_3:
        still_going = False

    # checks and returns who won!
    if row_1:
        return the_board[1]
    elif row_2:
        return the_board[4]
    elif row_3:
        return the_board[7]
    return


# TODO check columns
def check_columns():
    global still_going

    # checks if the columns is True but also doesn't mislabel the empty rows as a winning situation.
    col_1 = the_board[1] == the_board[4] == the_board[7] != " "
    col_2 = the_board[2] == the_board[5] == the_board[8] != " "
    col_3 = the_board[3] == the_board[6] == the_board[9] != " "

    # stops the game if someone one!
    if col_1 or col_2 or col_3:
        still_going = False

    # checks and returns who won!
    if col_1:
        return the_board[1]
    elif col_2:
        return the_board[2]
    elif col_3:
        return the_board[3]
    return


# TODO check diagonals
def check_diagonals():
    global still_going

    # checks if the diagonal is True but also doesn't mislabel the empty rows as a winning situation.
    diagonal_1 = the_board[1] == the_board[5] == the_board[9] != " "
    diagonal_2 = the_board[3] == the_board[5] == the_board[7] != " "

    # stops the game if someone one!
    if diagonal_1 or diagonal_2:
        still_going = False

    # checks and returns who won!
    if diagonal_1:
        return the_board[1]
    elif diagonal_2:
        return the_board[3]
    return


# TODO check tie
# if not a win and the game is over
def check_tie():
    return


# TODO flip player
# changes/flips from one player to another, checks x or o and flips it
def change_turns():
    return


# to initialize the game
play_game()