# Sudoku Solver and Generator

This Python project provides a Sudoku solver with both a Streamlit web app interface and a command-line interface.  It uses a backtracking algorithm to solve Sudoku puzzles and can generate puzzles for testing (although the current generator needs improvement - see below).

## Features

* **Backtracking Algorithm:**  Efficiently solves Sudoku puzzles using a recursive backtracking approach.
* **Input Options:**
    * **Web App:** Users can input their own puzzles in the Streamlit app or generate and solve multiple puzzles.
    * **Terminal:**  The command-line interface can solve a hardcoded puzzle or generate and test a large dataset.
* **Performance Analysis:** Measures and displays the time taken to solve puzzles, including total and average times.
* **Validity Checks:** Includes functions to verify row, column, and 3x3 box constraints.
* **Timer:** Measures and displays the solution time for each puzzle and calculates the average time across a large dataset.
* **Puzzle Generation:** Generates a set of Sudoku puzzles (currently using a placeholder – see below).
* **Bulk Testing:** Solves a large number of puzzles (default is 1,000,000) to evaluate performance.
* **Clear Output:**  Prints the number of valid puzzles, total solution time, and average solution time.
* **Copy Protection:** `copy.deepcopy()` protects the original input boards during solving.
* **Streamlit App:** Provides an interactive web interface for solving and generating puzzles.
* **Error Handling:**  The web app includes input validation and error handling for invalid Sudoku entries.

## Usage

**1. Web App (Streamlit):**

* **Live Demo:** [https://sudoku-solver-by-priyanuj.streamlit.app/](https://sudoku-solver-by-priyanuj.streamlit.app/)  (Try the app directly!)

* **Installation:**
```bash
pip install streamlit pandas numpy st-aggrid copy regex  # Install necessary libraries
```
* **Running the App:**
```bash
streamlit run your_app_name.py   # Replace your_app_name.py with the filename
```

The web app has two main sections:

* **Solve Your Own Sudoku:**  Enter a Sudoku puzzle (9 rows of 9 digits, 0 for empty cells) and click "Get Solution".
* **Generate and Solve Multiple Sudokus:**  Specify the number of puzzles to generate and solve.  The solved puzzles (and the original puzzles) will be displayed within an expandable section.

**2. Terminal:**

* Run the Python script directly:  `python your_script_name.py` (replace `your_script_name.py` with your filename)

**3. Using the Solver Function Directly:**

The `solve_sudoku(board)` function can be imported and used independently:

```python
import sudoku_solver  # Assuming the code is saved as sudoku_solver.py
import time

board = [
   # ... Your Sudoku puzzle (2D list) ...
]

start_time = time.time()
solution = sudoku_solver.solve_sudoku(board)
end_time = time.time()

if solution:
    # ... Use the solved board ...
    print("Time taken:", end_time - start_time, "seconds")
else:
    print("No solution found.")

```

This will generate and solve 1,000,000 Sudoku puzzles (you can change this number in the code) using the `generate_sudoku_set()` and `solve_sudoku()` functions.  The output shows the number of valid puzzles, the total time, and the average solving time.

## Important Note: Puzzle Generation

The included `generate_sudoku()` function creates a single base puzzle and shuffles its rows. This is a placeholder and does *not* produce a wide variety of Sudoku puzzles. For meaningful performance testing and to challenge the solver effectively, it's **crucial** to implement a more robust Sudoku generation algorithm that creates diverse and distinct puzzles, preferably with varying difficulty levels.

## Performance Analysis

The code generates and solves a large number of Sudoku puzzles (default 1,000,000 directly in terminal; 10,000 in streamlit). The average solving time provides a good measure of the algorithm's efficiency.  The results will be affected by:

* **Puzzle Difficulty Distribution:**  A robust generator should produce puzzles of varying difficulty.
* **Hardware:** Your computer's processing power (CPU, RAM) directly affects the solution time.
* **Algorithm Optimizations:** Any changes to the backtracking algorithm will impact performance.

## Example Input (Web App)

```
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
```
(9 rows of 9 digits, 0 for empty cells)


## Example Output

After running `python sudoku_solver.py`, the output will be similar to the following (the exact numbers will vary depending on the generated puzzles and your hardware):

```
Valid sudoku puzzles: 128391
Total time taken: 115.3798599243164 seconds
Average time taken: 0.0008986670295530525 seconds
```

This indicates that out of the 1,000,000 generated puzzles (or however many you generated), 128,391 were valid and solvable.  The total time taken to solve those valid puzzles was approximately 115.38 seconds, and the average solution time per valid puzzle was about 0.0009 seconds.


## Performance

The Sudoku Solver's performance was rigorously tested to ensure efficiency.  The primary optimization algorithm used in the sudoku solver is `Backtracking`. The following results were obtained on a laptop with the specifications:

* Processor: 11th Gen Intel Core i7-11370H @ 3.30GHz
* RAM: 16GB:

**Test 1:**

* Number of Puzzles: 6482
* Total Time: 5.62 seconds
* Average Time per Puzzle: 0.00087 seconds

**Test 2:**

* Number of Puzzles: 1247
* Total Time: 1.08 seconds
* Average Time per Puzzle: 0.00086 seconds

These results demonstrate that the solver can efficiently handle a large number of puzzles, achieving sub-millisecond performance per puzzle on average.
