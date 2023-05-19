#include "list.h"

void add_at_pos(node_t *head, int d, int pos){
  node_t *ptr = head;
  node_t *trg = malloc(sizeof(node_t));
  printf("Enter the data value of the inserted node and the position value: ");
  scanf("%d %d", &d, &pos);
  trg->data = d;
  trg->link = NULL;
  while (pos != 2){
    ptr = ptr->link;
    pos--;
  }
  trg->link = ptr->link;
  ptr->link = trg;
}
