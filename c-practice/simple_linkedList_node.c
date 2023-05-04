#include <stdio.h>
#include <stdlib.h>

typedef struct node{
  int data;
  struct node *link;
} node_t;

int main(void){
  node_t *head = NULL;
  head = malloc(sizeof(node_t));
  printf("Enter data value for the newly created node: ");
  scanf("%d", &head->data);
  head->link = NULL;
  printf("Node data value is %d", head->data);
  return (0);
}
