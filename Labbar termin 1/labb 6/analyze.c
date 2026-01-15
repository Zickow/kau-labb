#include "analyze.h"
#include "algorithm.h"
#include "util.h"

#include <stdio.h>
#include <time.h>
#include <stdbool.h>

//
// Private
//
typedef void (*init_func)(int *, int);
typedef void (*sort_func)(int *, int);
typedef bool (*search_func)(const int *, int, int);
typedef int (*target_func)(const int *, int);

static void bench_sort(init_func init, sort_func sort, result_t *buf, int n)
{
	int i, j, size, a[SIZE_START << n];
	time_t start, stop;
	double elapsed;
	
	size = SIZE_START;
	for (i=0; i<n; i++) {
		elapsed = 0;
		for (j=0; j<ITERATIONS; j++) {
			init(a, size);
			start = clock();
			sort(a, size);
			stop = clock();
			elapsed += (double)(stop-start) / CLOCKS_PER_SEC;
		}
		buf[i].size = size;
		buf[i].time = elapsed/ITERATIONS;
		size *= 2;
	}
}

void bench_search(search_func search, init_func init, target_func target,
	result_t *buf, int n)
{
	int i, j, size, value, a[SIZE_START << n];
	time_t start, stop;
	double elapsed;
	
	size = SIZE_START;
	for (i=0; i<n; i++) {
		elapsed = 0;
		for (j=0; j<ITERATIONS; j++) {
			init(a, size);
			value = target(a, size);
			start = clock();
			search(a, size, value);
			stop = clock();
			elapsed += (double)(stop-start) / CLOCKS_PER_SEC;
		}
		buf[i].size = size;
		buf[i].time = elapsed/ITERATIONS;
		size *= 2;
	}
}

static void benchmark_bubble_sort(const case_t c, result_t *buf, int n)
{
	if (c == best_t) {
		bench_sort(init_ascending, bubble_sort, buf, n);
	} else if (c == worst_t) {
		bench_sort(init_descending, bubble_sort, buf, n);
	} else {
		bench_sort(init_random, bubble_sort, buf, n);
	}
}

static void benchmark_insertion_sort(const case_t c, result_t *buf, int n)
{
	if (c == best_t) {
		bench_sort(init_ascending, insertion_sort, buf, n);
	} else if (c == worst_t) {
		bench_sort(init_descending, insertion_sort, buf, n);
	} else {
		bench_sort(init_random, insertion_sort, buf, n);
	}
}

static void benchmark_quick_sort(const case_t c, result_t *buf, int n)
{
	if (c == best_t) {
		bench_sort(init_reverse_partition, quick_sort, buf, n);
	} else if (c == worst_t) {
		bench_sort(init_ascending, quick_sort, buf, n);
	} else {
		bench_sort(init_random, quick_sort, buf, n);
	}
}

static void benchmark_linear_search(const case_t c, result_t *buf, int n)
{
	if (c == best_t) {
		bench_search(linear_search, init_ascending, first_value, buf, n);
	} else if (c == worst_t) {
		bench_search(linear_search, init_ascending, last_value, buf, n);
	} else {
		bench_search(linear_search, init_random, random_value, buf, n);
	}
}

static void benchmark_binary_search(const case_t c, result_t *buf, int n)
{
	if (c == best_t) {
		bench_search(binary_search, init_ascending, mid_value, buf, n);
	} else if (c == worst_t) {
		bench_search(binary_search, init_ascending, last_value, buf, n);
	} else {
		bench_search(binary_search, init_ascending, random_value, buf, n);
	}
}

//
// Public
//
void benchmark(const algorithm_t a, const case_t c, result_t *buf, int n)
{
	switch (a) {
		case bubble_sort_t: benchmark_bubble_sort(c, buf, n); break;
		case insertion_sort_t: benchmark_insertion_sort(c, buf, n); break;
		case quick_sort_t: benchmark_quick_sort(c, buf, n); break;
		case linear_search_t: benchmark_linear_search(c, buf, n); break;
		case binary_search_t: benchmark_binary_search(c, buf, n); break;
	}
}
