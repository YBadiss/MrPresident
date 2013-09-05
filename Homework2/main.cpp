#include "LinkedList.h"

using namespace std;

int main(void)
{
	LinkedList list;

	list.AddNode(1);
	list.AddNode(2);
	list.AddNode(3);
	list.AddNode(4);

	cout << list << endl;

	return 0;
}