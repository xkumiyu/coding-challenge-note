# 標準入力

## よく使う標準入力

``` py
S = input()
```

``` py
N = int(input())
```

``` py
N, K = map(int, input().split())
```

``` py
A = [int(x) for x in input().split()]
```

``` py
A = [int(input()) for _ in range(N)]
```

``` py
S = [list(input()) for _ in range(H)]
```

``` py
A = [[int(x) for x in input().split()] for _ in range(H)]
```

``` py
a, b = [None] * N, [None] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
```

## 標準入力の高速化

``` py
import sys
input = sys.stdin.readline
```

!!! Note
    10倍以上高速化できるので、$10^6$ を超える場合は使うこと

### 処理速度の比較

データ数が$10^6$のときの処理速度

![input_vs_sys_stdin_readline](../assets/images/input_vs_sys_stdin_readline.png)

出展: [Pythonの知っておくと良い細かい処理速度の違い8個](https://www.kumilog.net/entry/python-speed-comp#input-%E3%81%A8-sysstdinreadline)
