#include <stdio.h>
/**
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
}
