#include "list.h"

void del_last(node_t *head){
  node_t *trf = head;
  while (trf->link->link != NULL){
    trf = trf->link;
  }
  free(trf->link);
  trf->link = NULL;
}
