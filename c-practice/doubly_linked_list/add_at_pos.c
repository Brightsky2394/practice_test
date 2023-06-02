#include "list.h"

void add_at_pos(node_t **head, int d, int pos){
  node_t *trv = *head;
  node_t *brf;
  node_t *new_node = malloc(sizeof(node_t));
  printf("Enter the data value and position of the new node: ");
  scanf("%d %d", &d, &pos);
  new_node->data = d;
  new_node->prev = NULL;
  new_node->next = NULL;
  while (pos != 1){
    trv = trv->next;
    pos--;
  }
  if (trv->next == NULL){
    trv->next = new_node;
    new_node->prev = trv->prev;
  }
  else{
    brf = trv->next;
    trv->next = new_node;
    brf->prev = new_node;
    new_node->prev = trv->prev;
    new_node->next = brf;
  }
}
