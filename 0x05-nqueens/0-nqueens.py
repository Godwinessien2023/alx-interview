#!/usr/bin/python3
"""
ALX SE nqueens
"""
import sys


def print_solutions(board, N):
    """Prints the board configuration for a solution in the required format."""
    solution = [[row, board[row]] for row in range(N)]
    print(solution)


def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe from attacks.
    A queen can be attacked if there's another queen in the same column
    or on either diagonal.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """
    Recursively attempts to place queens
    on each row to find all solutions.
    """
    if row == N:
        print_solutions(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # Place queen at (row, col)
            solve_nqueens(board, row + 1, N)
            board[row] = -1  # Reset (backtrack)


def validate_and_parse_args():
    """
    Validates and parses command-line arguments.
    Ensures there's exactly one argument and that it's a valid integer ≥ 4.
    Returns the integer value of N if valid.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def main():
    """Main function to initialize the board and start solving."""
    N = validate_and_parse_args()
    board = [-1] * N
    solve_nqueens(board, 0, N)
