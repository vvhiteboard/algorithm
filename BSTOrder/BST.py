from collections import deque

class BSTNode:
    parent = None
    left = None
    right = None

    element = None

    def __init__(self, parent, element):
        self.parent = parent
        self.element = element

        if element is not None:
            self.left = BSTNode(self, None)
            self.right = BSTNode(self, None)

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

    def do_pre_order(self):
        print(self.element)

        if self.left.is_internal():
            self.left.do_pre_order()

        if self.right.is_internal():
            self.right.do_pre_order()

    def do_post_order(self):
        if self.left.is_internal():
            self.left.do_post_order()

        if self.right.is_internal():
            self.right.do_post_order()

        print(self.element)

    def do_in_order(self):
        if self.left.is_internal():
            self.left.do_in_order()

        print(self.element)

        if self.right.is_internal():
            self.right.do_in_order()


class BST:
    root = BSTNode(None, None)

    def get_root(self):
        return self.root

    def add_node(self, element):
        if self.root.is_external():
            self.root = BSTNode(None, element)

        else:
            node = self.search_node(element)
            if node.is_internal():
                print("does not add duplicated element")
                return

            if node.is_right():
                node.parent.right = BSTNode(node.parent, element)
            else:
                node.parent.left = BSTNode(node.parent, element)

    def pre_order(self):
        self.root.do_pre_order()

    def post_order(self):
        self.root.do_post_order()

    def in_order(self):
        self.root.do_in_order()

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


