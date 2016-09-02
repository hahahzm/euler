#include <stdio.h>

int main() {
	int i;
	int sum = 0;
	for (i = 1; i < 1000; i++) sum += ((i % 3) && (i % 5)) ? 0 : i;
	printf("SUM: %d\n", sum);
}