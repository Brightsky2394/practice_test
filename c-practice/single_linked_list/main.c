#include "list.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>


int main(void){
    node_t *head = malloc(sizeof(node_t));
    printf("Enter the data value of the initial node: ");
    scanf("%d", &head->data);
    head->link = NULL;
    node_t *ptr = head;
    int val, val1, num, num1, pos, d;
    add_at_beg(&head, val);
    add_at_beg(&head, val1);
    add_at_end(ptr, num);
    add_at_end(ptr, num1);
    add_at_pos(head, d, pos);
    printf("\nLinked list value before the deletion of first node: ");
    print_node(head);
    printf("\nNumber of available node: ");
    count_node(head);
    printf("\nLinked list value after the deletion of first node and last node: ");
    del_first(&head);
    del_last(head);
    print_node(head);
    printf("\nNumber of available node: ");
    count_node(head);
    return (0);
}
