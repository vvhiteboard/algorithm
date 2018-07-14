def user_input():
    user_input = input()

    inputs = user_input.split(" ")

    return int(inputs[0]), int(inputs[1])


def input_matrix(s):
    results = []
    for _ in range(s):
        row = input()
        rows = row.split(" ")
        result = []

        for value in rows:
            result.append(int(value))

        results.append(result)

    return results


def pow_matrix(matrix, times):
    if times is 1 or times is 0:
        return matrix

    if times % 2 == 0:
        return pow_matrix(multi_matrix(matrix, matrix), int(times/2))

    return multi_matrix(pow_matrix(multi_matrix(matrix, matrix), int((times-1)/2)), matrix)


def multi_matrix(matrix1, matrix2):
    results = []
    size = len(matrix1)

    for row1 in range(size):
        result = []
        for column2 in range(size):
            sum = 0
            for row2 in range(size):
                sum += (matrix1[row1][row2]*matrix2[row2][column2])
            result.append(sum % 1000)
        results.append(result)

    return results


if __name__ == "__main__":
    size, square = user_input()

    matrix = input_matrix(size)

    matrix = pow_matrix(matrix, square)

    for row in range(size):
        for column in range(size):
            matrix[row][column] = matrix[row][column] % 1000

    for row in range(size):
        print(*matrix[row])


# 5 99999999769
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1