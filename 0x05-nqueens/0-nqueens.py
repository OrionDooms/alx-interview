#!/usr/bin/python3
"""N queens"""
import sys


def solve_nqueens(N):
    """By solve the N Queens challenge I will using boolean arrays,
    this approach makes backtracking faster queen placement."""
    def backtracking(row):
        if row != N:
            for c in range(N):
                """The cols[c] is a boolean, that indicates the column is
                occupied by a queen. diag1[row - c + N - 1] tracks the queens
                on diagonals and diag2[row + c ] tracks the queens on
                anti-diagonals"""
                if not (cols[c] or diag1[row - c + N - 1] or diag2[row + c]):
                    board[row] = c
                    cols[c] = True
                    diag1[row - c + N - 1] = True
                    diag2[row + c] = True

                    backtracking(row + 1)
                    board[row] = -1
                    cols[c] = False
                    diag1[row - c + N - 1] = False
                    diag2[row + c] = False
        else:
            result.append([board.copy()])
            return
    result = []
    board = [-1] * N
    cols = [False] * N
    diag1 = [False] * (2 * N - 1)
    diag2 = [False] * (2 * N - 1)

    backtracking(0)
    return result


def print_result(x):
    for s in x:
        result = [[i, s[0][i]] for i in range(len(s[0]))]
        print(result)


if __name__ == "__main__":
    """Error handing. If N is less than 4 it print "N must be at least 4",
    if the argument isn't a number it prints "N must be at least 4", if the
    wrong number of arguments is provided it prints "Usage: nqueens N"."""
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

    x = solve_nqueens(N)
    print_result(x)
