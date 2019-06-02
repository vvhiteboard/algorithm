

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = {}

    def link(self, node):
        if self.is_opposite(node):
            return

        self.adjacents[node.name] = node

    def is_opposite(self, node):
        return node.name in self.adjacents