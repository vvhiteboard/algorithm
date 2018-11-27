import sys


class AVLTree:
	def __init__(self):
		self.tree = []
		self.root = TreeNode(None, None, None)

	def find_node(self, key):
		node = self.root

		while node.is_internal():
			if key < node.key:
				node = node.left
			elif key > node.key:
				node = node.right
			else:
				break

		return node

	def find_element(self, key):
		node = self.find_node(key)

		if node is None:
			return None

		return node.element

	def append_node(self, key, element):
		node = self.find_node(key)

		if node.is_internal():
			if node.element[0] < element[0]:
				node.element = element
			return

		node.key = key
		node.element = element
		AVLTree._expand_external(node)
		self._rebalance(node)
		# self._repair_tree(node)

	def remove_node(self, key, x):
		node = self.find_node(key)

		if node.is_external():
			return None

		if x is not None and node.element[0] != x:
			return None

		element = node.element

		target = node.left
		if not target.is_external():
			target = node.right

		if target.is_external():
			repiar_node = self._reduce_external(target)
		else:
			target = AVLTree._in_order_succeed(node)
			p_target = target.parent

			node.key = p_target.key
			node.element = p_target.element

			repiar_node = self._reduce_external(target)

		repiar_node = repiar_node.parent

		self._rebalance(node)
		# while repiar_node is not None:
		# 	self._repair_tree(repiar_node)
		# 	repiar_node = repiar_node.parent

		return element

	@staticmethod
	def _expand_external(node):
		node.right = TreeNode(node, None, None)
		node.left = TreeNode(node, None, None)

	def _reduce_external(self, node):
		p_node = node.parent
		pp_node = p_node.parent
		s_node = node.sibling()

		s_node.parent = pp_node

		if p_node.is_left():
			pp_node.left = s_node
		elif p_node.is_right():
			pp_node.right = s_node

		return s_node

	@staticmethod
	def _in_order_succeed(node):
		next_node = node.right

		while next_node.is_internal():
			next_node = next_node.left

		return next_node

	def _repair_tree(self, node):
		case = 0
		left_height = node.left.height()
		right_height = node.right.height()

		while node is not None:
			if left_height - right_height >= 2:
				case = 1
				p_node = node.left
				break

			if right_height - left_height >= 2:
				case = 3
				p_node = node.right
				break

			if node.is_left():
				left_height = max(left_height, right_height) + 1
				right_height = node.sibling().height()
			elif node.is_right():
				right_height = max(left_height, right_height) + 1
				left_height = node.sibling().height()

			node = node.parent

		# 불균형 노드가 없음
		if node is None:
			return

		pp_node = node

		lh = p_node.left.height()
		rh = p_node.right.height()

		if lh > rh:
			node = p_node.left
		else:
			if case == 1:
				case = 2
			else:
				case = 4
			node = p_node.right

		self._restructure(pp_node, p_node, node, case)

	def _rebalance(self, node):
		while node is not None:
			old_height = node.height

			if not node.is_balanced():
				self._restructure(node.get_tall_grandchild())

				self._recompute_height(node.left)
				self._recompute_height(node.right)

			self._recompute_height(node)

			if node.height == old_height:
				break
			else:
				node = node.parent


	def _restructure(self, node):
		a, b, c, t0, t1, t2, t3 = None, None, None, None, None, None, None
		p_node = node.parent
		pp_node = p_node.parent

		if pp_node.left == p_node:
			if p_node.left == node:
				a = node
				b = p_node
				c = pp_node
				t0 = a.left
				t1 = a.right
				t2 = b.right
				t3 = c.right
			elif p_node.right == node:
				a = p_node
				b = node
				c = pp_node
				t0 = a.left
				t1 = b.left
				t2 = b.right
				t3 = c.right
		elif pp_node.right == p_node:
			if p_node.left == node:
				a = pp_node
				b = node
				c = p_node
				t0 = a.left
				t1 = b.left
				t2 = b.right
				t3 = c.right
			elif p_node.right == node:
				a = pp_node
				b = p_node
				c = node
				t0 = a.left
				t1 = b.left
				t2 = c.left
				t3 = c.right

		if not pp_node.is_root():
			if pp_node.is_right():
				pp_node.parent.right = b
			else:
				pp_node.parent.left = b
		else:
			self.root = b

		b.parent = pp_node.parent

		b.left = a
		a.parent = b

		b.right = c
		c.parent = b

		a.left = t0
		t0.parent = a

		a.right = t1
		t1.parent = a

		c.left = t2
		t2.parent = c

		c.right = t3
		t3.parent = c

	# def find_range(self, start, end):
	# 	node = self.root
	# 	results = []
	#
	# 	while node.is_internal():
	# 		if start < node.key:
	# 			node = node.left
	# 		elif start > node.key:
	# 			node = node.right
	# 		else:
	# 			break
	#
	# 	# start 검색 결과가 없는 경우
	# 	if node.is_external():
	# 		if node.is_left():
	# 			node = node.parent
	# 		else:
	# 			while not node.is_root() and node.is_right():
	# 				node = node.parent
	# 			node = node.parent
	#
	# 	while node is not None:
	# 		if node.key < end:
	# 			results.append(node.element)
	# 		else:
	# 			break
	#
	# 		if node.right.is_internal():
	# 			node = node.right
	# 			while node.left.is_internal():
	# 				node = node.left
	# 		else:
	# 			while not node.is_root() and node.is_right():
	# 				node = node.parent
	# 			node = node.parent
	#
	# 	return results

	def find_ranged(self, node, start, end):
		results = []

		if node.is_external():
			return results

		if node.key >= end:
			if node.left.is_internal():
				results.extend(self.find_ranged(node.left, start, end))

			return results

		if node.key <= start:
			if node.right.is_internal():
				results.extend(self.find_ranged(node.right, start, end))

			return results

		results.append(node.element)

		if node.left.is_internal():
			results.extend(self.find_ranged(node.left, start, end))

		if node.right.is_internal():
			results.extend(self.find_ranged(node.right, start, end))

		return results

	def _recompute_height(self, node):
		if node is None or node.is_external():
			return

		node.height = max(node.left.height, node.right.height) + 1


class TreeNode:
	def __init__(self, parent, key, element):
		self.parent = parent
		self.left = None
		self.right = None
		self.key = key
		self.element = element
		self.height = 0

	def is_root(self):
		return self.parent is None

	def is_internal(self):
		return self.key is not None

	def is_external(self):
		return self.key is None

	def is_left(self):
		if self.is_root():
			return False

		return self is self.parent.left

	def is_right(self):
		if self.is_root():
			return False

		return self is self.parent.right

	def sibling(self):
		if self.parent is None:
			return None

		if self.is_left():
			return self.parent.right

		elif self.is_right():
			return self.parent.left

		else:
			return None

	def is_balanced(self):
		if self.is_external():
			return True

		return abs(self.left.height - self.right.height) <= 1

	def get_tall_child(self, favorleft=False):
		if self.left.height + (1 if favorleft else 0) > self.right.height:
			return self.left

		return self.right

	def get_tall_grandchild(self):
		child = self.get_tall_child()

		alignment = (child == self.left)
		return child.get_tall_child(alignment)


def get_distance(point_1, point_2):
	return (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2


def in_order(node):
	if node.is_external():
		print("external")
		return

	in_order(node.left)

	print(str(node.key) + ":" + str(node.element) + ":" + str(node.height))

	in_order(node.right)


import time


if __name__ == "__main__":
	sys.setrecursionlimit(100000)
	avlTree = AVLTree()
	n = int(input())
	points = []

	start = time.time()
	# fp = open("test3.txt", "r")

	for _ in range(n):
		# point = fp.readline().split("\n")[0].split(" ")
		point = input().split(" ")
		points.append((int(point[0]), int(point[1])))

	# fp.close()
	points = sorted(points, key=lambda point: point[0])

	point1 = points[0]
	point2 = points[1]

	min_distance = get_distance(point1, point2)

	avlTree.append_node(point1[1], point1)
	avlTree.append_node(point2[1], point2)

	min_index = 0

	for index in range(2, len(points)):
		point = points[index]

		while min_index < index and (points[min_index][0] - point[0]) ** 2 > min_distance:
			avlTree.remove_node(points[min_index][1], points[min_index][0])
			min_index += 1

		distance = min_distance ** 0.5
		elements = avlTree.find_ranged(avlTree.root, point[1] - distance, point[1] + distance)
		# elements = avlTree.find_range(point[1] - distance, point[1] + distance)
		# print(point, ":", elements)

		for element in elements:
			min_distance = min(get_distance(element, point), min_distance)

		avlTree.append_node(point[1], point)

	end = time.time()
	print(str(int(min_distance)))

	# print(end - start)

#
# 	avlTree.append_node(1, "A")
# 	avlTree.append_node(2, "B")
# 	avlTree.append_node(3, "C")
# 	avlTree.append_node(4, "D")
# 	avlTree.append_node(5, "E")
# 	avlTree.append_node(6, "F")
# 	avlTree.append_node(7, "G")
# 	avlTree.append_node(8, "H")
#
# #
# 	print("===")
# 	in_order(avlTree.root)
# 	result = avlTree.find_ranged(avlTree.root, 2, 6)
# 	print(result)
