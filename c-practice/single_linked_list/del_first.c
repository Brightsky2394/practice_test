#include "list.h"

void del_first(node_t **head){
  node_t *trv = *head;
  *head = (*head)->link;
  free(trv);
  trv = NULL;
}
