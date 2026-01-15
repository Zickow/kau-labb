// Exercise 3 – Vehicle Registry
// Student 1: Zakaria Bouchaoui
// Student 2: Elias Bouchaoui


#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_VEHICLES 10
#define FILENAME "registry.txt"
#define MAX_BRANDS 5
#define MAX_NAMES 5
#define MAX_BRAND_LEN 10
#define MAX_NAME_LEN 10
#define REG_LEN 20
#define MAX_RANDOM_REG 100
#define MIN_OWNER_AGE 18
#define MAX_OWNER_AGE 68  // 18 + 50

typedef struct {
    char name[50];
    int age;
} person;

typedef struct {
    char regnr[20];
    char model[50];
    person owner;
} vehicle;

// Hjälpfunktion för säker strängkopiering
void safe_strcpy(char *dest, const char *src, int max_len) {
    strncpy(dest, src, max_len - 1);
    dest[max_len - 1] = '\0';
}

// Hjälpfunktion för ålder-validering
int validate_age(int age) {
    return (age >= MIN_OWNER_AGE && age <= MAX_OWNER_AGE);
}

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
    if (*vehicle_count >= MAX_VEHICLES) {
        printf("Registret är fullt!\n");
        return;
    }
    
    if (!validate_age(owner_age)) {
        printf("Åldern måste vara mellan %d och %d år.\n", MIN_OWNER_AGE, MAX_OWNER_AGE);
        return;
    }
    
    safe_strcpy(registry[*vehicle_count].regnr, regnr, 20);
    safe_strcpy(registry[*vehicle_count].model, model, 50);
    safe_strcpy(registry[*vehicle_count].owner.name, owner_name, 50);
    registry[*vehicle_count].owner.age = owner_age;
    (*vehicle_count)++;
    printf("Fordon lagt till!\n");
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
    char brands[MAX_BRANDS][MAX_BRAND_LEN] = {"Volvo", "BMW", "Audi", "Ford", "Tesla"};
    char names[MAX_NAMES][MAX_NAME_LEN] = {"Anna", "Bjorn", "Cecilia", "David", "Elin"};
    char reg[REG_LEN];
    sprintf(reg, "ABC%02d", rand() % MAX_RANDOM_REG);

    add_vehicle(registry, vehicle_count, reg,
                brands[rand() % MAX_BRANDS],
                names[rand() % MAX_NAMES],
                MIN_OWNER_AGE + rand() % (MAX_OWNER_AGE - MIN_OWNER_AGE + 1));
}

// ---------------- Main ----------------

int main() {
    srand(time(NULL));  // Initialize random seed
    
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
        
        if (scanf("%d", &choice) != 1) {
            while (getchar() != '\n');  // Clear invalid input
            printf("Ogiltig inmatning!\n");
            continue;
        }
        getchar();

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
            if (scanf("%d", &owner_age) != 1) {
                while (getchar() != '\n');
                printf("Ogiltig ålder!\n");
            } else {
                getchar();
                add_vehicle(registry, &vehicle_count, regnr, model, owner_name, owner_age);
            }
        }
        else if (choice == 2) {
            print_vehicles(registry, vehicle_count);
        }
        else if (choice == 3) {
            int pos;
            printf("Ange fordonets position att ta bort (1-%d): ", vehicle_count);
            if (scanf("%d", &pos) == 1) {
                getchar();
                remove_vehicle(registry, &vehicle_count, pos - 1);
            } else {
                while (getchar() != '\n');
                printf("Ogiltig inmatning!\n");
            }
        }
        else if (choice == 4) {
            sort_registry(registry, vehicle_count);
        }
        else if (choice == 5) {
            int pos;
            printf("Ange position att visa (1-%d): ", vehicle_count);
            if (scanf("%d", &pos) == 1) {
                getchar();
                if (pos >= 1 && pos <= vehicle_count) {
                    print_vehicle(registry[pos - 1], pos - 1);
                } else {
                    printf("Ogiltig position!\n");
                }
            } else {
                while (getchar() != '\n');
                printf("Ogiltig inmatning!\n");
            }
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
            if (idx != -1) {
                print_vehicle(registry[idx], idx);
            } else {
                printf("Ingen fordon hittades med den ägaren.\n");
            }
        }

    } while (choice != 0);

    save_registry(registry, vehicle_count);
    printf("Registret har sparats.\n");
    return 0;
}
