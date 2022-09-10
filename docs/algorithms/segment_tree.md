# セグメント木

## Range Minimum Query (RMQ)

### Complexity

- `update`: $O(\log{N})$
- `query`: $O(\log{N})$

### Code

```py
class RMQ:
    def __init__(self, A: list) -> None:
        self.n = 2 ** (len(A) - 1).bit_length()
        self.data = [float("inf")] * (2 * self.n - 1)
        for i in range(len(A)):
            self.update(i, A[i])

    def update(self, i: int, x: int) -> None:
        """i番目の値をxに更新する"""
        i += self.n - 1
        self.data[i] = x
        while i >= 0:
            i = (i - 1) // 2
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def query(self, left: int, right: int) -> int:
        """区間[left, right)の最小値を取得する"""
        left += self.n
        right += self.n
        s = float("inf")
        while left < right:
            if left & 1:
                s = min(s, self.data[left - 1])
                left += 1
            left >>= 1
            if right & 1:
                right -= 1
                s = min(s, self.data[right - 1])
            right >>= 1
        return s
```

## Range Update Query (RUQ)

### Complexity

- `update`: $O(\log{N})$
- `find`: $O(\log{N})$

### Code

```py
class RUQ:
    def __init__(self, N: int) -> None:
        self.n = 2 ** (N - 1).bit_length()
        self.data = [None] * (2 * self.n - 1)
        self.t = 0

    def update(self, left: int, right: int, x: int) -> None:
        """区間[left, right)の値をxに更新する"""
        left += self.n
        right += self.n
        self.t += 1
        while left < right:
            if left & 1:
                self.data[left - 1] = (self.t, x)
                left += 1
            left >>= 1
            if right & 1:
                right -= 1
                self.data[right - 1] = (self.t, x)
            right >>= 1

    def find(self, i: int) -> int:
        """i番目の値を取得する"""
        i += self.n - 1
        x = (-1, float("-inf"))
        while i >= 0:
            if self.data[i] is not None:
                if x[0] < self.data[i][0]:
                    x = self.data[i]
            i = (i - 1) // 2
        return x[1]
```
