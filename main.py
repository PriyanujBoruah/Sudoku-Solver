import copy  # For deep copying the board
import time

def solve_sudoku(board):
    """Solves a Sudoku puzzle using backtracking."""

    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def is_valid(bo, num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def backtrack(bo):
        find = find_empty(bo)
        if not find:
            return True  # Puzzle solved
        else:
            row, col = find

        for num in range(1, 10):  # Try numbers 1-9
            if is_valid(bo, num, (row, col)):
                bo[row][col] = num

                if backtrack(bo):  # Recursive call
                    return True

                bo[row][col] = 0  # Backtrack if no solution found

        return False

    board_copy = copy.deepcopy(board) # Create a copy to avoid modifying original
    if backtrack(board_copy):
        return board_copy
    else:
        return None  # No solution exists



# Example usage (to run in the terminal):
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

start_time = time.time()
solution = solve_sudoku(board)
end_time = time.time()



if solution:
    for row in solution:
        print(row)
    print(end_time - start_time)
else:
    print("No solution found.")