#include "node.h"

Node::Node()
{
}

Node::Node(int d)
{
    data = d;
    next = 0;
}

int Node::getData()
{
    return data;
}
