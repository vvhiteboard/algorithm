from collections import deque
import time

class TreeNode:
    def __init__(self, element):
        self.parent = None
        self.failure_node = None
        self.output_node = None
        self.children = {}
        self.end_of_pattern = False
        self.indexs = {}

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

    def build_pattern_path(self, pattern, index):
        current = self.root

        for ch in pattern:
            if current.is_contain_children(ch):
                current = current.children[ch]
                continue

            current = current.add_children(ch)
            self.nodes.append(current)

        current.end_of_pattern = True
        current.indexs[index] = index

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

            if node.failure_node.end_of_pattern:
                node.output_node = node.failure_node
            else:
                node.output_node = node.failure_node.output_node

    def build_pattern_tree(self):
        self.init_pattern_tree()
        self.build_failure_path_and_output_path()

    def add_patterns(self, pattern_list):
        self.patterns.extend(pattern_list)
        for index in range(0, len(pattern_list)):
            self.build_pattern_path(pattern_list[index], index)
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

            print("node : %s, " % node.element, "children : %s" % str(node.children.keys()), "failure_node : %s, " % failure_node, "output_node : %s," % output_node, " indexs : %s" % node.indexs)

            queue.extend(node.children.values())

    def search_patterns(self, plain_text, prev, pattern_height):
        current = self.root
        results = prev
        count = 0

        for index in range(0, len(plain_text)):
            # print("===== %s =====" % element)
            result = []
            if not index in results:
                results[index] = []
            element = plain_text[index]

            while not current.is_contain_children(element):
                if current.is_root():
                    break
                current = current.failure_node

            if not current.is_contain_children(element) and current.is_root():
                continue

            if current.is_contain_children(element):
                current = current.children[element]

                if current.end_of_pattern:
                    # start = time.time()
                    results[index], a = self.get_current_pattern(results[index], current.indexs, pattern_height)
                    # end = time.time()
                    # print("find pattern time : %f" % (end - start))
                    count += a

                # if current.has_output_node():
                #     output = current.output_node
                #     results[index], a = self.get_current_pattern(results[index], output.indexs, pattern_height)
                #     count += a
                #
                #     while output.has_output_node():
                #         results[index], a = self.get_current_pattern(results[index], output.indexs, pattern_height)
                #         count += a

        return (results, count)

    def get_current_pattern(self, prev, current, pattern_height):
        temp = []
        count = 0

        if 0 in current:
            temp.append(0)

        # start = time.time()
        for key in prev:
            if key + 1 in current:
                if pattern_height - 1 == key + 1:
                    count += 1
                else:
                    temp.append(key + 1)
        # end = time.time()
        # print("find 2: %f" % (end-start))

        return (temp, count)



def calc_pattern_count(index, current, result_map):
    count = 0
    prev = result_map[index]
    current.reverse()

    for offset in current:
        if offset == 0:
            continue

        if offset-1 in prev:
            prev[offset] = prev[offset-1]
        prev[offset - 1] = False

        if offset in prev and prev[offset] is True:
            count += 1
            prev[offset] = False

    return count

if __name__ == "__main__":
    # pictures = [
    #     "xxxxxxoxxo",
    #     "oxxoooxoox",
    #     "xooxxxxoox",
    #     "xooxxxoxxo",
    #     "oxxoxxxxxx",
    #     "ooooxxxxxx",
    #     "xxxoxxoxxo",
    #     "oooxooxoox",
    #     "oooxooxoox",
    #     "xxxoxxoxxo"
    # ]
    #
    # patterns = [
    #     "oxxo",
    #     "xoox",
    #     "xoox",
    #     "oxxo"
    # ]

    pictures = []
    for _ in range(0, 2000):
        pictures.append("x" * 2000)
    #
    patterns = []
    for _ in range(0, 1000):
        patterns.append("x" * 1)

    # 입력부 ####
    # input_string = input()
    # input_array = input_string.split(" ")
    #
    # pattern_height = int(input_array[0])
    # pattern_width = int(input_array[1])
    #
    # picture_height = int(input_array[2])
    # picture_width = int(input_array[3])
    # #
    # pictures = []
    # patterns = []
    # #
    # for _ in range(0, pattern_height):
    #     patterns.append(input())
    #
    # for _ in range(0, picture_height):
    #     pictures.append(input())
    #######

    aho = AhoCorasick()
    aho.add_patterns(patterns)
    width = len(patterns[0])
    height = len(patterns)

    result_map = {}
    count = 0
    results = {}

    for line_index in range(0, len(pictures)):
        text = pictures[line_index]
        start = time.time()
        results, a = aho.search_patterns(text, results, height)
        end = time.time()
        print("full time : %f" % (end - start))
        # print(results)
        count += a
        # print("line : ", line_index, "count : ", count)

        # for index, offsets in results:
        #     if index in result_map:
        #         count += calc_pattern_count(index, offsets, result_map)
        #
        #     if 0 in offsets:
        #         if index in result_map:
        #             result_map[index][0] = True
        #         else:
        #             result_map[index] = {0: True}
            # print(result_map)

    print(count)


