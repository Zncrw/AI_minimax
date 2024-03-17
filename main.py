import numpy as np


def check_winner(board):
    """
    checking if the game has already winner
    :param board: current state of game board
    :return: 1 if X won, -1 if O won, 0 if no winner
    """
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        # checking rows
        if board[i].sum() == 3 or board[:, i].sum() == 3:
            return 1
        elif board[i].sum() == -3 or board[:, i].sum() == -3:
            return -1
    # numpy. trace() function is used to return the sum of the diagonals of the matrix
    if np.trace(board) == 3 or np.trace(np.fliplr(board)) == 3:
        return 1
    elif np.trace(board) == -3 or np.trace(np.fliplr(board)) == -3:
        return -1
    return 0


def board_full(board):
    """
    checking, if is not game board full
    :param board: current state of game board
    :return: boolean
    """
    if 0 in board:
        return False
    return True


def minimax(board, is_maximizer):
    """
    minimax algorithm
    :param board: current state of game board
    :param is_maximizer: if is maximizer on move
    :return: best_score
    """
    # checking for winner
    winner = check_winner(board)
    if winner != 0:
        return winner
    # checking if is still empty place in game board
    if board_full(board):
        return 0
    # maximizer on turn
    if is_maximizer:
        best_score = -10000
        for i in range(3):
            for j in range(3):
                # if still place in game board
                if board[i][j] == 0:
                    # try to put X here
                    board[i][j] = 1
                    # recursive call
                    score = minimax(board, False)
                    # undo changes
                    board[i][j] = 0
                    # find best score
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 10000
        for i in range(3):
            for j in range(3):
                # if still place in game board
                if board[i][j] == 0:
                    # try to put O here
                    board[i][j] = -1
                    # recursive call
                    score = minimax(board, True)
                    # undo changes
                    board[i][j] = 0
                    # find the lowest score
                    best_score = min(score, best_score)
        return best_score


def minimax_move(board):
    """
    make minimax player move
    :param board: current state of game board
    :return: best_move for current state of board
    """
    best_score = -10000
    best_move = None
    for i in range(3):
        for j in range(3):
            # if is game board still empty
            if board[i][j] == 0:
                # make a move
                board[i][j] = 1
                score = minimax(board, False)
                # undo changes
                board[i][j] = 0
                # finding best score, then best move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move


def print_board(board):
    """
    printing grid for tic-tac-toe
    :param board: current state of board
    """
    symbols = {0: ' ', 1: 'O', -1: 'X'}
    for row in board:
        print("|".join(symbols[val] for val in row))
        print("-----")


def create_board():
    """
    making gaming board as numpy array
    """
    # np.zeros return a new array of given shape (3x3) and type(int), filled with zeros.
    return np.zeros((3, 3), int)


def player_move(board):
    """
    make player to move and check for valid options
    :param board: current state of game

    """
    while True:
        try:
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))
            if board[row][col] == 0:
                return row, col
            else:
                print("This position is already taken. Please choose another.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    # create game board
    board = create_board()
    print("Welcome to Tic Tac Toe!")
    # print game board
    print_board(board)

    # loop on while is board empty
    while not board_full(board):
        # Player move
        player_row, player_col = player_move(board)
        board[player_row][player_col] = -1
        print_board(board)
        if check_winner(board) == -1:
            print("You win!")
            return
        if board_full(board):
            print("It's a draw!")
            return
        # AI move
        print("AI move:")
        ai_row, ai_col = minimax_move(board)
        board[ai_row][ai_col] = 1
        print_board(board)
        if check_winner(board) == 1:
            print("AI wins!")
            return
        if board_full(board):
            print("It's a draw!")
            return


if __name__ == "__main__":
    main()
