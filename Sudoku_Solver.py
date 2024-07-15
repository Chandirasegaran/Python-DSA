def is_valid_move(grid, row, column, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    for i in range(9):
        if grid[i][column] == number:
            return False

    corner_row = row - row % 3
    corner_column = column - column % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_column + y] == number:
                return False

    return True

def find_empty_location(grid):
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                return row, column
    return None, None

def solve(grid):
    row, column = find_empty_location(grid)
    if row is None:  # No empty space left
        return True

    for number in range(1, 10):
        if is_valid_move(grid, row, column, number):
            grid[row][column] = number

            if solve(grid):
                return True

            grid[row][column] = 0  # Reset the cell and backtrack

    return False

def main():
    grid = [[0, 0, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    if solve(grid):
        print("Congratulations!")
        print("- " * 11)
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
                if j == 2 or j == 5:
                    print("|", end=" ")
            if i == 2 or i == 5:
                print()
                print("- " * 11)
            else:
                print()
        print("- " * 11)
    else:
        print("No Solution")

if __name__ == '__main__':
    main()


# def is_valid_move(grid, row, column, number):
#     for i in range(9):
#         if grid[row][i] == number:
#             return False
#     for i in range(9):
#         if grid[i][column] == number:
#             return False
#
#     corner_row = row - row % 3
#     corner_column = column - column % 3
#
#     for x in range(3):
#         for y in range(3):
#             if grid[corner_row + x][corner_column + y] == number:
#                 return False
#
#     return True
#
#
# def solve(grid, row, column):
#     if column == 9:
#         if row == 8:
#             return True
#         row += 1
#         column = 0
#     if grid[row][column] > 0:
#         return solve(grid, row, column + 1)
#
#     for number in range(1, 10):
#         if is_valid_move(grid, row, column, number):
#             grid[row][column] = number
#
#             if solve(grid, row, column + 1):
#                 return True
#
#         grid[row][column] = 0
#
#     return False
#
#
# def main():
#     grid = [[0, 0, 0, 0, 3, 0, 9, 0, 1],
#             [0, 1, 0, 0, 0, 4, 0, 0, 0],
#             [4, 0, 7, 0, 0, 0, 2, 0, 8],
#             [0, 0, 5, 2, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 9, 8, 1, 0, 0],
#             [0, 4, 0, 0, 0, 3, 0, 0, 0],
#             [0, 0, 0, 3, 6, 0, 0, 7, 2],
#             [0, 7, 0, 0, 0, 0, 0, 0, 3],
#             [9, 0, 3, 0, 0, 0, 6, 0, 4]]
#
#     if solve(grid, 0, 0):
#         print("Congratulations!")
#         print("- " * 11)
#         for i in range(9):
#             for j in range(9):
#                 print(grid[i][j], end=" ")
#                 if j==2 or j==5 :
#                     print("|", end=" ")
#             if i==2 or i==5:
#                 print()
#                 print("- "*11)
#             else:
#                 print()
#         print("- " * 11)
#     else:
#         print("No Solution")
#
#
# if __name__ == '__main__':
#     main()
