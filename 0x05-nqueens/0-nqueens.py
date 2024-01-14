#!/usr/bin/python3
'''N Queens Challenge'''

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if board_size < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    queens_positions = []  # coordinates format [row, column]
    stop = False
    current_row = 0
    current_col = 0

    # iterate through rows
    while current_row < board_size:
        go_back = False
        # iterate through columns
        while current_col < board_size:
            # check if the current column is safe
            safe = True
            for queen_cords in queens_positions:
                col = queen_cords[1]
                if (col == current_col or
                        col + (current_row - queen_cords[0]) == current_col or
                        col - (current_row - queen_cords[0]) == current_col):
                    safe = False
                    break

            if not safe:
                if current_col == board_size - 1:
                    go_back = True
                    break
                current_col += 1
                continue

            # place queen
            coordinates = [current_row, current_col]
            queens_positions.append(coordinates)
            # if the last row, append solution and reset to the last unfinished row
            # and the last safe column in that row
            if current_row == board_size - 1:
                solutions.append(queens_positions[:])
                for queen_cords in queens_positions:
                    if queen_cords[1] < board_size - 1:
                        current_row = queen_cords[0]
                        current_col = queen_cords[1]
                for _ in range(board_size - current_row):
                    queens_positions.pop()
                if current_row == (
                        board_size - 1 and current_col == board_size - 1):
                    queens_positions = []
                    stop = True
                current_row -= 1
                current_col += 1
            else:
                current_col = 0
            break
        if stop:
            break
        # on fail: go back to the previous row
        # and continue from the last safe column + 1
        if go_back:
            current_row -= 1
            while current_row >= 0:
                current_col = queens_positions[current_row][1] + 1
                del queens_positions[current_row]
                if current_col < board_size:
                    break
                current_row -= 1
            if current_row < 0:
                break
            continue
        current_row += 1

    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
