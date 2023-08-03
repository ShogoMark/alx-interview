#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given cell
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(col):
        if col >= N:
            solution = [[row, board[row].index(1)] for row in range(N)]
            solutions.append(solution)
            return

        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0

    backtrack(0)

    for solution in sorted(solutions, key=lambda x: x[0][1]):
        for queen_pos in solution:
            print(queen_pos, end=" ")
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
