from algorithms.union_find import UnionFind, WeightedUnionFind


def test_union_find():
    """https://atc001.contest.atcoder.jp/tasks/unionfind_a"""
    N = 8
    P = [0, 0, 1, 1, 0, 1, 0, 0, 1]
    A = [1, 3, 1, 1, 2, 4, 4, 0, 0]
    B = [2, 2, 3, 4, 4, 1, 2, 0, 0]

    uf = UnionFind(N)
    result = []
    for p, a, b in zip(P, A, B):
        if p == 0:
            uf.union(a, b)
        else:
            if uf.is_same(a, b):
                result.append("Yes")
            else:
                result.append("No")

    assert result == ["Yes", "No", "Yes", "Yes"]


# TODO: WeightedUnionFindが必要な問題で確認する
def test_weighted_union_find():
    """https://atc001.contest.atcoder.jp/tasks/unionfind_a"""
    N = 8
    P = [0, 0, 1, 1, 0, 1, 0, 0, 1]
    A = [1, 3, 1, 1, 2, 4, 4, 0, 0]
    B = [2, 2, 3, 4, 4, 1, 2, 0, 0]

    uf = WeightedUnionFind(N)
    result = []
    for p, a, b in zip(P, A, B):
        if p == 0:
            uf.union(a, b, 0)
        else:
            if uf.is_same(a, b):
                result.append("Yes")
            else:
                result.append("No")

    assert result == ["Yes", "No", "Yes", "Yes"]
