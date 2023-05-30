#include "list.h"

void add_at_beg(node_t **head, int d){
  node_t *temp = malloc(sizeof(node_t));
  temp->prev = NULL;
  printf("Enter the data value of the new first node: ");
  scanf("%d", &d);
  temp->data = d;
  temp->next = NULL;
  temp->next = *head;
  (*head)->prev = temp;
  *head = temp;
}
