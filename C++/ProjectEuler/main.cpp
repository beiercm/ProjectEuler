#include <iostream>
#include <linkedlist.h>
#include <queue.h>
#include <problem1.h>
#include <problem2.h>

void printThis(int d)
{
    std::cout<< d << std::endl;
}

int main()
{
    LinkedList *ll = new LinkedList();
    ll->add(5);
    ll->add(6);
    ll->printList();

    Queue *q = new Queue();
    q->add(10);
    q->add(15);
    q->add(16);
    q->printList();
    printThis(q->dequeue());
    q->printList();

    printThis(ll->getSize());
    printThis(q->getSize());


    return 0;
}
