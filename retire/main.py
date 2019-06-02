def user_input():
    n = int(input())

    inq = []

    append = inq.append

    for _ in range(n):
        arr = input()
        arr = arr.split(" ")
        append((int(arr[0]), int(arr[1])))

    return n, inq


def inquiry(n, inquiries):
    results = [0 for _ in range(n+1)]

    for index in range(inquiries):
        day = inquiries[index][0]
        money = inquiries[index][1]

        if index == 0:
            if n+1 > index + day:
                results[index + day] = money
            continue

        target = results[index]
        before = results[index - 1]

        results[index] = max(target, before)

        if n+1 > index + day:
            results[index + day] = max(results[index + day], results[index] + money)

    return max(results[-1], results[-2])


if __name__ == "__main__":
    n, inq = user_input()

    result = inquiry(n, inq)
    print(result)
