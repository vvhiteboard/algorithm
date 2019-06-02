#include <stdio.h>

long long boxes[500000][4];
long long arr[500000][2];
int N;

long long min(long long a, long long b);
long long max(long long a, long long b);
int is_intersection(int box1, int box2);
long long calc_area(int box1, int box2);

int cut_boxes();

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i ++) {
        scanf("%lld %lld", &arr[i][0], &arr[i][1]);
    }

    int box_index = cut_boxes();

    long long max_area = 0;

    for(int i = 0 ; i < box_index; i++) {
        for(int j = 0; j < box_index; j++) {
            if (i == j) {
                continue;
            }

            if (is_intersection(i,j)) {
                max_area = max(max_area, calc_area(i,j));
            }
        }
    }

    printf("%lld", max_area);


    return 0;
}

int cut_boxes() {
    int box_index = 0;
    long long before_x = 0;

    for(int index = 1 ; index < N-1 ; index++) {
        if (index == 1) {
            before_x = arr[index][0];
            continue;
        }

        // down
        if (arr[index + 1][1] < arr[index][1]) {
            boxes[box_index][0] = before_x;
            boxes[box_index][1] = 0;
            boxes[box_index][2] = arr[index][0];
            boxes[box_index][3] = arr[index][1];
            box_index += 1;
        }

        else if (arr[index+1][1] > arr[index][1]) {
            long long start_x = 0;
            long long end_x = arr[N-1][0];

            if (arr[index-1][1] > arr[index-2][1]) {
                start_x = arr[index-1][0];
            } else {
                int ind = index - 1;

                while (ind > 0) {
                    if (arr[ind-1][1] < arr[index][1] && arr[index][1] < arr[ind][1]) {
                        start_x = arr[ind][0];
                        break;
                    }
                    ind -= 1;
                }
            }

            int ind = index + 1;

            while(ind < N-1) {
                if (arr[ind+1][1] < arr[index][1] && arr[index][1] < arr[ind][1]) {
                    end_x = arr[ind][0];
                    break;
                }

                ind += 1;
            }

            boxes[box_index][0] = start_x;
            boxes[box_index][1] = 0;
            boxes[box_index][2] = end_x;
            boxes[box_index][3] = arr[index][1];
            box_index += 1;
            before_x = arr[index][0];
        }
    }

    return box_index;
}

long long min(long long a, long long b) {
    if (a > b) {
        return b;
    }

    return a;
}

long long max(long long a, long long b) {
    if (a > b) {
        return a;
    }

    return b;
}

int is_intersection(int box1, int box2) {
    if ((boxes[box1][0] < boxes[box2][0] && boxes[box2][0] < boxes[box1][2]) || (boxes[box1][0] < boxes[box2][2] && boxes[box2][2] < boxes[box1][2])) {
        return 1;
    }

    return 0;
}

long long calc_area(int box1, int box2) {
    long long area1 = (boxes[box1][2] - boxes[box1][0]) * (boxes[box1][3] - boxes[box1][1]);
    long long area2 = (boxes[box2][2] - boxes[box2][0]) * (boxes[box2][3] - boxes[box2][1]);

    long long x = min(boxes[box1][2], boxes[box2][2]) - max(boxes[box1][0], boxes[box2][0]);
    long long y = min(boxes[box1][3], boxes[box2][3]) - max(boxes[box1][1], boxes[box2][1]);

    long long intersection_area = x * y;

    return area1 + area2 - intersection_area;
}