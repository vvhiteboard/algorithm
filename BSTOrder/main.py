from BST import BST

if __name__ == "__main__":
    bst = BST()
    bst.add_node("D")
    bst.add_node("B")
    bst.add_node("F")
    bst.add_node("A")
    bst.add_node("C")
    bst.add_node("E")
    bst.add_node("G")
    print("tree initialize complete")

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
