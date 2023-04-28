#!/usr/bin/python3
"""
Solve the nqueen problem
"""
import sys


def is_valid(board, row, col, N):
    """
    Check if it is safe to place a queen at position (row, col) on the board.

    Args:
    - board: A list of integers representing the current state of the board.
    - row: An integer representing the row to place the queen.
    - col: An integer representing the column to place the queen.
    - N: An integer representing the size of the board.

    Returns:
    - True if it is safe to place the queen at (row, col), False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens(board, row, N):
    """
    Recursively solve the N-queens problem.

    Args:
    - board: A list of integers representing the current state of the board.
    - row: An integer representing the current row to place the queen.
    - N: An integer representing the size of the board.

    Returns:
    - None. The function prints each solution to the N-queens problem.
    """
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return
    for col in range(N):
        if is_valid(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N)


if __name__ == "__main__":
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
    board = [-1] * N
    solve_n_queens(board, 0, N)
