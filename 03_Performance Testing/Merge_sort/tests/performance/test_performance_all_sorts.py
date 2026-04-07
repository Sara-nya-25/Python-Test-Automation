import time
import random
import pytest
import matplotlib.pyplot as plt
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from bubble_sort import bubble_sort

@pytest.mark.performance
def test_run_benchmarks():
    sizes = [100, 500, 1000, 1500, 2000, 2500, 3000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    results = {name: [] for name in algorithms}

    print(f"{'N':<10} | {'Bubble':<10} | {'Insert':<10} | {'Merge':<10} | {'Quick':<10}")
    print("-" * 60)

    for n in sizes:
        # Generate the exact same random list for all 4 algorithms
        test_data = [random.randint(0, 10000) for _ in range(n)]
        row = [f"{n:<10}"]

        for name, func in algorithms.items():
            start = time.perf_counter()
            func(test_data.copy())
            end = time.perf_counter()

            duration_ms = (end - start) * 1000
            results[name].append(duration_ms)
            row.append(f"{duration_ms:>8.2f}ms")

        print(" | ".join(row))

    # --- Plotting ---
    plt.figure(figsize=(12, 7))
    for name, times in results.items():
        plt.plot(sizes, times, label=name, marker='o')

    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("List Size (n)")
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)

    # Use 'r' to avoid unicode escape errors on Windows
    plt.savefig("all_sorts_comparison.png")
    plt.show()


if __name__ == "__main__":
    test_run_benchmarks()

"""

tests/performance/test_performance_all_sorts.py::test_run_benchmarks N          | Bubble     | Insert     | Merge      | Quick     
------------------------------------------------------------
100        |     0.72ms |     0.35ms |     0.29ms |     0.27ms
500        |    21.35ms |     9.13ms |     1.82ms |     1.46ms
1000       |    91.28ms |    36.63ms |     3.65ms |     2.89ms
1500       |   207.24ms |    81.53ms |     6.12ms |     4.43ms
2000       |   370.06ms |   147.62ms |     7.86ms |     6.70ms
2500       |   628.39ms |   232.96ms |    10.29ms |     7.24ms
3000       |   850.65ms |   344.02ms |    13.24ms |     9.95ms
PASSED

"""
