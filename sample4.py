

if __name__ == "__main__":
    global arr
    arr = input().split(" ")

    count1 = 0
    count2 = 0

    mask0 = 0
    mask1 = 1

    for a in arr:
        val = int(a)

        if val == mask0:
            count1 += 1

        if val == mask1:
            count2 += 1

        mask0 = (mask0 + 1) % 2
        mask1 = (mask1 + 1) % 2

    mask = 1

    for a in arr:
        val = int(a)

        if val == mask:
            count2 += 1

        mask = (mask + 1) % 2

    print(str(min(count1, count2)))



