from collections import deque

class TreeNode:
    def __init__(self, element):
        self.parent = None
        self.failure_node = None
        self.output_node = None
        self.children = {}
        self.end_of_pattern = False

        self.element = element

    def is_root(self):
        return self.element == "root"

    def is_end_node(self):
        if len(self.children) < 0:
            return True
        return False

    def is_empty_children(self):
        if len(self.children) < 0:
            return True
        return False

    def is_match_element(self, element):
        if self.element == element:
            return True
        return False

    def add_children(self, element):
        child = TreeNode(element)
        self.children[child.element] = child
        child.parent = self
        return child

    def is_contain_children(self, element):
        return element in self.children

    def has_output_node(self):
        return self.output_node is not None

    def get_pattern(self):
        if not self.end_of_pattern:
            return ""

        current = self
        result_str = ""
        while not current.is_root():
            result_str = current.element + result_str
            current = current.parent

        return result_str

class AhoCorasick:
    def __init__(self):
        self.root = TreeNode("root")
        self.nodes = []
        self.patterns = []

    def init_pattern_tree(self):
        for node in self.nodes:
            node.failure_node = None
            node.output_node = None

    def build_pattern_path(self, pattern):
        current = self.root

        for ch in pattern:
            if current.is_contain_children(ch):
                current = current.children[ch]
                continue

            current = current.add_children(ch)
            self.nodes.append(current)

        current.end_of_pattern = True

    def build_failure_path_and_output_path(self):
        queue = deque()

        queue.extend(self.root.children.values())

        while len(queue) > 0:
            node = queue.popleft()
            queue.extend(node.children.values())

            target = node.parent

            while node.failure_node is None:
                if target.is_root():
                    node.failure_node = target
                    continue

                target = target.failure_node

                if target.is_contain_children(node.element):
                    node.failure_node = target.children[node.element]

            if node.end_of_pattern:
                node.output_node = node
                continue

            if node.failure_node.end_of_pattern:
                node.output_node = node.failure_node
            else:
                node.output_node = node.failure_node.output_node

    def build_pattern_tree(self):
        self.init_pattern_tree()
        self.build_failure_path_and_output_path()

    def add_patterns(self, patterns):
        self.patterns.extend(patterns)
        for pattern in patterns:
            self.build_pattern_path(pattern)
        self.build_pattern_tree()

    def add_pattern(self, pattern):
        self.patterns.append(pattern)
        self.build_pattern_path(pattern)
        self.build_pattern_tree()

    def show_pattern_tree(self):
        queue = deque()

        queue.append(self.root)

        while len(queue) > 0:
            node = queue.popleft()

            if node.is_root():
                failure_node = "None"
            else:
                failure_node = str(node.failure_node.element)

            if node.output_node is None:
                output_node = "None"
            else:
                output_node = str(node.output_node.element)

            print("node : %s, " % node.element, "children : %s" % str(node.children.keys()), "failure_node : %s, " % failure_node, "output_node : %s" % output_node)

            queue.extend(node.children.values())

    def search_patterns(self, plain_text):
        current = self.root
        results = set()

        for element in plain_text:
            print("===== %s =====" % element)
            while not current.is_contain_children(element):
                if current.is_root():
                    break
                current = current.failure_node

            if not current.is_contain_children(element) and current.is_root():
                continue

            if current.is_contain_children(element):
                current = current.children[element]

                if current.has_output_node():
                    output = current.output_node
                    pattern = output.get_pattern()
                    print("find correct pattern : %s" % pattern)
                    results.add(pattern)

                    while output.has_output_node() and not output.end_of_pattern:
                        output = output.output_node
                        pattern = output.get_pattern()
                        print("find correct pattern : %s" % pattern)
                        results.add(pattern)

        return results
