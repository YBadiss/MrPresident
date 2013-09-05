#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <iostream>
#include "Node.h"
using namespace std;

class LinkedList
{
private:
	Node* Head;
	Node* End;

public:
	LinkedList();

	inline Node* GetHead() { return Head; }
	inline bool IsEmpty() { return Head == nullptr; }

	void AddNode(int v);

	friend ostream& operator<<(ostream& os, const LinkedList& list);

	~LinkedList();
};

#endif