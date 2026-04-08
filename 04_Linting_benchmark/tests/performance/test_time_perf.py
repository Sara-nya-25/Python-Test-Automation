import pytest
import time
from src.algorithms.prime import is_prime, get_primes

@pytest.mark.performance
def test__get_primes__benchmark():
    start_time = time.perf_counter()

    # Run the function with a significant amount
    get_primes(500)

    end_time = time.perf_counter()
    duration = end_time - start_time

    print(f"\n--- Performance Result ---")
    print(f"Time taken to find 500 primes: {duration:.5f} seconds")

    # Optional: ensure it's not "too slow" (e.g., under 2 seconds)
    assert duration < 2.0

@pytest.mark.performance
def test__get_primes__benchmark(benchmark):
    benchmark(get_primes, 3000)

"""
benchmark test results:

------------------------------------------------ benchmark: 1 tests ------------------------------------------------
Name (time in s)                   Min     Max    Mean  StdDev  Median     IQR  Outliers     OPS  Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------
test__get_primes__benchmark     2.1125  2.1301  2.1198  0.0064  2.1191  0.0058       2;0  0.4717       5           1
--------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
=============================================================================== 4 passed in 15.86s =====================
"""