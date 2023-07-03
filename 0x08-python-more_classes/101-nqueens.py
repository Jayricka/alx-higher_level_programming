#!/usr/bin/python3

import sys


class NQueens:
    """Solves the N Queens problem for a given size of the chessboard."""

    def __init__(self, size):
        """
        Initializes the NQueens object with the given size of the chessboard.

        Args:
            size (int): The size of the chessboard and the number of queens to place.
        """
        self.size = size
        self.board = [[0] * size for _ in range(size)]

    def is_safe(self, row, col):
        """
        Checks if it is safe to place a queen at the given position.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it is safe to place a queen, False otherwise.
        """
        for i in range(row):
            if self.board[i][col] == 1 or \
               self.board[i][row] == 1 or \
               (col - (row - i) >= 0 and self.board[i][col - (row - i)] == 1) or \
               (col + (row - i) < self.size and self.board[i][col + (row - i)] == 1):
                return False
        return True

    def solve(self, row=0):
        """
        Solves the N Queens problem using backtracking.

        Args:
            row (int): The current row being processed (default: 0).
        """
        if row == self.size:
            self.print_solution()
            return
        for col in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0

    def print_solution(self):
        """
        Prints the current valid solution to the N Queens problem.
        """
        solution = [[i, self.board[i].index(1)] for i in range(self.size)]
        print(solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    # Get the value of N from the command-line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an instance of NQueens and solve the problem
    n_queens = NQueens(N)
    n_queens.solve()
