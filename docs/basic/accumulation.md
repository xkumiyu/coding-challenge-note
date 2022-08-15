# 累積和

``` py
from itertools import accumulate

B = list(accumulate(A))
```

## 区間の総和

累積和 $B$ を用いて区間$[L, R]$の和を $B[R + 1] - S[L]$ で求めることができる

!!! Example

    ``` py
    >>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    >>> B = [0] + list(accumulate(A))
    [0, 3, 7, 13, 15, 16, 25, 25, 32, 37, 45]
    >>> # 区間[2, 4](A[2]=6, A[3]=2, A[4]=1)の和を求める
    >>> B[4 + 1] - B[2]
    9
    ```

## 積の累積

``` py
from itertools import accumulate
import operator

B = list(accumulate(A, operator.mul))
```

!!! Example

    ``` py
    >>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    >>> list(accumulate(A, operator.mul))
    [3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
    ```

## 最大値の累積

``` py
from itertools import accumulate

B = list(accumulate(A, max))
```

!!! Example

    ``` py
    >>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
    >>> list(accumulate(A, max))
    >>> [3, 4, 6, 6, 6, 9, 9, 9, 9, 9]
    ```

## XORの累積

``` py
from itertools import accumulate
import operator

B = list(accumulate(A, operator.xor))
```

## imos法

<https://imoz.jp/algorithms/imos_method.html>

### 1次元

```py
class Imos1d(object):
    def __init__(self, n):
        self.n = n
        self.x = [0] * n

    def add(self, l, r, v=1):
        self.x[l] += v
        self.x[r] -= v

    def calc(self):
        for i in range(1, self.n):
            self.x[i] += self.x[i - 1]
```
