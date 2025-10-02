CC = gc
CFLAGS = -Wall -std=c99

all: main

main: main.o file.o
$(CC) $(CFLAGS) -o main main.o file.o

main.o: main.c file.h
$(cc) $(CFLAGS) -c main.c

file.o: file.c file.h
$(CC) $(CFLAGS) -c file.c99

clean:
rm -f *.o main
