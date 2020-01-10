# AtCoder ABC054 D - Mixing Experiment

<https://atcoder.jp/contests/abc054/tasks/abc054_d>

## 問題概要

- 物質Aを`a`グラム、物質Bを`b`グラム含み`c`円である薬品が`N`個与えられる
- 物質Aと物質Bの比率が `Ma`: `Mb` になるように、薬品を買ったときの最小コストを求めよ
- 制約: `N <= 40`, `a, b <= 10`

## 解説とコード

3次元DPを用いて解きます。

```py
N, Ma, Mb = map(int, input().split())
items = [[int(x) for x in input().split()] for _ in range(N)]

# 物質AとBの合計値を求める
A, B = 0, 0
for a, b, _ in items:
    A += a
    B += b

# DPの初期化
# dp[i][j][k]: 薬品をi個まで選びjグラム、kグラムになるときの最小コスト
dp = [[[float("inf")] * (B + 1) for _ in range(A + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0][0] = 0

# DPの更新
# 3重ループの計算量は、それぞれO(N=40), O(Na=400), O(Nb=400)なので、O(10^6)
for i in range(N):
    a, b, c = items[i]
    for j in range(A + 1):
        for k in range(B + 1):
            # 薬品を加えることができる場合
            if j - a >= 0 and k - b >= 0:
                # 薬品を加えたときにコストが小さくなる場合更新する
                dp[i + 1][j][k] = min(dp[i][j - a][k - b] + c, dp[i][j][k])
            else:
                dp[i + 1][j][k] = dp[i][j][k]

# dp[N][:][:]の中から比率に合致するものを取り出す
ans = float("inf")
for x in range(1, min(A // Ma, B // Mb) + 1):
    a = Ma * x
    b = Mb * x
    ans = min(dp[N][a][b], ans)

if ans == float("inf"):
    ans = -1
print(ans)
```
