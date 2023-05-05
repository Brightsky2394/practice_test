#include <stdio.h>
#include <stdlib.h>

typedef struct node{
  int data;
  struct node *link;
} node_t;

node_t *add_to_end(node_t *ptr, int d){
  node_t *trm = malloc(sizeof(node_t));
  printf("Enter the data value of the new last node: ");
  scanf("%d", &trm->data);
  trm->link = NULL;
  ptr->link = trm;
  return trm;
}

node_t *add_to_beg(node_t *head, int d){
  node_t *tem = malloc(sizeof(node_t));
  printf("Enter data value of new node at the beginning of list: ");
  scanf("%d", &tem->data);
  tem->link = NULL;
  tem->link = head;
  head = tem;
  return head;
}
int main(void){
  node_t *head = malloc(sizeof(node_t));
  printf("Enter the data value of the first node: ");
  scanf("%d", &head->data);
  head->link = NULL;
  int num, num1, val, val1;
  node_t *ptr = head;
  head  = add_to_beg(head, num);
  head  = add_to_beg(head, num1);
  ptr = add_to_end(ptr, val);
  ptr = add_to_end(ptr, val1);
  ptr = head;
  while (ptr != NULL){
    printf("%d ", ptr->data);
    ptr = ptr->link;
  }
  return (0);
}
