def N_Queens(board, row):
    if row >= len(board):
        printBoard(board)
        return 

    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 'Q'
            N_Queens(board, row + 1)
            board[row][col] = '.'

def isSafe(board, row, col):
    # Check this column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def printBoard(board):
    print("------Board------")
    for row in board:
        print(" ".join(row))
    print()

l = int(input("Enter number of Queens: "))
board = [['.' for _ in range(l)] for _ in range(l)]
N_Queens(board, 0)
