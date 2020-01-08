# Coding Challenge NOTE

## 累積和

``` py
from itertools import accumulate

B = [x for x in accumulate(A)]
B = list(accumulate(A))
```

累積積

``` py
import operator
B = list(accumulate(A, operator.mul))
```

``` py
>>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> list(accumulate(A, operator.mul))
[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
```

累積max

``` py
B = list(accumulate(A, max))
```

``` py
>>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> list(accumulate(A, max))
>>> [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
```

累積XOR

``` py
B = list(accumulate(A, operator.xor))
```

## 二分探索

``` py
from bisect import bisect_left, bisect_right

# x と等しい値の探索(index)
i = bisect_left(A, x)
if i != len(A) and A[i] == x:
  return i

# x 以上の値が何個あるか(find_ge)
n = len(A) - bisect_left(A, x)
```

## mod

``` py
# b　の逆元
# mod空間では除算が逆元の積になる
pow(b, mod - 2, mod)

# a // b % mod
# a * pow(b, mod - 2, mod) % mod
# が同じ
```

## 最大公約数と最小公倍数

``` py
# 最大公約数, python 3.5 から math.gcd
from fractions import gcd
gcd(a, b)

# 最小公倍数
def lcm(a, b):
  return a * b // gcd(a, b)
```

## 文字列

``` py
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# 大文字/小文字に変換
S.upper()
S.lower()
```

## ceil

``` py
# math.ceil(x / y) と同じ
-(-x // y)

def ceil(x, y):
    if x % y == 0:
        return x // y
    else:
        return x // y + 1
```

## 最短経路

``` python
from scipy.sparse.csgraph import floyd_warshall
```

## 計算量, 高速化

- pythonでTLEの場合、pypyを試してみる

## メモ化

``` py
from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    pass
```

## 再帰回数の上限

デフォルトでは1000回までである
再帰関数を用いているときREになった場合は上限を上げてみる

``` py
import sys
sys.setrecursionlimit(10**6)
```

## その他気をつけること

- デバッグ時の`print`がないか確認する
- `Yes`と`YES`など出力に気をつける
- 出力形式にも気をつける
    - 1行でスペース区切りとか、複数行とか
