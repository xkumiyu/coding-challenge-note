# Union Find

## Complexity

$O(\alpha(N))$

!!! Note
    $\alpha(\cdot)$はアッカーマン関数であり、$\log$より小さい

## Code

``` python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rank = [0] * n
        self._size = [1] * n

    def find(self, x: int) -> int:
        """x が属するグループを探索"""
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        """x と y のグループを結合"""
        x = self.find(x)
        y = self.find(y)
        if x != y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        self._size[x] += self._size[y]

    def is_same(self, x: int, y: int) -> bool:
        """x と y が同じグループか否か"""
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        """x が属するグループの要素数"""
        x = self.find(x)
        return self._size[x]
```
