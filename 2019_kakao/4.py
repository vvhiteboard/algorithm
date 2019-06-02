def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    food_count = len(food_times)
    index_set = set([n for n in range(1, food_count + 1)])
    food_arr = [(index, food_times[index]) for index in range(food_count)]
    sorted_food = sorted(food_arr, key=lambda val: (val[1], val[0]))

    before_food = 0
    for food in sorted_food:
        temp = food[1] - before_food

        if temp * food_count > k:
            break

        before_food = food[1]
        index_set.remove(food[0] + 1)
        k -= temp * food_count
        food_count -= 1

    k = k % food_count
    index = 0
    for _ in range(k):
        index = (index + 1) % food_count

    index_arr = list(index_set)
    return index_arr[index]


def slow_solution(food_times, k):
    if k >= sum(food_times):
        return -1

    food_count = len(food_times)
    index = 0
    while k > 0:
        if food_times[index] == 0:
            index = (index + 1) % food_count
            continue

        food_times[index] -= 1
        index = (index + 1) % food_count
        k -= 1

    while food_times[index] == 0:
        index = (index + 1) % food_count

    return index + 1


if __name__ == "__main__":
    food_times = [7, 2, 1, 1, 8]
    k = 9
    answer = solution(food_times, k)
    print(answer)

