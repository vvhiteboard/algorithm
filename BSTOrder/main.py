from BST import BST

if __name__ == "__main__":
    print("tree-init-start")
    bst = BST()
    bst.add_node("D")
    bst.add_node("B")
    bst.add_node("F")
    bst.add_node("A")
    bst.add_node("C")
    bst.add_node("E")
    bst.add_node("G")
    print("""result is \nPre : D B A C F E G\nPost : A C B E G F D\nIn : A B C D E F G\nlevel : D B F A C E G""")
    print("tree-init-end")

    print("=========== Pre-Order ==========")
    bst.pre_order()
    print("================================")

    print("=========== Post-Order ==========")
    bst.post_order()
    print("================================")

    print("=========== In-Order ==========")
    bst.in_order()
    print("================================")

    print("=========== level-Order ==========")
    bst.level_order()
    print("================================")
