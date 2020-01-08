from collections import deque


def bfs(graph, start):
    """幅優先探索

    計算量: O(N+M)
    Nはグラフの頂点の数, Mは辺の数

    Args:
        graph (List[int]): 隣接リスト
        start (int): 開始ノード番号

    Returns:
        list: 開始ノードからの距離
    """
    que = deque([start])
    dist = [None] * len(graph)
    dist[start] = 0

    while len(que) != 0:
        # print(que)
        v = que.popleft()
        # print("v = ", v)
        # do something with v

        for u in graph[v]:
            if dist[u] is None:
                # print("  u = ", u)
                que.append(u)
                dist[u] = dist[v] + 1

    return dist
