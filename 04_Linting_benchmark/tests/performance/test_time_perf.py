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
'''
@pytest.mark.performance
def test__get_primes__benchmark():
    benchmark(get_primes, 3000)

'''