#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sum;

int iterate(int c) {
	if (c == 0) sum++;
	else if (c < 0);
	else {
		iterate(c - 1);
		iterate(c - 2);
	}
}

int main(int argc, char** argv) {
	int n = atoi(argv[1]);
	iterate(n);
	printf("SUM: %d\n", sum);
}