

if __name__ == '__main__':
    string = input()
    pattern = input()

    index = 0
    target_index = 0
    start_index = 0
    stack = []
    removeStack = []

    # search string pattern
    while index < len(string):
        if pattern[target_index] != string[index]:
            if pattern[0] == string[index]:
                stack.append((target_index, start_index))
                target_index = 0
                start_index = index
                continue

            if pattern[target_index] != string[index]:
                index += 1
                stack = []
                target_index = 0
                start_index = index
                continue

        target_index += 1
        index += 1

        if target_index < len(pattern):
            continue

        removeStack.append((start_index, index))

        if len(stack) == 0:
            target_index = 0
            start_index = index
        else:
            target_index, start_index = stack.pop()

    # explode string
    while len(removeStack) > 0 :
        start, end = removeStack.pop()

        while len(removeStack) > 0:
            next_start, next_end = removeStack[-1] # show last element

            if next_start > start and next_end < end:
                removeStack.pop()
                continue
            else :
                break

        string = string[:start] + string[end:]

    if len(string) == 0:
        print("FRULA")
    else:
        print(string)
