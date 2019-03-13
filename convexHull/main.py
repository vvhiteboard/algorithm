import math

def getDegree(stdPoint, point):
    # return (point[0] - stdPoint[0]) / ((point[0] - stdPoint[0]) ** 2 + (point[1] - stdPoint[1]) ** 2) ** 0.5
    return math.atan2(point[1] - stdPoint[1], point[0] - stdPoint[0])

def getDistance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def sortByDegree(minPoint):
    for point in arr:
        point[2] = getDegree(minPoint, point)
        point[3] = getDistance(minPoint, point)


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


def grahamScan(arr2, minPoint):
    stack = []

    stack.append(minPoint)
    stack.append(arr2[0])

    index = 1

    while index < len(arr2):
        p2, p1 = stack.pop(), stack.pop()
        p3 = arr2[index]

        # print(p1)
        # print(p2)
        # print(p3)
        ccw = isCcw(p1, p2, p3)
        # print(ccw)

        if ccw == 1:
            stack.append(p1)
            stack.append(p2)
            stack.append(p3)
            index += 1
        elif ccw == 0:
            stack.append(p1)
            stack.append(p3)
            index += 1
        else:
            stack.append(p1)

    p2, p1 = stack.pop(), stack.pop()
    p3 = minPoint

    ccw = isCcw(p1, p2, p3)

    stack.append(p1)

    if ccw == 1:
        stack.append(p2)

    return stack


if __name__ == "__main__":
    n = int(input())
    global arr

    arr = []

    minPoint = (40001, 40001, 0, 0)
    for _ in range(n):
        inp = input().split(" ")

        x = int(inp[0])
        y = int(inp[1])

        if minPoint[1] == 40001:
            minPoint = [x, y, 0, 0]
            continue

        if y < minPoint[1] or (y == minPoint[1] and x < minPoint[0]):
            arr.append(minPoint)
            minPoint = [x, y, 0, 0]
        else:
            arr.append([x, y, 0, 0])

    sortByDegree(minPoint)
    arr2 = sorted(arr, key=lambda value: (value[2], value[3]))
    # print(arr2)

    result = grahamScan(arr2, minPoint)
    print(str(len(result)))


