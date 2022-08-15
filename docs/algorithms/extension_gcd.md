# 拡張ユークリッドの互除法

一次不定方程式 $ax + by = c$ の整数解を求める

## Condition

整数解をもつ条件は $c$ が $\gcd(a, b)$ で割り切れること

## Complexity

$O(\log{\min{(a, b)}})$

## Code

```py
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0
```

```py
d, x, y = extgcd(a, b)
if c % d != 0:
    print("解なし")
x *= c // d
y *= c // d
```

## Examples

### １つの解

$6x + 8y = 10$ の整数解を求める

```py
>>> a, b, c = 6, 8, 10
>>> d, x, y = extgcd(a, b)
>>> d
2
>>> x
-1
>>> y
1
>>> c % d
0
>>> x * (c // d)
-5
>>> y * (c // d)
5
```

よって、$x=-5, y=5$

なお、`extgcd`の戻り値である $(x, y) = (-1, 1)$ は $6x + 8y = d(=\gcd(a, b))$ の解

### 一般解

$6x + 8y = 10$ の整数解の一般解を求める

```py
>>> a, b, c = 6, 8, 10
>>> d, x1, y1 = extgcd(a, b)
>>> c % d == 0
True
>>> x1 *= c // d
>>> y1 *= c // d
>>> x1, y1
(-5, 5)
>>> # x := (b // d)t + x1
>>> b // d
4
>>> x1
-5
>>> # y := (-a // d)t + y1
>>> -a // d
-3
>>> y1
5
```

よって、一般解は任意の整数$t$を用いて$x = 4t -5, y = -3t + 5$
