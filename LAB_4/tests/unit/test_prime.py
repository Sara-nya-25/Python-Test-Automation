import pytest
from src.algorithms.prime import is_prime, get_primes

pytestmark=pytest.mark.unit

def test__is_prime__returns_true():
    result = is_prime(5)
    assert result is True

def test__is_prime__returns_false():
    result = is_prime(10)
    assert result is False

def test__get_primes__4_first_primes():
    result = get_primes(4)
    assert result == [2,3,5,7]
"""
pylint tests/unit/test_prime.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.17/10, +0.83)

Test coverage: pytest --cov=src
Name                         Stmts   Miss  Cover
------------------------------------------------
src\\__init__.py                  0      0   100%
src\\algorithms\\__init__.py       0      0   100%
src\\algorithms\\prime.py         16      1    94%
------------------------------------------------
TOTAL                           16      1    94%
"""