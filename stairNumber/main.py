

def calculate_case(digit, num, case_map, is_visited):
    visited = copy_list(is_visited)
    visited[num] = True

    value = case_map[digit][num].get(tuple(visited))
    if value is not None and value > 0:
        return value

    if digit <= 1:
        if sum(visited) == 10:
            return 1
        else:
            return 0

    total = 0

    if num + 1 <= 9:
        total += calculate_case(digit - 1, num + 1, case_map, visited)

    if num - 1 >= 0:
        total += calculate_case(digit - 1, num - 1, case_map, visited)

    case_map[digit][num][tuple(visited)] = total % 1000000000
    return total


def copy_list(arr):
    return [a for a in arr]


if __name__ == "__main__":
    digit = int(input())

    case_map = [[{} for _ in range(10)] for _ in range(101)]

    total = 0

    # for digit in range(11, 41):
    for i in range(1, 10):
        is_visited = [False for _ in range(10)]
        total += calculate_case(digit, i, case_map, is_visited)
        # print("digit :", digit, "total :", total)

    # pprint.pprint(case_map)

    total = total % 1000000000

    print(total)


