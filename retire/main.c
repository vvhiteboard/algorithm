#include <stdio.h>

int arr[1500001][2] = {0};
int results[1500001] = {0};

int max(int a, int b) {
    if (a > b) {
        return a;
    }
    return b;
}

int main() {
    int n = 0;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d %d", &arr[i][0], &arr[i][1]);
    }


    for (int index= 0 ; index < n; index++) {
        int day = arr[index][0];
        int money = arr[index][1];

        if (index == 0) {
            if (n + 1 > index + day) {
                results[index + day] = money;
            }
            continue;
        }

        int target = results[index];
        int before = results[index - 1];

        results[index] = max(target, before);

        if (n+1 > index + day) {
            results[index + day] = max(results[index + day], results[index] + money);
        }
    }

    printf("%d", max(results[n], results[n-1]));
    return 0;
}