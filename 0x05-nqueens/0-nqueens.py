#!/usr/bin/python3
"""ALX SE nqueens"""
import sys


def n_queen(n):
    """Return all possible arrange for the n-queen problem."""
    col = set()
    pos = set()
    neg = set()
    res = []
    state = []

    def backtrack(r):
        """Backtrack using recursion"""
        if r == n:
            res.append([val for val in state])
        for c in range(n):
            if c in col or (r + c) in pos or (r - c) in neg:
                continue
            col.add(c)
            pos.add(r + c)
            neg.add(r - c)
            state.append([r, c])

            backtrack(r + 1)

            col.remove(c)
            pos.remove(r + c)
            neg.remove(r - c)
            state.pop()
    backtrack(0)
    return res


def main():
    """Main Entry"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for res in n_queen(n):
        print(res)


main()