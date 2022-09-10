# バブルソート

## Complexity

- 最悪: $O(N^2)$
- 最良: $O(N)$
- 平均: $O(N^2)$

## Code

### ソートのみ

```py
def bubble_sort(A: list) -> list:
    N = len(A)
    B = A.copy()
    for i in range(N):
        for j in range(1, N - i):
            if B[j] < B[j - 1]:
                B[j], B[j - 1] = B[j - 1], B[j]
    return B
```

### 転倒数を求める

```py
def inversion_by_bubble_sort(A: list) -> int:
    N = len(A)
    B = A.copy()
    cnt = 0
    for i in range(N):
        for j in range(1, N - i):
            if B[j] < B[j - 1]:
                B[j], B[j - 1] = B[j - 1], B[j]
                cnt += 1
    return cnt
```

BITを用いると$O(N\log{N})$と高速に求めることができる

## Examples

```py
>>> A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> bubble_sort(A)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> inversion_by_bubble_sort(A)
18
```
