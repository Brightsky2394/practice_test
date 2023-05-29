#include "list.h"

void del_list(node_t **head){
  node_t *brt = *head;
  while (brt != NULL){
    brt = brt->link;
    free(*head);
    *head = brt;
  }
}
