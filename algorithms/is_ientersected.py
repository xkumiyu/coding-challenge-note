def is_ientersected(a, b, c, d):
    """線分判定"""
    s = (a[0] - b[0]) * (c[1] - a[1]) - (a[1] - b[1]) * (a[0] - c[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) - (a[1] - b[1]) * (a[0] - d[0])
    if s * t > 0:
        return False

    s = (c[0] - d[0]) * (a[1] - c[1]) - (c[1] - d[1]) * (c[0] - a[0])
    t = (c[0] - d[0]) * (b[1] - c[1]) - (c[1] - d[1]) * (c[0] - b[0])
    if s * t > 0:
        return False

    return True
