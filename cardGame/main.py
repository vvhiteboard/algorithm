import sys

def turn(cards, front, rear, who, mem):
    if mem[front][rear] != -1:
        return mem[front][rear]

    if front == rear:
        if who == 0:
            return cards[front]
        else:
            return 0

    if who == 0:
        next = 1
    else:
        next = 0

    case_one_my = turn(cards, front + 1, rear, next, mem)
    case_two_my = turn(cards, front, rear - 1, next, mem)

    # 근우 턴
    if who == 0:
        if case_one_my + cards[front] > case_two_my + cards[rear]:  # 앞 카드 선택이 높은 경우
            mem[front][rear] = case_one_my + cards[front]
        else:  # 뒷 카드 선택이 높은 경우 or 같은 경우
            mem[front][rear] = case_two_my + cards[rear]

    # 명우 턴
    else:
        if case_one_my < case_two_my:
            mem[front][rear] = case_one_my
        else:
            mem[front][rear] = case_two_my

    return mem[front][rear]

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    test_case = int(input())

    for _ in range(test_case) :
        rear = int(input()) - 1
        temp = input().split(" ")

        mem = [[-1 for _ in range(1001)] for _ in range(1001)]

        cards = []
        for a in temp:
            cards.append(int(a))

        score = turn(cards, 0, rear, 0, mem)
        print(score)
