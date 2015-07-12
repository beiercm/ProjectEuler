#ifndef QUEUE_H
#define QUEUE_H
#include "linkedlist.h"


class Queue: public LinkedList
{
    int size;
public:
    Queue();
    //int peek();
    int dequeue();
    //void enqueue(int);
};

#endif // QUEUE_H
