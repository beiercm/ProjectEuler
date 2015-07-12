#ifndef NODE_H
#define NODE_H


class Node
{
    int data;
    Node *next;
public:
    friend class LinkedList;
    friend class Queue;
    Node();
    Node(int);
    int getData();
};

#endif // NODE_H
