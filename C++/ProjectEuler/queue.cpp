#include "queue.h"
#include <iostream>

Queue::Queue()
{
    size = 0;
    head = 0;
}

int Queue::dequeue()
{
    Node *curNode = head;
    int data = curNode->getData();
    head = head->next;
    delete curNode;
    setSize(getSize() - 1);
    return data;
}


