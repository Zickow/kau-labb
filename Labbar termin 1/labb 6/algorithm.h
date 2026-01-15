#include <stdio.h>    //Zakaria Bouchaoui , Elias Bouchaoui
#include <stdbool.h>

// Bubble Sort
void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

// Insertion Sort
void insertion_sort(int *arr, int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Quick Sort helper (partition)
static int partition(int *arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
    int tmp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = tmp;
    return i + 1;
}

// Quick Sort


// Quick Sort helper (recursive)
static void quick_sort_rec(int *arr, int low, int high) {
    if (low < high) {
        int p = partition(arr, low, high);
        quick_sort_rec(arr, low, p - 1);
        quick_sort_rec(arr, p + 1, high);
    }
}

// Quick Sort
void quick_sort(int *arr, int n) {
    quick_sort_rec(arr, 0, n - 1);
}




// Linear Search
bool linear_search(const int *arr, int n, int v) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == v) return true;
    }
    return false;
}

// Binary Search (array must be sorted)
bool binary_search(const int *arr, int n, int v) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == v) return true;
        else if (arr[mid] < v) low = mid + 1;
        else high = mid - 1;
    }
    return false;
}
