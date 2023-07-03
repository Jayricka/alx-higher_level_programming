#!/usr/bin/python3
""" N Queens """

import sys


class NQueens:
    """ NQueens class to solve the N Queens problem """

    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def solve(self, row=0):
        """ Solve the N Queens problem using backtracking. """
        if row == self.n:
            self.add_solution()
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0

    def is_safe(self, row, col):
        """ Check if it's safe to place a queen at position (row, col). """
        for i in range(row):
            if (
                self.board[i][col] == 1
                or (col - (row - i) >= 0 and
                    self.board[i][col - (row - i)] == 1)
                or (col + (row - i) < self.n and
                    self.board[i][col + (row - i)] == 1)
            ):
                return False
        return True

    def add_solution(self):
        """ Add the current valid solution to the list of solutions. """
        solution = []
        for row in range(self.n):
            for col in range(self.n):
                if self.board[row][col] == 1:
                    solution.append([row, col])
        self.solutions.append(solution)

    def print_solutions(self):
        """ Prints all the valid solutions to the N Queens problem. """
        if not self.solutions:
            print("No solutions found.")
        else:
            for solution in self.solutions:
                print(solution)


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

    n_queens = NQueens(N)
    n_queens.solve()
    n_queens.print_solutions()
