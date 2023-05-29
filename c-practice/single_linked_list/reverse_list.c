#include "list.h"

void  reverse_list(node_t **head){
  node_t *prev = NULL;
  node_t *next = NULL;
  while (*head != NULL){
    next = (*head)->link;
    ((*head)->link) = prev;
    prev = *head;
    *head = next;
  }
  *head = prev;
}
