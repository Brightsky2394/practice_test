#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

int main(void){
  node_t *head = NULL;
  int d, num, num1, val, val1, pos, d1;
  add_to_empty(&head, d);
  add_at_beg(&head, num);
  add_at_beg(&head, num1);
  add_at_end(&head, val);
  add_at_end(&head, val1);
  add_at_pos(&head, d1, pos);
  print_node(head);
}
