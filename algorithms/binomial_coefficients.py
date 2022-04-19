class Comb(object):
    """フェルマーの小定理を用いた二項係数の計算"""

    def __init__(self, N, mod=10**9 + 7):
        """前処理

        計算量: O(N)
        """
        self.mod = mod
        self.fac, self.inv = [1] * (N + 1), [1] * (N + 1)
        for i in range(2, N + 1):
            self.fac[i] = self.fac[i - 1] * i % mod
            self.inv[i] = self.inv[i - 1] * pow(i, mod - 2, mod) % mod

    def calc(self, n, k):
        """二項係数の計算

        計算量: O(1)

        Examples:
            >>> comb = Comb(10)
            >>> comb.calc(10, 2)
            45
        """
        if n >= k:
            return self.fac[n] * self.inv[k] * self.inv[n - k] % self.mod
        else:
            return 0
