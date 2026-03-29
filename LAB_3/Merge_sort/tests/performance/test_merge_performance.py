import time
import random
import pytest
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from merge_sort import merge_sort

def generate_list(size):
    return [random.randint(0, 100000) for _ in range(size)]

@pytest.mark.performance
def test_compare_algorithms():
    # We use smaller sizes because Insertion Sort is very slow at high N
    sizes = [500, 1000, 2000, 3000, 4000, 5000]
    insertion_times = []
    merge_times = []

    for n in sizes:
        data = generate_list(n)

        # Benchmark Insertion Sort
        start = time.perf_counter()
        insertion_sort(data.copy())
        insertion_times.append((time.perf_counter() - start) * 1000)

        # Benchmark Merge Sort
        start = time.perf_counter()
        merge_sort(data.copy())
        merge_times.append((time.perf_counter() - start) * 1000)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, insertion_times, label='Insertion Sort (O(n^2))', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort (O(n log n))', marker='s')
    plt.title('Performance Comparison: Insertion vs. Merge Sort')
    plt.xlabel('List Size (n)')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.grid(True)

    # Using 'r' to prevent the unicode error
    plt.savefig(r"tests/performance/comparison_graph.png")
    plt.show()


