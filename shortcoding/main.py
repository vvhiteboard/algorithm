from .Node import Node


def user_input() :
    expressions = input().split("&&")
    return expressions

def build_operation_graph(expressions):
    vertex = set()
    graph = {}

    for expr in expressions:
        if "==" in expr:
            e = expr.split("==")

            if e[0] in vertex:
                e1 = graph[e[0]]
            else:
                e1 = Node(e[0])
                vertex.add(e[0])

            if e[1] in vertex:
                e2 = graph[e[1]]
            else:
                e2 = Node(e[1])
                vertex.add(e[1])

            # 이미 연결되어있으면 안함
            e1.link(e2)
        else: # != 연산자이면
            pass


    return graph, vertex


def is_in_val(sub_arr, e1, e2):
    for a in sub_arr:
        in_e1 = e1 in a
        in_e2 = e2 in a

        if not in_e1 and not in_e2:
            new_sub_arr = set()
            new_sub_arr.put(e1)
            new_sub_arr.put(e2)
            sub_arr.append(new_sub_arr)
        elif in_e1 and not in_e2:
            a.append(e2)
        elif in_e2 and not in_e1:
            a.append(e1)

    return False


def split_sub_arr(e_results):
    splited_arr = []
    for e in e_results:
        e1 = e[0]
        e2 = e[2]

        if len(splited_arr) == 0:
            new_sub_arr = set()
            new_sub_arr.add(e1)
            new_sub_arr.add(e2)
            splited_arr.append(new_sub_arr)
            continue

        for a in splited_arr:
            in_e1 = e1 in a
            in_e2 = e2 in a

            if not in_e1 and not in_e2:
                new_sub_arr = set()
                new_sub_arr.add(e1)
                new_sub_arr.add(e2)
                splited_arr.append(new_sub_arr)
            elif in_e1 and not in_e2:
                a.add(e2)
            elif in_e2 and not in_e1:
                a.add(e1)

    return splited_arr


if __name__ == "__main__":
    graph, vertex = build_operation_graph(user_input())