#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_VEHICLES 10
#define FILENAME "registry.txt"

typedef struct {
    char name[50];
    int age;
} person;

typedef struct {
    char regnr[20];
    char model[50];
    person owner;
} vehicle;

// ---------------- Funktioner ----------------

void print_vehicle(vehicle v, int index) {
    printf("Fordon %d: %s, %s, Ägare: %s, %d år\n",
           index + 1,
           v.regnr,
           v.model,
           v.owner.name,
           v.owner.age);
}

void print_vehicles(vehicle registry[], int vehicle_count) {
    if (vehicle_count == 0) {
        printf("Inga fordon i registret.\n");
        return;
    }
    for (int i = 0; i < vehicle_count; i++) {
        print_vehicle(registry[i], i);
    }
}

void add_vehicle(vehicle registry[], int *vehicle_count, char regnr[], char model[], char owner_name[], int owner_age) {
    if (*vehicle_count < MAX_VEHICLES) {
        strcpy(registry[*vehicle_count].regnr, regnr);
        strcpy(registry[*vehicle_count].model, model);
        strcpy(registry[*vehicle_count].owner.name, owner_name);
        registry[*vehicle_count].owner.age = owner_age;
        (*vehicle_count)++;
        printf("Fordon lagt till!\n");
    } else {
        printf("Registret är fullt!\n");
    }
}

void remove_vehicle(vehicle registry[], int *vehicle_count, int index) {
    if (index >= 0 && index < *vehicle_count) {
        for (int i = index; i < *vehicle_count - 1; i++) {
            registry[i] = registry[i + 1];
        }
        (*vehicle_count)--;
        printf("Fordon borttaget!\n");
    } else {
        printf("Ogiltig position!\n");
    }
}

void sort_registry(vehicle registry[], int vehicle_count) {
    for (int i = 0; i < vehicle_count - 1; i++) {
        for (int j = 0; j < vehicle_count - i - 1; j++) {
            if (strcmp(registry[j].owner.name, registry[j + 1].owner.name) > 0) {
                vehicle temp = registry[j];
                registry[j] = registry[j + 1];
                registry[j + 1] = temp;
            }
        }
    }
    printf("Registret har sorterats efter ägarens namn.\n");
}

int binary_search_owner(vehicle registry[], int vehicle_count, char *owner) {
    int left = 0, right = vehicle_count - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        int cmp = strcmp(registry[mid].owner.name, owner);
        if (cmp == 0) return mid;
        else if (cmp < 0) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int load_registry(vehicle registry[]) {
    FILE *fp = fopen(FILENAME, "r");
    if (!fp) return 0;

    int count = 0;
    while (fscanf(fp, "%19[^,],%49[^,],%49[^,],%d\n",
                  registry[count].regnr,
                  registry[count].model,
                  registry[count].owner.name,
                  &registry[count].owner.age) == 4) {
        count++;
        if (count >= MAX_VEHICLES) break;
    }
    fclose(fp);
    return count;
}

void save_registry(vehicle registry[], int vehicle_count) {
    FILE *fp = fopen(FILENAME, "w");
    if (!fp) {
        printf("Kunde inte spara registret!\n");
        return;
    }
    for (int i = 0; i < vehicle_count; i++) {
        fprintf(fp, "%s,%s,%s,%d\n",
                registry[i].regnr,
                registry[i].model,
                registry[i].owner.name,
                registry[i].owner.age);
    }
    fclose(fp);
}

// Enkel random-generator för övning
void add_random_vehicle(vehicle registry[], int *vehicle_count) {
    char brands[5][10] = {"Volvo", "BMW", "Audi", "Ford", "Tesla"};
    char names[5][10] = {"Anna", "Bjorn", "Cecilia", "David", "Elin"};
    char reg[20];
    sprintf(reg, "ABC%02d", rand() % 100);

    add_vehicle(registry, vehicle_count, reg, brands[rand() % 5], names[rand() % 5], 18 + rand() % 50);
}

// ---------------- Main ----------------

int main() {
    vehicle registry[MAX_VEHICLES];
    int vehicle_count = load_registry(registry);
    printf("%d fordon laddades från fil.\n", vehicle_count);

    int choice;
    char regnr[20], model[50], owner_name[50];
    int owner_age;

    do {
        printf("\nMeny:\n");
        printf("1. Lägg till fordon\n");
        printf("2. Visa alla fordon\n");
        printf("3. Ta bort fordon\n");
        printf("4. Sortera registret\n");
        printf("5. Visa ett fordon\n");
        printf("6. Lägg till slumpmässigt fordon\n");
        printf("7. Sök efter ägare\n");
        printf("0. Avsluta\nVal: ");
        scanf("%d", &choice);
        getchar(); // rensa newline

        if (choice == 1) {
            printf("Registreringsnummer: ");
            fgets(regnr, 20, stdin);
            strtok(regnr, "\n");
            printf("Modell: ");
            fgets(model, 50, stdin);
            strtok(model, "\n");
            printf("Ägarens namn: ");
            fgets(owner_name, 50, stdin);
            strtok(owner_name, "\n");
            printf("Ägarens ålder: ");
            scanf("%d", &owner_age);
            getchar();
            add_vehicle(registry, &vehicle_count, regnr, model, owner_name, owner_age);
        }
        else if (choice == 2) {
            print_vehicles(registry, vehicle_count);
        }
        else if (choice == 3) {
            int pos;
            printf("Ange fordonets position att ta bort (1-%d): ", vehicle_count);
            scanf("%d", &pos);
            getchar();
            remove_vehicle(registry, &vehicle_count, pos - 1);
        }
        else if (choice == 4) {
            sort_registry(registry, vehicle_count);
        }
        else if (choice == 5) {
            int pos;
            printf("Ange position att visa (1-%d): ", vehicle_count);
            scanf("%d", &pos);
            getchar();
            if (pos >= 1 && pos <= vehicle_count) print_vehicle(registry[pos-1], pos-1);
            else printf("Ogiltig position!\n");
        }
        else if (choice == 6) {
            add_random_vehicle(registry, &vehicle_count);
        }
        else if (choice == 7) {
            char search_name[50];
            printf("Ange ägarens namn att söka efter: ");
            fgets(search_name, 50, stdin);
            strtok(search_name, "\n");
            sort_registry(registry, vehicle_count);
            int idx = binary_search_owner(registry, vehicle_count, search_name);
            if (idx != -1) print_vehicle(registry[idx], idx);
            else printf("Ingen fordon hittades med den ägaren.\n");
        }

    } while (choice != 0);

    save_registry(registry, vehicle_count);
    printf("Registret har sparats.\n");
    return 0;
}
