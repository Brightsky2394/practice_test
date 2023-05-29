#include "list.h"

void del_pos(node_t **head, int pos){
  printf("Enter the position of node to be deleted: ");
  scanf("%d", &pos);
  node_t *prev = *head;
  node_t *curr = *head;
  if (*head == NULL)
    printf("Linked list is already empty");
  else if (pos == 1){
    *head = (*head)->link;
    free(curr);
    curr = NULL;
  }
  else{
    while (pos != 1){
      prev = curr;
      curr = curr->link;
      pos--;
    }
    prev->link = curr->link;
    free(curr);
    curr = NULL;
  }
  
}
