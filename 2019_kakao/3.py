class CandidateKey:
    def __init__(self, relation):
        self.mem = {}
        self.relation = relation

    def get_target(self, row, target_index):
        target = []

        for index in target_index:
            target.append(row[index])

        return tuple(target)

    def calc_candidate_key_count(self, target_index):
        temp = tuple(target_index)

        count = 0
        if len(target_index) > 1:
            for n in target_index:
                sub = [i for i in target_index if i != n]
                count += self.calc_candidate_key_count(sub)

        if count > 0:
            return count

        keys = set()

        for row in self.relation:
            target = self.get_target(row, target_index)

            keys.add(target)

        if len(keys) == len(self.relation):
            count = 1
        else:
            count = 0

        self.mem[temp] = count
        return count


def solution(relation):
    ck = CandidateKey(relation)
    n = len(relation[0])
    target_index = [i for i in range(n)]

    ck.calc_candidate_key_count(target_index)

    answer = 0
    for key in ck.mem:
        answer += ck.mem[key]

    return answer


if __name__ == "__main__":
    relation = [["1","2","3","4","5","6"]]
    answer = solution(relation)
    print("count: ", answer)
