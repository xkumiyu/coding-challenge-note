# 二分探索

## 標準ライブラリ

```py
from bisect import bisect_left
```

```py
from bisect import bisect_right
```

`bisect_right`は`bisect`のエイリアスである。

!!! Note
    ソートされたリストに対して用いること

### x と等しい値の探索

```py
i = bisect_left(A, x)
if i != len(A) and A[i] == x:
    # 等しい値のインデックス
    print(i)
else:
    # 等しい値はない
    pass
```

#### Example

```py
>>> def f(A, x):
...     i = bisect_left(A, x)
...     if i != len(A) and A[i] == x:
...         return i
...     else:
...         return "Not Found"
...
>>> A = [2, 4, 5, 7]
>>> f(A, 4)
1
>>> f(A, 1)
'Not Found'
```

### x 以上の値が何個あるか

```py
n = len(A) - bisect_left(A, x)
```

#### Example

```py
>>> A = [2, 4, 5, 7]
>>> len(A) - bisect_left(A, 0)
4
>>> len(A) - bisect_left(A, 5)
2
```

## 自作

### Complexity

$\log{N}$

### Code

```py
def is_ok(mid) -> bool:
    # 求める点が区間[left, mid]に含まれる場合Trueになるように作成する
    pass

def binary_search(left, right):
    while left + 1 != right:
        mid = (left + right) // 2
        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right
```

### Example

`x`を挿入できる場所の探索(`bisect_left`と同じ)

```py
>>> A = [2, 4, 5, 7]
>>> x = 4
>>> def is_ok(mid):
...     return x <= A[mid]
>>> binary_search(-1, len(A))
... 1
```
