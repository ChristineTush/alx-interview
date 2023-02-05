#!/usr/bin/env python3
""" The N queens puzzle is the challenge of placing N non-attacking queens on
    an N×N chessboard. Write a program that solves the N queens problem.
    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
        print Usage: nqueens N, followed by a new line,
        and exit with the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module """
import sys


def solve(row, column):
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver


def place_queen(q, column, prev_solver):
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return(the_queen)



def n_queens():

    the_queen = init()
    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
