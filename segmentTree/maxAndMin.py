import sys


def build_tree(arr2):
	treex = [None for _ in range(3*(len(arr2)))]

	init_node(treex, 1, 1, len(arr), arr2)

	return treex


# node = (left, right, min, max)
def init_node(tree1, index, left, right, arr1):
	if left >= right:
		tree1[index] = (left, right, arr1[left-1], arr1[left-1])
		return

	init_node(tree1, index*2, left, int((left + right)/2), arr1)
	init_node(tree1, index*2 + 1, int((left + right)/2) + 1, right, arr1)

	_, _, lmin1, lmax1 = tree1[index * 2]
	_, _, rmin1, rmax1 = tree1[index * 2 + 1]

	tree1[index] = (left, right, min(lmin1, rmin1), max(lmax1, rmax1))


def get_max_and_min(tree2, index, start, end):
	# print("search index :", index, "start :", start, "end :", end)
	left, right, _, _ = tree2[index]

	if start > right or end < left:
		return None, None

	if start <= left and end >= right:
		return tree[index][2], tree2[index][3]

	# middle = int((left + right) / 2)

	lmin2, lmax2 = get_max_and_min(tree2, index * 2, start, end)
	rmin2, rmax2 = get_max_and_min(tree2, index * 2 + 1, start, end)

	if lmin2 is None or lmax2 is None:
		return rmin2, rmax2
	elif rmin2 is None or rmax2 is None:
		return lmin2, lmax2

	return min(lmin2, rmin2), max(lmax2, rmax2)


if __name__ == "__main__":
	sys.setrecursionlimit(1000000)
	inputs = input().split(" ")

	n = int(inputs[0])
	m = int(inputs[1])

	arr = []

	for _ in range(n):
		arr.append(int(input()))

	tree = build_tree(arr)
	# print(tree)

	for _ in range(m):
		inputs = input().split(" ")
		min_value, max_value = get_max_and_min(tree, 1, int(inputs[0]), int(inputs[1]))
		print(min_value, max_value)
