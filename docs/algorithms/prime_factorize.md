# 素因数分解

整数$N$を素因数分解する

## コード

```py
def prime_factorize(n):
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
```

## Example

```py
>>> prime_factorize(12)
[2, 2, 3]
```
