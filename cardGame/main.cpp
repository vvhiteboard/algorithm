#include <stdio.h>

int map[1001][1001] = { 0 };
int cards[1001];

void init_map();
int turn(int front, int rear, int who);

int main() {
	int rear;
	int test_case;

	scanf("%d", &test_case);

	for (int i = 0; i < test_case; i++) {
		init_map();

		scanf("%d", &rear);

		for (int i = 0; i < rear; i++) {
			scanf("%d", &cards[i]);
		}

		int score = turn(0, rear - 1, 0);
		printf("%d\n", score);
	}

	return 0;
}

void init_map() {
	for (int i = 0; i < 1001; i++) {
		for (int j = 0; j < 1001; j++) {
			map[i][j] = -1;
		}
	}
}

int turn(int front, int rear, int who) {
	if (map[front][rear] != -1) {
		return map[front][rear];
	}

	if (front == rear) {
		if (who == 0) {
			return cards[front];
		} else {
			return 0;
		}
	}

	int next = (who + 1) % 2;

	int case_front = turn(front + 1, rear, next);
	int case_rear = turn(front, rear - 1, next);

	if (who == 0) {
		if (case_front + cards[front] > case_rear + cards[rear]) {
			map[front][rear] = case_front + cards[front];
		} else {
			map[front][rear] = case_rear + cards[rear];
		}
	} else {
		if (case_front < case_rear) {
			map[front][rear] = case_front;
		} else {
			map[front][rear] = case_rear;
		}
	}

	return map[front][rear];
}
