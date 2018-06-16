if __name__ == "__main__":
    prime_map = {1: False}

    for n in range(2, 1000001):
        if n in prime_map:
            continue

        prime_map[n] = True

        if n > 500000:
            continue

        num = 2
        while n * num <= 1000000:
            index = n * num
            prime_map[index] = False
            num += 1

    temp = input().split(" ")

    start = int(temp[0])
    end = int(temp[1])

    for n in range(start, end + 1):
        if prime_map[n]:
            print(n)
