#include "LinkedList.h"

LinkedList::LinkedList()
{
	Head = nullptr;
	End = nullptr;
}

void LinkedList::AddNode(int v)
{
	if (IsEmpty())
	{
		Head = new Node(v);
		End = Head;
	}
	else
	{
		End->SetNext(new Node(v));
		End = End->GetNext();
	}
}

LinkedList::~LinkedList()
{
	while (!IsEmpty())
	{
		Node* next = Head->GetNext();
		delete Head;
		Head = next;
	}
}

ostream& operator<<(ostream& os, const LinkedList& list)
{
	for (Node* n = list.Head; n != nullptr; n = n->GetNext())
	{
		os << n->GetValue();
		if (n->HasNextNode())
		{
			os << " -> ";
		}
	}
    return os;
}