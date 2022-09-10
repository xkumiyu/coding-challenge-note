# 深さ優先探索（DFS）

## Complexity

- $O(N + M)$
    - $N$はグラフの頂点の数
    - $M$は辺の数

## Code

- graph (Dict[List[int]]): 隣接リスト
- start (int): 開始ノード番号

### 再帰あり

``` py
def dfs(graph, v, visited=None):
    if visited is None:
        visited = [False] * len(graph)
    visited[v] = True

    for u in graph[v]:
        if visited[u]:
            continue
        dfs(graph, u, visited)

dfs(graph, start)
```

### 再帰なし

``` py
def dfs(graph, start):
    stack = [start]
    visited = [False] * len(graph)
    visited[start] = True

    while len(stack) != 0:
        v = stack.pop()

        for u in graph[v]:
            if visited[u]:
                continue
            stack.append(u)
            visited[u] = True
```

## Examples

### 最短距離を求める

``` py
def dfs(graph, start):
    stack = [start]
    visited = [False] * len(graph)
    visited[start] = True
    dist = [0] * len(graph)

    while len(stack) != 0:
        v = stack.pop()

        for u in graph[v]:
            if visited[u]:
                continue
            stack.append(u)
            visited[u] = True
            dist[u] = dist[v] + 1

    return dist
```

## 木の直径を求める

最短距離を求めるDFSを2回行うことで、木の直径（木に存在する2つノード間の最大距離）を求めることができる

```py
v = 0
dist = dfs(graph, v)
v = dist.index(max(dist))
dist = dfs(graph, v)
max(dist) + 1  # 木の直径
```
