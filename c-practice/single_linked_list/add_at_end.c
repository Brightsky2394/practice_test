#include "list.h"

void add_at_end(node_t *head, int d){
  node_t *ptr = head;
  node_t *tmov = malloc(sizeof(node_t));
  printf("Enter the data value of the new last node: ");
  scanf("%d", &d);
  tmov->data = d;
  tmov->link = NULL;
  while (ptr->link != NULL){
    ptr = ptr->link;
  }
  ptr->link = tmov;
}
