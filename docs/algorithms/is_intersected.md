# 線分交差判定

線分`ab`と線分`cd`が交差しているか判定する

## コード

```py
def is_intersected(a, b, c, d):
    s = (a[0] - b[0]) * (c[1] - a[1]) + (a[1] - b[1]) * (a[0] - c[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) + (a[1] - b[1]) * (a[0] - d[0])
    if s * t > 0:
        return False

    s = (c[0] - d[0]) * (a[1] - c[1]) + (c[1] - d[1]) * (c[0] - a[0])
    t = (c[0] - d[0]) * (b[1] - c[1]) + (c[1] - d[1]) * (c[0] - b[0])
    if s * t > 0:
        return False

    return True
```

## Example

```py
>>> a = (0, 0)
>>> c = (1, 1)
>>> d = (0, 1)
>>> e = (1, 0)
>>> is_intersected(a, b, c, d)
True
```
