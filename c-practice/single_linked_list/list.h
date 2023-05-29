#ifndef LIST_H
#define LIST_H
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct node{
  int data;
  struct node *link;
} node_t;

void add_at_beg(node_t **head, int d);
void add_at_end(node_t *head, int d);
void add_at_pos(node_t *head, int d, int pos);
void print_node(node_t *head);
void count_node(node_t *head);
void del_first(node_t **head);
void del_last(node_t *head);
void del_pos(node_t **head, int pos);

#endif
