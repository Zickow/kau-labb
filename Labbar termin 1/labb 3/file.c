// Exercise 3 – Vehicle Registry
// Student 1: Zakaria Bouchaoui
// Student 2: Elias Bouchaoui

#include <stdio.h>
#include <string.h>
#include "file.h"

#define FILENAME "registry.txt"

int load_registry(vehicle registry[], int max_vehicles) {
    FILE *fp = fopen(FILENAME, "r");
    if (!fp) return 0;
    
    int count = 0;
    while (count < max_vehicles &&
           fscanf(fp, "%19[^,],%49[^,],%49[^,],%d\n",
                  registry[count].regnr,
                  registry[count].model,
                  registry[count].owner.name,
                  &registry[count].owner.age) == 4) {
        count++;
    }
    fclose(fp);
    return count;
}

void save_registry(vehicle registry[], int vehicle_count) {
    FILE *fp = fopen(FILENAME, "w");
    if (!fp) {
        printf("Kunde inte öppna filen för skrivning!\n");
        return;
    }
    for (int i = 0; i < vehicle_count; i++) {
        fprintf(fp, "%s;%s;%s;%d\n",
                registry[i].regnr,
                registry[i].model,
                registry[i].owner.name,
                registry[i].owner.age);
    }
    fclose(fp);
}