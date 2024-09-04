c = 0

def N_Queens(board, row):
    if row == len(board):
        printBoard(board)
        return

    for col in range(len(board)):
        if(isSafe(board, row, col)):
            board[row][col] = 'Q'
            N_Queens(board, row+1)
            board[row][col] = '.'

def Count_N_Queens(board, row):
    if row == len(board):
        return c

    for col in range(len(board)):
        if(isSafe(board, row, col)):
            board[row][col] = 'Q'
            Count_N_Queens(board, row+1)
            board[row][col] = '.'


def isSafe(board, row, col):
    # Vertically Up
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Diagonally Left Up
    i = row-1
    j = col-1 
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Diagonally Right Up
    i = row-1
    j = col+1 
    while i >= 0 and j < len(board) :
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def printBoard(board):
    print("------Board------")
    for row in board:
        print(" ".join(row))
    print()

l = int(input("Enter No of Queens : "))
board = [['.' for _ in range(l)] for _ in range(l)]
N_Queens(board, 0)
# Count_N_Queens(board, 0)