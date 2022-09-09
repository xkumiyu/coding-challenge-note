# 素数列挙

整数$N$までの素数をエラトステネスの篩で求める

## Complexity

$O(N\log{\log{N}})$

## Code

### 通常

```py
def primes(n: int) -> list:
    table = [True] * (n + 1)
    table[:2] = [False, False]
    for i in range(2, n + 1):
        if table[i]:
            for j in range(i + i, n + 1, i):
                table[j] = False
    return [i for i, c in enumerate(table) if c]
```

### 高速版

偶数を篩から落とすことにより、$N=10^7$で通常3000ms程度だったものが900ms程度まで高速化できる

```py
def primes(n):
    table = [True] * ((n + 1) // 2)
    for i in range(1, (int(n**0.5) + 1) // 2):
        if table[i]:
            for j in range(i * 3 + 1, (n + 1) // 2, i * 2 + 1):
                table[j] = False
    return [2] + [i * 2 + 1 for i, c in enumerate(table) if c][1:]
```

## Example

```py
>>> primes(12)
[2, 3, 5, 7, 11]
```
