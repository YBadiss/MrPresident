#ifndef WATCH_H
#define WATCH_H

#include <ctime>

class Watch
{
private:
	clock_t StartTime;

public:
	Watch();

	inline void StartWatch() { StartTime = clock(); }
	inline double ElapsedTime() { return ((double)(clock() - StartTime))/CLOCKS_PER_SEC; }

	~Watch();
};

#endif