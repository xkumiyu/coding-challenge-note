class Imos1d(object):
    """いもす法

    https://imoz.jp/algorithms/imos_method.html
    """

    def __init__(self, n):
        self.n = n
        self.x = [0] * n

    def add(self, l, r, v=1):  # noqa: E741
        self.x[l] += v
        self.x[r] -= v

    def calc(self):
        for i in range(1, self.n):
            self.x[i] += self.x[i - 1]
