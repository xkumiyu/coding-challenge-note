# 線分交差判定

線分ABと線分CDが交差しているかどうか判定する

``` py
def is_ientersected_1d(a, b, c, d, closed_section=False):
    tc = (a - b) * (c - a) + (a - b) * (a - c)
    td = (a - b) * (d - a) + (a - b) * (a - d)
    ta = (c - d) * (a - c) + (c - d) * (c - a)
    tb = (c - d) * (b - c) + (c - d) * (c - b)
```

``` py
def is_ientersected(a, b, c, d, closed_section=False):
    s = (a[0] - b[0]) * (c[1] - a[1]) + (a[1] - b[1]) * (a[0] - c[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) + (a[1] - b[1]) * (a[0] - d[0])
    if s * t > 0:
        return false
    ta = (c[0] - d[0]) * (a[1] - c[1]) + (c[1] - d[1]) * (c[0] - a[0])
    tb = (c[0] - d[0]) * (b[1] - c[1]) + (c[1] - d[1]) * (c[0] - b[0])
```
