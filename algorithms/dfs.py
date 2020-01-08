def dfs(graph, start):
    """深さ優先探索（再帰なし）

    計算量: O(N+M)
    Nはグラフの頂点の数, Mは辺の数

    Args:
        graph (List[int]): 隣接リスト
        start (int): 開始ノード番号
    """
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


def dfs_with_recursion(graph, start):
    """深さ優先探索（再帰あり）

    計算量: O(N+M)
    Nはグラフの頂点の数, Mは辺の数

    Args:
        graph (List[int]): 隣接リスト
        start (int): 開始ノード番号
    """

    def dfs(graph, visited, v):
        visited[v] = True
        # do something with v

        for u in graph[v]:
            if visited[u]:
                continue
            dfs(graph, visited, u)

    visited = [False] * len(graph)
    dfs(graph, visited, start)
