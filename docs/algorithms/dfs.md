# 深さ優先探索(DFS)

## 計算量

- O(N+M)
    - Nはグラフの頂点の数, Mは辺の数

## 使い方

- graph (List[int]): 隣接リスト
- start (int): 開始ノード番号

## 再帰あり

``` py
    def dfs(graph, visited, v):
        visited[v] = True
        # do something with v

        for u in graph[v]:
            if visited[u]:
                continue
            dfs(graph, visited, u)

    visited = [False] * len(graph)
    dfs(graph, visited, start)
```

## 再帰なし

``` py
def dfs(graph, start):
    stack = [start]
    visited = [False] * len(graph)
    visited[start] = True

    while len(stack) != 0:
        v = stack.pop()
        print("v = ", v)
        # do something with v

        for u in graph[v]:
            if visited:
                continue
            print("  u = ", u)
            stack.append(u)
            visited[u] = True
```
