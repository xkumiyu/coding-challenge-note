def count_divisor(n):
    """約数の個数をカウント

    計算量: O(√(N)), N=10^12 で 0.3sec

    Examples:
        >>> count_divisor(12)
        6
    """
    i, count = 1, 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count


def make_divisors(n):
    """約数を列挙

    出力はソートされないことに注意
    計算量: O(√(N))

    Examples:
        >>> make_divisors(12)
        [1, 12, 2, 6, 3, 4]
    """
    i, divisors = 1, []
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return divisors


def is_prime(n):
    """素数判定

    最悪計算量: O(√(N))

    Example:
        >>> is_prime(12)
        False
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def prime_factorize(n):
    """素因数分解

    Examples:
        >>> prime_factorize(12)
        [2, 2, 3]
    """
    if n == 1:
        return [1]

    i, factors = 2, []
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors


def prime_boolean_table(n):
    """エラトステネスの篩による素数表

    n までの素数を列挙
    計算量: O(NloglogN), N=10^6 で 0.3sec

    Examples:
        >>> prime_boolean_table(12)
        [False, False, True, True, False, ...]

        >>> [i for i, c in enumerate(prime_boolean_table(12)) if c]
        [2, 3, 5, 7, 11]
    """
    primes = [True] * (n + 1)
    primes[:2] = [False, False]
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False
    return primes
