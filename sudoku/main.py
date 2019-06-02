import sys
import numpy as np
from pprint import pprint


def convert_board(sudoku):
    sudoku = sudoku.split("\n")
    board = []

    for su in sudoku:
        if len(su.strip()) <= 0:
            continue
        row = []
        for s in su.strip():
            row.append(int(s))

        board.append(row)

    return board


def is_collect_column(board):
    b = np.array(board)

    for index in range(9):
        arr = list(b[:, index])
        fi = 0b111111111

        for a in arr:
            if a <= 0:
                continue

            fi = fi ^ (1 << (a - 1))

        if int(fi) is not 0:
            return False

    return True


def is_collect_row(board):
    for row in board:
        fi = 0b111111111

        for b in row:
            if b <= 0:
                continue

            fi = (fi ^ 1 << (b - 1))

        if fi is not 0:
            return False

    return True


def is_collect_rectangle(board):
    bo = np.array(board)

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            arr = bo[x:x+3, y:y+3]
            fi = 0b111111111
            for a in arr:
                for b in a:
                    if b <= 0:
                        continue
                    fi = (fi ^ 1 << (b - 1))

            if int(fi) is not 0:
                return False
    return True


def is_solved(board):
    return is_collect_column(board) and is_collect_row(board) and is_collect_rectangle(board)


def remove_candidate(candidate_map, x, y, value):
    for index in range(9):
        candidate_map[x][index].discard(value)
        candidate_map[index][y].discard(value)

    for i in range(3):
        for j in range(3):
            temp_x = x//3
            temp_y = y//3

            candidate_map[temp_x*3 + i][temp_y*3 + j].discard(value)


def get_candidate(board, x, y):
    candidate = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for index in range(9):
        candidate.discard(board[x][index])
        candidate.discard(board[index][y])

    for i in range(3):
        for j in range(3):
            temp_x = x//3
            temp_y = y//3

            candidate.discard(board[temp_x*3 + i][temp_y*3 + j])

    return candidate


def get_min_candidate(board):
    min_candidate = None
    min_x = -1
    min_y = -1

    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] is not 0:
                continue

            candidate = get_candidate(board, x, y)

            if min_candidate is None or len(min_candidate) > len(candidate):
                min_candidate = candidate
                min_x = x
                min_y = y

    return min_candidate, min_x, min_y


def fill_board(board):
    candidate, x, y = get_min_candidate(board)

    # 다 채운 경우
    if candidate is None:
        return board

    # 실패한 경우
    if len(candidate) is 0:
        return None

    for c in candidate:
        board[x][y] = c

        answer = fill_board(board)

        # 실패한 경우
        if answer is None:
            board[x][y] = 0
        elif is_solved(answer):
            return answer

    return None

if __name__ == "__main__":
    sys.setrecursionlimit(1000000)

    sudoku = """
    406700000
    000026870
    007000100
    040000080
    000908000
    080000020
    004000200
    035210000
    000004703
    """

    problem = convert_board(sudoku)

    # problem = [
    #     [0, 0, 0, 0, 7, 0, 0, 6, 0]
    #     , [0, 0, 5, 0, 0, 0, 0, 1, 3]
    #     , [0, 3, 0, 0, 1, 0, 0, 8, 0]
    #     , [0, 0, 1, 0, 0, 4, 0, 0, 0]
    #     , [4, 0, 0, 5, 0, 9, 0, 0, 0]
    #     , [0, 0, 7, 0, 0, 0, 0, 0, 0]
    #     , [0, 2, 4, 0, 0, 3, 6, 7, 0]
    #     , [3, 0, 0, 8, 0, 0, 0, 9, 0]
    #     , [0, 0, 0, 4, 0, 0, 0, 0, 8]
    # ]

    pprint(problem)
    print("\n\n")

    answer = fill_board(problem)
    pprint(answer)
