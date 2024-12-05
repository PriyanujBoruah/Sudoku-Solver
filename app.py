import streamlit as st
import copy
import time
import random
import pandas as pd
import numpy as np
import re

st.set_page_config(page_title="Sudoku Solver by Priyanuj", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def solve_sudoku(board):
    """Solves a Sudoku puzzle using backtracking."""

    def find_empty(bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)
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
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if is_valid(bo, num, (row, col)):
                bo[row][col] = num

                if backtrack(bo):
                    return True

                bo[row][col] = 0

        return False

    board_copy = copy.deepcopy(board)
    if backtrack(board_copy):
        return board_copy
    else:
        return None

def generate_sudoku():
    """Generates a solvable Sudoku puzzle (placeholder)."""
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
    random.shuffle(board)
    return board

def generate_sudoku_set(num_puzzles):
    """Generates a set of Sudoku puzzles."""
    return [generate_sudoku() for _ in range(num_puzzles)]

def clean_sudoku_input(user_input):
    """Removes all non-digit characters from the Sudoku input string."""
    return re.sub(r"[^0-9]", "", user_input)



st.html(f"<h1 style='text-align: center; color: #2f3133'><span style='color: #076EFF'>Sudoku</span> Solver <span style='font-size: medium;'>by <span style='color: #076EFF'>Priyanuj Boruah</span></span></h1>")

CON1 = st.container(border=True)

CON1.html(f"<h2 style='text-align: center; color: #2f3133'>Solve Your Own Sudoku</h2>")
user_input = CON1.text_area("Enter your Sudoku puzzle (9 rows of 9 digits, use 0 for empty cells):", height=200, placeholder="""530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079""")

if CON1.button("Get Solution", type="primary"):
    try:
        # Clean the input to remove non-digit characters
        cleaned_input = clean_sudoku_input(user_input)

        # Convert cleaned input to a 2D list of integers
        if len(cleaned_input) != 81:
            CON1.error("Please enter 81 digits (9 rows of 9).")
        else:
            user_board = []
            for i in range(9):
                row = []
                for j in range(9):
                    digit = int(cleaned_input[i * 9 + j])
                    row.append(digit)
                user_board.append(row)
            
            start_time = time.time()
            user_solution = solve_sudoku(user_board)
            end_time = time.time()
            time_taken = end_time - start_time

            if user_solution:
                df_user_solution = pd.DataFrame(user_solution)
                CON1.subheader("Solution:")
                CON1.text(f"Time taken: {time_taken:.6f} seconds")
                CON1.dataframe(df_user_solution, hide_index=None)
            else:
                CON1.error("No solution found for the provided Sudoku.")

    except (ValueError, IndexError):  # Handle potential errors during conversion
        CON1.error("Invalid input format. Please enter digits 0-9 only.") # More general error message.
      


# Generated Puzzles Section (same as before)


CON2 = st.container(border=True)
CON2.html(f"<h2 style='text-align: center; color: #2f3133'>Generate and Solve Multiple Sudokus</h2>")

num_puzzles = CON2.number_input("Number of puzzles:", min_value=100, max_value=100000, value=1000, step=100)

expander = st.expander("Sudokus")
COL1, COL2 = expander.columns(2, gap="medium")

if CON2.button("Generate and Solve", type="primary"):
    sudoku_puzzles = generate_sudoku_set(num_puzzles)
    times, valid_count = [], 0
    progress_bar = CON2.progress(0)

    for i, board in enumerate(sudoku_puzzles):
        start_time = time.time()
        solution = solve_sudoku(board)
        end_time = time.time()
        time_taken = end_time - start_time

        if solution:
            times.append(time_taken)
            valid_count += 1
            df_puzzle = pd.DataFrame(board)
            df_solution = pd.DataFrame(solution)
            COL1.caption(f"Valid Puzzle {valid_count}")
            COL1.dataframe(df_puzzle, hide_index=None)
            COL2.caption("Solution")
            COL2.dataframe(df_solution, hide_index=None)

        progress_bar.progress((i + 1) / num_puzzles)

    CON2.html(f"<p style='font-size: large'><span style='color: #076EFF'><b>{valid_count}</b></span> valid sudoku generated</p>")
    if times:
        CON2.html(f"""<p>Total Time: <span style='color: #076EFF'><b>{sum(times):.6f}</b></span> seconds
                  <br>
                  Average time: <span style='color: #076EFF'><b>{sum(times) / len(times):.6f}</b></span> seconds
                  </p>""")
    else:
        CON2.write("No valid Sudoku puzzles generated.")
