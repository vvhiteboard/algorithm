arr = [1, -1, 2, -1, -1, 3, -1, -1]


def areYouBinaryTree(im, index):
    if im == 0 :
        print("im root : ", arr[index])
    elif im == 1:
        print("left : ", arr[index])
    elif im == 2:
        print("right : ", arr[index])

    if arr[index] == -1:
        return index + 1

    nextIndex1 = areYouBinaryTree(1, index + 1)
    nextIndex2 = areYouBinaryTree(2, nextIndex1)
    return nextIndex2


# [-1]
# [3, 5, 6, 8, -1, -1, -1, 1, 7, -1, -1, -1, 4, -1, 2, -1, -1]
# [1, -1, 2, -1, -1, 3, -1, -1]
if __name__ == "__main__":
    lastIndex = areYouBinaryTree(0, 0)

    if lastIndex == len(arr):
        print("true")
    else:
        print("false")

