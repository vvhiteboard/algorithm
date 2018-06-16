if __name__ == "__main__":
    prime_map = {1: False}

    for n in range(2, 1001):
        if n in prime_map:
            continue

        prime_map[n] = True

        if n > 500:
            continue

        num = 2
        while n * num <= 1000:
            index = n * num
            prime_map[index] = False
            num += 1

    _ = int(input())

    temp = input().split(" ")

    arr = []
    count = 0

    for n in temp:
        if prime_map[int(n)]:
            count += 1

    print(count)
