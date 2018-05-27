class Huffman:
    def __init__(self, plain_text):
        self.frequency_map = self.calculate_frequency_map(plain_text)
        self.huffman_tree = self.build_huffman_tree(self.frequency_map)
        self.code_map = self.build_code_map(self.huffman_tree)

    def calculate_frequency_map(self, plain_text):
        frequency_map = {}

        for ch in plain_text:
            if ch in frequency_map:
                frequency_map[ch] = frequency_map[ch] + 1
            else:
                frequency_map[ch] = 1

        return frequency_map

    def build_huffman_tree(self, frequency_map):
        sorted_frequency_array = [(frequency_map[x], x) for x in sorted(frequency_map, key=lambda x: frequency_map[x])]

        while len(sorted_frequency_array) > 1:
            sorted_frequency_array[1] = (sorted_frequency_array[0][0] + sorted_frequency_array[1][0],
                                         (sorted_frequency_array[0], sorted_frequency_array[1]))
            sorted_frequency_array = sorted(sorted_frequency_array[1:], key=lambda x: x[0])

        return sorted_frequency_array[0]

    def build_code_map(self, huffman_tree):
        code_map = {}

        self.get_code_map("", huffman_tree, code_map)

        return code_map

    def get_code_map(self, code, subtree, code_map):
        element = subtree[1]

        if type(element) is str:
            code_map[element] = code
            return

        self.get_code_map(code + "0", element[0], code_map)
        self.get_code_map(code + "1", element[1], code_map)

    def compress(self, plain_text):
        compressed_text = ""

        for ch in plain_text:
            compressed_text = compressed_text + self.code_map[ch]

        return compressed_text

    def decompress(self, compressed_text):
        plain_text = ""
        current = self.huffman_tree[1]

        for ch in compressed_text:
            index = int(ch)

            current = current[index]
            if type(current[1]) is str:
                plain_text = plain_text + current[1]
                current = self.huffman_tree[1]
            else:
                current = current[1]

        return plain_text
