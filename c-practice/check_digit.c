#include <stdio.h>
/**
<<<<<<< HEAD
 * check whether a digit appears
 * more than once in a given number.
 * if yes, print yes and otherwise no.
 **/

int main(void){
	int seen[] = {0}, num;
	printf("Enter a number to be check: ");
	scanf("%d", &num);
	int rem;
	while (num > 0){
		rem = num % 10;
		if (seen[rem] == 1)
			break;
		seen[rem] = 1;
		num /= 10;

	}

	if (num > 0)
		printf("Yes");
	else
		printf("No");
	return (0);

=======
check whether a digit appears
more than one times in a number.
if yes, print yes and otherwise
no.
**/

int main(void){
  int seen[10] = {0}, num;
  printf("Enter a number to be check: ");
  scanf("%d", &num);
  int rem;
  while (num > 0){
    rem = num % 10;
    if (seen[rem] == 1)
      break;
    seen[rem] = 1;
    num /= 10;
  }
  if (num > 0)
    printf("Yes");
  else
    printf("No");
>>>>>>> 7069452011c104c5fb1514da7503f529812627fd
}
