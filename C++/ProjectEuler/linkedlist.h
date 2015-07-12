#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include <node.h>

class LinkedList
{
    int size;
protected:
    Node *head, *tail;
public:
    LinkedList();
    int getSize();
    void setSize(int);
    void add(int);
    void printList();
};


#endif // LINKEDLIST_H
