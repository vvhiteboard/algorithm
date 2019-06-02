from decimal import Decimal


def user_input():
    a = input().rstrip().split(" ")
    n, k = int(a[0]), int(a[1])
    arr = [int(n) for n in input().rstrip().split(" ")]
    return n, k, arr


n, k, arr = user_input()


sum_arr = [0 for _ in range(n)]
square_sum_arr = [0 for _ in range(n)]


def calc_range_sum(s_arr, start, end):
    if start == 0:
        return s_arr[end]

    return s_arr[end] - s_arr[start-1]


def calc_sum():
    sum_arr[0] = arr[0]
    square_sum_arr[0] = arr[0] ** 2

    for i in range(1, n):
        sum_arr[i] = sum_arr[i-1] + arr[i]
        square_sum_arr[i] = square_sum_arr[i-1] + arr[i] ** 2


def calc(start, end):
    sum_val = calc_range_sum(sum_arr, start, end)
    square_sum_val = calc_range_sum(square_sum_arr, start, end)

    k = end - start + 1

    sum_mean = Decimal(sum_val) / k
    square_sum_mean = Decimal(square_sum_val) / k

    # V(X) = E(X^2) - E(X)^2
    return square_sum_mean - sum_mean ** 2


if __name__ == "__main__":
    min_val = Decimal("INF")

    calc_sum()

    for end in range(k-1, n):
        for start in range(end - k + 2):
            val = calc(start, end)

            if min_val == -1:
                min_val = val
            else:
                min_val = min(min_val, val)

    print(min_val.sqrt())