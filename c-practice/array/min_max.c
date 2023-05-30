#include <stdio.h>
/**
determine the minimum and
maximum number in an array
of integers
**/

void minMax(int arr[], int len, int *min, int *max){
  *min = *max = arr[0];
  for (int j = 1; j < len; j++){
    if (arr[j] < *min)
      *min = arr[j];
    else if (arr[j] > *max)
      *max = arr[j];
  }
}

int main(void){
  int num, min, max;
  printf("Enter the number of array element: ");
    scanf("%d", &num);
  int my_array[num];
  printf("Enter %d array elements\n", num);
  for (int i = 0; i < num; i++){
    printf("Enter the %d array element: ", i + 1);
    scanf("%d", &my_array[i]);
  }
  minMax(my_array, num, &min, &max);
  printf("The minimum value is %d and maximum value is %d", min, max);
}
