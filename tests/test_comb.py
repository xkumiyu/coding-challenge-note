from algorithms.comb import Comb


def test_comb():
    comb = Comb(100)
    assert comb.calc(10, 2) == 45
