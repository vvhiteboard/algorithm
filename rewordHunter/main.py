import sys

read = lambda: sys.stdin.readline().rstrip()


contest_1 = (5000000, 3000000, 2000000, 500000, 300000, 100000)
contest_2 = (5120000, 2560000, 1280000, 640000, 320000)


def user_input():
    n = int(read())

    results = []

    for _ in range(n):
        a, b = read().split(" ")
        results.append((int(a), int(b)))

    return n, results


def get_reword(a, b):
    reword = 0

    if a != 0:
        for index in range(6):
            a -= (index + 1)
            if a <= 0:
                # print(contest_1[index])
                reword += contest_1[index]
                break
    if b != 0:
        for index in range(5):
            b -= 2**index
            if b <= 0:
                # print(contest_2[index])
                reword += contest_2[index]
                break

    return reword



if __name__ == "__main__":
    n, results = user_input()

    index = 0

    for result in results:
        print(get_reword(*result))