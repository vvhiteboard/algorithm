import sys


def input_nonogram():
    size_input = input()
    x, y = [int(s.strip()) for s in size_input.split(",")]

    x_input = input()
    x_input = [[int(i.strip()) for i in xi.strip().split(",")] for xi in x_input.split(" ")]

    y_input = input()
    y_input = [[int(i.strip()) for i in yi.strip().split(",")] for yi in y_input.split(" ")]

    return x, y, x_input, y_input


def make_line_candidate(size, inputs):
    candidate = []

    for i in inputs:
        cand = make_candidate(size, i)
        print(len(cand))
        candidate.append(cand)

    return candidate


def make_candidate(size, inputs):
    candidate = []

    if len(inputs) == 1:
        l = inputs[0]
        for s in range(size - l + 1):
            cand = [0 for _ in range(size)]

            cand[s:s+l] = [1 for _ in range(l)]
            candidate.append(cand)

        return candidate

    max_padding = size - (sum(inputs) + len(inputs) - 1)

    if max_padding == 0:
        cand = []

        for i in inputs:
            cand.extend([1 for _ in range(i)])
            cand.append(0)

        cand.pop()

        candidate.append(cand)
        return candidate

    for padding in range(max_padding + 1):
        results = make_candidate((size - padding - inputs[0] - 1), inputs[1:])
        # print(results)

        cand = [0 for _ in range(padding)]
        cand.extend([1 for _ in range(inputs[0])])
        cand.append(0)

        for result in results:
            candidate.append(cand + result)

    return candidate


def fill_board(board, x_candidate, y_candidate):
    while is_not_fill_all(board):

        search_x_candidate(board, x_candidate)
        search_y_candidate(board, y_candidate)
        print_board(board)
        print("\n\n\n\n\n")


def search_x_candidate(board, x_candidate):
    y_size = len(board)

    for index in range(len(x_candidate)):
        if x_candidate[index] is None:
            continue

        x_cand = []

        for cand in x_candidate[index]:
            result = True
            for i in range(y_size):
                if board[i][index] is -1:
                    continue
                elif board[i][index] != cand[i]:
                    result = False
                    break
            if result is True:
                x_cand.append(cand)

        x_candidate[index] = x_cand

        if len(x_cand) == 1: # 완전히 채운 곳
            for i in range(y_size):
                board[i][index] = x_cand[0][i]

            x_candidate[index] = None
            continue

        arr = [0 for _ in range(y_size)]
        for cand in x_cand:
            for i in range(y_size):
                arr[i] += cand[i]

        for i in range(len(arr)):
            a = arr[i]
            if a == 0:
                board[i][index] = 0

            elif a == len(x_cand):
                board[i][index] = 1


def search_y_candidate(board, y_candidate):
    x_size = len(board[0])

    for index in range(len(y_candidate)):
        if y_candidate[index] is None:
            continue

        y_cand = []

        for cand in y_candidate[index]:
            result = True
            for i in range(x_size):
                if board[index][i] is -1:
                    continue
                elif board[index][i] != cand[i]:
                    result = False
                    break
            if result is True:
                y_cand.append(cand)

        y_candidate[index] = y_cand

        if len(y_cand) == 1:  # 완전히 채운 곳
            for i in range(x_size):
                board[index][i] = y_cand[0][i]

            y_candidate[index] = None
            continue

        arr = [0 for _ in range(x_size)]
        for cand in y_cand:
            for i in range(x_size):
                arr[i] += cand[i]

        for i in range(len(arr)):
            a = arr[i]
            if a == 0:
                board[index][i] = 0

            elif a == len(y_cand):
                board[index][i] = 1

def is_not_fill_all(board):
    for row in board:
        for cell in row:
            if cell is -1:
                return True

    return False


def print_board(board):
    for row in board:
        r = ""
        for cell in row:
            if cell == 0:
                r += "☐"
            elif cell == 1:
                r += "◼"
            else:
                r += "."

        print(r)


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    x_size, y_size, x_input, y_input = input_nonogram()

    x_candidate = make_line_candidate(y_size, x_input)
    y_candidate = make_line_candidate(x_size, y_input)

    board = [[-1 for _ in range(x_size)] for _ in range(y_size)]

    fill_board(board, x_candidate, y_candidate)
    print_board(board)




# 0 7 6,5 4,7 11,7 15,7 1,12,7 5,9,7 1,1,9,6 5,8,6 1,12,6 15,2,3 3,3,3,2 3,2,1,3,4 2,2,4,1,1,2,1,1 2,3,2,1,2,2,1 2,1,1,2,3,3,2 2,3,3,2,4 3,3,2,2,6 4,1,5,7 5,13 5,3,14 2,2,1,14 2,4,12,1 3,14 4,3,1,3,3,2 12,1,1,1,4 5,3,3,1,1 4,3,3 3
# 6,3 1,1,1,1,4 1,1,1,1,6 7,10 3,7,5 3,4,3 3,3,3 8,4,2 8,2,2,5 8,5,4 8,2,4 8,1,3,3 8,2,2,1,1,2 10,1,3,3,2 10,2,3,2 4,2,1,3,6 2,1,9,1 1,14 1,6,1 2,10 2,7,1 1,3,9 1,5,1,2,6,1 14,1,10 12,12 10,2,1,12 10,2,8,1,1 12,7,5 14,9 0

# 40 50
# 5,1,5,3,2 3,1,5,3,2 4,2,3,1,6,3,2 1,6,1,2,2,4,2,2 2,1,2,2,3,2,7,3,1 2,3,2,3,1,11,1 3,1,4,3,2,2,2,4,3 2,3,6,3,2,2,2,4,3 1,1,1,6,1,3,2,1,10 4,1,2,1,5,1,2,2,1,6,3 2,1,2,2,9,2,1,3,5,3 1,2,2,1,6,3,2,1,6,3,1 1,2,1,1,4,1,1,2,1,1,5,3,1 1,2,2,1,4,3,2,2,1,1,3,6 3,5,1,4,2,3,1,2,1,4,5 1,2,3,5,3,2,3,1,12 2,3,12,3,5,1,6,1 2,3,25,9,2 2,3,38 7,1,1,27 2,4,2,3,23 1,2,5,1,3,20 3,4,1,1,1,17 1,5,1,1,3,1,10 1,5,3,1 2,5,1,3,1 2,1,3,1,1,2 8,2,1,1 8,1,3,2 1,4,4,1,3,2 2,2,5,1,2 1,2,1,1,7,8 3,1,2,1,19 1,2,1,2,3,1,3,11 3,3,1,1,2,1,3,6,3 2,3,1,1,2,1,9,4 6,2,3,2,6,6 5,2,7,5,1 4,1,3,13,3 3,8,10,2,1
# 1,3,3,1 7,1,1,1 2,3,4 2,10,6 2,3,3,1,2 6,9,6 3,10,2,5 11,1,7 1,6,2,3,4 2,6,1,2,2 1,1,4,1,4,1,1 2,8,1,3,5 1,2,3,4,4,3 2,3,1,2,3,10,1 8,3,1,2,3,4,1 1,1,4,2,2,3,4 5,9,6,1,3 3,1,4,2,2,5 1,1,5,2,2,1 2,2,6,3,3 6,3,3,1,2,2 1,2,5,4,1,1,6,2 3,8,5,3,2,2 1,8,5,3,6,2 10,7,5,7,2 9,2,5,3,8,2 1,2,3,1,5,2,6,2 1,7,1,2,1,6,3,5,2 1,5,1,1,2,10,5,3 4,3,3,1,6,2,4 3,2,4,2,7,8 9,2,8,6 1,4,2,10,4,1 3,3,1,1,7,2,2 1,2,4,11,3 1,5,1,1,8,2 2,2,1,9 6,3,1,1,6 8,2,1,9 2,6,2,2,7 5,16 1,14,6 1,21 2,10,8 2,6,9 5,1,11 1,19 2,13,2 3,5,3,2 4,3,3
