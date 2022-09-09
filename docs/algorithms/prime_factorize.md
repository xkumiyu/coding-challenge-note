# 素因数分解

整数$N$を素因数分解する

## SPFを用いた方法

### Complexity

- 前処理: $O(N\log{\log{N}})$
- クエリ: $O(\log{N})$

### Code

前処理

```py
def calc_spf(n: int) -> list:
    spf = [i for i in range(n + 1)]
    i = 2
    while i * i <= n:
        if spf[i] == i:
            j = i * i
            while j <= n:
                if spf[j] == j:
                    spf[j] = i
                j += i
        i += 1
    return spf
```

クエリ

```py
def prime_factorize(spf: list, n: int) -> dict:
    factors = {}
    while n != 1:
        m = spf[n]
        factors[m] = factors.get(m, 0) + 1
        n //= m
    return factors
```

### Example

```py
>>> spf = calc_spf(12)
>>> spf
[0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2]
>>> prime_factorize(spf, 12)
{2: 2, 3: 1}
```

## 試し割り法

### Complexity

$O(\sqrt{N})$

### Code

```py
def prime_factorize(n: int) -> list:
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

### Example

```py
>>> prime_factorize(12)
[2, 2, 3]
```

```py
>>> from collections import Counter
>>> Counter(prime_factorize(12))
Counter({2: 2, 3: 1})
```
