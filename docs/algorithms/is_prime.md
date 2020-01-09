# 素数判定

整数$N$の素数か否かを判定する

## 計算量

最悪計算量: $O(\sqrt{N})$

## コード

```py
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
```

## Example

```py
>>> is_prime(12)
False
```
