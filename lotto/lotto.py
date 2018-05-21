def get_user_input() :
    user_input = input()
    inputs = user_input.split()

    return int(inputs[0]), inputs[1:]

def run(k, arr):
    lotto(k, arr, [], 0, 0, k)

def lotto(k, arr, result, depth, start, end):
    if depth == 6:
        print(" ".join(result))
        return

    for index in range(start, end + (depth - 5)):
        result.append(arr[index])
        lotto(k, arr, result, depth + 1, index + 1, end)
        result.pop()

if __name__ == "__main__":
    while True:
        k, arr = get_user_input()

        if k is 0:
            break

        run(k, arr)
        print("")
