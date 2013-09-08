#include "LinkedList.h"
#include "Watch.h"
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime> 

using namespace std;

unsigned int GlobalStart;
unsigned int GlobalEnd;
unsigned int GlobalLimit;
unsigned int GlobalNoIteration;
unsigned int GlobalNbLoop;
double GlobalElapsed;

Watch time_watch;

void init()
{
	GlobalStart = 0;
	GlobalEnd = pow(2,5);
	GlobalLimit = pow(2,28);
	GlobalNoIteration = 5;
	GlobalNbLoop = 100;
	GlobalElapsed = 0;
}

void createFile(string name)
{
	ofstream outFile("results_" + name, ios::out);
	outFile << "power_of_2;time_traversing_list;time_per_node;" << endl;
	outFile.close();
}

void writeResults(string name)
{
	ofstream outFile("results_" + name, ios::out | ios::app);
	outFile << GlobalNoIteration << ";" << GlobalElapsed << ";" << GlobalElapsed / GlobalEnd << ";" << endl;
	outFile.close();
} 

int* createArray(unsigned int size, unsigned int stride = 0)
{
	int* array = new int[size];
	int value = stride + 1;
	for(unsigned int i = 1; i < size; i++)
	{
		value = value % size;
		if (value == 0) value = 1;
		array[i-1] = value++;
	}
	array[size-1] = -1;
	return array;
}

int* createRandomArray(unsigned int size)
{
	int* array = new int[size];
	array[size-1] = -1;

	int* temp = new int[size-2];
	for (unsigned int i = 0; i < size-2; i++)
	{
		temp[i] = i+1;
	}

	int current = 0;
	for (unsigned int i = 0; i < size-2; i++)
	{
		unsigned int r = (rand() % (size-2-i)) + i;
		
		int t = temp[i];
		temp[i] = temp[r];
		temp[r] = t;

		array[current] = temp[i];
		current = temp[i];
	}
	array[current] = size-1;
	return array;
}

void arrayTraversal(int* array, unsigned int size, string name)
{
	cout << "2^" << GlobalNoIteration << " = " << GlobalEnd << " :\n";

	time_watch.StartWatch();
	
	//double nbLoop = pow(2,28-GlobalNoIteration);
	double nbLoop = 10;
	for (unsigned int j = 0; j < nbLoop; j++)
	{
		for (int i = 0; array[i] != -1; i = array[i])
		{
		}
	}
	GlobalElapsed = (double) (time_watch.ElapsedTime() / nbLoop);

	writeResults(name);

	cout << "\tArray traversed in " << GlobalElapsed << " seconds\n";
	cout << "\tTime per element is " << GlobalElapsed / size << " seconds\n";
}

void listTraversal()
{
	LinkedList list;

	createFile("list");
	while(GlobalEnd <= GlobalLimit)
	{
		cout << "2^" << GlobalNoIteration << " = " << GlobalEnd << " :\n";

		time_watch.StartWatch();
		for(unsigned int i = GlobalStart; i < GlobalEnd; i++)
		{
			list.AddNode(0);
		}
		GlobalElapsed = time_watch.ElapsedTime();
		cout << "\tList built in " << GlobalElapsed << " seconds\n";

		// cout << list << endl;

		time_watch.StartWatch();
		for (unsigned int j = 0; j < GlobalNbLoop; j++)
		{
			for (Node* n = list.GetHead(); n != nullptr; n = n->GetNext())
			{

			}
			if (GlobalNoIteration >= 25) break;
		}
		GlobalElapsed = (double) (time_watch.ElapsedTime() / (double)((GlobalNoIteration >= 25) ? 1 : GlobalNbLoop));

		writeResults("list");

		cout << "\tList traversed in " << GlobalElapsed << " seconds\n";
		cout << "\tTime per element is " << GlobalElapsed / GlobalEnd << " seconds\n";

		GlobalStart = GlobalEnd;
		GlobalEnd *= 2;
		GlobalNoIteration++;
	}
}

void randomArrayTraversal()
{
	createFile("array_rand");

	while (GlobalEnd <= GlobalLimit)
	{
		int* array = createRandomArray(GlobalEnd);
		arrayTraversal(array, GlobalEnd, "array_rand");

		GlobalStart = GlobalEnd;
		GlobalEnd *= 2;
		GlobalNoIteration++;

		delete array;
	}
}

void strideArrayTraversal(unsigned int stride)
{
	string name = "array_stride_" + to_string(stride);
	createFile(name);

	while (GlobalEnd <= GlobalLimit)
	{
		int* array = createArray(GlobalEnd, stride);
		arrayTraversal(array, GlobalEnd, name);

		GlobalStart = GlobalEnd;
		GlobalEnd *= 2;
		GlobalNoIteration++;

		delete array;
	}
}

int main(void)
{
	srand (time(NULL));
	init();

	strideArrayTraversal(0);
	for (int i = 1; i < 20; i++)
	{
		init();
		strideArrayTraversal(1 << i);
	}

	return 0;
}

