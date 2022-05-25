# ダイクストラ法

2点間の最短経路を求めるアルゴリズム

## 計算量

- $O((E + V)\log{V})$
    - $V$: 頂点の数
    - $E$: 辺の数

## Code

```py
from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(graph, start):
    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0
    prev = {}

    Q = []
    heappush(Q, (dist[start], start))

    while Q:
        dist_u, u = heappop(Q)
        if dist[u] < dist_u:
            continue
        for v, c in graph[u]:
            if dist[v] > dist_u + c:
                dist[v] = dist_u + c
                prev[v] = u
            heappush(Q, (dist[v], v))

    return dist, prev
```

隣接グラフによる有向グラフを構築する。

```py
g = defaultdict(list)
for _ in range(N):
    src, dst, cost = map(int, input().split())
    g[src].append((dst, cost))
    g[dst].append((src, cost))
```

## Example

```py
>>> edges = [
...     (0, 1, 5),
...     (0, 2, 4),
...     (0, 3, 2),
...     (1, 2, 2),
...     (1, 5, 6),
...     (2, 3, 3),
...     (2, 4, 2),
...     (3, 4, 6),
...     (4, 5, 4),
... ]
...
>>> g = defaultdict(list)
>>> for src, dest, cost in edges:
...     g[src].append((dst, cost))
...     g[dst].append((src, cost))
...
>>> v = 0 # 始点
>>> u = 5 # 終点
>>> dist, prev = dijkstra(g, v)
```

### 最短距離を求める

```py
>>> dist[u]
10
```

### 最短経路を求める

```py
>>> path = []
>>> node = u
>>> while node is not None:
...     path.append(node)
...     node = prev[node]
>>> path[::-1]
[0, 2, 4, 5]
```
