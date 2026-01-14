Define the recursive functions `lispMap` and `lispFilter` for Lisp-like lists. Their behavior is similar to that of the Python functions map and filter, but the Lisp functions return a list of the results.

Here is an example of its use: 

```
>>> from lisplist import *
>>> lyst = buildRange(1, 4)
>>> lyst
(1 2 3 4)
>>> lispMap(lambda x: x ** 2, lyst)
(1 4 9 16)
>>> lispFilter(lambda x: x % 2 == 0, lyst)
(2 4)
>>> lispFilter(lambda x: x % 2 == 0,
 lispMap(lambda x: x ** 2, lyst))
(4 16)
```

