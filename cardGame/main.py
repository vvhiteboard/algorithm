import sys

def turn(cards, front, rear, who, mem):
    if mem[front][rear] != -1:
        # print(mem[front][rear])
        if who == 0:
            return mem[front][rear]
        else:
            my, your = mem[front][rear]
            return your, my

    if front == rear:
        if who == 0:  # 짝수면 근우 턴
            return cards[front], 0
        else:  # 홀수면 명우 턴
            return 0, cards[front]

    next = (who + 1) % 2
    case_one_my, case_one_your = turn(cards, front + 1, rear, next, mem)
    case_two_my, case_two_your = turn(cards, front, rear - 1, next, mem)

    # 근우 턴
    if who == 0:
        if case_one_my + cards[front] > case_two_my + cards[rear]:  # 앞 카드 선택이 높은 경우
            mem[front][rear] = (case_one_my + cards[front], case_one_your)
        else:  # 뒷 카드 선택이 높은 경우 or 같은 경우
            mem[front][rear] = (case_two_my + cards[rear], case_two_your)

    # 명우 턴
    else:
        if case_one_your + cards[front] > case_two_your + cards[rear]:
            mem[front][rear] = (case_one_my, case_one_your + cards[front])
        else:
            mem[front][rear] = (case_two_my, case_two_your + cards[rear])

    return mem[front][rear]

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    test_case = int(input())

    for _ in range(test_case) :
        rear = int(input()) - 1
        mem = [[-1 for _ in range(rear + 1)] for _ in range(rear + 1)]

        temp = input().split(" ")
        cards = []
        for a in temp:
            cards.append(int(a))

        score, _ = turn(cards, 0, rear, 0, mem)
        print(score)
