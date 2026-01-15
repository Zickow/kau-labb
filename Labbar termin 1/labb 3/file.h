// Exercise 3 – Vehicle Registry
// Student 1: Zakaria Bouchaoui
// Student 2: Elias Bouchaoui

#ifndef FILE_H
#define FILE_H



typedef struct {
    char name [50];
    int age;
} person;

typedef struct {
    char regnr[20];
    char model[50];
    person owner;
} vehicle;

int load_registry(vehicle registry[], int max_vehicles);
void save_registry(vehicle registry[], int vehicle_count);

#endif