#include "linkedlist.h"
#include "node.h"
#include <iostream>

LinkedList::LinkedList()
{
    size = 0;
    head = 0;
    tail = 0;
}

int LinkedList::getSize()
{
    return size;
}

void LinkedList::setSize(int n)
{
    size = n;
}

void LinkedList::add(int d)
{
    if(head == 0)
    {
        head = new Node(d);
        tail = head;
    }
    else
    {
        tail->next = new Node(d);
        tail = tail->next;
    }

    setSize(getSize() + 1);
}

void LinkedList::printList()
{
    Node *curNode = head;

    //std::cout << "\n";

    while(curNode != 0)
    {
        std::cout << curNode->getData() << std::endl;
        curNode = curNode->next;
    }

    std::cout << "\n\n";
}
