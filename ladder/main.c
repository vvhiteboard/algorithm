#include <stdio.h>

int ladder[31][11] = { 0 };
int candidates[1000][2] = { 0 };
int n, m, h;
int size = 0;

void extract_candidates();
int search_path(int start, int depth);
int is_correct_ladder();

int main() {
	scanf("%d %d %d", &n, &m, &h);

	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);

		ladder[a - 1][b - 1] = 1;
		ladder[a - 1][b] = 2;
	}

	extract_candidates();

	int result = search_path(0, 1);

	printf("%d\n", result);
}

void extract_candidates() {
	//    printf("###### start extract candidates #######\n");
	for (int line = 0; line < n - 1; line++) {
		for (int cross = 0; cross < h; cross++) {
			if (ladder[cross][line] == 0 && ladder[cross][line + 1] == 0) {
				//                printf("cross: %d, line: %d\n", cross, line);
				candidates[size][0] = cross;
				candidates[size][1] = line;
				size += 1;
			}
		}
	}

	//    printf("###### end extract candidates #######\n");
}

int is_correct_ladder() {
	int arr[10] = { 0,1,2,3,4,5,6,7,8,9 };

	for (int cross = 0; cross < h; cross++) {
		for (int line = 0; line < n; line++) {
			if (ladder[cross][line] == 1) {
				int temp = arr[line];
				arr[line] = arr[line + 1];
				arr[line + 1] = temp;
			}
		}
	}

	for (int index = 0; index < n; index++) {
		if (arr[index] != index) {
			return 0;
		}
	}

	return 1;
}


int search_path(int start, int depth) {
	int min_count = -1;

	if (is_correct_ladder()) {
		return 0;
	} else if (size == 0) {
		return -1;
	}

	for (int s = start; s < size; s++) {
		int cross = candidates[s][0];
		int line = candidates[s][1];
		//        printf("depth: %d, cross: %d, line: %d\n", depth, cross, line);

		if (ladder[cross][line] != 0 || ladder[cross][line + 1] != 0) {
			continue;
		}

		ladder[cross][line] = 1;
		ladder[cross][line + 1] = 2;

		if (is_correct_ladder()) {
			ladder[cross][line] = 0;
			ladder[cross][line + 1] = 0;
			return 1;
		}

		if (depth == 3) {
			ladder[cross][line] = 0;
			ladder[cross][line + 1] = 0;
			continue;
		}

		int count = search_path(s + 1, depth + 1);
		//        printf("depth: %d, count : %d\n", depth, count);

		if (count > 3 || count == -1) {
			ladder[cross][line] = 0;
			ladder[cross][line + 1] = 0;
			continue;
		}

		if (min_count == -1) {
			min_count = count + 1;
		} else {
			if (min_count > count + 1) {
				min_count = count + 1;
			}
		}

		ladder[cross][line] = 0;
		ladder[cross][line + 1] = 0;
	}

	return min_count;
}