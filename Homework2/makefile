CC=g++ -std=c++11
CFLAGS=-c -Wall

all: main

main: main.o LinkedList.o Node.o Watch.o
	$(CC) main.o LinkedList.o Node.o Watch.o -o main.out

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

LinkedList.o: LinkedList.cpp Node.o
	$(CC) $(CFLAGS) LinkedList.cpp

Node.o: Node.cpp
	$(CC) $(CFLAGS) Node.cpp

Watch.o: Watch.cpp
	$(CC) $(CFLAGS) Watch.cpp

test: test.o
	$(CC) test.o -o test.out

test.o: test.cpp
	$(CC) $(CFLAGS) test.cpp

clean:
	rm -rf *.o main.out test.out