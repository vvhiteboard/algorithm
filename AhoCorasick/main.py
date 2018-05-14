from AhoCorasick import AhoCorasick

if __name__ == '__main__':
    aho = AhoCorasick()

    # aho.add_patterns(["root", "ser", "oo", "er", "!!", "robot"])
    aho.add_patterns(["acf", "c"])
    aho.show_pattern_tree()

    print("===========================")

    # string = "root user super power so good~!!"
    string = "ac"
    results = aho.search_patterns(string)
    print("========== result ===========")
    for pat in results:
        print(pat)