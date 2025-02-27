import random


board = [[" ", " ", " ",],
         [" ", " ", " ",],
         [" ", " ", " ",]]

def place_symbol(symbol, i, j):
    board[i][j] = symbol

def print_board():
    for row in board:
        print(row)

def change_symbol(symbol):
    return "X" if symbol == "O" else "O"




def check_for_win(board):

    #top to bottom checks:
    for row in range(3):
        if board[row][0] == "X" and board[row][1] == "X" and board[row][2] == "X":
            winning_player = "Player X"
            print(f"Game Over! {winning_player} wins!")
            return True

        elif board[row][0] == "O" and board[row][1] == "O" and board[row][2] == "O":
            winning_player = "Player O"
            print(f"Game Over! {winning_player} wins!")
            return True


    #left to right checks:
    for column in range(3):
        if board[0][column] == "X" and board[1][column] == "X" and board[2][column] == "X":
            winning_player = "Player X"
            print(f"Game Over! {winning_player} wins!")
            return True

        elif board[0][column] == "O" and board[1][column] == "O" and board[2][column] == "O":
            winning_player = "Player O"
            print(f"Game Over! {winning_player} wins!")
            return True


    #diagonal right-up
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        winning_player = "Player X"
        print(f"Game Over! {winning_player} wins!")
        return True

    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        winning_player = "Player O"
        print(f"Game Over! {winning_player} wins!")
        return True


    #diagonal left-down
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        winning_player = "Player X"
        print(f"Game Over! {winning_player} wins!")
        return True

    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        winning_player = "Player O"
        print(f"Game Over! {winning_player} wins!")
        return True

    #check for tie
    if all(cell != " " for row in board for cell in row):
        print("Tie!")
        return True

player = random.randint(1,2)


if player == 1:
    symbol = "X"
else:
    symbol = "O"


game_is_over = False

while not game_is_over:

    choice = input("Choose what square to play (0,1,2 on Y axis   0,1,2 on x axis): ")
    i, j = choice[:len(choice) // 2], choice[len(choice) // 2]  # splits the choice into coordinates for later use
    i, j = int(i), int(j)

    while 0 < i > 2 or 0 < j > 2:
        print("Not within range. Try again")
        choice = input("Choose what square to play (0,1,2 on Y axis   0,1,2 on x axis): ")
        i, j = choice[:len(choice) // 2], choice[len(choice) // 2]
        i, j = int(i), int(j)


    # need to still check if there is an empty place before placing it
    if board[i][j] != " ":
        print("Place already taken, try again")
    else:
        place_symbol(symbol, i, j)
        print_board()
        symbol = change_symbol(symbol)

    if check_for_win(board):
        game_is_over = True

