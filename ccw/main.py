def isCcw(point1, point2, point3):
    x1 = int(point1[0])
    y1 = int(point1[1])
    x2 = int(point2[0])
    y2 = int(point2[1])
    x3 = int(point3[0])
    y3 = int(point3[1])

    vector1_x = x2 - x1
    vector1_y = y2 - y1

    vector2_x = x3 - x2
    vector2_y = y3 - y2

    vector_z = vector1_x * vector2_y - vector1_y * vector2_x

    if vector_z > 0:
        return 1
    elif vector_z < 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    point1 = input().split(" ")
    point2 = input().split(" ")
    point3 = input().split(" ")

    print(isCcw(point1, point2, point3))

