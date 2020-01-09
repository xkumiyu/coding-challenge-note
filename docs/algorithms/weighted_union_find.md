# Weighted Union Find

## コード

```py
class WeightedUnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.diff_weight = [0 for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            root = self.find(self.par[x])
            self.diff_weight[x] += self.diff_weight[self.par[x]]
            self.par[x] = root
            return root

    def union(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.par[y] = x
            self.diff_weight[y] = w

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)
```
