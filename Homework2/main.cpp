#include "LinkedList.h"
#include "Watch.h"
#include <cmath>

using namespace std;

int main(void)
{
	LinkedList list;
	Watch time_watch;

	unsigned int start = 0;
	unsigned int end = pow(2,5);
	unsigned int limit = pow(2,28);
	unsigned int no_iteration = 5;
	int nb_loop = 100;

	double elapsed = 0;

	while(end <= limit)
	{
		cout << "2^" << no_iteration << " = " << end << " :\n";

		time_watch.StartWatch();
		for(unsigned int i = start; i < end; i++)
		{
			list.AddNode(0);
		}
		elapsed = time_watch.ElapsedTime();
		cout << "\tList built in " << elapsed << " seconds\n";

		// cout << list << endl;

		time_watch.StartWatch();
		for (int j = 0; j < nb_loop; j++)
		{
			for (Node* n = list.GetHead(); n != nullptr; n = n->GetNext())
			{

			}
		}
		elapsed = time_watch.ElapsedTime();
		cout << "\tList traversed in " << elapsed / nb_loop << " seconds\n";
		cout << "\tTime per element is " << (elapsed / nb_loop) / end << " seconds\n";

		start = end;
		end *= 2;
		no_iteration++;
	}
	
	return 0;
}