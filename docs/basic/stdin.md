# 標準入力

## よく使う標準入力

### 文字列

``` text
string
```

``` py
S = input()
```

### 数字

``` text
1
```

``` py
N = int(input())
```

### 複数の数字

#### 別々の変数

``` text
10 5
```

``` py
N, K = map(int, input().split())
```

#### 1つの変数（リスト）

``` text
1 2 3 4 5
```

``` py
A = [int(x) for x in input().split()]
```

### 複数行の文字列

``` text
#..#
..##
```

``` py
S = [list(input()) for _ in range(H)]
```

``` python
>>> print(S)
[['#', '.', '.', '#'], ['.', '.', '#', '#']]
```

### 複数行の数字

``` text
1
2
3
```

``` py
A = [int(input()) for _ in range(N)]
```

### 複数行に複数の数字

``` text
1 4
2 5
3 6
```

#### 1つの2次元リスト

``` py
A = [[int(x) for x in input().split()] for _ in range(H)]
```

``` py
>>> print(A)
[[1, 4], [2, 5], [3, 6]]
```

#### 別々の1次元リスト

``` py
a, b = [None] * N, [None] * N
for i in range(N):
    a[i], b[i] = map(int, input().split())
```

``` py
>>> print(a)
[1, 2, 3]
>>> print(b)
[4, 5, 6]
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
