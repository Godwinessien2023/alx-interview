#!/usr/bin/python3
"""ALX SE nqueens"""
import sys



def print_solutions(board, N):
    """Print the board configuration for a solution"""
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                solution.append([row, col])
    print(solution)

def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col] without conflicts"""
    for i in range(row):
        # Check column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N):
    """Recursive backtracking function to find all solutions"""
    if row == N:
        print_solutions(board, N)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            solve_nqueens(board, row + 1, N)
            board[row] = -1  # Backtrack

def main():
    """Main function to handle input and validate arguments"""
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

    board = [-1] * N  # -1 indicates no queen is placed in the row
    solve_nqueens(board, 0, N)

if __name__ == "__main__":
    main()
