class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """x が属するグループを探索"""
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """x と y のグループを結合"""
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """x と y が同じグループか否か"""
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """x が属するグループの要素数"""
        x = self.find(x)
        return self.size[x]


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
