import sys

def get_root_index(tree):
    if len(tree) == 1:
        return 0

    max_index = 0
    for index in range(len(tree)):
        if tree[max_index][1][1] < tree[index][1][1]:
            max_index = index

    return max_index


def pre_order(tree, result):
    if len(tree) == 0:
        return

    if len(tree) == 1:
        result.append(tree[0][0])
        return

    root_index = get_root_index(tree)

    result.append(tree[root_index][0])

    pre_order(tree[:root_index], result)
    pre_order(tree[root_index + 1:], result)


def post_order(tree, result):
    if len(tree) == 0:
        return

    if len(tree) == 1:
        result.append(tree[0][0])
        return

    root_index = get_root_index(tree)

    post_order(tree[:root_index], result)
    post_order(tree[root_index + 1:], result)

    result.append(tree[root_index][0])


def solution(nodeinfo):
    nodes = [(index + 1, nodeinfo[index]) for index in range(len(nodeinfo))]

    sorted_nodes = sorted(nodes, key=lambda val: val[1][0])
    pre_result = []
    post_result = []
    pre_order(sorted_nodes, pre_result)
    post_order(sorted_nodes, post_result)

    return [pre_result, post_result]


if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    answer = solution(nodeinfo)
    print(answer)