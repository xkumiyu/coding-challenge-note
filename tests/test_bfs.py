from algorithms.bfs import bfs


def test_bfs():
    graph = [[1, 2], [0, 3], [0, 3], [1, 2]]
    start = 0

    dist = bfs(graph, start)
    assert dist == [0, 1, 1, 2]
