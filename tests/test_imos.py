from algorithms.imos import Imos1d


def test_imos():
    N = 7
    imos = Imos1d(N)

    imos.add(1, 4, v=2)
    imos.add(3, 4, v=3)
    imos.add(0, 6, v=1)

    imos.calc()

    assert imos.x == [1, 3, 3, 6, 1, 1, 0]
