import pytest

from algorithms.is_intersected import is_intersected


@pytest.mark.parametrize(
    "a, b, c, d, expected",
    [((0, 0), (1, 1), (0, 1), (1, 0), True), ((0, 0), (1, 0), (0, 1), (1, 1), False)],
)
def test_is_intersected(a, b, c, d, expected):
    result = is_intersected(a, b, c, d)
    assert result is expected
