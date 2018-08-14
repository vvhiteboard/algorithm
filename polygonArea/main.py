def inputPoint():
    point = input().split(" ")
    point = (int(point[0]), int(point[1]))

    return point

def getArea(vector1, vector2):
    X = 0
    Y = 1

    area = vector1[X] * vector2[Y] - vector1[Y] * vector2[X]
    return area / 2.0


if __name__ == "__main__":
    X = 0
    Y = 1

    n = int(input())

    totalArea = 0

    basePoint = inputPoint()
    point = inputPoint()

    beforeVector = (point[X] - basePoint[X], point[Y] - basePoint[Y])

    for _ in range(n-2):
        newPoint = inputPoint()

        newVector = (newPoint[X] - basePoint[X], newPoint[Y] - basePoint[Y])
        totalArea += getArea(beforeVector, newVector)

        beforeVector = newVector

    if totalArea < 0:
        totalArea = totalArea * -1

    print("{0:.1f}".format(totalArea))

"""
4
0 0
0 10
10 10
10 0
"""

