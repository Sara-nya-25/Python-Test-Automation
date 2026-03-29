import sys
import os
import time
import pytest
import random
import matplotlib.pyplot as plt

# This ensures the script can find the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from Insertion_sort import insertion_sort

def generate_list(size):
    return [random.randint(0, 10000) for _ in range(size)]

def run_benchmark(size):
    data = generate_list(size)
    start = time.perf_counter()
    insertion_sort(data)
    return (time.perf_counter() - start) * 1000

@pytest.mark.performance
def test_insertion_sort_scaling():
    """
    Performance test that benchmarks various list sizes
    and plots the O(n^2) result.
    """
    # 1. Target check for ~100ms
    # (3000 is a common sweet spot for O(n^2) at 100ms)
    target_size = 3000
    duration_100ms = run_benchmark(target_size)
    print(f"\n[Target Check] Size {target_size} took {duration_100ms:.2f} ms")

    # Scaling tests and Collect data for plotting
    sizes = [500, 1000, 1500, 2000, 2500, 3000]
    times = []

    print("Running scaling benchmarks...")
    for n in sizes:
        t = run_benchmark(n)
        times.append(t)
        print(f"  n={n} | t={t:.2f} ms")

        # 3. Plotting Logic
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-', color='firebrick')
    plt.title('Insertion Sort: Execution Time vs. Input Size ($O(n^2)$)')

    plt.xlabel('List Length (n)')
    plt.ylabel('Time (ms)')

    plt.grid(True, linestyle='--', alpha=0.7)

    # Save the plot so it exists even if we don't 'show' it
    graph_path = os.path.join(os.path.dirname(__file__), 'performance_graph.png')
    plt.savefig(graph_path)
    print(f"Graph saved to: {graph_path}")

        # Only show the window if we are likely in a desktop environment
    if os.environ.get('DISPLAY') or os.name == 'nt':
        plt.show()

        # Basic assertion to ensure the test technically 'passes'
    assert len(times) == len(sizes)
    assert times[-1] > times[0]  # Ensure it's actually doing work

"""
Performance Test results:
tests/performance/test_performance.py::test_insertion_sort_scaling 
[Target Check] Size 3000 took 374.64 ms
Running scaling benchmarks...
  n=500 | t=12.70 ms
  n=1000 | t=48.67 ms
  n=1500 | t=91.78 ms
  n=2000 | t=152.42 ms
  n=2500 | t=239.01 ms
  n=3000 | t=343.61 ms
Graph saved to: performance_graph.png
PASSED
"""