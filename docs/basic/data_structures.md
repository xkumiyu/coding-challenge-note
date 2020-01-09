# データ構造

## リスト

### リストの初期化

``` py
# x[N][M]
x = [[None] * M for _ in range(N)]
```

!!! Note
    多重リストは内包表記で初期化する

### 多重リストのループ

- `product` を使うと短く書ける

``` py
from itertools import product
```

!!! Example

    ``` py
    >>> from itertools import product
    >>> for p in product([0, 1], repeat=3):
    ...     print(p)
    ...
    (0, 0, 0)
    (0, 0, 1)
    (0, 1, 0)
    (0, 1, 1)
    (1, 0, 0)
    (1, 0, 1)
    (1, 1, 0)
    (1, 1, 1)
    ```

### 2次元リストをflatten（一次元）に変換する

``` py
[x for l in A for x in l]
```

!!! Example

    ``` py
    >>> A = [[0, 1], [2, 3]]
    >>> [x for l in A for x in l]
    [0, 1, 2, 3]
    ```

### リストの出力

``` py
print(' '.join(map(str, ans)))
```

!!! Example

    ``` py
    >>> ans = [1, 2, 3]
    >>> print(' '.join(map(str, ans)))
    1 2 3
    ```

## 辞書

### デフォルト値を持つ辞書の初期化

``` py
from collections import defaultdict
```

### 辞書のソート

- `itemgetter`を使用するほうがlamndaより高速

``` py
from operator import itemgetter
sorted(x, key=itemgetter(0))
```

!!! Example

    ``` py
    >>> from operator import itemgetter
    >>> x = {"a": 2, "b": 1}

    # key
    >>> sorted(x, key=itemgetter(0))
    [('a', 2), ('b', 1)]

    # value
    >>> sorted(x, key=itemgetter(1))
    [('b', 1), ('a', 2)]
    ```

### カウンター

``` py
from collections import Counter
```

## 集合

``` py
x in set
```

!!! Note
    重複を含まない要素の探索の場合は `set` を使う

- `list`: O(N)
- `set`: O(1)

## キュー

``` py
from collections import deque
que = deque()
```

### 優先度付きキュー

- heappush: O(logN)
- heappop: O(1)

#### 最小ヒープ

``` py
from heapq import heappop, heappush
que = []
heappush(que, v)
v = heappop(que)
```

#### 最大ヒープ

``` py
from heapq import heappop, heappush
que = []
heappush(que, v * -1)
v = heappop(que) * -1
```
