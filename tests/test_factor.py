from algorithms.factor import (
    count_divisor,
    is_prime,
    make_divisors,
    prime_boolean_table,
    prime_factorize,
)


def test_count_divisor():
    assert count_divisor(12) == 6


def test_make_divisors():
    assert make_divisors(12) == [1, 12, 2, 6, 3, 4]


def test_prime():
    assert is_prime(12) is False


def test_prime_factorize():
    assert prime_factorize(12) == [2, 2, 3]


def test_prime_boolean_table():
    assert prime_boolean_table(6) == [False, False, True, True, False, True, False]
    assert [i for i, c in enumerate(prime_boolean_table(12)) if c] == [2, 3, 5, 7, 11]
