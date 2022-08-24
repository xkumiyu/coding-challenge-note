# いもす法

## Code

### 1次元

```py
def imos1d(N: int, x: list[tuple]):
    S = [0] * N
    for l, y, v in x:
        S[l] += v
        S[r] -= v

    for i in range(N):
        S[i] += S[i - 1]

    return S
```

### 2次元

矩形の左下の点を$(lx, ly)$、右上の点を$(rx, ry)$とする

```py
def imos2d(H: int, W: int, xy: list[tuple]) -> list:
    S = [[0] * W for _ in range(H)]
    for lx, ly, rx, ry, v in xy:
        S[ly][lx] += v
        S[ly][rx] -= v
        S[ry][lx] -= v
        S[ry][rx] += v

    for y in range(H):
        for x in range(1, W):
            S[y][x] += S[y][x - 1]
    for y in range(1, H):
        for x in range(W):
            S[y][x] += S[y - 1][x]

    return S
```

## Reference

- <https://imoz.jp/algorithms/imos_method.html>
