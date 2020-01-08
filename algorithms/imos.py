class Imos1d(object):
    """いもす法

    https://imoz.jp/algorithms/imos_method.html
    """

    def __init__(self, n):
        self.n = n
        self.x = [0] * n

    def add(self, l, r):
        self.x[l] += 1
        self.x[r] -= 1

    def calc(self):
        for i in range(self.n - 1):
            self.x[i] += self.x[i - 1]
