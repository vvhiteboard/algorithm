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
		self._repair_tree(node)

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
			repiar_node = AVLTree._reduce_external(target)
		else:
			target = AVLTree._in_order_succeed(node)
			p_target = target.parent

			node.key = p_target.key
			node.element = p_target.element

			repiar_node = AVLTree._reduce_external(target)

		repiar_node = repiar_node.parent

		while repiar_node is not None:
			self._repair_tree(repiar_node)
			repiar_node = repiar_node.parent

		return element

	@staticmethod
	def _expand_external(node):
		node.right = TreeNode(node, None, None)
		node.left = TreeNode(node, None, None)

	@staticmethod
	def _reduce_external(node):
		p_node = node.parent
		pp_node = p_node.parent
		s_node = node.sibling()

		s_node.parent = pp_node

		if p_node.is_left():
			pp_node.left = s_node
		else:
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

	def _restructure(self, pp_node, p_node, node, case):
		if case is 1:
			a = node
			b = p_node
			c = pp_node
			t0 = a.left
			t1 = a.right
			t2 = b.right
			t3 = c.right

		elif case is 2:
			a = p_node
			b = node
			c = pp_node
			t0 = a.left
			t1 = b.left
			t2 = b.right
			t3 = c.right

		elif case is 3:
			a = pp_node
			b = node
			c = p_node
			t0 = a.left
			t1 = b.left
			t2 = b.right
			t3 = c.right

		else:
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

	@staticmethod
	def in_order(node):
		if node.is_external():
			print("external")
			return

		AVLTree.in_order(node.left)

		print(str(node.key) + ":" + str(node.element))

		AVLTree.in_order(node.right)

	def find_range(self, start, end):
		node = self.root
		results = []

		while node.is_internal():
			if start < node.key:
				node = node.left
			elif start > node.key:
				node = node.right
			else:
				break

		if node.is_external():
			if node.is_left():
				node = node.parent
			else:
				while not node.is_root() and node.is_right():
					node = node.parent
				node = node.parent

		while node is not None:
			if node.key <= end:
				results.append(node.element)
			else:
				break

			if node.right.is_internal():
				node = node.right
				while node.left.is_internal():
					node = node.left
			else:
				while not node.is_root() and node.is_right():
					node = node.parent
				node = node.parent

		return results


class TreeNode:
	def __init__(self, parent, key, element):
		self.parent = parent
		self.left = None
		self.right = None
		self.key = key
		self.element = element

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

	def height(self):
		if self.is_external():
			return 0

		return max(self.left.height(), self.right.height()) + 1
