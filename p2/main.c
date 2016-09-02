#include <stdio.h>
#define LIMIT 4000000


int main() {
	int sum = 0;
	int left = 1;
	int middle;
	int right = 2;
	while (right < LIMIT) {
		sum += (right % 2) ? 0 : right;
		middle = right;
		right += left;
		left = middle;
	}
	printf("SUM: %d\n", sum);
}