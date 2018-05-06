#include <stdio.h>
#include <stdlib.h>

int main() {
	int arr[505][505];
	int len;

	scanf("%d", &len);

	for(int i = 0 ; i < len; i ++) {
		for (int j = 0 ; j <= i ; j++) {
			scanf("%d", &arr[i][j]);
		}
	}

	for(int i = 0 ; i < len; i ++) {
		for (int j = 0 ; j <= i; j++) {
		    // 루트인 경우(위쪽에 숫자가 없는 경우)
			if (i -1 < 0) {
				continue;
			}

            // 왼쪽에 숫자가 없는 경우(가장 왼쪽 라인)
			if (j - 1 < 0) {
				arr[i][j] += arr[i-1][j];
				continue;
			}

            // 오른쪽에 숫자가 없는 경우(가장 오른쪽 라인)
			if (j >= i) {
				arr[i][j] += arr[i-1][j-1];
				continue;
			}

			int a = arr[i-1][j];
			int b = arr[i-1][j-1];

            // 왼쪽과 오른쪽에서 내려왔을때 숫자가 가장 커지는 값을 찾아서 저장
			if (a > b) {
				arr[i][j] += a;
			} else {
				arr[i][j] += b;
			}
		}
	}

	int max = 0;

    // 가장 마지막 라인에서 가장 큰 숫자 출력
	for (int i = 0; i < len; i ++) {
		if (max < arr[len-1][i]) {
			max = arr[len-1][i];
		}
	}

	printf("%d", max);

	return 0;
}