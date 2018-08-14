def getCcw(vector1, vector2):
    vector1_x = vector1[0]
    vector1_y = vector1[1]

    vector2_x = vector2[0]
    vector2_y = vector2[1]

    vector_z = vector1_x * vector2_y - vector1_y * vector2_x

    if vector_z > 0:
        return 1
    elif vector_z < 0:
        return -1
    else:
        return 0


def isLine(vector1, point1, point2):
    X = 0
    Y = 1

    if vector1[X] == 0:
        return point1[X] == point2[X]

    return point2[Y] == (vector1[Y]/vector1[X])*(point2[X] - point1[X]) + point1[Y]


def getCrossPoint(vector1, vector2, point1, point2):
    X = 0
    Y = 1

    if vector1[X] == 0:
        crossPoint_y =  (vector2[Y]/vector2[X])*(point1[X] - point2[X]) + point2[Y]
        return point1[X], crossPoint_y

    elif vector2[X] == 0:
        crossPoint_y = (vector1[Y]/vector1[X])*(point2[X] - point1[X]) + point1[Y]
        return point2[X], crossPoint_y

    if vector1[Y] == 0:
        crossPoint_x = (vector2[X]/vector2[Y])*(point1[Y] - point2[Y]) + point2[X]
        return crossPoint_x, point1[Y]
    elif vector2[Y] == 0:
        crossPoint_x = (vector1[X] / vector1[Y]) * (point2[Y] - point1[Y]) + point1[X]
        return crossPoint_x, point2[Y]


    crossPoint_x = point1[Y] - point2[Y] + vector2[Y]/vector2[X]*point2[X] - vector1[Y]/vector1[X]*point1[X]
    crossPoint_x = crossPoint_x / (vector2[Y]/vector2[X] - vector1[Y]/vector1[X])

    crossPoint_y = (vector1[Y]/vector1[X])*(crossPoint_x - point1[X]) + point1[Y]

    return crossPoint_x, crossPoint_y


if __name__ == "__main__":
    X = 0
    Y = 1
    test_case = int(input())

    for _ in range(test_case):
        line = input().split(" ")
        point1 = (int(line[0]), int(line[1]))
        point2 = (int(line[2]), int(line[3]))
        point3 = (int(line[4]), int(line[5]))
        point4 = (int(line[6]), int(line[7]))

        vector1 = (point2[X] - point1[X], point2[Y] - point1[Y])
        vector2 = (point4[X] - point3[X], point4[Y] - point3[Y])

        ccw = getCcw(vector1, vector2)

        if ccw == 0:
            if isLine(vector1, point1, point3):
                print("LINE")
            else:
                print("NONE")
        else:
            crossPoint = getCrossPoint(vector1, vector2, point1, point3)
            print("POINT {0:0.2f} {1:0.2f}".format(crossPoint[0], crossPoint[1]))
"""₩
5
0 0 4 4 0 4 4 0
5 0 7 6 1 0 2 3
5 0 7 6 3 -6 4 -3
2 0 2 27 1 5 18 5
0 3 4 0 1 2 2 5
"""