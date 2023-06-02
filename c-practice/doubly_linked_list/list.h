#ifndef LIST_H
#define LIST_H
#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct node{
  struct node *prev;
  int data;
  struct node *next;
} node_t;

void add_to_empty(node_t **head, int data);
void print_node(node_t *head);
void add_at_beg(node_t **head, int d);
void add_at_end(node_t **head, int d);
void add_at_pos(node_t **head, int d, int pos);
#endif

