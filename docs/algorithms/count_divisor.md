# 約数の個数をカウント

整数$N$の約数の個数を数える

## 計算量

$O(\sqrt{N})$

!!! Note
    $N = 10^{12}$ で 300ms程度

## コード

```py
def count_divisor(n):
    i, count = 1, 0
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count
```

## Example

``` py
>>> count_divisor(12)
6
```
