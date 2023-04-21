#include <stdio.h>

int main(void){
	int seen[10] = {0};
	int N;
	printf("Enter any integer number of your choose: ");
	scanf("%d", &N);
	while (N > 0){
		rem = N % 10;
		if (seen[rem] == 1)
			break;
		seen[rem] = 1;
		N = N / 10
	}

	if (N > 0)
		print("Yes")
	else
		print("No")
}
