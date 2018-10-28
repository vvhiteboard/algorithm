import sys

def makeParentAndDepth(parent, now, depth):
    adjacent = tree[now][2]

    if len(adjacent) is 0:
        return

    for child in adjacent:
        if child == parent:
            continue
        tree[child][0] = now
        mem[child][0] = now
        tree[child][1] = depth
        makeParentAndDepth(now, child, depth+1)


def searchLCA(u, v):
    depthA = tree[u][1]
    depthB = tree[v][1]

    # 깊이가 더 낮은쪽이 높이를 맞춘다.
    if depthA > depthB:
        u = getSameHight(u, depthA - depthB)
    elif depthA < depthB:
        v = getSameHight(v, depthB - depthA)

    if u == v or u == 1:
        return u

    for k in range(17, -1, -1):
        if mem[u][k] == -1 or mem[u][k] == mem[v][k]:
            continue

        u = mem[u][k]
        v = mem[v][k]

    return mem[u][0]


def getSameHight(node, diff):
    k = 0
    while diff > 0:
        if diff & 1 == 1:
            node = mem[node][k]

        k += 1
        diff = diff >> 1

    return node


# index : node 번호
# (parent, depth, adjacent)
if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 8)
    root = 1
    N = int(input())
    global tree
    tree = [[None, -1, []] for _ in range(N + 1)]
    global mem
    mem = [[-1 for _ in range(20)] for _ in range(N + 1)]

    for _ in range(N-1):
        ins = input().split(" ")

        tree[int(ins[0])][2].append(int(ins[1]))
        tree[int(ins[1])][2].append(int(ins[0]))

    tree[root][1] = 0
    makeParentAndDepth(-1, root, 1)

    for k in range(20):
        for n in range(1, N+1):
            if mem[n][k] != -1:
                mem[n][k+1] = mem[mem[n][k]][k]

    M = int(input())

    for _ in range(M):
        ins = input().split(" ")
        a = int(ins[0])
        b = int(ins[1])

        lca = searchLCA(a, b)
        print(lca)


