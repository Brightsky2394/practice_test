#include "list.h"

void add_at_beg(node_t **head, int d){
  node_t *trv = malloc(sizeof(node_t));
  printf("Enter the data value of the first new node: ");
  scanf("%d", &d);
  trv->data = d;
  trv->link = NULL;
  trv->link = *head;
  *head = trv;
}
