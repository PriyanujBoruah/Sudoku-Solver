# Sudoku Solver

This Python code provides a backtracking algorithm to solve Sudoku puzzles.  It can be used as a standalone solver in the terminal or integrated into a larger Sudoku application.

## Features

* **Backtracking Algorithm:**  Implements a recursive backtracking approach to efficiently find solutions.
* **Validity Checks:**  Includes functions to check row, column, and 3x3 box constraints.
* **Timer:** Measures and displays the time taken to solve the puzzle.
* **Clear Output:** Prints the solved Sudoku grid to the console.
* **Error Handling:**  Indicates if a puzzle is unsolvable.
* **Copy Protection:** Uses `copy.deepcopy()` to avoid modifying the original input board.

## Usage

**1. Standalone Solver (Terminal):**

```bash
python sudoku_solver.py 
```
This will execute the solver with a sample Sudoku puzzle hardcoded in the script and print the solution (if found) along with the time taken to solve.

**2.  Integrating into a Sudoku Application:**

The `solve_sudoku(board)` function can be imported and used within other Python projects.  Pass a 2D list representing the Sudoku board (0 for empty cells) to the function. It returns a solved board or `None` if no solution exists.

```python
import sudoku_solver  # Assuming you've saved the code as sudoku_solver.py

board = [
    # ... Your Sudoku board ...
]

solution = sudoku_solver.solve_sudoku(board)

if solution:
    # ... Use the solved board in your application ...
else:
    # ... Handle the case where no solution is found ... 
```


## Example Input

The Sudoku board is represented as a 2D list of integers:

```
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
```

`0` represents empty cells.

## Example Output (Terminal)

The output will be the solved Sudoku grid followed by the execution time:

```
[7, 8, 5, 4, 3, 9, 1, 2, 6]
[6, 1, 2, 8, 7, 5, 3, 4, 9]
[4, 9, 3, 6, 2, 1, 5, 7, 8]
[8, 5, 7, 9, 4, 3, 2, 6, 1]
[2, 6, 1, 7, 5, 8, 9, 3, 4]
[9, 3, 4, 1, 6, 2, 7, 8, 5]
[5, 7, 8, 3, 9, 4, 6, 1, 2]
[1, 2, 6, 5, 8, 7, 4, 9, 3]
[3, 4, 9, 2, 1, 6, 8, 5, 7]
0.0023  # Example 
