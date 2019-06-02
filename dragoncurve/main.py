
def make_dragon(curve):
    x, y, d, g = curve

    dragon = set()

    dragon.add((x,y))
    base = (x, y)

    pivot = go(x, y, d)
    dragon.add(pivot)

    for _ in range(g):
        temp_dragon = set()
        for point in dragon:
            temp_dragon.add(spin(pivot, point))

        pivot = spin(pivot, base)
        dragon = dragon.union(temp_dragon)

    return dragon


def how_many_rectangle(dragon):
    count = 0
    for x in range(100):
        for y in range(100):
            rectangle = set([(x, y), (x+1, y), (x, y+1), (x+1, y+1)])
            if rectangle.issubset(dragon):
                count += 1

    return count


def go(x, y, d):
    if d == 0:
        return (min(x+1, 100), y)
    elif d == 1:
        return (x, max(y-1, 0))
    elif d == 2:
        return (max(x-1, 0), y)
    else:
        return (x, min(y+1, 100))


def spin(pivot, point):
    a = pivot[0] - point[0]
    b = point[1] - pivot[1]

    newX = pivot[0] - b
    newY = pivot[1] - a

    if newX < 0 or newX > 100 or newY < 0 or newY > 100:
        return None

    return (newX, newY)


if __name__ == "__main__":
    n = int(input())

    curves = []
    dragons = set()

    for _ in range(n):
        curves.append([int(p) for p in input().split(" ")])

    for curve in curves:
        results = make_dragon(curve)
        dragons = dragons.union(results)

    count = how_many_rectangle(dragons)
    # print(dragons)
    print(count)






