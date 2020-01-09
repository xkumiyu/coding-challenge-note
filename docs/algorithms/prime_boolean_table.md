# 素数を列挙

整数$N$までの素数をエラトステネスの篩で求める

## 計算量

$O(N\log{\log{N}})$

!!! Note
    $N = 10^{6}$ で 300ms程度

## コード

```py
def prime_boolean_table(n):
    primes = [True] * (n + 1)
    primes[:2] = [False, False]
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i + i, n + 1, i):
                primes[j] = False
    return primes
```

## Example

```py
>>> prime_boolean_table(12)
[False, False, True, True, False, ...]

>>> [i for i, c in enumerate(prime_boolean_table(12)) if c]
[2, 3, 5, 7, 11]
```
