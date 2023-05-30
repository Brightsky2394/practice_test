#include "list.h"

void add_to_empty(node_t **head, int data){
  node_t *trf = malloc(sizeof(node_t));
  trf->prev = NULL;
  printf("Enter the data value of node: ");
  scanf("%d", &data);
  trf->data = data;
  trf->next = NULL;
  *head = trf;
}
