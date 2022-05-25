# 二分探索

```py
from bisect import bisect_left
```

```py
from bisect import bisect_right
```

`bisect_right`は`bisect`のエイリアスである。

!!! Note
    ソートされたリストに対して用いること

## x と等しい値の探索

```py
i = bisect_left(A, x)
if i != len(A) and A[i] == x:
  # 等しい値のインデックス
  print(i)
else:
  # 等しい値はない
  pass
```

!!! Example

    ```py
    >>> def f(A, x):
    ...   i = bisect_left(A, x)
    ...   if i != len(A) and A[i] == x:
    ...     return i
    ...
    >>> A = [2, 4, 5, 7]
    >>> f(A, 4)
    1
    >>> f(A, 1)
    ```

## x 以上の値が何個あるか

```py
n = len(A) - bisect_left(A, x)
```

!!! Example

    ```py
    >>> A = [2, 4, 5, 7]
    >>> len(A) - bisect_left(A, 0)
    4
    >>> len(A) - bisect_left(A, 5)
    2
    ```
