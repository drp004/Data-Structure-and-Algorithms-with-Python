def SudokuSolver(sudoku, row, col):
    # Base Case
    if row == 9 :
        return True

    # next row & col
    nextrow = row
    nextcol = col + 1
    if col+1 == 9:
        nextrow = row + 1
        nextcol = 0 

    #Recursion
    if(sudoku[row][col] != 0):
        return SudokuSolver(sudoku, nextrow, nextcol)

    for i in range(1, 10):
        if isSafe(sudoku, row, col, i):
            sudoku[row][col] = i
            if SudokuSolver(sudoku, nextrow, nextcol):
                return True
            sudoku[row][col] = 0

    return False

def isSafe(sudoku, row, col, dig):

    # check for col
    for i in range(9):
        if sudoku[i][col] == dig:
            return False

    # check in rows
    for j in range(9):
        if sudoku[row][j] == dig:
            return False

    
    # check in grid
    sr = (row//3) * 3
    sc = (col//3) * 3

    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if sudoku[i][j] == dig:
                return False

    return True

def printSudoku(sudoku):
    for row in sudoku:
       print(row)
    print() 

sudoku = [[0, 0, 8, 0, 0, 0, 0, 0, 0], 
          [4, 9, 0, 1, 5, 7, 0, 0, 2], 
          [0, 0, 3, 0, 0, 4, 1, 9, 0], 
          [1, 8, 5, 0, 6, 0, 0, 2, 0], 
          [0, 0, 0, 0, 2, 0, 0, 6, 0], 
          [9, 6, 0, 4, 0, 5, 3, 0, 0], 
          [0, 3, 0, 0, 7, 2, 0, 0, 4], 
          [0, 4, 9, 0, 3, 0, 0, 5, 7], 
          [8, 2, 7, 0, 0, 9, 0, 1, 3]]
if SudokuSolver(sudoku, 0, 0):
    print("Solution Exists")
    printSudoku(sudoku)
else:
    print("Solution not Exists")