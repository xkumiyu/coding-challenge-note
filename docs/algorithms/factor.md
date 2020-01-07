# 約数

## 約数の個数をカウント

計算量: O(√(N)), N=10^12 で 0.3sec

``` py
def count_divisor(n):
    i, count = 1, 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return coun
```

### Examples

``` py
>>> count_divisor(12)
6
```
