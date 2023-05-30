#include "list.h"

void print_node(node_t *head){
  node_t *ptr = head;
  while (ptr != NULL){
    printf("%d ", ptr->data);
    ptr = ptr->next;
  }
}
