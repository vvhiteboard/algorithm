def user_input():
    cakes = int(input())
    persons = int(input())

    result = []
    expected_max = -1
    expected_max_user = -1
    for num in range(persons):
        temp = input().split(" ")
        p = int(temp[0])
        k = int(temp[1])

        if k-p+1 > expected_max :
            expected_max = k-p+1
            expected_max_user = num

        result.append([num, p-1, k-1, k-p+1, 0])

    return expected_max_user + 1, [-1 for _ in range(cakes)], result




if __name__ == "__main__":
    expected_max_user, cakes, persons = user_input()

    persons.reverse()

    print(expected_max_user)
    # print(persons)

    for person in persons:
        cakes[person[1]: person[2]+1] = [person[0] for _ in range(person[3])]

    persons.reverse()

    # print(cakes)

    for cake in cakes:
        if cake < 0:
            continue

        persons[cake][4] += 1

    actual_max = -1
    actual_max_user = -1

    for person in persons:
        if person[4] > actual_max:
            actual_max = person[4]
            actual_max_user = person[0]

    print(actual_max_user + 1)

