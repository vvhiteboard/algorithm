def build_frequency_map(arr):
    element_map = {}

    for index in range(0, len(arr)):
        element = arr[index]

        if element in element_map:
            element_map[element] += 1
        else:
            element_map[element] = 1

    return element_map


def decrease_all(element_map):
    for key in element_map.keys():
        element_map[key] -= 1

def is_empty(element_map):
    for key in element_map.keys():
        if element_map[key] > 0:
            return False

    return True

def is_all_not_empty(element_map):
    for key in element_map.keys():
        if element_map[key] == 0:
            return False

    return True

def append_all(element_map, parent, path, k):
    if is_all_not_empty(element_map):
        decrease_all(element_map)

        # for


def build_tree(element_map, nary):
    root = []
    path = []

    append_all(element_map, root, path, nary)
    pass

def show_code_map(tree, arr):
    pass

if __name__ == "__main__":
    # testcase = int(input())

    Z = int(input())
    N = int(input())
    arr = input()
    frequency_map = build_frequency_map(arr)

    temp = Z - N
    decrease_all(frequency_map)
    count = 0
    while temp > 0:
        temp = temp - N + 1
        count += 1
        decrease_all(frequency_map)

    subtree_map = {}
    for key in frequency_map.keys():
        temp = int(frequency_map[key] / (N - 1))
        if temp is not 0:
            subtree_map[key] = temp

    print(subtree_map)

    tree = sorted(subtree_map, key=lambda x: subtree_map[x])
    tree.reverse()
    print(tree)
    #
    # tree = build_tree(frequency_map, nary)
    #
    # show_code_map(tree, arr)



