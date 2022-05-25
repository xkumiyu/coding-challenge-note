# bit全探索

```py
from itertools import product

N = 3
for p in product([0, 1], repeat=N):
  print(p)
```

!!! Example

    ```py
    (0, 0, 0)
    (0, 0, 1)
    (0, 1, 0)
    (0, 1, 1)
    (1, 0, 0)
    (1, 0, 1)
    (1, 1, 0)
    (1, 1, 1)
    ```

```py
N = 3
for i in range(1 << N):
  p = []
  for j in range(N):
    p.append(1 & (i >> j))
  print(p)
```

!!! Example

    ```py
    [0, 0, 0]
    [1, 0, 0]
    [0, 1, 0]
    [1, 1, 0]
    [0, 0, 1]
    [1, 0, 1]
    [0, 1, 1]
    [1, 1, 1]
    ```
