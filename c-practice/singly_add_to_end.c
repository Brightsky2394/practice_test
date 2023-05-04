#include <stdio.h>
#include <stdlib.h>

typedef struct node{
  int data;
  struct node *link;
} node_t;

node_t * add_to_end(node_t *ptr, int d){
  node_t *tev = malloc(sizeof(node_t));
  printf("Enter data value of next node: ");
  scanf("%d", &tev->data);
  tev->link = NULL;
  ptr->link = tev;
  return tev;
}

int main(void){
  node_t *head = malloc(sizeof(node_t));
  printf("Enter the data value of the first node: ");
  scanf("%d", &head->data);
  head->link = NULL;
  node_t *ptr = head;
  int val, val1;
  ptr = add_to_end(ptr, val);
  ptr = add_to_end(ptr, val1);
  ptr = head;
  while (ptr != NULL){
    printf("%d ", ptr->data);
    ptr = ptr->link;
  }
  return (0);
}
