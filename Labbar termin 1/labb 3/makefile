# Exercise 3 – Vehicle Registry
# Student 1: Zakaria Bouchaoui
# Student 2: Elias Bouchaoui


CC = gcc
CFLAGS = -Wall -std=c99																												

all: main

main: main.o file.o
	$(CC) $(CFLAGS) -o main main.o file.o

main.o: main.c file.h
	$(CC) $(CFLAGS) -c main.c

file.o: file.c file.h
	$(CC) $(CFLAGS) -c file.c

clean:
	rm -f *.o main