# 組合せ論

## 順列

配列Aからk個を選ぶ順列のリスト

``` py
from itertools import permutations
permutations(A, k)
```

## 組合せ

配列Aからk個を選ぶ組み合わせのリスト

``` py
from itertools import combinations
combinations(A, k)
```

n個からk個を選ぶ組み合わせ数（nCk）

- scipy > 1.0.0 scipy.special
- n=10^4くらいまで

``` py
from scipy.misc import comb
comb(n, k, exact=True)
```

## 階乗

``` py
# 階乗
from math import factorial
factorial(x)

# 階乗テーブル
fac = [1] * N
for i in range(1, N):
    fac[i] = (fac[i - 1] * i) % mod
# 逆元テーブル
inv = [1] * N
inv[N - 1] = pow(fac[N - 1], mod - 2, mod)
for i in range(N - 1, 0, -1):
    inv[i - 1] = (inv[i] * i) % mod
```
