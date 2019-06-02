import sys

read = lambda: sys.stdin.readline().rstrip()

ladder = [[0 for _ in range(10)] for _ in range(30)]
candidates = []
c_count = 0


def is_correct_ladder():
    global ladder

    n = len(ladder[0])

    arr = [_ for _ in range(n)]

    for cross in ladder:
        for index in range(len(cross)):
            if cross[index] is 1:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp

    # print("arr: {}".format(arr))
    for index in range(len(arr)):
        if arr[index] is not index:
            return False

    return True


def search_path(start, depth):
    global ladder
    global candidates
    global c_count

    min_count = -1
    if is_correct_ladder():
        return 0
    elif c_count == 0:
        return -1

    for index in range(start, c_count):
        cross, line = candidates[index]
        # print("depth : {}, cross : {}, line : {}".format(depth, cross, line))

        if ladder[cross][line] is not 0 or ladder[cross][line + 1] is not 0:
            continue

        ladder[cross][line] = 1
        ladder[cross][line + 1] = 2

        if is_correct_ladder():
            ladder[cross][line] = 0
            ladder[cross][line + 1] = 0
            return 1

        if depth is 3:
            ladder[cross][line] = 0
            ladder[cross][line + 1] = 0
            continue

        count = search_path(index + 1, depth + 1)

        if count > 3 or count is -1:
            ladder[cross][line] = 0
            ladder[cross][line + 1] = 0
            continue

        if min_count == -1:
            min_count = count + 1
        else:
            min_count = min(min_count, count + 1)

        ladder[cross][line] = 0
        ladder[cross][line + 1] = 0

    return min_count


def extract_condidate(n, h):
    global candidates
    global c_count

    for line in range(n - 1):
        for cross in range(h):
            if ladder[cross][line] is 0 and ladder[cross][line + 1] is 0:
                candidates.append((cross, line))
                c_count += 1


def user_input():
    arr = read().split(" ")
    n = int(arr[0])
    m = int(arr[1])
    h = int(arr[2])
    return n, m, h


if __name__ == "__main__":
    n, m, h = user_input()

    for _ in range(m):
        ar = read().split(" ")
        a = int(ar[0])
        b = int(ar[1])

        ladder[a - 1][b - 1] = 1
        ladder[a - 1][b] = 2

    extract_condidate(n, h)

    result = search_path(0, 1)

    print(result)
