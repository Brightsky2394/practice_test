#include <stdio.h>
#include <stdlib.h>

typedef struct node{
  int data;
  struct node *link;
} node_t;

node_t *add_to_beg(node_t *head, int d){
  node_t *trv = malloc(sizeof(node_t));
  printf("Enter data value of new first node: ");
  scanf("%d", &trv->data);
  trv->link = NULL;
  trv->link = head;
  head = trv;
  return head;
}

int main(void){
  node_t *head = malloc(sizeof(node_t));
  printf("Enter the data value of the last node: ");
  scanf("%d", &head->data);
  node_t *ptr;
  int val, val1;
  head = add_to_beg(head, val);
  head = add_to_beg(head, val1);
  ptr = head;
  while (ptr != NULL){
    printf("%d", ptr->data);
    ptr = ptr->link;
  }
  return (0);
}
