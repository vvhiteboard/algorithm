#include <stdio.h>
#include <stdlib.h>

int caves[200005] = { 0 };
int minTorch[200005] = { 0 };

void run();
int getlastTorchIndex(int index);
int getCoverage(int);
int findLastTorchIndex(int, int);

int main() {
   int testCase = 0;

   scanf("%d", &testCase);

   for (int test = 0; test < testCase; test++) {
      run();
   }


   return 0;
}

void run() {
   int lastTorchIndex = 0;
   int caveSize = 0;

   scanf("%d", &caveSize);

   for (int i = 0; i < caveSize; i++) {
      scanf("%d", &caves[i]);
   }

   for (int index = 0; index < caveSize; index++) {
      // 맨 앞 동굴은 1
      if (index == 0) {
         minTorch[index] = 1;
         lastTorchIndex = index;
         continue;
      }

      // case 1-1 : 현재 동굴에 횃불을 추가하면 앞 동굴 전체를 밝힐 수 있음
      if (getlastTorchIndex(index) < 0) {
         minTorch[index] = 1;
         if (getCoverage(lastTorchIndex) < getCoverage(index)) {
            lastTorchIndex = index;
         }
         continue;
      }

      // 현재 동굴의 바로 앞 동굴까지의 횃불 개수
      int before = minTorch[index - 1];

      // 현재 동굴에 횃불을 꽂았을때의 횃불 개수 - 1
      int current = minTorch[getlastTorchIndex(index)];

      // case 1-2 : 현재 동굴에 횃불을 추가하면 이전 최소갯수보다 더 적어지는 경우
      if (current < before) {
         minTorch[index] = current + 1;
         if (getCoverage(lastTorchIndex) < getCoverage(index)) {
            lastTorchIndex = index;
         }
         continue;
      }

      // case 2-1 : 최소 횃불 갯수가 그대로인 경우 (현재 동굴까지 불이 밝혀지는 경우)
      if (index <= getCoverage(lastTorchIndex)) {
         minTorch[index] = before;

      } else { // case 2-2 : 최소 횃불 갯수가 증가하는 경우 (현재 동굴은 불이 닿지 않는 경우)
         minTorch[index] = before + 1;
         lastTorchIndex = findLastTorchIndex(lastTorchIndex, index);
      }
   }

   printf("%d\n", minTorch[caveSize - 1]);
}

int getlastTorchIndex(int index) {
   return index - (caves[index] - 1) - 1;
}

int getCoverage(int index) {
   return index + caves[index] - 1;
}

int findLastTorchIndex(int lastTorchIndex, int currentIndex) {
   int maxIndex = 0;
   int max = -1;
   for (int index = lastTorchIndex; index <= currentIndex; index++) {
      if (max < getCoverage(index)) {
         max = getCoverage(index);
         maxIndex = index;
      }
   }

   return maxIndex;
}