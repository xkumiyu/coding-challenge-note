# データ構造

## リスト

### リストの初期化

```py
# x[N][M]
x = [[None] * M for _ in range(N)]
```

!!! Note
    多重リストは内包表記で初期化する

### 多重リストのループ

- `product` を使うと短く書ける

```py
from itertools import product
```

!!! Example

    ```py
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

### 2次元リストをflatten（1次元）に変換する

```py
[x for l in A for x in l]
```

!!! Example

    ```py
    >>> A = [[0, 1], [2, 3]]
    >>> [x for l in A for x in l]
    [0, 1, 2, 3]
    ```

### リストの出力

```py
print(' '.join(map(str, ans)))
```

!!! Example

    ```py
    >>> ans = [1, 2, 3]
    >>> print(' '.join(map(str, ans)))
    1 2 3
    ```

## 辞書

### デフォルト値を持つ辞書の初期化

```py
from collections import defaultdict
```

!!! Example
    引数に `int` を指定すると、keyはすべて0で初期化される。

    ```py
    >>> d = defaultdict(int)
    >>> d["key"] += 1
    >>> d
    defaultdict(<class 'int'>, {'key': 1})
    ```

!!! Example
    引数に `lambda` を用いて任意の値を指定できる。

    ```py
    >>> d = defaultdict(lambda: 1)
    >>> d["key"] += 1
    >>> d
    defaultdict(<function <lambda> at 0x10bffe5e0>, {'key': 2})
    ```

### 辞書のソート

`itemgetter` を使用するほうが `lambda` より若干高速である。

```py
from operator import itemgetter
sorted(x, key=itemgetter(0))
```

!!! Example

    ```py
    >>> from operator import itemgetter
    >>> x = {"a": 2, "b": 1}

    # key
    >>> sorted(x, key=itemgetter(0))
    [('a', 2), ('b', 1)]

    # value
    >>> sorted(x, key=itemgetter(1))
    [('b', 1), ('a', 2)]
    ```

### 要素の数え上げ

```py
from collections import Counter
```

!!! Example

    ```py
    >>> A = ["a", "b", "c", "a"]
    >>> Counter(A)
    Counter({'a': 2, 'b': 1, 'c': 1})
    ```

## 集合

```py
x in set
```

重複を含まない要素の探索の場合は `set` を使うほうが高速である。

- `list`: O(N)
- `set`: O(1)

## キュー

```py
from collections import deque
que = deque()
```

### 優先度付きキュー

- heappush: O(logN)
- heappop: O(1)

#### 最小ヒープ

```py
from heapq import heappop, heappush
que = []
heappush(que, v)
v = heappop(que)
```

#### 最大ヒープ

```py
from heapq import heappop, heappush
que = []
heappush(que, v * -1)
v = heappop(que) * -1
```
