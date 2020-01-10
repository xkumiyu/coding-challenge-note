def is_intersected(a, b, c, d):
    """交差判定

    線分abと線分cdが交差するか判定する
    端点は含まない

    Args:
        a, b, c, d(tuple): x, y座標
    """
    s = (a[0] - b[0]) * (c[1] - a[1]) + (a[1] - b[1]) * (a[0] - c[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) + (a[1] - b[1]) * (a[0] - d[0])
    if s * t > 0:
        return False

    s = (c[0] - d[0]) * (a[1] - c[1]) + (c[1] - d[1]) * (c[0] - a[0])
    t = (c[0] - d[0]) * (b[1] - c[1]) + (c[1] - d[1]) * (c[0] - b[0])
    if s * t > 0:
        return False

    return True
