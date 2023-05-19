#include "list.h"

void count_node(node_t *head){
  node_t *ptr = head;
  int count = 0;
  while (ptr != NULL){
    count++;
    ptr = ptr->link;
  }
  printf("%d", count);
}
