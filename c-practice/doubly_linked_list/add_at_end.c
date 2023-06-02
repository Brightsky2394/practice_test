#include "list.h"

void add_at_end(node_t **head, int d){
  node_t *ptr = *head;
  node_t *trv = malloc(sizeof(node_t));
  printf("Enter the data value of the new last node: ");
  scanf("%d", &d);
  trv->prev = NULL;
  trv->data = d;
  trv->next = NULL;
  while (ptr->next != NULL){
    ptr = ptr->next;
  }
  ptr->next = trv;
  trv->prev = ptr->prev;
}
