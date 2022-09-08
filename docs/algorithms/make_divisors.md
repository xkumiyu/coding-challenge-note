# 約数列挙

整数$N$の約数の列挙する

## 計算量

$O(\sqrt{N})$

## コード

```py
def make_divisors(n):
    i, divisors = 1, []
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return divisors
```

!!! Warning
    出力はソートされないことに注意

## Example

```py
>>> make_divisors(12)
[1, 12, 2, 6, 3, 4]
```
