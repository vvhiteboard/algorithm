def user_input():
    n = int(input())

    arr = []

    for _ in range(n):
        point = list(map(int, input().rstrip().split()))
        arr.append(point)

    return n, arr


def cut_box(n, arr):
    boxes = []

    before_x = 0

    for index in range(1, n-1):
        if index == 1:
            before_x = arr[index][0]
            continue

        # down
        if arr[index+1][1] < arr[index][1]:
            boxes.append((before_x, 0, arr[index][0], arr[index][1]))

        # up
        elif arr[index+1][1] > arr[index][1]:
            start_x = 0
            end_x = arr[n-1][0]

            if arr[index-1][1] > arr[index-2][1]:
                start_x = arr[index-1][0]
            else:
                ind = index - 1
                while ind > 0:
                    if arr[ind-1][1] < arr[index][1] < arr[ind][1]:
                        start_x = arr[ind][0]
                        break
                    ind -= 1

            ind = index + 1
            while ind < n-1:
                if arr[ind + 1][1] < arr[index][1] < arr[ind][1]:
                    end_x = arr[ind][0]
                    break
                ind += 1

            boxes.append((start_x, 0, end_x, arr[index][1]))
            before_x = arr[index][0]

    return boxes


def is_intersection(box1, box2):
    return (box1[0] < box2[0] < box1[2]) or (box1[0] < box2[2] < box1[2])


def get_union_area(box1, box2):
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

    x = min(box1[2], box2[2]) - max(box1[0], box2[0])
    y = min(box1[3], box2[3]) - max(box1[1], box2[1])

    intersection_area = x * y

    return area1 + area2 - intersection_area


"""
8
0 0
0 20
10 20
10 15
15 15
15 10
20 10
20 0
"""



"""
6
0 0
0 10
10 10
10 20
20 20
20 0
"""

"""
14
0 0
0 30
10 30
10 20
20 20
20 25
30 25
30 30
40 30
40 23
50 23
50 30
60 30
60 0
"""



if __name__ == "__main__":
    n, arr = user_input()

    # print(n, arr)
    boxes = cut_box(n, arr)
    # print(boxes)

    max_area = 0

    for i in range(len(boxes)):
        box1 = boxes[i]
        for j in range(len(boxes)):
            if i == j:
                continue
            box2 = boxes[j]
            if is_intersection(box1, box2):
                max_area = max(max_area, get_union_area(box1, box2))

    print(max_area)



