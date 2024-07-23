import os
import time

def n_queen(n):
    # Initialize the matrix with zeros
    matrix = [['-' for _ in range(n)] for _ in range(n)]
    if solveNQueen(matrix, 0):
        printNQueen(n, matrix)
    else:
        print('No solution')

def solveNQueen(matrix, row):
    os.system('cls' if os.name == 'nt' else 'clear')


    printNQueen(len(matrix), matrix)
    print()
    # time.sleep(0.005)  # Add FOR DELAY TO VIEW FULL PROCESS (! TRY AT YOUR OWN RISK)
    if row >= len(matrix):
        return True
    for col in range(len(matrix[0])):
        if isValidPlace(matrix, row, col):
            matrix[row][col] = 'Q'
            if solveNQueen(matrix, row + 1):
                return True
            matrix[row][col] = '-'
    return False

def isValidPlace(matrix, row, col):
    # Row Check
    for i in range(len(matrix)):
        if matrix[row][i] == 'Q':
            return False
    # Column Check
    for i in range(len(matrix[0])):
        if matrix[i][col] == 'Q':
            return False
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'Q':
                if abs(row - i) == abs(col - j):
                    return False
    return True

def printNQueen(n, matrix):
    for row in range(n):
        for col in range(n):
            print(matrix[row][col], end=" ")
        print()

def main():
    n = 8
    n_queen(n)

if __name__ == '__main__':
    main()
