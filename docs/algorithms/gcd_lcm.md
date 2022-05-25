# 最大公約数と最小公倍数

## 最大公約数

```py
from math import gcd
gcd(a, b)
```

## 最小公倍数

```py
def lcm(a, b):
  return a * b // gcd(a, b)
```
