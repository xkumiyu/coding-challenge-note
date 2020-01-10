# 幅優先探索（BFS）

## 計算量

- O(N+M)
    - Nはグラフの頂点の数
    - Mは辺の数

## コード

- Args:
    - graph (List[int]): 隣接リスト
    - start (int): 開始ノード番号
- Returns:
    - list: 開始ノードからの距離

``` py
from collections import deque


def bfs(graph, start):
    que = deque([start])
    dist = [None] * len(graph)
    dist[start] = 0

    while len(que) != 0:
        v = que.popleft()
        # do something with v

        for u in graph[v]:
            if dist[u] is None:
                que.append(u)
                dist[u] = dist[v] + 1

    return dist
```
