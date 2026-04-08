"""
This module provides functions to identify and generate prime numbers.
"""
def is_prime(n):
    """Checks if a given number is a prime number."""
    if n < 2:
        return False

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def get_primes(amount):
    """Generates a list containing the specified amount of prime numbers."""
    primes = []
    i = 2
    while len(primes) < amount:
        if is_prime(i):
            primes.append(i)
        i += 1

    return primes

"""
Linting:
pylint src/algorithms/prime.py
************* Module src.algorithms.prime
src\\algorithms\\prime.py:19:0: C0304: Final newline missing (missing-final-newline)
src\\algorithms\\prime.py:1:0: C0114: Missing module docstring (missing-module-docstring)
src\\algorithms\\prime.py:2:0: C0116: Missing function or method docstring (missing-function-docstring)
src\\algorithms\\prime.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
-----------------------------------
Your code has been rated at 7.33/10
------------------------------------
-----------------
After correction:|
-----------------
 pylint src/algorithms/prime.py
************* Module src.algorithms.prime
src\\algorithms\\prime.py:25:0: W0105: String statement has no effect (pointless-string-statement)

------------------------------------------------------------------
Your code has been rated at 9.38/10 (previous run: 8.75/10, +0.62)

"""
