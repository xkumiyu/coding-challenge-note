# その他

## 高速化

PythonでTLEの場合、pypyで実行してみる。

## メモ化

``` py
from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
    pass
```

## 再帰回数の上限

デフォルトでは1000回までである。

再帰関数を用いているとき`RE`になった場合は上限を上げてみる。

``` py
import sys
sys.setrecursionlimit(10**6)
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

## 文字列

### アルファベット

```py
alphabet = 'abcdefghijklmnopqrstuvwxyz'
```

### 大文字に変換

```py
s.upper()
```

### 小文字に変換

```py
s.lower()
```
