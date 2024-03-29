# 組合せ論

## 順列

配列`A`から`k`個を選ぶ順列のリスト

```py
from itertools import permutations
permutations(A, k)
```

## 組合せ

配列`A`から`k`個を選ぶ組み合わせのリスト

```py
from itertools import combinations
combinations(A, k)
```

配列`A`から重複を許して`k`個を選ぶ組み合わせのリスト

```py
from itertools import combinations_with_replacement
combinations_with_replacement(A, k)
```

`n`個から`k`個を選ぶ組み合わせ数（nCk）

```py
from scipy.special import comb
comb(n, k, exact=True)
```

!!! Note
    $n=10^4$ で200ms程度, $n=10^5$ で2sec程度

`n`個から重複を許して`k`個を選ぶ組み合わせ数

```py
from scipy.special import comb
comb(n, k, exact=True, repetition=True)
```

```py
# n個からn + k - 1個を選ぶ組み合わせ数と等しい
comb(n + k - 1, k, exact=True)
```

[フェルマーの小定理を用いた二項係数の計算](../algorithms/binomial_coefficients.md)

## 階乗

```py
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

## mod

mod空間において加算、減算、乗算は通常の四則演算と同じだが、除算は逆元の積をとる

`a // b % mod` ではなく `pow(b, mod - 2, mod)` を用いる
