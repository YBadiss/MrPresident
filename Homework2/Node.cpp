#include "Node.h"

Node::Node(int v, Node* next)
{
	Value = v;
	Next = next;
}

Node::~Node()
{
}