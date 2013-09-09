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
double GlobalElapsed;

Watch time_watch;

void init()
{
	GlobalStart = 0;
	GlobalEnd = pow(2,5);
	GlobalLimit = pow(2,28);
	GlobalNoIteration = 5;
	GlobalElapsed = 0;
}

void createFile(string name)
{
	ofstream outFile("results_" + name + ".csv", ios::out);
	outFile << "power_of_2;time_traversing_list;time_per_node;" << endl;
	outFile.close();
}

void writeResults(string name, unsigned int iteration, unsigned int size)
{
	ofstream outFile("results_" + name + ".csv", ios::out | ios::app);
	outFile << iteration << ";" << GlobalElapsed << ";" << GlobalElapsed / size << ";" << endl;
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

	
	double nbLoop = pow(2,28-GlobalNoIteration);

	time_watch.StartWatch();
	for (unsigned int j = 0; j < nbLoop; j++)
	{
		for (int i = 0; array[i] != -1; i = array[i])
		{
		}
	}
	GlobalElapsed = (double) (time_watch.ElapsedTime() / nbLoop);

	writeResults(name, GlobalNoIteration, size);

	cout << "\tArray traversed in " << GlobalElapsed << " seconds\n";
	cout << "\tTime per element is " << GlobalElapsed / size << " seconds\n";
}

void randomArrayTraversal()
{
	init();
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
	init();
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

void singleSizeStrideArrayTraversal(unsigned int size)
{
	init();
	string name = "array_stride_single";
	createFile(name);

	for (int power = 1; power < 20; power++)
	{
		unsigned int stride = 1 << power;
		unsigned int nbLoop = 10;
		int* array = createArray(size, stride);
		cout << "2^" << power << " = " << stride << " :\n";

		time_watch.StartWatch();
		for (unsigned int j = 0; j < nbLoop; j++)
		{
			for (int i = 0; array[i] != -1; i = array[i])
			{
			}
		}
		GlobalElapsed = (double) (time_watch.ElapsedTime() / nbLoop);

		writeResults(name, power, size);

		cout << "\tArray traversed in " << GlobalElapsed << " seconds\n";
		cout << "\tTime per element is " << GlobalElapsed / size << " seconds\n";
		delete array;
	}
}

void listTraversal()
{
	init();
	LinkedList list;
	string name = "list";

	createFile(name);
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

		time_watch.StartWatch();
		double nbLoop = pow(2,28-GlobalNoIteration);
		for (unsigned int j = 0; j < nbLoop; j++)
		{
			for (Node* n = list.GetHead(); n != nullptr; n = n->GetNext())
			{

			}
		}
		GlobalElapsed = (double) (time_watch.ElapsedTime() / nbLoop);

		writeResults(name, GlobalNoIteration, GlobalEnd);

		cout << "\tList traversed in " << GlobalElapsed << " seconds\n";
		cout << "\tTime per element is " << GlobalElapsed / GlobalEnd << " seconds\n";

		GlobalStart = GlobalEnd;
		GlobalEnd *= 2;
		GlobalNoIteration++;
	}
}

int main(void)
{
	srand (time(NULL));

	singleSizeStrideArrayTraversal(1 << 25);

	// list
	// listTraversal();

	// Regular array
	strideArrayTraversal(0);
	for (int i = 1; i < 20; i++)
	{
		// Srided array by 2^i
		strideArrayTraversal(1 << i);
	}

	// Random array
	randomArrayTraversal();

	return 0;
}
