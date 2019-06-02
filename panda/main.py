import sys

"""
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
"""


def user_input():
    n = int(input())

    lines = []
    for _ in range(n):
        lines.append([int(x) for x in input().split()])

    return n, lines


def get_next(n, bamboo_map, mem, x, y, next_x, next_y):
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
        return -1

    next = 1

    if bamboo_map[y][x] > bamboo_map[next_y][next_x]:
        if mem[next_y][next_x] >= 0:
            next = mem[next_y][next_x] + 1
        else:
            next = dfs(n, bamboo_map, mem, next_x, next_y) + 1

    return next


def dfs(n, bamboo_map, mem, x, y):
    if mem[y][x] >= 0:
        return mem[y][x]

    left = get_next(n, bamboo_map, mem, x, y, x - 1, y)
    right = get_next(n, bamboo_map, mem, x, y, x + 1, y)
    top = get_next(n, bamboo_map, mem, x, y, x, y - 1)
    bottom = get_next(n, bamboo_map, mem, x, y, x, y + 1)

    best = max(left, right, top, bottom, 1)
    mem[y][x] = best
    return best


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    n, bamboo_map = user_input()
    mem = [[-1 for _ in range(n)] for _ in range(n)]
    best = 0

    for y in range(n):
        for x in range(n):
            if mem[y][x] is not -1:
                continue

            best = max(dfs(n, bamboo_map, mem, x, y), best)

    print(best)