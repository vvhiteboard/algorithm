from collections import deque


class BST:
    class BSTNode:
        parent = None
        left = None
        right = None

        element = None

        def __init__(self, parent, element):
            self.parent = parent
            self.element = element

            if element is not None:
                self.left = BST.BSTNode(self, None)
                self.right = BST.BSTNode(self, None)

        def is_external(self):
            if self.element is None:
                return True
            return False

        def is_internal(self):
            if self.element is not None:
                return True
            return False

        def is_root(self):
            if self.parent is None:
                return True
            return False

        def is_right(self):
            if self.is_root():
                return False
            elif self.parent.right == self:
                return True
            return False

        def is_left(self):
            if self.is_root():
                return False
            elif self.parent.left == self:
                return True
            return False

        def visit(self):
            print(self.element)




    root = BSTNode(None, None)

    def get_root(self):
        return self.root

    def add_node(self, element):
        if self.root.is_external():
            self.root = BST.BSTNode(None, element)

        else:
            node = self.search_node(element)
            if node.is_internal():
                print("does not add duplicated element")
                return

            if node.is_right():
                node.parent.right = BST.BSTNode(node.parent, element)
            else:
                node.parent.left = BST.BSTNode(node.parent, element)

    def pre_order(self):
        self.do_pre_order(self.root)

    def do_pre_order(self, node):
        node.visit()

        if node.left.is_internal():
            self.do_pre_order(node.left)

        if node.right.is_internal():
            self.do_pre_order(node.right)

    def post_order(self):
        self.do_post_order(self.root)

    def do_post_order(self, node):
        if node.left.is_internal():
            self.do_post_order(node.left)

        if node.right.is_internal():
            self.do_post_order(node.right)

        node.visit()

    def in_order(self):
        self.do_in_order(self.root)

    def do_in_order(self, node):
        if node.left.is_internal():
            self.do_in_order(node.left)

        node.visit()

        if node.right.is_internal():
            self.do_in_order(node.right)

    def level_order(self):
        queue = deque()

        queue.append(self.root)

        while len(queue) > 0:
            node = queue.popleft()

            print(node.element)

            if node.left.is_internal():
                queue.append(node.left)

            if node.right.is_internal():
                queue.append(node.right)

    def search_node(self, element):
        node = self.root
        while node.is_internal():
            if node.element < element:
                node = node.right
            elif node.element > element:
                node = node.left
            else:
                return node

        return node


