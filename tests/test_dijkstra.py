from algorithms.dijkstra import Dijkstra, Graph


def test_dijkstra():
    # (from, to, cost)
    edges = [
        (0, 1, 5),
        (0, 2, 4),
        (0, 3, 2),
        (1, 2, 2),
        (1, 5, 6),
        (2, 3, 3),
        (2, 4, 2),
        (3, 4, 6),
        (4, 5, 4),
    ]

    g = Graph()
    for src, dst, weight in edges:
        g.add_edge(src, dst, weight)
        g.add_edge(dst, src, weight)
    d = Dijkstra(g, 0)

    assert d.shortest_path(5) == [0, 2, 4, 5]
    assert d.shortest_distance(5) == 10
