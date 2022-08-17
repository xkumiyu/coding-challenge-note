# 強連結成分分解（SCC）

有向グラフを強連結（お互いに行き来できる ⇔ 同じグループ）になるようにグループ分けする

## Complexity

2回DFSを行う

- $O(N + M)$
    - $N$はグラフの頂点の数
    - $M$は辺の数

## Code

```py
def scc(n: int, graph: dict, rev_graph: dict) -> list:
    """強連結成分分解（SCC）

    Args:
        n: 頂点の数
        graph: 順方向の隣接グラフ
        rev_graph: 逆方向の隣接グラフ

    Return:
        頂点ごとのグループ番号
    """
    order = []
    visited = [False] * n
    group = [None] * n

    def dfs(v):
        visited[v] = True
        for u in graph[v]:
            if visited[u] is False:
                dfs(u)
        order.append(v)

    def rev_dfs(v, col):
        group[v] = col
        visited[v] = True
        for u in rev_graph[v]:
            if visited[u] is False:
                rev_dfs(v, col)

    for v in range(n):
        if visited[v] is False:
            dfs(v)

    visited = [False] * n
    label = 0
    for v in reversed(order):
        if visited[v] is False:
            rev_dfs(v, label)
            label += 1
    return group
```
