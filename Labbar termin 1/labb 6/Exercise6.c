#include <stdio.h>
#include "algorithm.h"
#include "util.h"

//
// Private (om du behöver helper-funktioner)
//
static int partition(int *a, int low, int high) {
    int pivot = a[high];
    int i = low - 1;
    int temp;

    for (int j = low; j < high; j++) {
        if (a[j] <= pivot) {
            i++;
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
    }

    temp = a[i + 1];
    a[i + 1] = a[high];
    a[high] = temp;

    return i + 1;
}

static void quick_sort_rec(int *a, int low, int high) {
    if (low < high) {
        int pi = partition(a, low, high);
        quick_sort_rec(a, low, pi - 1);
        quick_sort_rec(a, pi + 1, high);
    }
}

//
// Public
//

// -------------------
// Bubble Sort
// -------------------
void bubble_sort(int *a, int n)
{
    int temp;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }
}

// -------------------
// Insertion Sort
// -------------------
void insertion_sort(int *a, int n)
{
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

// -------------------
// Quick Sort
// -------------------
void quick_sort(int *a, int n)
{
    quick_sort_rec(a, 0, n - 1);
}

// -------------------
// Linear Search
// -------------------
bool linear_search(const int *a, int n, int v)
{
    for (int i = 0; i < n; i++) {
        if (a[i] == v)
            return true;
    }
    return false;
}

// -------------------
// Binary Search
// -------------------
bool binary_search(const int *a, int n, int v)
{
    int left = 0;
    int right = n - 1;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (a[mid] == v)
            return true;
        else if (a[mid] < v)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return false;
}
