CC=g++ -std=c++11
CFLAGS=-c -Wall

all: main

main: main.o LinkedList.o Node.o
	$(CC) main.o LinkedList.o Node.o -o main.out

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

LinkedList.o: LinkedList.cpp Node.o
	$(CC) $(CFLAGS) LinkedList.cpp

Node.o: Node.cpp
	$(CC) $(CFLAGS) Node.cpp

clean:
	rm -rf *.o main