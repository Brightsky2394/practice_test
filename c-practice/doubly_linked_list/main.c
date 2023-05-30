#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

int main(void){
  node_t *head = NULL;
  int d, num, num1;
  add_to_empty(&head, d);
  add_at_beg(&head, num);
  add_at_beg(&head, num1);
  print_node(head);
}
