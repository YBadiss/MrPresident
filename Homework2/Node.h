#ifndef NODE_H
#define NODE_H

class Node
{
private:
	int Value;
	Node* Next;

public:
	Node(int v, Node* next = nullptr);

	inline int GetValue() { return Value; }
	inline Node* GetNext() { return Next; }

	inline void SetValue(int v) { Value = v; }
	inline void SetNext(Node* next) { Next = next; }
	
	inline bool HasNextNode() { return Next != nullptr; }

	~Node();
};

#endif