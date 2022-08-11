# その他

## 高速化

PythonでTLEの場合、pypyで実行してみる。

## メモ化

``` py
from functools import lru_cache

@lru_cache(maxsize=None)
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

## 文字列

### アルファベット

```py
import string
alphabet = string.ascii_lowercase
```

以下と同じ

```py
alphabet = "abcdefghijklmnopqrstuvwxyz"
```

### 大文字に変換

```py
s.upper()
```

### 小文字に変換

```py
s.lower()
```
